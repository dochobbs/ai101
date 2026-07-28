# 14 Days to GitHub — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship `github.html`, a self-contained 14-day module that takes a clinician from a folder on their laptop to a backed-up repo they can branch, review, merge, and resolve conflicts in — plus retrofit `claude-code.html` Days 19–20 to hand off to it.

**Architecture:** A single static HTML page built on the exact chassis of `claude-code.html` — embedded CSS, `article.day` cards, sidebar with scroll-spy, localStorage progress meter. No build step, no framework, no dependencies. Deployed by pushing to `main` (GitHub Pages, apex domain).

**Tech Stack:** Static HTML5, embedded CSS custom properties, vanilla JS (one IIFE), Google Fonts, Lucide icons (index only), Pickaxe embed for the Echs chat widget.

**Approved spec:** `docs/plans/2026-07-27-github-module-design.md`

## Global Constraints

- **No emojis anywhere.** Site-wide convention.
- **Typographic characters use HTML entities** to match the existing files: `&mdash;` for em dash, `&rsquo;`/`&ldquo;`/`&rdquo;` for curly quotes. Literal curly characters also appear in `claude-code.html`; either is acceptable, but be consistent within a block.
- **Learners never touch the `ai101` repo.** No instruction anywhere in the module may direct a reader to open an issue or pull request against `dochobbs/ai101`. Every command runs against the learner's own repository.
- **New repos are created `--private`.** The audience is clinicians who may put personal notes in a file. Public is mentioned as an option they can choose later, never as the default.
- **`.gitignore` is taught before the first push** (Day 6 before Day 8). This ordering is a safety requirement, not a preference.
- **localStorage key is `github14-progress-v1`.** It must never be `claude30-progress-v1` — sharing the key would corrupt the other module's meter.
- **`TOTAL = 15`** (days 0 through 14 inclusive).
- **Footer version is `v1.13 · 2026`** on every page after Task 8.
- **Canonical/OG URLs use `https://ai101.health/`**, never the `github.io` origin.
- **No new external dependencies.** Fonts and the existing Pickaxe bundle only.
- **`contribute.html` is out of scope.** Do not add a submission route to it in this build.

---

## File Structure

**Create:**
- `github.html` — the entire module. Self-contained: embedded `<style>`, embedded `<script>`, no shared CSS file. This matches `claude-code.html`, which is also self-contained; `styles.css` serves the *topic* pages, not the module pages.

**Modify:**
- `claude-code.html` — Days 19–20 retrofit (lines 1471–1526), footer cross-link (line ~1950), version bump
- `index.html` — new module card after line 352, version bump
- `sitemap.xml` — one new `<url>` entry
- `updates.html` — v1.13 entry
- All remaining root `*.html` — footer version bump only

**Deliberate duplication:** `github.html` copies the ~780-line `<style>` block from `claude-code.html` rather than extracting a shared `module.css`. Extraction would mean rewriting the styling of the site's flagship page with no CI and no visual regression tests to catch a mistake. The duplication is the cheaper risk. If a third module is ever built, extract then.

---

## Voice Guide

Read `claude-code.html:1013–1100` before writing any day. The house voice:

- Second person, present tense, short sentences. "Open the terminal. Type this. Press Enter."
- Commands are always in a `.codeblock` with a `.copy-btn`, one command block per idea, with a sentence of plain English before it explaining what it does.
- Reassurance is specific, never generic. Not "don't worry" but "You won't see this prompt again on this computer."
- Every day ends with a `.learned` box: one or two sentences, the takeaway in plain language.
- `.callout` boxes carry a `.callout-label` naming what kind of aside it is: "First time only", "If something goes wrong", "Windows".
- Never claim the reader will remember a command. The recurring promise is that they can ask.

Structural template for every day, copied verbatim from `claude-code.html:1012–1042`:

```html
<article class="day" id="day-N">
  <header class="day-header"><span class="day-label">Day 0N</span><h3 class="day-title">Title</h3></header>
  <div class="day-body">
    <p>Plain-English framing.</p>
    <div class="codeblock"><pre>command here</pre><button class="copy-btn">Copy</button></div>
    <div class="callout">
      <div class="callout-label">Label</div>
      Aside text.
    </div>
    <div class="learned">
      <div class="learned-label">What you just learned</div>
      The takeaway.
    </div>
    <button class="complete-btn" data-day="N"><span class="check"></span><span class="label">Mark complete</span></button>
  </div>
</article>
```

---

## Verification Harness

There is no test framework and no CI in this repo — confirmed, there is no `.github/` directory. Verification is a local server plus structural assertions plus a browser pass.

