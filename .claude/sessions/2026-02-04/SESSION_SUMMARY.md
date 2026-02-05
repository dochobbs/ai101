# Session Summary - 2026-02-04

## Project
AI 101 - A Self-Paced Guide to AI in Medicine
`/Users/dochobbs/Downloads/ai101` (clinician site)
`/Users/dochobbs/Downloads/ai101-hub` (new hub landing page)

## Branch
main (both repos)

## Accomplishments
- Reviewed the full AI 101 project (44 HTML pages, Flask companion app, design system)
- Designed domain architecture for ai101.health serving two audiences (clinicians + patients)
- Created `ai101-hub` repo with landing page routing to clinicians.ai101.health and patients.ai101.health
- Built hub landing page matching existing site branding (Fraunces, Source Sans 3, teal/violet palette)
- Added CNAME files to both repos for GitHub Pages custom domain configuration
- Wrote comprehensive domain setup plan with DNS records, step-by-step instructions, and rollback strategy
- Created and pushed new `ai101-hub` GitHub repo

## Commits Made

### ai101 (clinician repo)
- `3560392`: FEATURE: Add CNAME and domain setup plan for clinicians.ai101.health

### ai101-hub (new repo)
- `e02a413`: FEATURE: Initial hub landing page for ai101.health

## Issues Encountered
- None

## Decisions Made
- **Stay on GitHub Pages** — no need to switch hosting for static sites
- **Subdomain architecture** — ai101.health (hub), clinicians.ai101.health, patients.ai101.health
- **Hub as landing page** — neither audience owns the root domain; simple router page
- **Separate repos per audience** — already the case, subdomains map naturally to this
- **Push now, configure later** — CNAME files are inert until GitHub Pages settings are changed

## Next Steps
- Configure DNS at Namecheap (A records + CNAME records per plan doc)
- Enable GitHub Pages on ai101-hub with custom domain ai101.health
- Set custom domain on ai101 repo to clinicians.ai101.health
- Verify redirects from dochobbs.github.io/ai101/ work correctly
- Configure patients.ai101.health when patient repo is ready
- Consider archiving legacy HTML files (unit-0-orig.html, module-*-orig.html, week-*.html) to reduce root clutter
