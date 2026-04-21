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
- [patients-ai.html](patients-ai.html) — When Patients Use AI Too

**What's Next** — go deeper
- [whats-next.html](whats-next.html) — So...What Next?
- [vibe-coding.html](vibe-coding.html) — Vibe Coding
- [ai-tools-mcp.html](ai-tools-mcp.html) — How AI Talks to Your Tools (APIs, MCP)
- [openclaw.html](openclaw.html) — OpenClaw (autonomous agent risk)

**Resources** — supporting content
- [ai-news.html](ai-news.html) — Ongoing news feed (+ [ai-news-feed.xml](ai-news-feed.xml) RSS)
- [environmental-footprint.html](environmental-footprint.html) — AI's Environmental Footprint
- [local-models.html](local-models.html) — Running AI Models on Your Own Computer
- [glossary.html](glossary.html) — AI Glossary & Learning Resources

**Meta pages**
- [start-here.html](start-here.html) — NotebookLM-driven practical on-ramp
- [about.html](about.html) — Course philosophy
- [contribute.html](contribute.html) — Contribution guide
- [updates.html](updates.html) — Version changelog visible to readers
- [resources.html](resources.html) — Legacy curated resources page (orphaned — nav entry
  commented out in index.html; has placeholder `#` links)

## Companion App (`ai101-companion/`)
A small Flask + vanilla-JS chatbot named **Spark** that teaches prompting and
recommends AI tools. Knowledge bases in `data/*.json` (glossary, prompts,
tools). Serves on `localhost:5050` (note: the README says 5000 — needs fix).

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
- Current version: **v1.3 · 2026** (bumped each release)
- Deployment: GitHub Pages via [dochobbs/ai101](https://github.com/dochobbs/ai101)
- Custom domain: ai101.health (CNAME configured)

## Legacy Content
The original curriculum was modeled after BlueDot Impact's 12-week cohort
format (Phase I/II/III, numbered modules, `week-*.html` pages). That structure
was retired in favor of topic-based, self-paced navigation. The old drafts live
in [archive/](archive/) and are not linked from any live page.

## Operational Workflow
- **Weekly audit**: a scheduled remote agent scans the AI landscape every
  Sunday 12:00 PT, emails `michael@hobbs.md` with a punch list of pages
  needing updates, link-check results, and a ready-to-paste [updates.html](updates.html)
  entry. See [docs/PROJECT_CHANGELOG.md](docs/PROJECT_CHANGELOG.md) for
  history.
- **Version bumps** happen in the footer of every page at release time
  (currently `v1.3 · 2026`).
- **ai-news.html** is the lightweight running log; `updates.html` is the
  formal changelog for readers.
