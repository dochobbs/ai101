# Content currency audit: November 7, 2026

Audited at `bc3d757`. Report only: no site page was changed. Not legal advice; items marked COUNSEL need a lawyer's read.

## Status

- **Research:** COMPLETE for the 22 home page cards. Five agents read every page in full and checked it against primary sources. Gaps are listed under "Still open".
- **Links:** PARTIAL. Only links behind a finding were checked. The Nov 1 sweep is not repeated here.
- **Delivery:** this file, plus the five detailed reports in `docs/audits/assets/2026-11-07/`. Uncommitted.
- **Publication:** nothing published. `docs/audits/latest.json` not advanced.
- **Batch 1 (v1.17):** Priority 1 items 1-19, the Tanzania date, card dates, and the HTI-5 and Clinicians BAA cards were prepared on branch `maintenance/ai101-audit-2026-11-07-batch1`. Agents re-read each primary source before writing. Omitted as unverified: AB 1979 operative date, HTI-5 "14 of 60" count, Epic plugin launch date, Doctronic renewal after Oct 24. Publication is recorded separately after merge.
- **Routine:** brief updated Nov 7 and read back. First run on it is Nov 8. Web access for the cloud environment is unconfirmed until that run reports it per source family.

## Bottom line

138 findings across 21 pages (models 43, foundations 38, regulation 30, clinical 27), plus 12 proposed news cards and 1 wrong date among the Nov 1 cards. Some findings are the same error on several pages. No page came back clean.

The problem is bigger than stale dates. Several errors could lead a clinician to mishandle PHI or misread the law, and a few have been wrong since the day they were written, so they aren't just drift.

Of the 14 cards labeled "Updated Nov 2026", only `big-three` and `phi-hipaa` got substantive work on Nov 1. The other 12 got a sentence, a callout, or a rename.

## How far to trust this

**Checked against the primary source by the lead, independently of the agents:** items marked [V] below. Everything else is agent-read with sources in the detailed reports, and should be re-read before its text is quoted on the site.

**Corrections to the agent reports:**

1. `audit-clinical` C6 proposes adding a "no BAA" row for ChatGPT for Clinicians. That is the same error item 1 fixes, and it took the claim from the site's own pages. Add the row with the corrected BAA status.
2. Custom GPT creation (item 9) is narrower than `audit-models` states. OpenAI bars new GPTs on personal accounts, but its Clinicians help page says "Clinicians can create and use custom GPTs in ChatGPT for Clinicians." The Dec 11 retirement still applies.
3. Trusted clinical search is unresolved. The help article lists it as a Clinicians feature, but the HIPAA list says "Enable Trusted clinical search (Available ChatGPT for Healthcare only)". Don't state that PHI in that search is covered on the free tier.
4. The FDA link at `clinical-decision-support.html:1335` is live. The 404 in issue #14 did not reproduce, so that item can close with no site change.
5. The HTI-5 "14 of 60 criteria" count is agent-read from the Federal Register. The lead confirmed the effective date and the model card removal, but not that count, because the Federal Register blocked direct fetching.

## Priority 1: fix now

Wrong in a way that affects PHI handling, legal duties, or clinical judgment.

