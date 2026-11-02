# AI 101 for Clinicians — Project Summary

## What This Is
A self-paced static website that teaches clinicians and medical learners to
evaluate, supervise, and thoughtfully integrate AI tools into practice.
Topic-organized (not cohort/week-based), hosted on GitHub Pages at
**ai101.health**.

## Site Structure

The site is organized into four sections driven by [index.html](index.html):

**Foundations** — core mental models
- [llm-thinking.html](llm-thinking.html) — How LLMs Think Like Clinicians
- [phi-hipaa.html](phi-hipaa.html) — PHI, HIPAA, and AI
- [prompting.html](prompting.html) — The Art of the Ask (+ [prompting-exercise.html](prompting-exercise.html))
- [big-three.html](big-three.html) — The Big Three (Claude, ChatGPT, Gemini)
- [bias-ethics.html](bias-ethics.html) — Bias, Ethics, and the Training Data Problem
- [medical-learners.html](medical-learners.html) — AI 101 for Medical Learners

**Using AI** — practical applications
- [clinical-decision-support.html](clinical-decision-support.html) — Clinical Decision Support Tools
- [ambient-ai.html](ambient-ai.html) — Ambient AI Tools (scribes)
- [ai-search.html](ai-search.html) — AI-Powered Search
- [image-video.html](image-video.html) — AI Image and Video Creation
- [everyday-ai.html](everyday-ai.html) — Everyday Ways to Use AI
- [patients-ai.html](patients-ai.html) — When Patients Bring AI to the Exam Room

**What's Next** — go deeper
- [whats-next.html](whats-next.html) — So...What Next?
- [vibe-coding.html](vibe-coding.html) — Vibe Coding
- [ai-tools-mcp.html](ai-tools-mcp.html) — How AI Talks to Your Tools (APIs, MCP)
- [openclaw.html](openclaw.html) — AI agents introduction and OpenClaw/Hermes security case studies

**Resources** — supporting content
- [ai-news.html](ai-news.html) — Ongoing news feed (+ [ai-news-feed.xml](ai-news-feed.xml) RSS)
- [environmental-footprint.html](environmental-footprint.html) — AI's Environmental Footprint
- [local-models.html](local-models.html) — Running AI Models on Your Own Computer
- [glossary.html](glossary.html) — AI Glossary

**Meta pages**
- [start-here.html](start-here.html) — NotebookLM-driven practical on-ramp
- [claude-code.html](claude-code.html) — "30 Days to Claude Code" daily program
  (also reachable at the vanity URL `/30-days` via [30-days.html](30-days.html))
- [about.html](about.html) — Course philosophy
- [contribute.html](contribute.html) — Contribution guide
- [updates.html](updates.html) — Version changelog (linked from every page footer)
- [resources.html](resources.html) — Curated resources page (in the nav site-wide
  as of v1.10)

## Companion App (`ai101-companion/`)
A small Flask + vanilla-JS chatbot named **Spark** that teaches prompting and
recommends AI tools. Knowledge bases in `data/*.json` (glossary, prompts,
tools). Serves on `localhost:5050`.

## Design System
- **Fonts**: Fraunces (display), Source Sans 3 (body), JetBrains Mono (code)
- **Aesthetic**: Editorial/academic — clean, generous whitespace
- **Icons**: Lucide via CDN
- **Chatbot embed**: Pickaxe deployment widget in nav on most pages
- **Responsive**: Breakpoints at 900px and 600px
- **Shared stylesheet**: [styles.css](styles.css)

## Technical Notes
- Pure HTML/CSS — no framework, no build step
- Google Fonts + Lucide loaded via CDN
- All internal links relative — works locally or hosted
- Published version: **v1.15 · 2026**; this review branch prepares **v1.16** (bumped each release; the footer version on
  every page links to [updates.html](updates.html))
- Deployment: GitHub Pages via [dochobbs/ai101](https://github.com/dochobbs/ai101)
- Custom domain: ai101.health (CNAME configured)

## Legacy Content
The original curriculum was modeled after BlueDot Impact's 12-week cohort
format (Phase I/II/III, numbered modules, `week-*.html` pages). That structure
was retired in favor of topic-based, self-paced navigation. The old drafts live
in [archive/](archive/) and are not linked from any live page.

## Operational Workflow
- **Sunday research:** Claude routine `trig_01KvbzVEe51SjAHdzHhwSMqQ`, at
  17:00 UTC (noon CDT / 11 AM CST). Future changes are to be prepared as a PR
  for owner review. Research, delivery, and publication are separate outcomes.
  `CLAUDE.md` points to [the maintenance instructions](docs/operations/weekly-audit.md)
  and [persistent audit ledger](docs/audits/latest.json). Carry calendar-only
  findings forward; an empty issue list does not mean no backlog.
- **Independent check:** GitHub Actions `Weekly maintenance check`, Sundays at
  19:37 UTC, plus manual dispatch. Checks freshness, local targets, XML, bounded
  primary-source reachability, and the live release. Bot-authored issue delivery
  is separate from Claude's credential. Outstanding work stays in one assigned
  issue; failed or incomplete checks fail the workflow. Receipts are artifacts.
- **Known boundary (November 1):** Claude's own GitHub issue credential returns
  403; its cloud source egress has been restricted. Reports have been delivered
  to Calendar since July, with a risk of losing findings between weeks. The
  [recovery report](docs/audits/2026-11-01.md) records fixes and what still needs
  a live research-run check. A platform Succeeded badge is not publication proof.
- **Version bumps** happen in the footer of every page at release time
  (currently `v1.15 · 2026`). One-liner:
  `perl -pi -e 's/v1\.OLD · 2026/v1.NEW · 2026/g' *.html`
- **ai-news.html** is the lightweight running log; `updates.html` is the
  formal changelog for readers.

The second November 1 pass is documented in [the full site audit](docs/audits/full-site-audit-2026-11-01.md). Its prepared changes are not a deployment receipt. `scripts/sync_news_feed.py` maintains the complete RSS mirror from canonical news HTML.
