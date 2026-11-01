# Weekly content maintenance

The Claude routine `trig_01KvbzVEe51SjAHdzHhwSMqQ` runs Sundays at 17:00 UTC
(noon CDT / 11 AM CST). It researches changes; it does not automatically publish.
The GitHub `Weekly maintenance check` runs at 19:37 UTC every Sunday, with a
manual dispatch for verification. These are separate jobs with separate receipts.

## Each research run

1. Read this file, `docs/audits/latest.json`, the previous committed audit reports,
   open `audit` issues, and the last four AI 101 audit calendar events. Reconcile
   every unresolved finding against current source files. Include calendar-only
   findings even when GitHub returns zero issues. Only close a finding with a
   file/commit reference or an explicit, sourced reason for dropping it.
2. Verify source access separately for Anthropic, OpenAI, Google, and a medical
   publisher/regulator. One reachable vendor does not establish usable research
   connectivity. Read primary sources; do not treat snippets as verification.
3. Review developments since the last completed content review, not merely the
   last seven days. Prioritize changes affecting clinician decisions and deployed
   workflows. Separate vendor benchmarks, simulated cases, silent deployments,
   and patient outcomes. Never inherit a factual claim from an earlier audit
   without checking its evidence.
4. Prepare source-linked edits to affected pages, `ai-news.html`, its RSS mirror,
   `updates.html`, and relevant index/sitemap timestamps. Historical update blocks
   retain their historical dates; current offering sections must be current.
5. Prepare a reviewable content-update branch named
   `claude/ai101-audit-YYYY-MM-DD` (append a unique suffix if necessary), commit
   the proposed changes and report, and push that branch using the cloud
   session's configured Git transport. `open-audit-pr.yml` opens the PR using a
   short-lived Actions credential, independently of Claude's blocked issue API.
   Read back the resulting PR URL; do not infer creation from a successful push.
   If Git push itself is blocked, retain the complete proposed patch in the
   calendar fallback and mark delivery degraded. Do not publish unattended unless the owner explicitly changes the
   policy. Keep unrelated files out. Include the report and proposed changes so
   the owner can review something concrete, not just a list of work to do.
6. Record the run in `docs/audits/YYYY-MM-DD.md` and propose an update to
   `docs/audits/latest.json`. Advance `content_reviewed_at` only after all required
   source families were checked and the content review completed. Advance
   `content_published_at` only when the corresponding edits actually deployed.
   A clean week may advance the review date without inventing news or a release.
7. Try GitHub issue delivery once. A 403 is a delivery failure, not a clean week.
   Put the full report, outstanding findings, and branch/PR link in the calendar
   fallback and push notification. Mark it `DEGRADED — delivery` when GitHub
   filing fails. Do not report zero backlog from an empty issue query alone.

Every report must show these independent results:

- Research: COMPLETE / PARTIAL / NOT RUN, with blocked source families.
- Links: COMPLETE / PARTIAL / NOT RUN, with actual scope and counts.
- Delivery: GitHub issue/PR URL, or calendar fallback and the error.
- Publication: deployed commit/URL, PR pending review, or no changes required.
- Outstanding work: explicit carry-forward entries and disposition evidence.

The platform's “Succeeded” badge only says the agent stopped normally.

## Independent GitHub check

`.github/workflows/weekly-maintenance.yml` runs deterministic freshness, local
link, primary-source reachability, and deployed-version checks. It creates or
updates a single **assigned** issue with a bot credential scoped to issue writes.
Its managed report section is refreshed; the owner's notes and checkboxes are
preserved. It does not close the issue automatically. Check failures cause the
workflow to fail after the report is delivered, rather than producing a green
badge for partial work. Issue-delivery failures also fail the job.

The JSON receipt and Markdown report are retained as Actions artifacts. This
check cannot independently establish that Claude executed or that its factual
research was adequate. A missing receipt for the most recent Sunday (or a review
older than 8 days) fails; a news entry
older than 14 days prompts review, without requiring fabricated filler news.

`Open audit update PR` opens reviews when an authorized contributor pushes a
`claude/ai101-audit-*` or `maintenance/ai101-audit-*` branch. It runs no branch
code and never merges or approves a PR. GitHub's bundled repository setting
allowing Actions to create/approve PRs is enabled because creation requires it;
the default token permissions remain read-only. Only this job requests PR write
access, and only the maintenance reporter requests issue write access.

GitHub can delay scheduled jobs and disable schedules after 60 days without
repository activity in public repositories. Review the Actions run history at
each maintenance session; the separate Claude schedule remains a fallback.

## Manual verification

```sh
python3 scripts/weekly_maintenance.py --check-external --check-live --output /tmp/ai101-check
gh workflow run weekly-maintenance.yml --repo dochobbs/ai101
gh run list --repo dochobbs/ai101 --workflow weekly-maintenance.yml --limit 3
```

Do not infer deployed state from a local commit or a completed research run.
