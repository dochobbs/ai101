# AI 101 for Clinicians - Detailed Project Changelog

> Full history of every change to the AI 101 course website, from initial commit to present.

**Project:** AI 101 for Clinicians (ai101.health)
**Repository:** GitHub Pages static site
**Date range:** November 28, 2025 - February 10, 2026
**Total commits:** 57
**Cumulative stats:** ~35,600 lines added, ~1,350 lines removed across 413 file-change events
**Current pages:** 43 HTML topic pages + supporting assets

---

## Table of Contents

- [Phase 1: Initial Launch (Nov 28, 2025)](#phase-1-initial-launch-nov-28-2025)
- [Phase 2: Structure & Navigation Overhaul (Nov 28-29, 2025)](#phase-2-structure--navigation-overhaul-nov-28-29-2025)
- [Phase 3: Quality & Accuracy Pass (Nov 30, 2025)](#phase-3-quality--accuracy-pass-nov-30-2025)
- [Phase 4: Features & Interactivity (Nov 30, 2025)](#phase-4-features--interactivity-nov-30-2025)
- [Phase 5: Echs AI Assistant (Dec 1, 2025)](#phase-5-echs-ai-assistant-dec-1-2025)
- [Phase 6: Major Content Expansion (Dec 7-8, 2025)](#phase-6-major-content-expansion-dec-7-8-2025)
- [Phase 7: Research & Case Studies (Dec 13, 2025)](#phase-7-research--case-studies-dec-13-2025)
- [Phase 8: About Page & Link Fixes (Dec 14, 2025)](#phase-8-about-page--link-fixes-dec-14-2025)
- [Phase 9: What's Next Module (Dec 15, 2025)](#phase-9-whats-next-module-dec-15-2025)
- [Phase 10: Updates Page & Version Bump (Dec 16, 2025)](#phase-10-updates-page--version-bump-dec-16-2025)
- [Phase 11: Big Three Rewrite & Image Updates (Dec 17-18, 2025)](#phase-11-big-three-rewrite--image-updates-dec-17-18-2025)
- [Phase 12: UI Polish (Dec 20, 2025)](#phase-12-ui-polish-dec-20-2025)
- [Phase 13: New Year Features (Jan 1, 2026)](#phase-13-new-year-features-jan-1-2026)
- [Phase 14: AI News Expansion (Jan 6 - Feb 1, 2026)](#phase-14-ai-news-expansion-jan-6---feb-1-2026)
- [Phase 15: Domain & Planning (Feb 4-10, 2026)](#phase-15-domain--planning-feb-4-10-2026)

---

## Phase 1: Initial Launch (Nov 28, 2025)

### `3a24cce` - FEATURE: Initial commit of AI 101 course website
**Date:** 2025-11-28 | **Files:** 39 | **+20,722 lines**

The foundational commit establishing the entire course website. Created as a static HTML/CSS site hosted on GitHub Pages.

**Content created:**
- **index.html** - Main landing page with course overview and module navigation
- **styles.css** - Complete site-wide stylesheet (2,836 lines)
- **unit-0.html** / **unit-0-new.html** / **unit-0-orig.html** - "Start Here" introductory unit (3 versions)
- **module-1.html** / **module-1-orig.html** - "How LLMs Think" (+ original draft)
- **module-2.html** / **module-2-orig.html** - "PHI & HIPAA" (+ original draft)
- **module-3.html** / **module-3-orig.html** / **module-3-exercise.html** - "Prompting" (+ original draft + exercise)
- **module-4.html** - "The Big Three" (ChatGPT, Claude, Gemini)
- **module-9.html** - "Clinical Decision Support"
- **module-10.html** - "Ambient AI"
- **module-11.html** - "Image & Video AI"
- **modules/module-12.html** - "Everyday AI"
- **appendix-1.html** - "Environmental Footprint of AI"
- **appendix-2.html** - Glossary
- **bonus-vibe-coding.html** - "Vibe Coding" bonus topic
- **about.html** - About the course and author
- **resources.html** - Curated resources page
- **week-1.html through week-12.html** - Weekly schedule pages (12 files)
- **PROJECT-SUMMARY.md** - Project documentation
- **images/** - Prompt comparison screenshots (good_prompt_statins.png, bad_prompt_statins.png)
- **modules/PHI_HIPAA_AI_Guide.docx** - Downloadable PHI guide

**Architecture:** Pure static HTML/CSS site with no JavaScript framework, designed for GitHub Pages deployment. Each module is a standalone HTML page with shared navigation and styling.

---

## Phase 2: Structure & Navigation Overhaul (Nov 28-29, 2025)

### `fd174f0` - FIX: Renumber Phase II modules from 9-12 to 5-8
**Date:** 2025-11-28 | **Files:** 8 | **+34 / -34 lines**

Renumbered advanced modules for sequential ordering:
- module-9.html -> module-5.html (Clinical Decision Support)
- module-10.html -> module-6.html (Ambient AI)
- module-11.html -> module-7.html (Image & Video)
- modules/module-12.html -> module-8.html (Everyday AI)

### `6c6ef6a` - FIX: Rename Unit 0 to Module 0 for consistency
**Date:** 2025-11-28 | **Files:** 4 | **+10 / -10 lines**

Renamed unit-0.html to module-0.html, updated all internal references.

### `f25b8e7` - REFACTOR: Replace modules/phases with topics/categories
**Date:** 2025-11-28 | **Files:** 14 | **+103 / -294 lines**

**Major structural change.** Replaced the numbered module/phase system with descriptive topic names:
- module-0.html -> **start-here.html**
- module-1.html -> **llm-thinking.html**
- module-2.html -> **phi-hipaa.html**
- module-3.html -> **prompting.html**
- module-3-exercise.html -> **prompting-exercise.html**
- module-4.html -> **big-three.html**
- module-5.html -> **clinical-decision-support.html**
- module-6.html -> **ambient-ai.html**
- module-7.html -> **image-video.html**
- module-8.html -> **everyday-ai.html**
- appendix-1.html -> **environmental-footprint.html**
- appendix-2.html -> **glossary.html**
- bonus-vibe-coding.html -> **vibe-coding.html**

Simplified the index.html layout significantly (-191 lines).

### `9e6e7ea` - FEATURE: Add new topic "When Patients Use AI Too"
**Date:** 2025-11-28 | **Files:** 4 | **+771 / -4 lines**

New topic page: **patients-ai.html** (755 lines). Covers patient use of AI chatbots, implications for clinicians, and how to address AI-assisted patients in clinical encounters.

### `4e5f60f` - FEATURE: Add "AI 101 for Medical Learners" topic
**Date:** 2025-11-28 | **Files:** 5 | **+1,046 / -4 lines**

New topic page: **medical-learners.html** (1,004 lines). Tailored content for medical students and residents. Added new CSS styles for the learners category card.

### `846e19b` - FEATURE: Add "Running AI Models on Your Own Computer" resource topic
**Date:** 2025-11-28 | **Files:** 4 | **+999 / -4 lines**

New topic page: **local-models.html** (983 lines). Covers Ollama, LM Studio, and running local LLMs for privacy-conscious clinicians.

### `8669bfc` - FIX: Update navigation from "Modules" to "Topics" across all pages
**Date:** 2025-11-29 | **Files:** 14 | **+14 / -14 lines**

Updated nav link text from "Modules" to "Topics" across all 14 active topic pages.

---

## Phase 3: Quality & Accuracy Pass (Nov 30, 2025)

### `2485f60` - FIX: Replace 11 broken links with working alternatives
**Date:** 2025-11-30 | **Files:** 6 | **+14 / -14 lines**

Fixed broken external links across big-three.html, llm-thinking.html, local-models.html, phi-hipaa.html, start-here.html, and unit-0-new.html.

### `7017753` - FIX: Correct factual inaccuracies identified in accuracy review
**Date:** 2025-11-30 | **Files:** 3 | **+10 / -9 lines**

Corrected inaccuracies in environmental-footprint.html, glossary.html, and vibe-coding.html after a thorough content accuracy review.

---

## Phase 4: Features & Interactivity (Nov 30, 2025)

### `f3b9177` - FEATURE: Add resources and fix styling across multiple pages
**Date:** 2025-11-30 | **Files:** 4 | **+151 / -29 lines**

Added new resources to llm-thinking.html and medical-learners.html. Fixed styling issues in phi-hipaa.html. Added new CSS rules.

### `227407f` - FEATURE: Add benchmarks, custom instructions, patient AI tools, and contribute page
**Date:** 2025-11-30 | **Files:** 21 | **+996 / -174 lines**

**Multi-topic expansion:**
- **contribute.html** - New page for community contributions (176 lines)
- **big-three.html** - Added AI benchmark comparisons (+186 lines)
- **prompting.html** - Major expansion with custom instructions guide (+263 lines)
- **patients-ai.html** - Added provider-facing tools (+148 lines)
- **phi-hipaa.html** - Expanded with additional resources (+134 lines)
- Updated about.html with new navigation options

### `5228b7c` - FEATURE: Add Pickaxe AI chatbot to all pages
**Date:** 2025-11-30 | **Files:** 46 | **+1,693 lines**

Integrated a Pickaxe-powered AI chatbot widget across all pages. Also included the **ai101-companion/** directory - a separate Replit-based companion app with:
- Python Flask backend (app.py - 433 lines)
- JSON data files (glossary, prompts, tools)
- Frontend with custom CSS and JavaScript
- Replit deployment configuration

### `1b17bcc` - FEATURE: Add Pickaxe chatbot to navigation header
**Date:** 2025-11-30 | **Files:** 20 | **+36 lines**

Added a chatbot button to the navigation header bar across all topic pages, with supporting CSS (17 lines of new styles).

### `9381c40` - CHORE: Remove redundant bottom-right chatbot widget
**Date:** 2025-11-30 | **Files:** 33 | **-33 lines**

Removed the duplicate floating chatbot widget from all pages after moving the chatbot to the nav header.

---

## Phase 5: Echs AI Assistant (Dec 1, 2025)

### `85cb80a` - FEATURE: Add Part 0 introducing Echs AI assistant
**Date:** 2025-12-01 | **Files:** 1 | **+12 lines**

Added an introductory section to start-here.html introducing "Echs" (pronounced "X") as the course's AI guide persona.

### `2c83e66` - FIX: Clarify Echs pronunciation
**Date:** 2025-12-01 | **Files:** 1 | **+1 / -1 lines**

### `2548bf6` - FIX: Simplify Echs intro text
**Date:** 2025-12-01 | **Files:** 1 | **+1 / -1 lines**

### `72721e9` - FIX: Update punctuation in Echs intro
**Date:** 2025-12-01 | **Files:** 1 | **+1 / -1 lines**

Three quick follow-up fixes to polish the Echs introduction text.

---

## Phase 6: Major Content Expansion (Dec 7-8, 2025)

### `d5b613f` - FEATURE: Update CDS and Ambient AI modules with 2025 research
**Date:** 2025-12-07 | **Files:** 3 | **+285 / -40 lines**

Major updates to clinical-decision-support.html (+102 lines) and ambient-ai.html (+217 lines) with current 2025 research, clinical evidence, and updated tool references.

### `e67e730` - FEATURE: Update Image/Video and Everyday AI modules with 2025 tools
**Date:** 2025-12-07 | **Files:** 4 | **+374 / -78 lines**

Updated image-video.html with latest AI image generation tools (+293 lines net). Expanded everyday-ai.html with new productivity tools (+153 lines). Added a Gemini-generated demonstration image.

### `99dc9af` - FEATURE: Enhance patients-ai module with empathy focus
**Date:** 2025-12-07 | **Files:** 2 | **+298 / -21 lines**

Rewrote significant portions of patients-ai.html to focus on empathetic communication and added provider-facing tools and strategies (+316 lines).

### `f6f26d9` - FEATURE: Add AI-Powered Search module, expand Vibe Coding and Glossary
**Date:** 2025-12-07 | **Files:** 4 | **+1,607 / -69 lines**

**Largest single-commit expansion:**
- **ai-search.html** - Brand new topic (954 lines) covering AI-powered search tools (Perplexity, Google AI Overview, etc.)
- **glossary.html** - Major expansion (+340 lines) with new terms
- **vibe-coding.html** - Significant expansion (+364 lines) with updated tools and examples

### `76d7872` - CHORE: Add reading times, update embed code, wire up contribute form
**Date:** 2025-12-07 | **Files:** 21 | **+46 / -82 lines**

Added estimated reading times to all topic pages. Simplified the contribute form. Updated embed codes and minor fixes across 21 files.

### `b6d2101` - CHORE: Add author bio and fix contact email on about page
**Date:** 2025-12-08 | **Files:** 1 | **+19 / -1 lines**

Added author biography section to about.html and corrected the contact email address.

### `497b7a8` - FEATURE: Add Bias, Ethics, and Training Data module
**Date:** 2025-12-08 | **Files:** 6 | **+994 / -4 lines**

New topic page: **bias-ethics.html** (885 lines). Covers algorithmic bias in healthcare AI, ethical frameworks, and training data concerns. Also enhanced start-here.html (+75 lines) and phi-hipaa.html (+17 lines) with cross-references.

---

## Phase 7: Research & Case Studies (Dec 13, 2025)

### `935fea7` - FEATURE: Add BMJ article on parallel pressures
**Date:** 2025-12-13 | **Files:** 2 | **+13 / -2 lines**

Added reference to a BMJ research article exploring parallels between physician misinformation pressures and LLM hallucination to llm-thinking.html.

### `0ac4012` - DOCS: Add feedback loop concept from BMJ article
**Date:** 2025-12-13 | **Files:** 1 | **+8 lines**

Expanded the BMJ reference with a discussion of the feedback loop concept in llm-thinking.html.

### `2ad03f0` - CHORE: Update LLM Thinking card to show 7 readings
**Date:** 2025-12-13 | **Files:** 1 | **+1 / -1 lines**

Updated the index.html card for LLM Thinking to reflect the new reading count.

### `e28f45c` - FEATURE: Add semantic drift case study from Dr. Milgrom
**Date:** 2025-12-13 | **Files:** 1 | **+61 lines**

Added a real-world case study to clinical-decision-support.html illustrating semantic drift in AI-assisted clinical workflows, contributed by Dr. Milgrom.

---

## Phase 8: About Page & Link Fixes (Dec 14, 2025)

### `d57b07c` - CHORE: Remove unbuilt sections from About
**Date:** 2025-12-14 | **Files:** 1 | **-38 lines**

Removed placeholder sections ("Small Experiment" and "The Catch") from about.html that were never built out.

### `db1f3de` - FEATURE: Add Buy Me a Coffee support button
**Date:** 2025-12-14 | **Files:** 1 | **+2 lines**

Added a Buy Me a Coffee donation button to the about page.

### `fb579ee` - DOCS: Add support blurb above Buy Me a Coffee button
**Date:** 2025-12-14 | **Files:** 1 | **+4 lines**

Added explanatory text above the donation button.

### `4223291` - FIX: Replace broken NotebookLM YouTube link
**Date:** 2025-12-14 | **Files:** 2 | **+7 / -7 lines**

Fixed a broken YouTube link in start-here.html and unit-0-new.html, replacing it with the official NotebookLM tutorial.

### `34a9d90` - FIX: Correct broken links in PHI/HIPAA module resources
**Date:** 2025-12-14 | **Files:** 1 | **+10 / -10 lines**

Fixed 10 broken resource links in phi-hipaa.html.

### `e7cbebe` - FIX: Correct broken links and remove redundant content
**Date:** 2025-12-14 | **Files:** 2 | **+2 / -52 lines**

Fixed links in phi-hipaa.html and removed 50 lines of redundant content from prompting.html.

### `05fce23` - CHORE: Remove broken/not useful resources
**Date:** 2025-12-14 | **Files:** 3 | **+1 / -58 lines**

Cleaned out broken or low-value resource links from glossary.html, image-video.html, and patients-ai.html.

---

## Phase 9: What's Next Module (Dec 15, 2025)

### `cc3fcfc` - FEATURE: Add What's Next module with blue card styling
**Date:** 2025-12-15 | **Files:** 3 | **+675 lines**

New topic page: **whats-next.html** (636 lines). A forward-looking module guiding learners on next steps after completing the course. Added new blue card styling to styles.css (+26 lines) for the "What's Next" category.

### `691d624` - FEATURE: Expand What's Next module to ~6,200 words
**Date:** 2025-12-15 | **Files:** 2 | **+927 / -64 lines**

Major expansion of whats-next.html with developer foundations content, bringing the module to approximately 6,200 words. Added sections on building with AI APIs, contributing to healthcare AI, and career pathways.

---

## Phase 10: Updates Page & Version Bump (Dec 16, 2025)

### `948fe16` - FEATURE: Add Updates page and bump version to v1.1
**Date:** 2025-12-16 | **Files:** 40 | **+270 / -39 lines**

New page: **updates.html** (197 lines). A changelog/updates page documenting site changes for visitors. Bumped the site version to v1.1 across all page footers. Enhanced the whats-next.html with additional content.

### `6b8a8c1` - CHORE: Add AI Cred resource, update changelog
**Date:** 2025-12-16 | **Files:** 2 | **+4 / -7 lines**

Added "AI Cred" resource link. Cleaned up the updates page.

### `ec96868` - CHORE: Add GitHub commit history link to updates page
**Date:** 2025-12-16 | **Files:** 1 | **+2 / -1 lines**

Added a direct link to the GitHub commit history on the updates page for transparency.

---

## Phase 11: Big Three Rewrite & Image Updates (Dec 17-18, 2025)

### `bec853a` - REFACTOR: Rewrite Big Three module to remove subjective claims
**Date:** 2025-12-17 | **Files:** 3 | **+1,235 / -165 lines**

**Major content rewrite.** Rewrote big-three.html to remove subjective model comparison claims and replace them with factual, evidence-based descriptions. Archived the original version as **big-three-v1.0-archive.html** (1,043 lines) for reference. Updated the updates page.

### `ca5ad5d` - FEATURE: Update image module with GPT-4o native image generation
**Date:** 2025-12-18 | **Files:** 2 | **+42 / -6 lines**

Updated image-video.html with information about GPT-4o's native image generation capabilities.

### `0e7ffaf` - FIX: Correct image module with GPT Image 1.5
**Date:** 2025-12-18 | **Files:** 2 | **+25 / -27 lines**

Corrected the image-video.html content to accurately reflect GPT Image 1.5 (released December 16, 2025), replacing the earlier GPT-4o native image references.

---

## Phase 12: UI Polish (Dec 20, 2025)

### `5a5f55a` - FEATURE: Add module update dates to home screen cards
**Date:** 2025-12-20 | **Files:** 3 | **+63 / -2 lines**

Added "last updated" date labels to each topic card on index.html, so visitors can see which content is most recently revised. New CSS for date badges. Updated the updates page with a comprehensive list of all update dates.

---

## Phase 13: New Year Features (Jan 1, 2026)

### `b782656` - FEATURE: Add favicon to site
**Date:** 2026-01-01 | **Files:** 43 | **+42 lines**

Added **favicon.png** and linked it across all 42 HTML pages for consistent branding.

### `f0f19bb` - FEATURE: Add AI Resolution Challenge promo sticker
**Date:** 2026-01-01 | **Files:** 3 | **+62 lines**

Added a promotional "AI Resolution Challenge" sticker graphic to the hero section of the homepage. Included new image asset (aidb-sticker-bg.png) and 58 lines of CSS for sticker styling and animation.

### `4de4b73` - FEATURE: Add AI News page with RSS feed
**Date:** 2026-01-01 | **Files:** 4 | **+215 lines**

New page: **ai-news.html** (126 lines). A curated AI healthcare news feed for clinicians. Also created **ai-news-feed.xml** (20 lines) as an RSS feed. Added a news card to the homepage and new CSS styles for the news layout.

---

## Phase 14: AI News Expansion (Jan 6 - Feb 1, 2026)

### `6530a14` - FEATURE: Add OpenAI Healthcare Ally document to AI News
**Date:** 2026-01-06 | **Files:** 1 | **+15 lines**

Added a news item covering OpenAI's Healthcare Ally announcement.

### `424cf25` - FEATURE: Add multiple AI news items for January 2026
**Date:** 2026-01-16 | **Files:** 3 | **+125 / -2 lines**

Bulk addition of January 2026 news items to ai-news.html and ai-news-feed.xml. Added new CSS for news item styling.

### `8187527` - FEATURE: Update AI news and remove New Year challenge
**Date:** 2026-02-01 | **Files:** 2 | **+65 / -4 lines**

Added February 2026 news items. Removed the expired AI Resolution Challenge sticker from the homepage.

---

## Phase 15: Domain & Planning (Feb 4-10, 2026)

### `3560392` - FEATURE: Add CNAME and domain setup plan
**Date:** 2026-02-04 | **Files:** 2 | **+143 lines**

Added CNAME file for clinicians.ai101.health custom domain. Created a detailed domain setup plan document at **docs/plans/2026-02-04-custom-domain-setup.md**.

### `7b95bc4` - CHORE: Archive session 2026-02-04
**Date:** 2026-02-04 | **Files:** 4 | **+107 lines**

Archived the February 4 development session with session summary, changelog, metrics, and updated project worklist.

### `68b6b86` - FIX: Remove CNAME to restore GitHub Pages site
**Date:** 2026-02-06 | **Files:** 1 | **-1 line**

Removed the CNAME file as it was interfering with the existing GitHub Pages deployment before DNS was properly configured.

### `4275009` - FEATURE: Update vibe coding module and add AI Off Call series design
**Date:** 2026-02-10 | **Files:** 2 | **+1,072 / -13 lines**

Updated vibe-coding.html with expanded content (+117 lines net). Created a comprehensive design document for a new "AI Off Call" educational series at **docs/plans/2026-02-07-ai-off-call-series-design.md** (968 lines).

### `6fb619b` - CHORE: Archive session 2026-02-07
**Date:** 2026-02-10 | **Files:** 4 | **+97 / -1 lines**

Archived the February 7 development session with session artifacts.

---

## Summary: Content Growth Over Time

| Date | Topics Available | Key Milestone |
|------|-----------------|---------------|
| Nov 28 | 13 modules + 2 appendices | Initial launch |
| Nov 28 | 16 topics (renamed) | Restructured to topics, added 3 new |
| Nov 30 | 17 topics + contribute page | Quality pass, chatbot, benchmarks |
| Dec 1 | 17 topics | Echs AI assistant introduced |
| Dec 7 | 18 topics | AI Search added, 5 topics expanded |
| Dec 8 | 19 topics | Bias & Ethics added |
| Dec 15 | 20 topics | What's Next added |
| Dec 16 | 20 topics + Updates page | Version v1.1, updates page |
| Jan 1 | 20 topics + AI News | Favicon, news feed, resolution challenge |
| Feb 10 | 20 topics + AI News | AI Off Call series planned |

## Current Topic Pages

**Foundations:**
- Start Here (start-here.html)
- How LLMs Think (llm-thinking.html)
- PHI & HIPAA (phi-hipaa.html)
- Prompting (prompting.html) + Exercise (prompting-exercise.html)
- The Big Three (big-three.html)

**Clinical:**
- Clinical Decision Support (clinical-decision-support.html)
- Ambient AI (ambient-ai.html)
- When Patients Use AI (patients-ai.html)
- Bias, Ethics & Training Data (bias-ethics.html)

**Tools & Applications:**
- Image & Video AI (image-video.html)
- Everyday AI (everyday-ai.html)
- AI-Powered Search (ai-search.html)
- Vibe Coding (vibe-coding.html)

**Advanced & Resources:**
- AI 101 for Medical Learners (medical-learners.html)
- Running Local Models (local-models.html)
- Environmental Footprint (environmental-footprint.html)
- Glossary (glossary.html)
- What's Next (whats-next.html)

**Meta Pages:**
- About (about.html)
- Updates (updates.html)
- AI News (ai-news.html)
- Contribute (contribute.html)
- Resources (resources.html)
