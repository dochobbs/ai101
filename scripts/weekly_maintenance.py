#!/usr/bin/env python3
"""Independent maintenance receipt. No model, extra package, or personal token."""
import argparse
import concurrent.futures
import datetime as dt
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from sync_news_feed import generate as generate_rss

ROOT = Path(__file__).resolve().parents[1]
MARKER = '<!-- ai101-maintenance -->'
START = '<!-- automated-report:start -->'
END = '<!-- automated-report:end -->'


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []

    def handle_starttag(self, tag, attrs):
        self.targets += [v for k, v in attrs if k in ('href', 'src') and v]


def age_days(value, today):
    age = (today - dt.date.fromisoformat(value)).days
    if age < 0:
        raise ValueError(f'Future date is not a valid receipt: {value}')
    return age


def fetch(url):
    request = urllib.request.Request(url, headers={'User-Agent': 'AI101-Maintenance/1.0'})
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            return {'url': url, 'status': response.status,
                    'body': response.read(2_000_000).decode('utf-8', errors='replace')}
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return {'url': url, 'status': None, 'error': str(exc)}


def check(today, check_external=False, check_live=False):
    state = json.loads((ROOT / 'docs/audits/latest.json').read_text())
    problems, checks = [], []
    review_age = age_days(state['content_reviewed_at'], today)
    checks.append(f'Content review: {state["content_reviewed_at"]} ({review_age} days ago).')
    last_sunday = today - dt.timedelta(days=(today.weekday() + 1) % 7)
    if review_age > 8 or dt.date.fromisoformat(state['content_reviewed_at']) < last_sunday:
        problems.append(f'Content review overdue: no completed review receipt for Sunday {last_sunday}. Prepare a content-update PR; a completed agent session alone does not clear this.')
    published_age = age_days(state['content_published_at'], today)
    checks.append(f'Content publication: {state["content_published_at"]} ({published_age} days ago), {state["version"]}.')
    if not state.get('publication_verified', False):
        problems.append(f'Publication of {state["version"]} has not yet been verified.')
    news = (ROOT / 'ai-news.html').read_text()
    added = re.findall(r'Added: ([A-Z][a-z]{2} \d{1,2}, \d{4})', news)
    if not added:
        problems.append('No parseable Added dates in the news page.')
    else:
        latest = max(dt.datetime.strptime(x, '%b %d, %Y').date() for x in added)
        news_age = age_days(latest.isoformat(), today)
        checks.append(f'Newest news addition: {latest} ({news_age} days ago).')
        if news_age > 14:
            problems.append('News review needed: latest addition is more than 14 days old. Review for real developments; do not invent filler.')

    tracked = subprocess.check_output(['git', 'ls-files', '*.html'], cwd=ROOT, text=True).splitlines()
    pages = [ROOT / p for p in tracked if '/' not in p]
    broken = []
    for page in pages:
        parser = Links()
        parser.feed(page.read_text())
        for target in parser.targets:
            url = urllib.parse.urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            local = (ROOT if url.path.startswith('/') else page.parent) / urllib.parse.unquote(url.path.lstrip('/'))
            if not local.exists():
                broken.append(f'{page.name}: {target}')
    checks.append(f'Local file links/assets: {len(pages)} tracked root HTML pages, {len(broken)} missing targets (anchors not checked).')
    problems.extend(f'Missing local target: {x}' for x in sorted(set(broken)))
    try:
        ET.parse(ROOT / 'ai-news-feed.xml')
        ET.parse(ROOT / 'sitemap.xml')
        checks.append('RSS and sitemap: parse successfully.')
        rss = (ROOT / 'ai-news-feed.xml').read_text()
        build_date = ET.fromstring(rss).findtext('./channel/lastBuildDate')
        if generate_rss(news, rss, build_date) != rss:
            problems.append('RSS content differs from the HTML news page. Run scripts/sync_news_feed.py and review the changes.')
        else:
            checks.append('RSS is a complete, reproducible mirror of HTML news, with unique story identifiers.')
    except (ET.ParseError, ValueError) as exc:
        problems.append(f'RSS/sitemap XML error: {exc}')

    sources = state['primary_sources']
    network = []
    if check_external:
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
            network = list(pool.map(fetch, sources))
        for result in network:
            if result.get('status') != 200:
                problems.append(f'External source UNVERIFIED: {result["url"]} — {result.get("error", result.get("status"))}. This is not proof of a dead link.')
        passed = sum(x.get('status') == 200 for x in network)
        checks.append(f'External reachability: {passed}/{len(sources)} maintained primary sources returned HTTP 200; remaining site links not checked. Reachability does not validate source claims.')
    else:
        checks.append('External source reachability: NOT RUN.')
    if check_live:
        live = fetch('https://ai101.health/updates.html')
        footer = re.search(r'<footer\b[^>]*>(.*?)</footer>', live.get('body', ''), re.S)
        release = re.search(r'\bv\d+(?:\.\d+)+\b', footer.group(1)) if footer else None
        if live.get('status') != 200 or not release or release.group(0) != state['version']:
            observed = release.group(0) if release else 'unavailable'
            problems.append(f'Deployment UNVERIFIED: live footer release is {observed}; published receipt expects {state["version"]}.')
        else:
            checks.append(f'Live site: updates.html footer confirms {state["version"]}.')
    else:
        checks.append('Live deployment: NOT RUN.')
    for item in state.get('outstanding_operations', []):
        problems.append(f'Outstanding operation: {item}')
    return {'date': today.isoformat(), 'status': 'NEEDS ATTENTION' if problems else 'CHECKS PASSED',
            'checks': checks, 'problems': problems,
            'external': [{k: v for k, v in r.items() if k != 'body'} for r in network]}


