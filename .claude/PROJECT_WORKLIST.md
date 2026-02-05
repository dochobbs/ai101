# AI 101 - Project Worklist

## Priority: Domain Setup
- [ ] Configure DNS at Namecheap (A records + CNAME records — see docs/plans/2026-02-04-custom-domain-setup.md)
- [ ] Enable GitHub Pages on ai101-hub with custom domain ai101.health
- [ ] Set custom domain on ai101 repo to clinicians.ai101.health
- [ ] Verify dochobbs.github.io/ai101/ redirects correctly
- [ ] Enable HTTPS on all three domains
- [ ] Configure patients.ai101.health when patient repo is ready

## Content Housekeeping
- [ ] Move legacy files to archive/ (unit-0-orig.html, module-*-orig.html, week-*.html, big-three-v1.0-archive.html)
- [ ] Fix placeholder reading list links (currently #)
- [ ] Host referenced PDFs/templates (Model Cards, CLAIM checklist)

## Technical Improvements
- [ ] Add site-wide search (44 pages)
- [ ] Optimize favicon.png (132KB — compress or convert to ICO)
- [ ] Add skip-to-content links for accessibility
- [ ] Improve ARIA labeling across interactive elements
- [ ] Consider auto-generating RSS feed from ai-news.html

## Companion App (Spark)
- [ ] Add ai101-companion/.venv/ to .gitignore if not already
- [ ] Sync glossary/tools/prompts data between app and main site

## Future
- [ ] Build interactive exercises (Alert Fatigue Simulator, Prompt Golf)
- [ ] Add assessment/quiz tracking
- [ ] Add analytics to measure content usage
