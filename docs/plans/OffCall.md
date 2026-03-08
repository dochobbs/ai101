# AI Off Call: Operational Design

**AI 101 x Offcall | v2.0 | February 2026**

---

## Series Overview

4-session webinar series. Monthly(?), 60 minutes each. Hosted by Graham Walker (Offcall) with Dr. Michael Hobbs (AI 101) as expert guest.

**Audience:** Practicing clinicians, mixed AI skill levels.

**Arc:**

| Session | Title | Identity Shift |
|---------|-------|----------------|
| 1 | Your First AI Shift | Skeptic → User |
| 2 | The AI Toolkit | User → Evaluator |
| 3 | AI Without the Hype | Evaluator → Leader |
| 4 | The Vibe Code Session | Leader → Builder |

**Frameworks:**

| Session | Framework | Purpose |
|---------|-----------|---------|
| 1 | CRAFT Check | Quality-gate any AI output in 30 seconds |
| 2 | Tool Assessment + Personal Toolkit Plan | Compare tools, build your 3-tool kit |
| 3 | SHIELD | Six questions before any AI deployment |
| 4 | Builder's Ladder | Consumer → Customizer → Prototyper → Builder |

---

## Hosting Model

Every session follows the same pattern:

| Role | Graham (Host) | Michael (Guest) |
|------|--------------|-----------------|
| Opens session | ✓ Pre-poll results, burnout framing, callbacks | |
| Story | Introduces | Delivers |
| Live Demo | Co-demos at least one segment | Leads primary demos |
| Lab | Owns transition, narrates, reads chat | Interprets results |
| Q&A | Triages, answers some, keeps pace | Answers clinical/AI questions |
| Closes session | ✓ Ties to Offcall, teases next session | |

Target split: Graham ~60%, Michael ~40% of speaking time. 

---

## Session Format (All Sessions)

| Segment | Duration | Purpose |
|---------|----------|---------|
| The Story | 5 min | Real clinical narrative, stakes |
| The Live Demo | 8-15 min | Screen-share of real tools, raw |
| The Lab | 5-15 min | Hands-on interactive exercise |
| The Framework | 7-10 min | Monday-morning takeaway |
| The Q&A | 15-20 min | Live, Graham-led |

Design principles: No slides (or almost none). Failures are features. Every session produces a Monday-morning takeaway.

---

## Session 1: Your First AI Shift

**Story:** "The 4:47 PM Note" — Michael's origin story of using AI for documentation out of exhaustion, not enthusiasm. 70% note, changed his Tuesday.

**Demo (15 min):**

| Part | What | Who | Duration |
|------|------|-----|----------|
| A: Naive prompt | Vague prompt → bad note, narrate failures | Michael | 4 min |
| B: Structured prompt | Full-context prompt → dramatically better note | Graham | 6 min |
| C: NotebookLM | Upload AAP guideline → parent handout + audio summary | Michael | 5 min |

Key beat: Michael writes the bad prompt (his origin story). Graham writes the good one.

**Honest Failures Montage (2 min):** Pre-collected screenshots — fabricated meds, wrong dosing, fake citations.

**Lab (5 min):** Slido CRAFT scoring of Graham's structured prompt output. 5 yes/no questions (one per CRAFT letter). Aggregate reveal on screen. (not 100% sold on it)

**Framework (10 min):** CRAFT Check — Complete, Reliable, Actionable, Fitting, Trustworthy. 30-second quality gate. Analogy: co-signing a resident's note. Analogy: training a new med student

**Wow Moment:** NotebookLM generates podcast-style audio from a clinical guideline in 60 seconds.

### Runsheet

| Time | Segment | Who |
|------|---------|-----|
| 0:00 | Welcome, framing, pre-poll results | Graham |
| 3:00 | "The 4:47 PM Note" | Michael |
| 8:00 | Demo A: Naive prompt | Michael |
| 12:00 | Demo B: Structured prompt | Graham + Michael |
| 18:00 | Demo C: NotebookLM | Michael |
| 23:00 | Failures montage | Michael |
| 25:00 | Lab: CRAFT scoring via Slido | Graham |
| 28:00 | Aggregate reveal | Graham + Michael |
| 30:00 | CRAFT framework | Michael |
| 40:00 | Burnout connection | Graham |
| 43:00 | Q&A | Graham leads |
| 57:00 | Close, resources, Session 2 tease | Graham |

### Pre-Session

- 90-sec casual video from both (phone-recorded)
- One-page PDF: LLMs in 3 sentences, Big Three in 30 seconds
- 5-question poll (60 sec): AI usage, biggest concern, specialty

### Post-Session (all registered)

- Recording
- CRAFT one-pager PDF
- "Your First AI Week" 5-day email drip (Day 1: write your first prompt)
- Prompt templates from demo

---

## Session 2: The AI Toolkit