def markdown(report):
    return '\n'.join([
        f'## Maintenance check — {report["date"]}: {report["status"]}', '',
        'This is a deterministic check, not a receipt that Claude researched or published updates.', '',
        *[f'- {x}' for x in report['checks']], '', '### Work requiring attention', '',
        *([f'- {x}' for x in report['problems']] or ['- No deterministic check failures. Review the research PR separately.']), '',
        'Sunday content updates must be prepared as a PR for the owner to review. An empty issue list does not clear calendar-only findings.', '',
        f'Run: {os.environ.get("GITHUB_SERVER_URL", "https://github.com")}/{os.environ.get("GITHUB_REPOSITORY", "dochobbs/ai101")}/actions/runs/{os.environ.get("GITHUB_RUN_ID", "local")}',
    ])


def api(path, method='GET', payload=None):
    token = os.environ['GH_TOKEN']
    data = json.dumps(payload).encode() if payload is not None else None
    request = urllib.request.Request('https://api.github.com/' + path, method=method, data=data,
        headers={'Authorization': f'Bearer {token}', 'Accept': 'application/vnd.github+json',
                 'X-GitHub-Api-Version': '2022-11-28', 'Content-Type': 'application/json'})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def replace_report(body, report):
    section = f'{START}\n{report}\n{END}'
    if START in body and END in body:
        return body[:body.index(START)] + section + body[body.index(END) + len(END):]
    return body + '\n\n' + section


def deliver(body):
    repo = os.environ.get('GITHUB_REPOSITORY', 'dochobbs/ai101')
    issue = None
    for page in range(1, 101):
        batch = api(f'repos/{repo}/issues?state=open&per_page=100&page={page}')
        issue = next((x for x in batch if not x.get('pull_request') and MARKER in (x.get('body') or '')), None)
        if issue or len(batch) < 100:
            break
    if issue:
        updated = replace_report(issue.get('body') or '', body)
        api(f'repos/{repo}/issues/{issue["number"]}', 'PATCH', {'body': updated})
        # A bot-authored comment notifies the assigned owner each Sunday.
        receipt = api(f'repos/{repo}/issues/{issue["number"]}/comments', 'POST', {'body': body})
    else:
        initial = '\n'.join([MARKER, '# Weekly AI 101 maintenance', '',
            'Owner notes and unresolved findings stay here until explicitly resolved.', '',
            '- [ ] Review the Sunday content-update PR and verify deployment.',
            '- [ ] Reconcile any findings delivered only through Calendar.', '',
            f'{START}\n{body}\n{END}'])
        receipt = api(f'repos/{repo}/issues', 'POST', {'title': 'AI 101: weekly content maintenance',
            'body': initial, 'labels': ['audit'], 'assignees': [repo.split('/')[0]]})
    print(f'Issue delivery verified: {receipt["html_url"]}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--date', default=dt.date.today().isoformat())
    parser.add_argument('--check-external', action='store_true')
    parser.add_argument('--check-live', action='store_true')
    parser.add_argument('--deliver', action='store_true')
    parser.add_argument('--output', type=Path, default=Path('/tmp/ai101-check'))
    args = parser.parse_args()
    report = check(dt.date.fromisoformat(args.date), args.check_external, args.check_live)
    args.output.mkdir(parents=True, exist_ok=True)
    body = markdown(report)
    (args.output / 'report.json').write_text(json.dumps(report, indent=2) + '\n')
    (args.output / 'report.md').write_text(body + '\n')
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as out:
            out.write(body + '\n')
    print(body)
    if args.deliver:
        deliver(body)  # Fail loudly if reporting failed, even when checks passed.
    return 1 if report['problems'] else 0


if __name__ == '__main__':
    sys.exit(main())
