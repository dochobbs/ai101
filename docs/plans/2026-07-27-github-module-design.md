# 14 Days to GitHub — Design

**Date:** 2026-07-27
**Status:** Approved, not yet implemented
**Deliverable:** `github.html`, plus a retrofit of `claude-code.html` Days 19–20 and supporting site integration

---

## Goal

A standalone, self-paced module that takes a clinician from "my work lives in a folder on my laptop" to "my work is backed up online, I can branch to try something risky, and I can open a pull request, review it, merge it, and resolve a conflict."

It is the sequel to `30 Days to Claude Code`, but it does not require it.

## The frame

The site already runs a traveling metaphor in `claude-code.html`: learning the terminal is learning to get around a foreign country, and Claude is the local who speaks the language. This module extends that frame rather than competing with it.

> Git is your memory. GitHub is your meeting place. Claude is your guide. The command line is the country you are learning to navigate.

Git is a travel journal: each commit is a dated entry saying "this is what the project looked like at this moment." Branches are side roads you can explore without changing the main route. GitHub is base camp — the shared home where the journal lives online, gets backed up, and can be read and reviewed by other people.

## Decisions made during brainstorming

| Question | Decision |
|---|---|
| Scope | Publish and collaborate. Ends at pull request → review → merge. **No GitHub Actions.** |
| Length and format | 14 days, one concept per day, own page, same day-card format as the Claude Code module. |
| Who reviews the learner's PR | The learner opens a PR against their own `main` and asks Claude to review the diff. No second human required, nothing for the site owner to maintain. |
| Overlap with Claude Code Days 19–20 | Deliberate. Days 19–20 give intuition and one habit; `github.html` teaches the full curriculum from zero so a cold arrival gets a complete module. |
| Capstone against `ai101` | **Rejected.** Learners never touch the site's repo — no PRs, no issues. All work stays in their own repository. |
| GitHub Pages | Out of scope. Different promise, would be a fifteenth unit. Possible bonus day later. |
| Terminal vs browser | Split deliberately: `git` and `gh` at the command line for Days 1–11; github.com in the browser for Days 12–13, because reading a diff and leaving a review is a visual act. |

## Architecture

New page `github.html`, built on the chassis of `claude-code.html`:

- Same slate design system and typography (Fraunces / Source Sans 3 / JetBrains Mono)
- Same `article.day` cards with `.day-header`, `.day-body`, `.callout`, `.learned`, `.complete-btn`
- Same `.codeblock` + `.copy-btn` pattern on every command
- Same sidebar with `.nav-day` links, scroll-spy `IntersectionObserver`, progress meter, reset button
- Same Echs Pickaxe embed in the sidebar
- Same `section.phase` structure with per-phase accent cycling

**Separate progress state.** `STORAGE_KEY = "github14-progress-v1"`, `TOTAL = 15` (days 0–14). The two modules track independently; finishing one must not affect the other's meter.

**Favicon:** the existing inline SVG with `14` in place of `30`.

**Head:** canonical, OG, and Twitter tags following the pattern established in the v1.11 SEO pass.

- Title: `14 Days to GitHub · Where Your Work Lives`
- Canonical: `https://ai101.health/github.html`

## Structure

**Day 0 · Base Camp Setup** — standalone preamble, mirroring Day 00 of the Claude Code module.

**Phase 1 · Your Own Journal (Days 1–5)** — entirely local. Nothing leaves the laptop, so there is nothing yet to be embarrassed about.

**Phase 2 · Base Camp (Days 6–9)** — the work goes online.

**Phase 3 · Side Roads (Days 10–14)** — branches, issues, pull requests, review, conflict.

## The 14 days

### Day 0 — Base Camp Setup
**Unit:** GitHub account, `gh` install, authentication.
Create the account. Install the GitHub CLI. Run `gh auth login`, then `gh auth status` to confirm. Ends before any git concept is introduced, so setup friction never contaminates a teaching day.

### Phase 1 · Your Own Journal

**Day 1 — Start the Journal**
**Unit:** `git init`, repository.
The repository is the entire expedition folder: maps, journal, supplies list, and the history of the trip. Learner runs `git init` in the tool they built on Day 21 or 27 of the Claude Code module. Cold arrivals build a small three-file folder first.

**Day 2 — Where Am I?**
**Unit:** `git status`, working directory.
The working directory is what is spread out on the table right now. `git status` asks: where am I, and what have I changed? Learner edits a file, runs status, watches the output change. First feedback loop.

**Day 3 — Packing the Bag**
**Unit:** `git add`, staging area.
Staging is packing the bag before departure — choosing exactly which changes are ready to go. Learner stages one file, deliberately leaves another unstaged, and runs `git status` to see the two groups side by side. The point of the day is that staging is a *choice*, not a formality.

**Day 4 — The Dated Entry**
**Unit:** `git commit`, `git log`.
The commit is the dated journal entry. Learner writes their first commit message, then reads the journal back with `git log`. Includes a short note on what makes a message useful to the version of you that reads it in six months.

**Day 5 — What Changed**
**Unit:** `git diff`, `git diff --staged`.
Comparing today's map against the last saved version. Learner makes a change, reads the diff, stages it, reads `--staged`, and sees why the two differ.

### Phase 2 · Base Camp

**Day 6 — The Things That Stay Behind**
**Unit:** `.gitignore`.
The list of what stays out of the journal: temporary files, secrets, local settings, clutter. **Deliberately placed before the first push** so that nobody's first act at base camp is publishing an API key. Ordering as a safety measure.

**Day 7 — A Note for the Next Traveler**
**Unit:** README.
The note handed to someone arriving cold: where they are, what the trip is for, how to start. Learner asks Claude to draft one, then edits it so it sounds like them.