**Story:** "The Monday Morning Meltdown" — Colleague spending $160/month on 7 AI tools, using 1.5 of them. Tool Fatigue.

**Demo (15 min):** One clinical scenario (14yo with pancytopenia, rare blasts on smear), same prompt into 5 tools. Graham and Michael split the driving.

| Tool | Demo Lead |
|------|-----------|
| ChatGPT | Graham |
| Claude | Michael |
| OpenEvidence | Graham |
| Perplexity Pro | Michael |
| Glass Health - UpToDate - Other| Graham |

**Wow Moment:** Split-screen showdown. OpenEvidence wins the clinical round (citations, guidelines). Claude wins the human round (explaining possible leukemia to parents). "You need a toolkit, not a tool."

**Lab (10 min):** Attendees run their own clinical question (pre-assigned homework) through 2 tools, score both with Tool Scorecard via live polling. Aggregate reveal.

**Framework (10 min):** Tool Scorecard (Citations, Reasoning, Accuracy, Fit, Time-to-useful — 1-5 scale) + Personal Toolkit Plan (Daily Driver, Clinical Partner, Specialist). Re-evaluation habit: every 3 months.

Note: Tool Scorecard uses the CRAFT letters as a memory aid but is explicitly a different instrument from the CRAFT Check.

### Pre-Session

- Homework: save one real clinical question from this week
- Tool setup checklist: accounts on at least 2 tools (free tiers)
- Session 1 recap video (2 min)

### Post-Session (all registered)

- Recording
- Tool Scorecard PDF (laminated-card format)
- Personal Toolkit Planner worksheet
- Aggregate lab results by specialty

---

## Session 3: AI Without the Hype

**Story:** "The Mom Who Came Prepared" — Parent's ChatGPT correctly diagnosed contact dermatitis, then missed septic arthritis. Trust built on easy diagnosis transferred to dangerous one.

**Demo (15 min):** Three live stress tests.

| Test | Target Risk | Demo Lead |
|------|------------|-----------|
| Hallucination Trap | Fabricated citations, Google them live | Michael |
| Bias Reveal | Identical vignettes, different demographics, side-by-side | Graham |
| Privacy Leak | Copy-paste note → ask AI to recall patient name/MRN | Michael |

Bias Reveal backup plan: If model produces identical outputs, acknowledge improvement, show pre-recorded example, teach ongoing auditing.

**Lab (10 min):** AI Risk Rounds (M&M conference format). Three scenarios, self-selected by complexity:

| Scenario | Complexity | Topic |
|----------|-----------|-------|
| A: Documentation Assistant | Low | Ambient scribe with problematic BAA |
| B: Triage Bot | Mid | Vendor tool trained on non-representative population |
| C: Clinical Decision Support | High | Antibiotic AI deployed without ID consultation |

Attendees assess using four quadrants (Accuracy, Bias, Privacy, Governance) via Slido. Debrief highlights what the group caught vs. missed.

**Framework (10 min):** SHIELD — Source, Hallucination, Inequity, Exposure, Liability, Decision. Six questions before any deployment.

### Pre-Session

- Assignment: find out if your hospital has a formal AI policy
- Provocation: ask one patient if they've used ChatGPT for symptoms

### Post-Session (all registered)

- Recording
- SHIELD PDF (committee-meeting format)
- "Conversation Starter" template for forwarding to CMO/chair
- Aggregate lab results

---

## Session 4: The Vibe Code Session

**Story:** "The 2 AM Problem" — IT quoted $40K/6-8 months for a triage guide. Built a prototype with Claude in 45 minutes. Explicitly narrates his own ladder: "Six months ago I was on Rung 1."

**Demo (8 min):** Audience votes on what gets built (3 pre-rehearsed options). Michael builds live in Claude Code. Key beats: first prompt, first result, a real failure + recovery, one audience-suggested feature implemented in 30 seconds.

| Option | Description |
|--------|-------------|
| A | Antibiotic Duration Calculator |
| B | On-Call Handoff Generator |
| C | Patient Discharge Instruction Builder |

**Framework (7 min):** Builder's Ladder — Consumer → Customizer → Prototyper → Builder. "You don't need Rung 4. Most of you get enormous value from Rung 2 or 3." Frames the upcoming Lab as Rung 3.

**Lab (15 min):** Attendees build in Claude.ai Artifacts using a fill-in-the-blank Builder's Prompt Template. This is the session's climax — Graham narrates the cascade of screenshots as physicians build working tools simultaneously.

### Pre-Session

- Account setup: free claude.ai account
- Homework: one sentence describing a small workflow annoyance

### Post-Session (all registered)

- Recording
- Builder's Prompt Template
- "25 Tools Physicians Can Build This Weekend" (by specialty)
- Builder's Ladder graphic

---

## Content Distribution Model

**All registered attendees get all materials** regardless of live attendance.

**Live-only value:** Aggregate reveals, real-time demos, community Lab moments, audience feature in Session 4.