**Serve locally** (used by every task's verification step):

```bash
cd /Users/dochobbs/Downloads/ai101 && python3 -m http.server 8765
```

Port 8765 is the port used for the v1.10 visual verification pass. Check it is free first with `lsof -iTCP:8765 -sTCP:LISTEN -P -n`.

**Structural assertion script** — save as `/tmp/check-github-module.sh` in Task 1, re-run at the end of every content task:

```bash
#!/usr/bin/env bash
set -u
F=github.html
fail=0
chk() { # chk <description> <expected> <actual>
  if [ "$2" = "$3" ]; then echo "ok   $1 ($3)"; else echo "FAIL $1 — expected $2, got $3"; fail=1; fi
}
chk "day articles"       "$1" "$(grep -c '<article class="day"' $F)"
chk "complete buttons"   "$1" "$(grep -c 'class="complete-btn"' $F)"
chk "sidebar day links"  "$1" "$(grep -c 'class="nav-day"' $F)"
chk "copy buttons match codeblocks" "$(grep -c '<div class="codeblock">' $F)" "$(grep -c 'class="copy-btn"' $F)"
chk "correct storage key" "1" "$(grep -c 'github14-progress-v1' $F)"
chk "no claude30 key"     "0" "$(grep -c 'claude30-progress-v1' $F)"
chk "TOTAL is 15"         "1" "$(grep -c 'const TOTAL = 15' $F)"
chk "no ai101 issue/PR instructions" "0" "$(grep -ci 'gh issue create --repo\|dochobbs/ai101' $F)"
chk "no emoji" "0" "$(grep -cP '[\x{1F300}-\x{1FAFF}\x{2700}-\x{27BF}]' $F)"
echo "---"; [ $fail -eq 0 ] && echo "ALL CHECKS PASS" || echo "FAILURES PRESENT"
exit $fail
```

Called as `bash /tmp/check-github-module.sh <expected-day-count>`.

**Browser pass** — after each content task, use the Playwright MCP tools: navigate to `http://localhost:8765/github.html`, take a snapshot, read console messages. Expected: zero console errors, sidebar renders, progress meter reads `0`.

---

## Task 1: Scaffold `github.html`

Produces a complete, styled, working page with zero day content. Everything structural is decided here so the content tasks only insert `<article>` blocks.

**Files:**
- Create: `github.html`
- Create: `/tmp/check-github-module.sh` (from the Verification Harness section above)
- Reference: `claude-code.html:1–1011` (head, style, sidebar, hero, intro)

**Interfaces:**
- Produces: the page shell with three empty `<section class="phase">` containers (`#phase-1`, `#phase-2`, `#phase-3`) and an empty sidebar `<nav>`; the `<script>` IIFE with `STORAGE_KEY = "github14-progress-v1"` and `TOTAL = 15`. Content tasks insert `<article class="day">` blocks after the matching phase section and `<a class="nav-day">` links into the sidebar.

- [ ] **Step 1: Copy the chassis**

```bash
cd /Users/dochobbs/Downloads/ai101
cp claude-code.html github.html
```

- [ ] **Step 2: Strip all day content and phase sections from the copy**

Delete every `<article class="day">…</article>` block and every `<section class="phase">…</section>` block from `github.html`. Delete every `<a class="nav-day">` from the sidebar. Delete the closing sections after the last day (the troubleshooting `<section>` and closing paragraph) — they get rewritten in Task 5. Keep: `<head>`, the `<style>` block, `<nav>`, the hero, the sidebar shell with its progress meter and Echs div, the site footer, and the `<script>`.

- [ ] **Step 3: Rewrite the head**

Replace the head metadata. Exact values:

```html
<title>14 Days to GitHub · Where Your Work Lives</title>
<meta name="description" content="A 14-day, 10-minutes-a-day module that takes clinicians from a folder on their laptop to a backed-up GitHub repository they can branch, review, merge, and recover.">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://ai101.health/github.html">
  <meta property="og:title" content="14 Days to GitHub · Where Your Work Lives">
  <meta property="og:description" content="A 14-day, 10-minutes-a-day module that takes clinicians from a folder on their laptop to a backed-up GitHub repository they can branch, review, merge, and recover.">
  <meta property="og:image" content="https://ai101.health/og-image.png">
  <meta property="og:site_name" content="AI 101">
  <meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="https://ai101.health/github.html">
```

- [ ] **Step 4: Swap the favicon digits**

The inline SVG favicon renders `30`. Change the text node to `14`:

```html
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%231e293b'/%3E%3Ctext x='16' y='23' font-family='ui-monospace,monospace' font-size='17' font-weight='700' fill='%23fb923c' text-anchor='middle'%3E14%3C/text%3E%3C/svg%3E">
```

- [ ] **Step 5: Reduce phase accent cycling from four phases to three**

In the `<style>` block, find the four rules near line 731 and delete the `#phase-4` rule entirely. Keep `#phase-1` (teal), `#phase-2` (violet), `#phase-3` (orange). The remaining three rules are unchanged:

```css
#phase-1, #phase-1 ~ article.day { --accent:#0d9488; --accent-hover:#0f766e; --accent-soft:#99f6e4; --accent-faint:#ccfbf1; }
#phase-2, #phase-2 ~ article.day { --accent:#7c3aed; --accent-hover:#6d28d9; --accent-soft:#ddd6fe; --accent-faint:#ede9fe; }
#phase-3, #phase-3 ~ article.day { --accent:#ea580c; --accent-hover:#c2410c; --accent-soft:#fed7aa; --accent-faint:#ffedd5; }
```

- [ ] **Step 6: Update the script constants**

```javascript
const STORAGE_KEY = "github14-progress-v1";
const TOTAL = 15; // days 0–14
```

- [ ] **Step 7: Write the hero and intro**

Replace the hero copy. The intro must establish the frame and promise, and must state that the module stands alone. Required beats:

- The one-line frame, used verbatim: *Git is your memory. GitHub is your meeting place. Claude is your guide. The command line is the country you are learning to navigate.*
- Git as a travel journal: each commit is a dated entry saying this is what the project looked like at this moment.
- GitHub as base camp: where the journal lives online, gets backed up, and can be read by someone else.
- The shape of the two weeks: five days keeping a journal locally, four days getting it online, five days on side roads and review.
- An explicit note that finishing *30 Days to Claude Code* helps but is not required, with a link to `claude-code.html`.
- Ten minutes a day.

- [ ] **Step 8: Write the three empty phase sections**

```html
<section class="phase" id="phase-1">
  <div class="phase-num">Phase One</div>
  <h2 class="phase-title">Your Own Journal</h2>
  <p class="phase-sub">Days 1 to 5 · Everything stays on your laptop.</p>
  <p class="phase-intro">Nothing leaves your machine this week. No account, no audience, nothing to be embarrassed about. You are just learning to keep a journal of your own work &mdash; what changed, when, and why.</p>
</section>

<section class="phase" id="phase-2">
  <div class="phase-num">Phase Two</div>
  <h2 class="phase-title">Base Camp</h2>
  <p class="phase-sub">Days 6 to 9 · The work goes online.</p>
  <p class="phase-intro">This week your journal gets a home that isn&rsquo;t your hard drive. We start by deciding what should never leave the laptop, then send everything else somewhere safe.</p>
</section>

<section class="phase" id="phase-3">
  <div class="phase-num">Phase Three</div>
  <h2 class="phase-title">Side Roads</h2>
  <p class="phase-sub">Days 10 to 14 · Trying things without breaking things.</p>
  <p class="phase-intro">The last five days are the ones people think are hard: branches, pull requests, review, and the dreaded merge conflict. You are going to cause a merge conflict on purpose and fix it, which is the fastest way to stop being afraid of one.</p>
</section>
```

- [ ] **Step 9: Update the site footer**

```html
<footer class="site-footer">
  <div><strong>AI 101</strong> · <a href="index.html">A Self-Paced Guide to AI in Medicine</a></div>
  <div><a href="claude-code.html">30 Days to Claude Code</a> · <a href="vibe-coding.html">Vibe Coding module</a> · <a href="https://docs.github.com/en/get-started" target="_blank" rel="noopener">Official GitHub docs</a></div>
  <div><a href="updates.html">v1.13 · 2026</a></div>
</footer>
```

- [ ] **Step 10: Save the verification script**

Write the script from the Verification Harness section to `/tmp/check-github-module.sh`.

- [ ] **Step 11: Verify the shell**

```bash
cd /Users/dochobbs/Downloads/ai101 && bash /tmp/check-github-module.sh 0
```

Expected: all checks pass with 0 day articles, 0 complete buttons, 0 nav-day links, storage key present, TOTAL is 15, no `claude30` key, no `dochobbs/ai101` reference, no emoji.

- [ ] **Step 12: Browser check**

Start `python3 -m http.server 8765`, navigate to `http://localhost:8765/github.html`, snapshot, read console.
Expected: page renders with hero, three phase headers, empty sidebar, progress meter showing `0`. Zero console errors.

- [ ] **Step 13: Commit**

```bash
git add github.html
git commit -m "FEATURE: 14 Days to GitHub — page scaffold"
```

---

## Task 2: Day 0 and Phase 1 (Days 1–5)

**Files:**
- Modify: `github.html` — insert six `<article>` blocks and six sidebar links

**Interfaces:**
- Consumes: the phase shell and script from Task 1
- Produces: `~/github-lab` as the working folder referenced by every later day; `notes.md`, `ideas.md`, `todo.md` as the three tracked files; the first commit on `main`

Sidebar links to add (Day 0 above the Phase 1 group, then the five):

```html
<a class="nav-day" href="#day-0" data-day="0"><span class="day-dot"></span><span class="day-num">00</span><span>Base Camp Setup</span></a>
<a class="nav-day" href="#day-1" data-day="1"><span class="day-dot"></span><span class="day-num">01</span><span>Start the Journal</span></a>
<a class="nav-day" href="#day-2" data-day="2"><span class="day-dot"></span><span class="day-num">02</span><span>Where Am I?</span></a>
<a class="nav-day" href="#day-3" data-day="3"><span class="day-dot"></span><span class="day-num">03</span><span>Packing the Bag</span></a>
<a class="nav-day" href="#day-4" data-day="4"><span class="day-dot"></span><span class="day-num">04</span><span>The Dated Entry</span></a>
<a class="nav-day" href="#day-5" data-day="5"><span class="day-dot"></span><span class="day-num">05</span><span>What Changed</span></a>
```

- [ ] **Step 1: Write Day 0 — Base Camp Setup**

Framing: two different tools with confusingly similar names. `git` runs on your machine and keeps the journal. `gh` talks to GitHub. Today installs both and proves they work.

Commands, in order, each in its own `.codeblock`:

```
git --version
```
```
brew install gh
```
```
winget install --id GitHub.cli
```
```
gh auth login
```
```
gh auth status
```

Required callouts:
- `.callout` labelled **"Windows"** — use the `winget` line instead of `brew`; everything after that is identical.
- `.callout` labelled **"First time only"** — `gh auth login` opens a browser and asks for a one-time code. Choose HTTPS when it asks about protocol. You will not do this again on this computer.
- `.callout` labelled **"Before you start"** — you need a free GitHub account. Sign up at github.com first; the username you pick will be visible on anything you publish, so pick one you would put on a CV.

Learned box: *Git keeps the journal on your machine. GitHub stores it online. `gh` is the phone line between them. Nothing is tracked yet.*

- [ ] **Step 2: Write Day 1 — Start the Journal**

Framing: the repository is the whole expedition folder — maps, journal, supply list, and the record of the trip. `git init` is telling git to start watching one.

Cold-start block, in a `.callout` labelled **"Starting here?"** — if you did not do 30 Days to Claude Code, make a practice folder now:

```
mkdir ~/github-lab
cd ~/github-lab
echo "Things I want to remember" > notes.md
echo "Half-formed ideas" > ideas.md
echo "Things to do" > todo.md
```

Otherwise: `cd` into the tool you built on Day 21 or Day 27 of the Claude Code module.

Then:

```
git init
```
```
ls -a
```

Point out the new `.git` folder and say plainly: that folder is the journal. Do not open it, do not edit it, and never delete it unless you mean to throw the history away.

Claude prompt block:

```
I just ran git init in this folder. In plain English, what did that actually do?
```

Learned box: *A repository is just a folder git has agreed to watch. Making one changes nothing about your files &mdash; and nothing has been saved yet.*

- [ ] **Step 3: Write Day 2 — Where Am I?**

Framing: the working directory is what is spread out on the table right now. `git status` asks two questions at once: where am I, and what have I changed?

```
git status
```

Explain the output: three untracked files, nothing staged, nothing committed. Then have them change something:

```
echo "Blood pressure cuff sizes are a menace" >> notes.md
```
```
git status
```

Claude prompt block:

```
Explain this git status output to me line by line, like I've never seen it before.
```

Learned box: *`git status` is the question you will ask more than any other. When you are lost, it is always the right first move.*

- [ ] **Step 4: Write Day 3 — Packing the Bag**

Framing: staging is packing the bag before you leave. You choose exactly what goes in this trip and what waits for the next one.

```
git add notes.md
```
```
git status
```

Point out the two groups now visible: `notes.md` is staged, the other two are not. That split is the whole point of the day.

Show it is reversible:

```
git restore --staged notes.md
```
```
git status
```

Then stage everything for real:

```
git add .
```

`.callout` labelled **"Why not always `git add .`?"** — because a commit should be one idea. If you fixed a typo and rewrote a whole section, staging them separately gives you two clean entries instead of one confusing one. Today it does not matter. On a real project it will.

Learned box: *Staging is a choice, not a formality. It is the difference between "everything I touched" and "the part I meant."*

- [ ] **Step 5: Write Day 4 — The Dated Entry**

Framing: the commit is the dated journal entry. This is what the project looked like at this moment, and here is what I was doing.

```
git commit -m "Start tracking notes, ideas, and todo"
```
```
git log
```
```
git log --oneline
```

`.callout` labelled **"On messages"** — write the message for the version of you who reads it in six months with no memory of today. "Fixed stuff" tells that person nothing. "Fix wrong cuff size in notes" tells them everything. It takes the same four seconds.

Learned box: *A commit is a dated entry with your name on it. The history you are building is only as useful as the messages you write.*

- [ ] **Step 6: Write Day 5 — What Changed**

Framing: comparing today's map against the last saved version.

```
echo "Ask about the vaccine fridge alarm" >> todo.md
```
```
git diff
```

Explain the `+` lines. Then the twist that teaches the concept:

```
git add todo.md
```
```
git diff
```

It is empty now. That surprises everyone. Then:

```
git diff --staged
```

`.callout` labelled **"Why it went blank"** — `git diff` compares the table to the bag. `git diff --staged` compares the bag to the last entry. Once you pack something, it is no longer on the table.

Then commit:

```
git commit -am "Add fridge alarm to todo"
```

Learned box: *`git diff` and `git diff --staged` answer two different questions. Knowing which one you are asking is most of the confusion, gone.*

- [ ] **Step 7: Verify**

```bash
cd /Users/dochobbs/Downloads/ai101 && bash /tmp/check-github-module.sh 6
```
Expected: 6 day articles, 6 complete buttons, 6 nav-day links, all other checks pass.

- [ ] **Step 8: Browser check**

Navigate to `http://localhost:8765/github.html`. Click "Mark complete" on Day 1, reload the page, confirm it is still marked. Open a second tab on `claude-code.html` and confirm *its* meter is unaffected.
Expected: progress persists on `github.html`, `claude-code.html` meter unchanged. Zero console errors.

- [ ] **Step 9: Commit**

```bash
git add github.html
git commit -m "CONTENT: 14 Days to GitHub — Day 0 and Phase 1"
```

---

## Task 3: Phase 2 (Days 6–9)

**Files:**
- Modify: `github.html` — insert four `<article>` blocks and four sidebar links

**Interfaces:**
- Consumes: `~/github-lab` with committed history on `main` from Task 2
- Produces: a private GitHub repo named `github-lab` with `origin` configured; a local clone at `~/github-lab-copy` used by no later task

Sidebar links:

```html
<a class="nav-day" href="#day-6" data-day="6"><span class="day-dot"></span><span class="day-num">06</span><span>What Stays Behind</span></a>
<a class="nav-day" href="#day-7" data-day="7"><span class="day-dot"></span><span class="day-num">07</span><span>A Note for the Next Traveler</span></a>
<a class="nav-day" href="#day-8" data-day="8"><span class="day-dot"></span><span class="day-num">08</span><span>Base Camp</span></a>
<a class="nav-day" href="#day-9" data-day="9"><span class="day-dot"></span><span class="day-num">09</span><span>Bringing It Home</span></a>
```

- [ ] **Step 1: Write Day 6 — The Things That Stay Behind**

Framing: every expedition has things that do not go in the journal — scratch paper, receipts, the key to the cabin. `.gitignore` is that list. **This comes before anything goes online, on purpose.**

```
touch .gitignore
```

Contents to put in it:

```
.DS_Store
*.log
.env
secrets.txt
```

Then:

```
git status
```

Note that `.DS_Store` clutter is gone from the output. Then commit the ignore file itself:

```
git add .gitignore
git commit -m "Add gitignore"
```

`.callout` labelled **"This one matters"** — the most common way people get burned by git is committing a password or an API key, then pushing it somewhere public. Git never forgets, so deleting the file afterward does not help: the key is still in the history. If it ever happens to you, the fix is not to delete the file. The fix is to go to whoever issued the key and revoke it. Assume it is compromised the moment it is pushed.

Claude prompt block:

```
Look at the files in this folder and tell me if any of them contain something that should never be committed to git.
```

Learned box: *`.gitignore` is the list of what stays out of the journal. Write it before your first push, not after.*

- [ ] **Step 2: Write Day 7 — A Note for the Next Traveler**

Framing: the README is the note you hand someone arriving cold — where they are, what this is for, how to start.

Claude prompt block:

```
Write a short README.md for this folder. Explain what it is, who it's for, and how someone would start using it. Keep it under 200 words and don't make it sound like a corporate press release.
```

Then have them edit it so it sounds like them, and commit:

```
git add README.md
git commit -m "Add README"
```

`.callout` labelled **"Why bother, if it's just you?"** — because in four months you will be the stranger. The README is the fastest note-to-self you will ever write.

Learned box: *A README is the difference between a folder someone can use and a folder someone abandons.*

- [ ] **Step 3: Write Day 8 — Base Camp**

Framing: a remote is another known location where a copy of the expedition lives. `origin` is just git's default nickname for the one you started from. Today the journal stops being only on your laptop.

```
gh repo create github-lab --private --source=. --remote=origin --push
```

Break the flags down in prose: `--private` means only you can see it, `--source=.` means use this folder, `--remote=origin` names the connection, `--push` sends everything up immediately.

```
git remote -v
```
```
gh repo view --web
```

Then have them make one more change and push it manually, so `push` is a thing they have done on its own:

```
echo "Base camp established" >> notes.md
git commit -am "Note that the repo is live"
git push
```

`.callout` labelled **"Private on purpose"** — we are starting private because a practice folder is exactly where a stray phone number or patient initial ends up. When you have a project you actually want to share, you can flip it in the repo settings, or create the next one with `--public`. Never flip a repo public without reading its history first.

`.callout` labelled **"No PHI, ever"** — this is a public-internet service with no BAA. Nothing that identifies a patient goes in a repo, private or not.

Learned box: *Your journal now exists in two places. If the laptop dies tonight, the work does not.*

- [ ] **Step 4: Write Day 9 — Bringing It Home**

Framing: cloning is making a complete local copy of shared expedition materials. Pulling is bringing back what changed while you were away.

```
cd ~
git clone https://github.com/YOUR-USERNAME/github-lab.git github-lab-copy
cd github-lab-copy
ls
```

Everything is there, including the history:

```
git log --oneline
```

Now make a change in the copy and push it:

```
echo "Edited from the clone" >> notes.md
git commit -am "Edit from the clone"
git push
```

Then go back to the original and pull it down:

```
cd ~/github-lab
git pull
cat notes.md
```

`.callout` labelled **"What just happened"** — you edited a file in one folder and it appeared in another, because both are talking to the same base camp. That is the entire idea behind working with other people, rehearsed with only yourself involved.

Learned box: *Clone makes a copy. Pull brings changes home. This is the whole mechanism behind collaboration, and you just did both halves.*

- [ ] **Step 5: Verify**

```bash
cd /Users/dochobbs/Downloads/ai101 && bash /tmp/check-github-module.sh 10
```
Expected: 10 day articles, 10 complete buttons, 10 nav-day links, all other checks pass.

Additional assertion — confirm `.gitignore` is taught before `git push`:

```bash
[ "$(grep -n 'id="day-6"' github.html | cut -d: -f1)" -lt "$(grep -n 'id="day-8"' github.html | cut -d: -f1)" ] && echo "ok: gitignore precedes push" || echo "FAIL: ordering violated"
```

- [ ] **Step 6: Browser check**

Navigate to `http://localhost:8765/github.html`, scroll to Phase 2, confirm the accent color changes from teal to violet at the Phase Two header and that the sidebar highlights track scrolling.
Expected: correct per-phase accent, scroll-spy active, zero console errors.

- [ ] **Step 7: Commit**

```bash
git add github.html
git commit -m "CONTENT: 14 Days to GitHub — Phase 2"
```

---

## Task 4: Phase 3 (Days 10–14)

**Files:**
- Modify: `github.html` — insert five `<article>` blocks and five sidebar links

**Interfaces:**
- Consumes: `~/github-lab` with a configured `origin` from Task 3
- Produces: nothing later tasks depend on; this is the end of the curriculum

Sidebar links:

```html
<a class="nav-day" href="#day-10" data-day="10"><span class="day-dot"></span><span class="day-num">10</span><span>The Side Road</span></a>
<a class="nav-day" href="#day-11" data-day="11"><span class="day-dot"></span><span class="day-num">11</span><span>Pin a Note to the Board</span></a>
<a class="nav-day" href="#day-12" data-day="12"><span class="day-dot"></span><span class="day-num">12</span><span>Presenting the Route</span></a>
<a class="nav-day" href="#day-13" data-day="13"><span class="day-dot"></span><span class="day-num">13</span><span>The Other Travelers</span></a>
<a class="nav-day" href="#day-14" data-day="14"><span class="day-dot"></span><span class="day-num">14</span><span>Two Maps, One Disagreement</span></a>
```

- [ ] **Step 1: Write Day 10 — The Side Road**

Framing: a branch is a side road. You can drive down it, make a mess, and the main route is untouched the whole time.

```
git switch -c experiment
```
```
git status
```

Make a substantial change and commit it on the branch:

```
echo "REWRITE: this whole file is different now" >> notes.md
git commit -am "Try a different approach in notes"
```

Now the moment that teaches it:

```
git switch main
cat notes.md
```

The line is gone. Then:

```
git switch experiment
cat notes.md
```

It is back. Tell them to do that twice more and watch the file change under them, because that is the day's entire lesson and it lands physically, not conceptually.

`.callout` labelled **"Nothing is lost"** — switching branches does not delete anything. Both versions exist at once. You are choosing which one is on the table.

Learned box: *A branch lets you try something risky while the working version stays exactly where it was. This is what makes experimenting safe.*

- [ ] **Step 2: Write Day 11 — Pinning a Note to the Board**

Framing: an issue is a note pinned to the planning board — a bug, a question, an idea, a task. It is not bureaucracy; it is the thing you would otherwise forget.

Have them file one real annoyance about their own project:

```
gh issue create --title "README doesn't say how to actually start" --body "A stranger reading this still wouldn't know the first command to run."
```
```
gh issue list
```
```
gh issue view 1 --web
```

`.callout` labelled **"Make it a real one"** — do not invent a fake issue for the exercise. Pick something that genuinely bothers you about this folder. On Day 13 you are going to close it, and closing a real one feels different.

Learned box: *An issue is a note to your future self that other people can also read. Note the number it was given &mdash; you will need it on Day 12.*

- [ ] **Step 3: Write Day 12 — Presenting the Route**

Framing: returning from a scouting trip and presenting your proposed route to the group before the official map changes.

```
git switch experiment
git push -u origin experiment
```

Explain `-u`: it tells git this local branch and that remote branch are the same road, so future pushes need no arguments.

```
gh pr create --title "Rework the notes file" --body "Closes #1"
```

`.callout` labelled **"That `Closes #1` is not decoration"** — put the word `Closes` and your issue number in the description and GitHub will close that issue automatically the moment this is merged. Two things stay in sync for free.

```
gh pr view --web
```

**This is the day they leave the terminal.** Walk them through the browser: the Files changed tab, the green and red lines, the comment box. Say plainly why — reading a diff is a visual act, and pretending the terminal is better at it would be dogma.

Learned box: *A pull request is a proposal, not a change. Nothing has moved yet. That gap between proposing and merging is where review happens.*

- [ ] **Step 4: Write Day 13 — The Other Travelers**

Framing: the other travelers check your route for cliffs, wrong turns, and better shortcuts. Today Claude plays that role, and it is genuinely useful rather than a stand-in.

```
git diff main..experiment
```

Claude prompt block:

```
You are reviewing a pull request. Run `git diff main..experiment` and read the change. You are the other traveler checking my route: where are the cliffs, what did I miss, and is there a simpler way to do this? Be direct.
```

Then merge:

```
gh pr merge --merge --delete-branch
```
```
git switch main
git pull
```

Confirm the loop closed:

```
gh issue list
```

The issue from Day 11 is gone from the open list. Point at that explicitly — the note came off the board because the work is done.

`.callout` labelled **"Why review your own work?"** — because a diff is a different view than the file. Things that looked fine while you were writing them look obviously wrong in red and green. Solo developers open pull requests on their own repos for exactly this reason.

Learned box: *Review is reading your change as a stranger would. Merge is the moment the main route officially changes.*

- [ ] **Step 5: Write Day 14 — Two Maps, One Disagreement**

Framing: two travelers edited the same part of the map differently. Git can show you the disagreement, but a person has to decide which route is right. **We are going to cause one on purpose.**

Build the collision deliberately:

```
git switch -c route-a
```

Edit the **first line** of `notes.md` to read `Route A: go around the lake` and commit:

```
git commit -am "Route A"
```

Then go back and edit the **same first line** differently:

```
git switch main
```

Edit line one to read `Route B: go over the ridge`, then:

```
git commit -am "Route B"
```

Now force the collision:

```
git merge route-a
```

It fails, and the failure is the lesson. Open `notes.md` and show them exactly what they will see:

```
<<<<<<< HEAD
Route B: go over the ridge
=======
Route A: go around the lake
>>>>>>> route-a
```

Explain each marker in plain English: everything between `<<<<<<<` and `=======` is what is on your current branch, everything between `=======` and `>>>>>>>` is what is coming in, and the job is to delete the markers and leave the text you want.

Claude prompt block:

```
I have a merge conflict in notes.md. Explain what each part of the conflict is showing me, then help me decide which version to keep.
```

Resolve, then finish:

```
git add notes.md
git commit -m "Resolve conflict between routes"
git push
```

`.callout` labelled **"The thing nobody tells you"** — a merge conflict is not an error and you have not broken anything. Git is telling you it found a decision it is not allowed to make for you. That is all a conflict has ever been.

Closing paragraph for the day, and for the module: this is the part of git that frightens people most, and you just caused one deliberately and fixed it in ten minutes.

Learned box: *Git shows the disagreement. A person decides. You are now past the thing that stops most people.*

- [ ] **Step 6: Verify**

```bash
cd /Users/dochobbs/Downloads/ai101 && bash /tmp/check-github-module.sh 15
```
Expected: 15 day articles, 15 complete buttons, 15 nav-day links, all other checks pass.

- [ ] **Step 7: Browser check**

Navigate to `http://localhost:8765/github.html`. Mark all 15 days complete in sequence and confirm the meter reaches 15 and the bar fills to 100%. Click Reset, confirm it returns to 0.
Expected: meter reads `15`, fill is 100%, reset works, zero console errors.

- [ ] **Step 8: Commit**

```bash
git add github.html
git commit -m "CONTENT: 14 Days to GitHub — Phase 3"
```

---

## Task 5: Closing sections

**Files:**
- Modify: `github.html` — append two sections after Day 14

**Interfaces:**
- Consumes: the completed 15 days
- Produces: nothing

- [ ] **Step 1: Write the "When something goes weird" section**

Model it on `claude-code.html:1800–1845` — a `<ul>` of `.weird-q` / `.weird-a` pairs. Required entries, each answered in one or two plain sentences:

- *It says "fatal: not a git repository."* — You are in the wrong folder. Run `pwd`, then `cd` to your project.
- *It asked me for a username and password and rejected them.* — GitHub stopped accepting passwords for this in 2021. Run `gh auth login` again; that replaces the password entirely.
- *I committed something I shouldn't have.* — If it has not been pushed, ask Claude to help you undo the last commit. If it has been pushed and it was a key or a password, revoke the key. Deleting the file does not remove it from history.
- *I'm on a branch and I don't know how I got here.* — `git status` tells you which branch you are on. `git switch main` takes you home.
- *It opened a text editor I don't recognize and I can't get out.* — That is vim. Type `:q!` and press Enter. This happens to everyone exactly once.
- *My push was rejected.* — Someone (probably you, from another folder) pushed first. Run `git pull`, resolve anything it flags, then push again.
- *My question isn't on this list.* — Ask Echs, the chat button on this page, or ask Claude directly in the terminal.

- [ ] **Step 2: Write the closing paragraph**

One `<p class="closing">` in the register of the Claude Code module's closer. It should land the frame one final time: the journal is yours, base camp is somewhere it can be found, and the reason any of it matters is that you can now try something risky without being afraid of it.

- [ ] **Step 3: Confirm the Echs embed survived the scaffold**

```bash
grep -c 'deployment-eac8a421-3c54-4717-bbef-54bb81b54243' github.html
grep -c 'studio.pickaxe.co/api/embed/bundle.js' github.html
```
Expected: `1` and `1`.

- [ ] **Step 4: Browser check**

Navigate to `http://localhost:8765/github.html`, confirm the Echs widget renders in the sidebar and the troubleshooting list is styled like the Claude Code module's.
Expected: widget visible, consistent styling, zero console errors.

- [ ] **Step 5: Commit**

```bash
git add github.html
git commit -m "CONTENT: 14 Days to GitHub — troubleshooting and closing"
```

---

## Task 6: Claude Code Days 19–20 retrofit

**Files:**
- Modify: `claude-code.html:1471–1526`

**Interfaces:**
- Consumes: `github.html` existing at the site root (created in Task 1)
- Produces: nothing

- [ ] **Step 1: Retitle Day 19**

Change line 1472:

```html
<header class="day-header"><span class="day-label">Day 19</span><h3 class="day-title">A Travel Journal for Your Files (Git)</h3></header>
```

- [ ] **Step 2: Delete the EHR-chart analogy**

Remove line 1476 entirely:

> If you've used an EHR, you already understand the idea: every version of the chart is kept, every change has a name and a timestamp on it, and nothing is ever really gone. Git is that, for your files.

It duplicates the work the time-machine image already does, and two images for one concept is the limit.

- [ ] **Step 3: Rewrite the Day 19 opening to lead with the journal**

Replace line 1474's paragraph with the travel-journal frame: git keeps a record of the important places your project has reached, what changed along the way, and how to get back if you take a wrong turn. Each commit is a dated entry saying this is what the project looked like at this moment. Keep the time machine as a single clause about going back, not as the frame. Keep the existing reassurance that git has a reputation for being confusing and that Claude handles the commands.

- [ ] **Step 4: Recast the three vocabulary words in the journal frame**

Replace lines 1479–1483:

```html
<ul>
  <li><strong>Repository</strong> (or &ldquo;repo&rdquo;) &mdash; the whole expedition folder git is watching.</li>
  <li><strong>Commit</strong> &mdash; one dated entry. The label is yours to write.</li>
  <li><strong>Diff</strong> &mdash; comparing today&rsquo;s map against the last entry.</li>
</ul>
```

- [ ] **Step 5: Make Day 19 self-contained**

Line 1486 hard-depends on `~/claude-lab`, and line 1494 on `reflections.md`, both built in earlier days. Soften both. Before the first codeblock, add:

```html
<p>We&rsquo;ll use your lab folder &mdash; or any folder with a couple of files in it, if you&rsquo;ve landed here without doing the earlier days.</p>
```

And change the line 1494 instruction from "Change something in reflections.md" to "Change something in one of your files."

- [ ] **Step 6: Reframe Day 20's opening to the wrong-turn image**

Keep the title, keep the exercise, and keep the caveat paragraph at line 1518 verbatim — it is the best line in the day. Reframe the opening so recovering is described as going back to the last place you knew the map was right.

- [ ] **Step 7: Add the handoff callout at the end of Day 20**

Insert before the `.learned` box at line 1520:

```html
<div class="callout">
  <div class="callout-label">Where this goes next</div>
  Git is your memory. GitHub is your meeting place. Everything you just did lives only on this laptop &mdash; when you want the journal backed up somewhere safe, readable by someone else, and able to hold two versions of an idea at once, that&rsquo;s <a href="github.html">14 Days to GitHub</a>.
</div>
```

- [ ] **Step 8: Add the cross-link to the Claude Code footer**

```html
<div><a href="github.html">14 Days to GitHub</a> · <a href="vibe-coding.html">Vibe Coding module</a> · <a href="https://code.claude.com/docs/en/overview" target="_blank" rel="noopener">Official Claude Code docs</a></div>
```

- [ ] **Step 9: Verify**

```bash
cd /Users/dochobbs/Downloads/ai101
grep -c 'Travel Journal for Your Files' claude-code.html   # expect 1
grep -ci "If you've used an EHR\|If you&rsquo;ve used an EHR" claude-code.html   # expect 0
grep -c 'github.html' claude-code.html                     # expect 2 (callout + footer)
grep -c 'reflections.md' claude-code.html                  # expect fewer than before; Day 19-20 no longer require it
grep -c 'A Time Machine for Your Files' claude-code.html   # expect 0
```

- [ ] **Step 10: Browser check**

Navigate to `http://localhost:8765/claude-code.html#day-19`, confirm the retitled day renders, the callout at the end of Day 20 links to `github.html`, and the link resolves.
Expected: no broken layout, working link, zero console errors.

- [ ] **Step 11: Commit**

```bash
git add claude-code.html
git commit -m "CONTENT: Retrofit Days 19-20 to travel-journal frame, hand off to GitHub module"
```

---

## Task 7: Site integration

**Files:**
- Modify: `index.html` (card after line 352)
- Modify: `sitemap.xml`

**Interfaces:**
- Consumes: `github.html` at the site root
- Produces: nothing

- [ ] **Step 1: Add the module card to `index.html`**

Insert immediately after the closing `</a>` of the 30 Days card at line 352:

```html
        <a href="github.html" class="week-card bonus has-badge">
          <span class="badge-new">New</span>
          <h3 class="week-title">14 Days to GitHub</h3>
          <p class="week-description">
            The sequel to 30 Days to Claude Code&mdash;14 small steps from
            &ldquo;my work lives in a folder&rdquo; to a backed-up repository you can
            branch, review, merge, and recover. Git is your memory; GitHub is
            your meeting place.
          </p>
          <div class="week-meta">
            <span><i data-lucide="calendar-days"></i> 14-day track</span>
            <span><i data-lucide="git-branch"></i> Publish and collaborate</span>
          </div>
          <span class="week-updated">New Jul 2026</span>
        </a>
```

Leave the hero ribbon at line 52 pointing at `claude-code.html`. Two ribbons is worse than one, and 30 Days remains the front door.

- [ ] **Step 2: Verify the Lucide icon name exists**

`git-branch` must be a real Lucide icon or it renders as nothing.

```bash
grep -o 'data-lucide="[^"]*"' index.html | sort -u
```

If `git-branch` is not already in use elsewhere on the site, confirm it against the Lucide set before shipping; substitute `git-merge` or fall back to `share-2` if unavailable.

- [ ] **Step 3: Add the sitemap entry**

Match the format of the existing entries exactly:

```xml
  <url>
    <loc>https://ai101.health/github.html</loc>
    <lastmod>2026-07-27</lastmod>
  </url>
```

Check whether existing entries carry `<changefreq>` or `<priority>` and mirror whatever is there.

- [ ] **Step 4: Verify**

```bash
cd /Users/dochobbs/Downloads/ai101
grep -c 'github.html' index.html    # expect 1
grep -c 'github.html' sitemap.xml   # expect 1
xmllint --noout sitemap.xml && echo "sitemap parses"
```

- [ ] **Step 5: Browser check**

Navigate to `http://localhost:8765/index.html`, confirm the new card renders beside the 30 Days card with a working icon and that clicking it reaches the module.
Expected: card styled identically to its neighbor, icon visible, link works, zero console errors.

- [ ] **Step 6: Commit**

```bash
git add index.html sitemap.xml
git commit -m "FEATURE: Add 14 Days to GitHub card and sitemap entry"
```

---

## Task 8: Version bump and changelog

**Files:**
- Modify: `updates.html`
- Modify: all root `*.html` — footer version string

**Interfaces:**
- Consumes: everything from Tasks 1–7
- Produces: nothing

- [ ] **Step 1: Count the footers to be changed**

```bash
cd /Users/dochobbs/Downloads/ai101
grep -l 'v1\.12 · 2026' *.html | tee /tmp/v112-files.txt | wc -l
```

Record the number. Note that `videos.html` and `30 Days to Claude Code _standalone_.html` are untracked and intentionally excluded from commits — leave them alone if they appear.

- [ ] **Step 2: Bump the version string**

```bash
cd /Users/dochobbs/Downloads/ai101
grep -l 'v1\.12 · 2026' *.html | grep -v 'videos.html' | grep -v 'standalone' | while read f; do
  sed -i '' 's/v1\.12 · 2026/v1.13 · 2026/g' "$f"
done
```

- [ ] **Step 3: Verify the bump**

```bash
grep -c 'v1\.13 · 2026' *.html | grep -v ':0' | wc -l   # should equal the count from Step 1, minus exclusions
grep -l 'v1\.12 · 2026' *.html                          # should return only excluded/untracked files, or nothing
```

- [ ] **Step 4: Write the v1.13 entry in `updates.html`**

Read the existing `<!-- vX.Y -->` blocks first and match the format exactly. Content to cover:

- **New: 14 Days to GitHub** — a 14-day module picking up where the Claude Code one leaves off. Local journal (Days 1–5), getting it online (Days 6–9), branches through merge conflicts (Days 10–14). Everything happens in the learner's own repository.
- **30 Days to Claude Code, Days 19–20 retrofit** — git reframed as a travel journal, made self-contained so it works without the earlier days, and now handing off to the new module.
- **Weekly audit routine hardened** — after two silent Sundays (Jul 19 and Jul 26) that were caused by blocked network access rather than a clean week, the routine now carries unresolved items forward from open audit issues, files a `DEGRADED` report when it cannot reach the web instead of exiting quietly, and distinguishes an anti-bot 403 from a genuine broken link. Model bumped to Claude Sonnet 5.

- [ ] **Step 5: Verify**

```bash
grep -c 'v1.13' updates.html    # expect at least 1
```
Read the new entry back and confirm it matches the surrounding format.

- [ ] **Step 6: Full-site browser pass**

With the server running, load `index.html`, `github.html`, `claude-code.html`, and `updates.html` in turn. Confirm every footer reads `v1.13 · 2026` and every cross-link between the two modules resolves.
Expected: consistent version, no 404s, zero console errors.

- [ ] **Step 7: Commit**

```bash
git add updates.html *.html
git commit -m "CONTENT: v1.13 — 14 Days to GitHub module, Days 19-20 retrofit, audit routine hardening"
```

---

## Notes for the implementer

**Do not push.** The repo owner commits and pushes on his own instruction. Every task ends at `git commit`.

**Do not touch these files**, all intentionally untracked: `videos.html`, `VIDEO_TOPICS.md`, `AI101 (1).zip`, `30 Days to Claude Code _standalone_.html`, `handoff/`.

**Do not add a nav link to `videos.html`** anywhere. Videos are not being exposed yet.

**Every command in the module must actually work.** Before writing a day, run its commands yourself in a scratch folder under the scratchpad directory. A command that fails on Day 8 costs a learner the whole module. Pay particular attention to `gh repo create` flag combinations and `git switch` availability (git 2.23+).

**Verify against the spec** at `docs/plans/2026-07-27-github-module-design.md` when anything here is ambiguous. The spec wins.

---

## Self-Review

**Spec coverage:** All 15 days (0–14) have a task. The retrofit has Task 6. Every site-integration bullet in the spec maps to Task 7 or 8, except `contribute.html`, which the spec explicitly places out of scope. The rejected `ai101` capstone appears in the Global Constraints as a prohibition rather than as content, which is the correct way for a rejected decision to survive into implementation.

**Placeholder scan:** No TBDs. Every command block contains the literal command. Every callout has its actual text or a specific content requirement with named beats. Prose paragraphs are specified by required beats plus a voice guide rather than written verbatim, which is deliberate: the voice guide points at real line numbers in the existing file, and duplicating 1,500 lines of finished prose into a plan would make the plan the implementation.

**Type consistency:** `github14-progress-v1` and `TOTAL = 15` are used identically in Task 1 and asserted in the check script. Day IDs are `day-0` through `day-14` throughout, matching `data-day` attributes. Folder name is `~/github-lab` in every task that references it; the clone is `~/github-lab-copy`. Files are `notes.md`, `ideas.md`, `todo.md` from Task 2 onward, and `notes.md` is the one carried into the conflict exercise.

**One open verification:** the Lucide icon name `git-branch` is asserted in Task 7 Step 2 rather than assumed, with two named fallbacks.