**Day 8 — Base Camp**
**Unit:** `gh repo create`, remote, origin, `git push`.
Remote is another known location where a copy lives. Origin is Git's default nickname for where you cloned from. Learner creates the repo and pushes. The journal is now online. First moment of visible payoff.

**Day 9 — Bringing It Home**
**Unit:** `git clone`, `git pull`.
Learner clones their own repo into a different folder — the tactile proof that it really is out there and not just a claim. Then clones a real public repo, read-only, to see what someone else's expedition looks like.

### Phase 3 · Side Roads

**Day 10 — The Side Road**
**Unit:** `git branch`, `git switch -c`.
A side road you can explore without changing the main route. Learner makes a branch, makes a risky change, switches back, and watches the files change underneath them. That moment is the day's whole lesson.

**Day 11 — Pinning a Note to the Board**
**Unit:** issues, `gh issue create`.
A note pinned to the planning board: a bug, question, idea, or task. Learner files one real issue against their own tool — one thing that genuinely annoys them about it. **This sets up Day 13**, where it gets closed.

**Day 12 — Presenting the Route**
**Unit:** pull request, `gh pr create`.
Returning from a scouting trip and presenting the proposed route before the official map changes. Learner pushes the branch and opens the PR, then **moves to the browser** to read the diff on github.com.

**Day 13 — The Other Travelers**
**Unit:** code review, merge.
The other travelers check the route for cliffs and wrong turns. Learner asks Claude to review the diff in that role — "you are the other traveler; where are the cliffs?" — then merges, and closes the Day 11 issue. The module opens and resolves its own loop, which is what stops issues from feeling like bureaucracy.

**Day 14 — Two Maps, One Disagreement**
**Unit:** merge conflict.
Two travelers edited the same part of the map differently. Git shows the disagreement; a person decides. **The conflict is manufactured on purpose:** same line, two branches, merge, conflict markers, resolved with Claude reading alongside. Closes on the point that this is the one part of git that genuinely frightens people, and they just caused one deliberately and fixed it.

### No capstone against `ai101`
Considered and **rejected** (2026-07-27). Learners never touch the `ai101` repo — no pull requests, no issues. Everything in the module happens in the learner's own repository. Days 11–13 already teach the full issue → PR → review → merge cycle solo, so nothing is lost pedagogically, and the site owner takes on no inbound review burden and no risk to a live site that has no CI.

## Claude Code retrofit — Days 19–20

**Day 19 retitled:** `A Time Machine for Your Files (Git)` → `A Travel Journal for Your Files (Git)`. Time machine moves into the body as the thing a journal lets you *do*.

**Two analogies, not three.** Day 19 currently opens with an EHR-chart comparison ("every version of the chart is kept, every change has a name and a timestamp, nothing is ever really gone"). **Cut it.** It does the same work as the time machine, and two images for one concept is already the limit.

- Travel journal — primary frame, carries the module
- Time machine — one clause about going back, not a frame

**Made self-contained.** Day 19 hard-depends on `~/claude-lab` and `reflections.md`, both created in earlier days. Both soften to "your lab folder — or any folder with a couple of files in it, if you're arriving here directly." Two sentences, and the unit stands alone.

**Vocabulary stays at three words,** recast in the journal frame: repository as the expedition folder, commit as the dated entry, diff as comparing today's map against the last entry. The other eleven terms belong to the new module.

**Day 20 keeps its title and its best line** — that git only restores what was committed, and the protective habit costs five seconds. Body reframes to the wrong-turn image: go back to the last place you knew the map was right.

**Day 20 ends with the handoff callout:** Git is your memory, GitHub is your meeting place — when you want the journal backed up and readable by someone else, that is the next fourteen days. Links to `github.html`.

## Site integration

- **`index.html`** — new `week-card bonus has-badge` beside the 30 Days card. Title "14 Days to GitHub", `New Jul 2026`, meta row "14-day track · Publish and collaborate".
- **Hero ribbon** — unchanged. Two competing ribbons is worse than one, and 30 Days remains the front door.
- **`contribute.html`** — **out of scope for this build.** The page describes what to submit and how to format it but has no submission route at all (no form, no mailto, no repo link). The obvious fix — a GitHub issue link — was rejected along with the capstone: the site owner does not want learners filing against the `ai101` repo. Needs a different answer (a form, or an address he controls) decided separately.
- **`claude-code.html` footer** — add the new module beside the existing Vibe Coding link.
- **`sitemap.xml`** — add `https://ai101.health/github.html`.
- **`updates.html`** — v1.13 entry covering the module, the Days 19–20 retrofit, the contribute fix, and the audit-routine changes.
- **Footer version bump** — `v1.12` → `v1.13` across all pages.

## Out of scope

- GitHub Actions and any CI/automation content
- GitHub Pages / publishing a public URL
- A `14-days.html` redirect stub (`30-days.html` exists only because a slide deck points at it; no deck exists for this module)
- Rebasing, cherry-picking, submodules, tags, releases, forks-of-other-people's-work beyond the optional capstone

## Related work, not part of this build

Audit issues **#10 (Jun 28), #11 (Jul 5), #12 (Jul 12)** remain open and unactioned — roughly a month of findings, including Claude Sonnet 5 being absent from every page and `ai-news.html` running a month behind. Needs its own session.

The weekly audit routine (`trig_01KvbzVEe51SjAHdzHhwSMqQ`) was patched on 2026-07-27: model bumped to `claude-sonnet-5`, a carry-forward step added that re-reads open audit issues against current repo contents, and a degraded-run rule added so a network failure files an issue instead of exiting silently as a clean week.