**Registration incentive:** Access to interactive lab tools (when built) for 30 days post-session.

---

## Build Requirements (Tiered)

### Session 1

| Priority | Item | Effort |
|----------|------|--------|
| Must-ship | Slido poll (5 CRAFT questions + pre-session poll) | 1 hr |
| Must-ship | CRAFT one-pager PDF | 2-3 hrs |
| Must-ship | Prompt templates doc | 1 hr |
| Must-ship | Pre-session video (phone-recorded) | 1 hr |
| Ship-if-ready | 5-day email drip | 2 hrs |
| Ship-if-ready | Pre-session PDF | 1 hr |

### Session 2

| Priority | Item | Effort |
|----------|------|--------|
| Must-ship | Tool Scorecard PDF | 2-3 hrs |
| Must-ship | Personal Toolkit Planner | 1 hr |
| Must-ship | Slido setup (6+ polls) | 1-2 hrs |
| Must-ship | Demo environment (5 tools tested) | 2-3 hrs |
| Ship-if-ready | Aggregate results summary | 2-3 hrs |
| Defer | Tool Landscape Visual | 3-4 hrs |

### Session 3

| Priority | Item | Effort |
|----------|------|--------|
| Must-ship | SHIELD PDF | 2-4 hrs |
| Must-ship | Conversation Starter template | 2-3 hrs |
| Must-ship | Pre-tested demo vignettes + backup recordings | 4-6 hrs |
| Must-ship | Slido setup (Risk Rounds) | 1-2 hrs |
| Ship-if-ready | Risk Rounds custom web tool | 1-2 days |

### Session 4

| Priority | Item | Effort |
|----------|------|--------|
| Must-ship | Builder's Prompt Template | 2-3 hrs |
| Must-ship | Three rehearsed demos | 1-2 days |
| Must-ship | Builder's Ladder graphic | 2-3 hrs |
| Ship-if-ready | "25 Tools" document | 3-4 hrs |

### Cross-Session

| Priority | Item | Effort |
|----------|------|--------|
| Must-ship | Series landing page (ai101.health/offcall) | 1 day |
| Must-ship | Post-session email templates | 2-3 hrs |
| Defer | Co-branded design templates | 3-4 hrs |
| Defer | Per-session landing pages | 2-3 hrs each |

---

## Risk Mitigation

| Risk | Mitigation |
|------|-----------|
| Live demo failure | Screenshots + pre-recorded backups. Session 4: fall back to Artifacts if Claude Code is down. |
| Session 1 lab failure | Slido only dependency. If down, Graham reads questions aloud for chat/hand responses. |
| Sessions 2-3 lab failure | Attendees on own tools. Backup prompts dropped in chat. |
| Session 4 lab failure | If Artifacts down, use ChatGPT Canvas or any LLM + screenshots. |
| Audience skill skew | Session 3 Risk Rounds self-selected by complexity. Graham calibrates Q&A mix. |
| Bias demo doesn't show bias | Acknowledge model improvement, show pre-recorded example, teach ongoing auditing. |
| Privacy/compliance | All vignettes fictional. No real PHI. Stated at session start. Disclaimers displayed. |

---

## CME Learning Objectives

**Session 1:** (1) Use AI for clinical documentation. (2) Apply CRAFT to evaluate AI output. (3) Identify AI failure modes in medical text.

**Session 2:** (1) Compare AI tools using Tool Scorecard. (2) Develop a personal AI toolkit. (3) Assess tool fitness for specific clinical tasks.

**Session 3:** (1) Identify hallucination, bias, and privacy risks. (2) Apply SHIELD to evaluate AI deployments. (3) Articulate governance needs to leadership.

**Session 4:** (1) Prototype clinical tools with AI-assisted development. (2) Apply iterative prompt refinement. (3) Evaluate physician-driven tool creation.

---

## Success Metrics

| Metric | Target |
|--------|--------|
| Live attendance per session | 100-200 |
| Post-session resource downloads | 50%+ of registered |
| "Would recommend" | 80%+ |
| Return rate (Session 1 → 2) | 60%+ |
| Series completion (all 4) | 40%+ |
| ai101.health traffic increase | 3-5x during series |
| Weekly AI use at 30 days | 50%+ self-reported |

---

## Existing AI 101 Resources to Leverage

| Resource | Sessions |
|----------|----------|
| start-here.html, prompting.html, llm-thinking.html | 1, 4 |
| big-three.html, clinical-decision-support.html, ai-search.html, ambient-ai.html | 2 |
| bias-ethics.html, phi-hipaa.html, local-models.html, patients-ai.html, environmental-footprint.html | 3 |
| vibe-coding.html, everyday-ai.html | 4 |
| Spark companion app (Tool Finder, Glossary, Prompt Library) | 1, 2 |

---

*AI 101 x Offcall | February 2026*