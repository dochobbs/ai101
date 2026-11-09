import datetime as dt
import json
import unittest
from unittest.mock import patch
import weekly_maintenance as audit


class MaintenanceTest(unittest.TestCase):
    def test_receipt_expires_and_future_dates_are_invalid(self):
        self.assertEqual(audit.age_days('2026-11-01', dt.date(2026, 11, 10)), 9)
        with self.assertRaises(ValueError):
            audit.age_days('2026-11-11', dt.date(2026, 11, 10))

    def test_stale_review_fails_even_without_open_issues(self):
        report = audit.check(dt.date(2026, 11, 24))
        self.assertEqual(report['status'], 'NEEDS ATTENTION')
        self.assertTrue(any('Content review overdue' in p for p in report['problems']))
        self.assertTrue(any('News review needed' in p for p in report['problems']))

    def test_network_denial_is_visible_not_a_clean_check(self):
        with patch.object(audit, 'fetch', side_effect=lambda url: {'url': url, 'error': '403 policy denied', 'status': None}):
            report = audit.check(dt.date(2026, 11, 9), check_external=True)
        self.assertEqual(report['status'], 'NEEDS ATTENTION')
        self.assertTrue(any('External source UNVERIFIED' in p for p in report['problems']))

    def test_next_sunday_requires_a_new_receipt(self):
        report = audit.check(dt.date(2026, 11, 15))
        self.assertTrue(any('Sunday 2026-11-15' in p for p in report['problems']))

    def test_owner_backlog_survives_report_replacement(self):
        body = f'{audit.MARKER}\n- [ ] Unresolved calendar finding\n{audit.START}\nold\n{audit.END}\nOwner note'
        updated = audit.replace_report(body, 'new report')
        self.assertIn('- [ ] Unresolved calendar finding', updated)
        self.assertIn('Owner note', updated)
        self.assertNotIn('\nold\n', updated)

    def test_historical_changelog_version_cannot_clear_a_different_release(self):
        version = json.loads((audit.ROOT / "docs/audits/latest.json").read_text())["version"]
        with patch.object(audit, 'fetch', return_value={'status': 200, 'body': f'<h2>{version}</h2><footer>v99.0 · 2026</footer>'}):
            report = audit.check(dt.date(2026, 11, 9), check_live=True)
        self.assertTrue(any('live footer release is v99.0' in p for p in report['problems']))

    def test_footer_release_matches_publication_receipt(self):
        version = json.loads((audit.ROOT / "docs/audits/latest.json").read_text())["version"]
        with patch.object(audit, 'fetch', return_value={'status': 200, 'body': f'<h2>v0.0</h2><footer>{version} · 2026</footer>'}):
            report = audit.check(dt.date(2026, 11, 9), check_live=True)
        self.assertFalse(any('Deployment UNVERIFIED' in p for p in report['problems']))


    def test_card_labels_cannot_outrun_content_or_the_calendar(self):
        def card(page, label):
            return f'<a href="{page}" class="week-card x"><h3>t</h3><span class="week-updated">{label}</span></a>'
        today = dt.date(2026, 11, 7)
        ok, _ = audit.check_card_dates(today, card('phi-hipaa.html', 'Updated Nov 2026'))
        self.assertEqual(ok, [])
        future, _ = audit.check_card_dates(today, card('phi-hipaa.html', 'Updated Dec 2026'))
        self.assertTrue(any('in the future' in p for p in future))
        garbled, _ = audit.check_card_dates(today, card('phi-hipaa.html', 'Recently updated'))
        self.assertTrue(any('unparseable' in p for p in garbled))
        with patch.object(audit, 'last_content_change', return_value=dt.date(2026, 5, 20)), \
             patch.object(audit.subprocess, 'run', wraps=audit.subprocess.run) as run:
            run.side_effect = lambda *a, **k: audit.subprocess.CompletedProcess(a, 0, stdout='false\n', stderr='')
            stale, _ = audit.check_card_dates(today, card('vibe-coding.html', 'Updated Nov 2026'))
        self.assertTrue(any('last content change is 2026-05-20' in p for p in stale))

    def test_footer_only_commits_do_not_count_as_content(self):
        self.assertTrue(audit.ROUTINE_LINE.search('+  <div><a href="updates.html">v1.17 · 2026</a></div>'))
        self.assertFalse(audit.ROUTINE_LINE.search('+ <p>HTI-5 is final.</p>'))

if __name__ == '__main__':
    unittest.main()