| # | Where | Site says | Correct | Check |
|---|---|---|---|---|
| 1 | `phi-hipaa.html:346`; `big-three.html:251, 264-268, 299-301, 564-565`; `updates.html:815` | ChatGPT for Clinicians has no BAA and is not for PHI | Eligible individuals can sign a BAA under Settings > Agreements, and only if authorized to sign for their account. Improved memory is not covered. Connected services are not automatically covered. See correction 3. | [V] |
| 2 | `claude-code.html:982`, `:968` | "Everything stays on your computer" | Files stay local, but prompts, outputs, and what Claude reads are sent to Anthropic. Consumer plans have no BAA. | [V] line and retention; agent for quote |
| 3 | `claude-code.html:956, 982, 1032, 1132`; `openclaw.html:283, 810` | It asks permission first | Since v2.1.283, auto mode is the starting mode: a classifier reviews actions instead of the user. Add a Manual mode step to Day 00. See a clean install first. | [V] docs |
| 4 | `claude-code.html:1856, 1825` | Type "stop" to stop it | Typing queues a message. Press Esc. | Agent |
| 5 | `ai-search.html:272-273` | Perplexity Health suits "clinicians querying their own patients' records" | Built around a person's own data. The announcement describes no clinician workflow or BAA. Delete. | [V] |
| 6 | `clinical-decision-support.html:1182-1184` | Non-device CDS should give "a single, clinically appropriate recommendation" | Reversed. Option lists meet Criterion 3 and a specific directive fails it. Enforcement discretion applies when only one option is clinically appropriate and all other criteria are met. | [V] FDA transcript |
| 7 | `bias-ethics.html:492-505` | IL, NV, RI, VT only restrict who may offer therapy, and these are not consent rules | All six also reach licensees. Several require written consent or notice before AI touches recorded sessions. Who counts as covered varies; Illinois's definition needs a careful read. COUNSEL. | [V] IL §20(b); others agent |
| 8 | `bias-ethics.html` after `:470`; `ambient-ai.html:643` | No law binding general clinicians appears on the site | Add RI Ch. 199/372: notify patients and review AI documentation, in force Jun 22, 2026, with no opt-out in the text. Add TX SB 1188, CA AB 3030, CA AB 1979, 45 CFR 92.210. COUNSEL. | [V] RI Ch. 372; others agent |
| 9 | `everyday-ai.html:107, 488-518` and others; `whats-next.html:315, 1300, 1347, 1375` | Build a Custom GPT on Plus | New GPTs are unavailable on personal accounts. Standard retirement is **Dec 11, 2026**. See correction 2. | [V] |
| 10 | `everyday-ai.html` (whole page) | Sample prompts upload visit data and callback logs, with no PHI warning anywhere on the page | Add a warning near the top and de-identify the examples. | Agent |
| 11 | `local-models.html:98, 136, 659` | Data never leaves your machine | Ollama and LM Studio now offer cloud options from the same tools. "Local" depends on what you select. | Agent |
| 12 | `phi-hipaa.html:785-800`; `bias-ethics.html:444-447` | HTI-5 is proposed | Final, 91 FR 67916, effective Dec 28, 2026 (some provisions Jan 1, 2027). Model card requirements removed. | [V] |
| 13 | `phi-hipaa.html:767-776`; `clinical-decision-support.html:1216-1222`; `patients-ai.html:1452-1493` | Doctronic renews prescriptions autonomously | Utah's page says Phase 1, with a licensed practitioner authorizing every request. Renewal after Oct 24 is unknown. | Agent, 2 reports agree |
| 14 | `openclaw.html:578-704`; `llm-thinking.html:426-446`; `ai-news.html:790-799`; `updates.html:276` | The agents "stayed inside the assignment" | OpenAI's Aug 26 report says they circumvented isolation controls and acted against their assigned tasks. Keep what wasn't shown: internal research model, reduced safeguards, no deployed product. Don't swing to the sensational reading. | [V] OpenAI; METR agent |
| 15 | `openclaw.html:1321-1325` | Lockdown Mode restricts memory | OpenAI: it "does not change memory"; it limits outbound network features. | [V] |
| 16 | `bias-ethics.html:889-900` | 9 LLMs, 32-46% when framed as expert advice | According to PubMed: 20 LLMs, 3.4M+ prompts. Base 31.7%; real notes with a false line inserted 46.1%; authority framing added only 2.9 points. [DOI](https://doi.org/10.1016/j.landig.2025.100949) | [V] PubMed |
| 17 | `ambient-ai.html:1489-1500` | Three April publications "all found" scribes upcode vs coders | Sources don't support that. Dates and one citation are wrong. | Agent |
| 18 | `patients-ai.html:104-108, 885-897`; `bias-ethics.html:910-917` | KFF 66M and 1-in-10 unsafe; crisis cases linked to ScienceDaily | The figures aren't in the cited pages. The US News source is unread. Cut until sourced. | Agent |
| 19 | `local-models.html:771, 785-792, 592, 596` | Printed Ollama commands and hardware tiers | Flags don't exist, the tag doesn't exist, and several models won't fit the listed hardware. | [V] flags; rest agent |

## Priority 2: rewrite and correct

Full detail in the asset reports.

- **`openclaw.html`:** July section (item 14), EchoLeak named the wrong product, red-team demo called real-world harm, HIPAA penalty unit, stale "safer alternatives" line counts.
- **`bias-ethics.html`:** Art. 50 transitional date, Maine and Colorado dates written as future, FDA count (1,614 entries by count), ECRI and KFF dates.
- **`patients-ai.html`:** missing 2026 Nature Medicine triage studies, custom GPT triage advice conflicts with the page's own business-associate warning, athenaAmbient isn't a patient tool.
- **`ambient-ai.html`:** Lukac and Afshar dates and "Nabla outperforms DAX", JAMA study unit, consent litigation, recording script that promises deletion, Freed and Heidi pricing.
- **`clinical-decision-support.html`:** OpenEvidence ad funding, Doximity GPT is now Ask, "standard of care" wording.
- **`big-three.html`:** Enterprise/Edu BAA wording, "consumer" Google HIPAA pathway, DALL-E, Grok version.
- **`whats-next.html`:** Atlas and Operator retired, "zero risk" email automation.
- **`medical-learners.html`:** AAMC and NRMP application rules, Philips self-report labeled as measured.
- **`prompting.html` and `glossary.html`:** settings paths, default memory, model names.
- **`claude-code.html` and `github.html`:** Windows commands, `claude doctor` for "not found", gh installer.
- **Sitewide:** NotebookLM rename still open on several pages; run a repo-wide grep and keep dated history.

## News

12 proposed cards in `assets/2026-11-07/audit-news.md`. Priority A first:

- Three disclosures of patient data entered into unapproved AI tools (Weill Cornell, Hopkins Bayview, Washington State)
- JAMA Netw Open RCT: pregnancy chatbot showed no improvement in anxiety or depression at 12 months
- Doximity dosing test (vendor data, launched with its own product)
- HTI-5 final
- NEJM AI: AI care plans cost 3.2x documented physician plans (no outcomes measured)
- California AB 1979 and SB 503, effective Jan 1, 2027 per law firms; confirm
- ChatGPT Clinicians BAA correction and the Epic integration

Priority B cards (lamotrigine suit, JAMA OpenEvidence usage, pre-visit summary RCT, Utah acne pilot, pharmacist simulation) can be cut first.

Fix in Nov 1 cards: Tanzania retinopathy trial is Oct 12, not Oct 1 (`ai-news.html:152`, `ai-news-feed.xml:79`).

## Card dates

The "Today" column is what each card can honestly say now. Any page fixed in a batch moves to Nov 2026 when that batch ships.

| Page | Label now | Today |
|---|---|---|
| ai-news | Updated Jun 2026 | Updated Nov 2026 |
| big-three | Updated Nov 2026 | Updated Nov 2026 |
| phi-hipaa | Updated Nov 2026 | Updated Nov 2026 |
| clinical-decision-support | Updated Nov 2026 | Updated Aug 2026 |
| ambient-ai | Updated Nov 2026 | Updated Aug 2026 |
| ai-search | Updated Nov 2026 | Updated Aug 2026 |
| local-models | Updated Nov 2026 | Updated Aug 2026 |
| openclaw | Updated Sep 2026 | Updated Sep 2026 |
| prompting | Updated Nov 2026 | Updated Jul 2026 |
| bias-ethics | Updated Nov 2026 | Updated Jul 2026 |
| medical-learners | Updated Nov 2026 | Updated Jul 2026 |
| image-video | Updated Nov 2026 | Updated Jul 2026 |
| patients-ai | Updated Nov 2026 | Updated Jul 2026 |
| whats-next | Updated Nov 2026 | Updated Jul 2026 |
| llm-thinking | Updated Apr 2026 | Updated Jul 2026 |
| ai-tools-mcp | New Mar 2026 | Updated Jul 2026 |
| glossary | Updated Jun 2026 | Updated Jul 2026 |
| claude-code | New May 2026 | Updated Jul 2026 |
| github | New Jul 2026 | New Jul 2026 (drop any "New" badge) |
| everyday-ai | Updated Nov 2026 | Updated Jun 2026 |
| vibe-coding | Updated Nov 2026 | Updated May 2026 |
| environmental-footprint | Updated May 2026 | Updated May 2026 |

`index.html:285-288` and `:301-304` also advertise July and May content in the card text, and `glossary.html:1307` has its own "Last updated: June 2026".

## Still open

**Needs the owner:**

- OpenEvidence `/cme` and `/policies/baa` return 403 to automated fetches. Check the BAA signing step and which boards accept its MOC credit in a browser.
- The NYT Epic/Mythos MyChart audit-log story was only partly readable. Priority A if confirmed; a subscription copy would clear it.
- US News article behind the chatbot-harm claims (`bias-ethics.html:921`, `patients-ai.html:886`) could not be read.
- COUNSEL: state statute coverage, signing authority for employed clinicians, patient-facing GPT advice.
- Decide whether Sunday runs stay report-only or prepare PRs. `docs/operations/weekly-audit.md` and the routine's brief disagree.
- Cloud environment network access, if the Nov 8 run still reports blocked families.

**Not run:**

- Clean first-run Claude Code session, and safe-start hooks under auto mode
- Windows commands
- `gh` end to end, since it creates real GitHub objects

**Unverified by anyone:** listed in each asset report, including Utah §63I-2-213 (possible 2027 sunset of HB 452), AB 1979's operative date, the Doctronic pilot's renewal after Oct 24, and several tracker-only state laws. Do not publish those yet. Missouri SB 1019 should stay off the site: trackers report an AI ad ban, but the truly agreed text has no AI language.

**Audit-report errors found:** the Nov 1 report's "GPT-6 Astra is an unconfirmed rumor" was wrong, and the Oct 18 "opt-out" label on Rhode Island's law is not in the enacted text.

## Backlog

- Oct 4, 18, 25 model and NotebookLM findings: fixed on `big-three`, `vibe-coding`, `ai-search`. The rename is still open elsewhere.
- Rhode Island scribe law and Sutter/MemorialCare suit (Oct 18): open, verified above.
- Issue #14: the FDA 404 can close; the routine's credential and egress items stay open.

## Recommended order

1. **Batch 1:** Priority 1 items, the Tanzania date, honest card dates for the rest, and the HTI-5 and BAA cards.
2. **Batch 2:** Priority 2 pages, each moving to Nov 2026 as it ships.
3. **Batch 3:** Remaining news cards and the card-date check in `scripts/weekly_maintenance.py`.
