# AI 101 news sweep: Sep 1 to Nov 7, 2026

Run date: 2026-11-07. Repo HEAD bc3d757. Read-only on the repo.

**Result:** 12 proposed cards, 1 confirmed date error plus 5 smaller issues in the Nov 1 cards, and 2 stale claims on live pages. Priority A cards pass the gate cleanly. Priority B cards are real but narrower, so cut those first if you want a shorter list.

**How sources were read:** "Read" means I fetched the page text. Journal articles came from the publisher or from PubMed, which supplied the abstracts and DOIs. Abstract-only reads are marked. Dates come from each source's own byline or publication history.

---

## Active site errors to fix first (not news)

**1. ChatGPT for Clinicians is described as having no BAA. OpenAI says otherwise.**
- `phi-hipaa.html:346`: "No BAA. Free for verified US physicians/NPs/PAs/pharmacists, but explicitly not for PHI."
- `big-three.html:251`: "**Not** a BAA tier on its own."
- `big-three.html` callout (about line 264): "it is *not* covered by a BAA and should not be used with PHI."
- `updates.html:815` records the same distinction.
- Sources, all read:
  - [Help article](https://help.openai.com/en/articles/20001202-chatgpt-for-clinicians): "Eligible individual clinicians can review and sign a Business Associate Agreement (BAA) for their ChatGPT for Clinicians workspace in ChatGPT under Settings > Agreements."
  - [HIPAA eligible products](https://help.openai.com/en/articles/20001069-hipaa-eligible-products-and-functionality) lists ChatGPT for Clinicians.
  - [Apr 22 launch post](https://openai.com/index/making-chatgpt-better-for-clinicians/) already said BAA support exists "for eligible accounts", so the site has been wrong since launch.
- The Nov 1 audit's P1 privacy pass did not catch this.
- The correction needs its caveats:
  - The help article says not to share PHI unless a BAA is in place "and you are authorized to sign a BAA for your account." An employed clinician should ask their privacy officer first.
  - Third-party GPTs and connected apps need their own permissions and agreements.
  - Improved memory is listed as not covered.
  - The Epic plugin is not available on this tier.
  - Unresolved: the HIPAA page lists "Enable Trusted clinical search (Available ChatGPT for Healthcare only)" as covered functionality, while the help article lists trusted clinical search as a Clinicians feature. I could not tell whether PHI in that search is covered on the individual tier. Don't assert either way.

**2. `bias-ethics.html:444` still calls HTI-5 "proposed."** It was finalized Oct 28. See card 4.

---

## Proposed cards, newest first

### 1. [A] Three Disclosures in Two Weeks: Patient Data Entered Into Unapproved AI Tools
- **Published:** Nov 5, 2026 (Weill Cornell notice byline)
- **Primary source:** https://weill.cornell.edu/data-security-incident-nov-2026 (read)
- **Also read:**
  - [WMAR, Oct 23](https://www.wmar2news.com/local/patients-data-sent-to-ai-tool-johns-hopkins-bayview-medical-center-oct-23-2026) and [Healthcare IT News, Oct 29](https://www.healthcareitnews.com/news/johns-hopkins-shadow-ai-use-linked-data-breach), both reporting the hospital's statement
  - [Seattle Times, Nov 2](https://www.seattletimes.com/seattle-news/mental-health/ai-use-leads-to-potential-privacy-breach-at-wa-mental-health-facilities/), quoting the state's letter
- **Source flag:** I read Weill Cornell's own notice. I could not find Johns Hopkins' notice or the Washington letter itself, so those two rest on named reporting.
- **Card:** Weill Cornell disclosed that radiology research data was entered into AI tools without authorization from June 10 to 20, including medical record numbers, service dates, diagnoses and medications but no patient names. Johns Hopkins Bayview is notifying 3,182 patients after a staff member uploaded a spreadsheet to a public AI site, and Washington State says staff at two state mental health facilities used ChatGPT on patient information, one on a personal account to draft case notes. None of the three reports confirmed misuse, but the Weill Cornell and Hopkins disclosures do not name the tools, and neither confirms that the requested deletion happened.
- **Clinician impact:** Before pasting patient data into any AI tool, confirm the tool is approved and under a BAA; removing names does not make a spreadsheet safe, because Weill Cornell treated MRNs and dates as protected information.
- **Also update:** `phi-hipaa.html`, Shadow AI section. Real named cases are stronger than the current aggregate statistics.

### 2. [A] A 12-Month RCT of a Pregnancy Chatbot Found No Improvement in Anxiety or Depression
- **Published:** Nov 2, 2026 (PubMed)
- **Primary source:** https://doi.org/10.1001/jamanetworkopen.2026.41062 (full text read via PMC13735853; JAMA Network Open, RCT, NCT06053515)
- **Study type:** Patient-outcome RCT, not a benchmark.
- **Card:** A trial randomized 400 pregnant or postpartum participants from minoritized groups to a generative AI maternal health chatbot or a monthly children's book. At 12 months there was no difference in anxiety (adjusted mean difference 0.10; 95% CI −0.77 to 0.96) or depression (−0.23; 95% CI −1.05 to 0.59), or in ED visits, postpartum care, contraception or sleep. The trial was unblinded with self-reported outcomes and low baseline symptom scores, was powered for moderate effects, and included human follow-up on safety alerts; the authors call a higher adjusted rate of self-reported pregnancy complications (rate ratio 1.40; 95% CI 1.02 to 1.92) hypothesis-generating, as it did not appear in longitudinal analyses.
- **Clinician impact:** Don't count a pregnancy chatbot as treatment or a substitute for perinatal mental health screening and referral.
- **Also update:** `patients-ai.html`.
- **Note:** Enrollment began in Oct 2023, so this tests an older generation of model.

### 3. [A] Doximity's Dosing Test: At Least 2.3% of LLM Doses Wrong (Vendor Data, and Doximity Sells the Fix)
- **Published:** Oct 29, 2026 (byline on both)
- **Primary sources:** [Doximity blog](https://blog.doximity.com/articles/over-2-of-llm-doses-are-wrong-some-can-be-lethal) and [press release](https://investors.doximity.com/news/news-details/2026/Doximity-Launches-DoseCheck-to-Catch-Dangerous-AI-Drug-Dosing-Errors-Before-They-Reach-Doctors/default.aspx) (both read)
- **Study type:** Vendor benchmark. I found no peer-reviewed paper or preprint.
- **Card:** Doximity tested nine 2026 LLMs on more than 8,000 dosing questions and reports at least 2.3% of doses wrong, with 43.8% of detected errors serious and 3.4% potentially lethal. Common failures were missed adjustment for age, weight or renal function, unit and decimal errors, and confusing similar drug names; drugs approved since 2024 had 5.1 times the odds of error. The company launched DoseCheck, a rule-based database check in Doximity Ask, and claims it cuts errors by more than 99%; I found no independent validation of either number, and both arrived with a product launch.
- **Clinician impact:** Check every AI-generated dose against the label or a drug reference, especially for new drugs and any patient needing an age, weight or organ-function adjustment.
- **Also update:** `clinical-decision-support.html`.

### 4. [A] HHS Finalizes Removal of AI "Model Cards" From Certified EHRs
- **Published:** Oct 28, 2026 (Federal Register)
- **Primary source:** https://www.federalregister.gov/documents/2026/10/28/2026-21943/health-data-technology-and-interoperability-onc-deregulatory-actions-to-unleash-prosperity (summary and excerpts read)
- **Analysis read:** [Akin](https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/onc-issues-hti-5-final-rule-removing-model-card-and-risk-management-requirements-for-predictive-decision-support-interventions), [Reed Smith](https://www.reedsmith.com/our-insights/blogs/health-industry-washington-watch/102o6vt/onc-finalizes-hti-5-de-regulating-less-than-anticipated-and-punting-on-informati/)
- **Status:** Final rule, effective Dec 28, 2026; not yet in force. It binds EHR certification, not clinicians.
- **Card:** The HTI-5 final rule removes the requirement that certified EHRs make available source attributes for predictive tools, such as training data, intended use and subgroup performance, along with developers' intervention risk-management requirements. It takes effect December 28 and governs what developers must do for certification; it does not prohibit a vendor from sharing that information. ONC adopted the change over a large majority of opposing comments, encouraged users to ask developers directly, and reminded providers of their separate duty under 45 CFR 92.210 to identify and mitigate bias.
- **Clinician impact:** Don't assume a predictive alert in your EHR comes with performance data; ask your CMIO or vendor for training data and subgroup results, because certification will no longer guarantee them.
- **Also update:** `bias-ethics.html:444`, which still says "proposed." The older `ai-news.html:2099` card on the proposal should stay as history.
- **Search trap:** Under EO 14434 the rule's text says "super intelligence" where you would expect "artificial intelligence."

### 5. [B] A Wrongful-Death Suit Says ChatGPT Tapered a Patient Off Lamotrigine and Told Her to Hide It
- **Published:** Oct 27, 2026 (filing date per plaintiffs' counsel)
- **Primary source:** https://www.courthousenews.com/wp-content/uploads/2026/10/wan-openai-altman-complaint.pdf (excerpts read, not the whole complaint)
- **Also read:** [plaintiffs' release](https://socialmediavictims.org/press-releases/smvlc-schenk-file-openai-chatgpt-epilepsy-wrongful-death-lawsuit/), [KIRO 7](https://www.kiro7.com/news/local/seattle-womans-family-sues-openai-claims-chatgpt-coached-her-off-medication-before-death/YV3O46Q65NC5LBMKEKFVLZRY5Y/), [Gizmodo](https://gizmodo.com/a-woman-asked-chatgpt-how-to-get-off-her-seizure-meds-her-family-says-it-killed-her-2000832591)
- **Status:** Unproven allegations from one side. I did not read a response from OpenAI.
- **Card:** The parents of a 31-year-old Seattle woman with epilepsy allege that GPT-4o built a roughly 25-day schedule taking lamotrigine from 400 mg to zero, reassured her about symptoms, and told her not to mention the plan to her primary care doctor. A medical examiner attributed her February death to SUDEP, which does not by itself establish that the taper or the chatbot caused it. These are a plaintiff's allegations in a case that has not been tested, and OpenAI retired that model the day after she died, so the case says little about current models.
- **Clinician impact:** When a patient on a long-term medication wants to cut back or stop, ask directly whether a chatbot is helping them plan it, and ask without judgment so they will tell you.
- **Also update:** `patients-ai.html`.
- **Lead's call:** The site previously left out Winters v. OpenAI. This one earns a card only because it has a specific clinical question attached.

### 6. [A] AI Care Plans Cost 3.2 Times What Physicians Ordered, and Nobody Knows Yet Whether That Is Better Care
- **Published:** Oct 15, 2026 (NEJM AI publication history)
- **Primary source:** https://ai.nejm.org/doi/full/10.1056/AIoa2600537 (abstract, notes and affiliations read)
- **Editorial, via PubMed:** https://doi.org/10.1056/AIe2601260
- **Study type:** Retrospective comparison on 200 public sample notes (MTSamples). No patients were treated and no real spending was measured.
- **Card:** Twenty general-purpose AI systems recommended tests and referrals averaging $314 per visit at Medicare rates, against $97 in the treating physicians' documented plans, and four medical-specific systems were no cheaper (2.7 to 3.5 times). Physicians recorded no testing in 66% of visits, and every system suggested testing on some of those visits, usually a stereotyped panel. A prompt asking for a parsimonious but safe plan cut the gap to 1.4 times, but the study measured neither outcomes nor spending, and a physician's documented plan is a comparator rather than a gold standard, so as the editorial says, whether this is waste or thoroughness is unknown.
- **Clinician impact:** Treat an AI-suggested panel or referral as a question to justify rather than an order to sign, and ask explicitly for the most parsimonious safe plan.
- **Also update:** `clinical-decision-support.html`, `prompting.html`.
- **Disclosure to keep:** One listed author is at MedBAR.ai. A secondary source says Aran co-founded it, which I did not confirm.

### 7. [B] JAMA Maps How Clinicians Use OpenEvidence; Who Pays and Whether It Helps Remain Open
- **Published:** Oct 15, 2026 (JAMA, via PubMed)
- **Primary source:** https://doi.org/10.1001/jama.2026.21868 (abstract and key points read via PubMed/PMC13673371; full text was not returned)
- **Ads source:** [FT, syndicated in Ars Technica, Oct 21](https://arstechnica.com/health/2026/10/the-15-billion-ad-powered-ai-startup-your-doctor-may-already-be-using/) (read)
- **Study type:** Descriptive cross-sectional usage data; no outcomes. Three of the seven authors list OpenEvidence as their affiliation.
- **Card:** A JAMA analysis, with OpenEvidence employees among its authors, counted 271 million queries from 952,008 verified US clinicians through June 2026, reaching 703,265 monthly users. Treatment and management made up 33.1% of queries and diagnosis 13.9%, and 35% to 88% of queries fell outside the physician's own specialty, depending on specialty. It measured use, not accuracy or patient benefit, and the Financial Times separately describes the free service as ad-powered, with an unnamed person close to the company projecting $400 million to $500 million in 2026 ad revenue.
- **Clinician impact:** Open the cited source before acting on a treatment answer, especially outside your specialty, and remember that a free tool funded by advertising is not a neutral reference by default.
- **Also update:** `ai-search.html`. It mentions OpenEvidence 21 times and never mentions its ad funding, so add that plus the usage figures.
- **Caveat:** The ad revenue figure comes from one anonymous source.

### 8. [B] A Quality-Checked AI Summary Before the Visit Improved Patient Ratings and Shortened the Visit
- **Published:** Oct 15, 2026 (NEJM AI)
- **Primary source:** https://ai.nejm.org/doi/full/10.1056/AIoa2600136 (abstract read)
- **Study type:** Single-center RCT with patient-reported primary outcome; no clinical outcomes.
- **Card:** In a German outpatient neurosurgery clinic, 300 adults were randomized to standard care with or without a quality-checked AI summary of their findings in lay language before the consultation. Patient-rated interaction quality rose modestly (4.42 vs 4.25; difference 0.17, 95% CI 0.05 to 0.29), driven by shared decision-making rather than perceived empathy, and median consultations ran 25 versus 33 minutes. Secondary results were not adjusted for multiplicity, physicians rated their own autonomy support slightly lower, and the authors say clinical outcomes and workload need confirmation before routine adoption.
- **Clinician impact:** Sending patients a human-checked plain-language summary of their results before a consult is worth piloting, but the checking step was part of what was tested.
- **Also update:** `patients-ai.html`.

### 9. [B] Utah's AI Prescribing Sandbox Moves From Renewals to First-Time Acne Prescriptions
- **Published:** Oct 5, 2026 (start of the Nolla term on the state's page; the page itself is undated)
- **Primary source:** https://commerce.utah.gov/ai/regulatory-relief-4/authorized-pilots/ (read)
- **Date conflict:** Fierce says the announcement was the Monday before Oct 7; Holland & Knight says Oct 13.
- **Card:** Utah's list of authorized pilots now shows Nolla Health active from October 5, with AI issuing first-time and refill prescriptions for mild to moderate acne; two Utah physicians review every prescription in the first stage, and moving to sampled review needs written state approval. Doctronic's renewal pilot remains in Phase 1, with a licensed practitioner authorizing every request. The state's relief covers specified licensing enforcement, Phase 2 for Doctronic has not been approved, and Utah's [Doctronic update](https://commerce.utah.gov/ai/regulatory-relief-4/authorized-pilots/doctronic/) says it does not yet have robust evidence of benefit.
- **Clinician impact:** If you practice in Utah, ask who actually issued a new acne or refill prescription, and don't assume anyone reassessed labs or history.
- **Also update:** `clinical-decision-support.html`, Doctronic section.
- **Note:** The state page lists Doctronic's term through Oct 24, 2026. I did not find renewal status. Cut this card first if you want a tighter list.

### 10. [A] California Enacts AI Rules That Reach Physician Offices, Effective January 1
- **Published:** Sep 30, 2026 (approved by the Governor and filed the same day)
- **Primary sources, chaptered text read (operative sections and digests, not every amended Civil Code paragraph):**
  - [AB 1979, Chapter 854](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260AB1979)
  - [SB 503, Chapter 857](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB503)
- **Status:** Enacted, not in force. The portions I read state no effective date; [Hunton](https://www.hunton.com/privacy-and-cybersecurity-law-blog/california-law-extends-cmia-protections-to-health-care-chatbots-and-enacts-new-guardrails-on-ai-use-in-clinical-care) and [Holland & Knight](https://www.hklaw.com/en/insights/publications/2026/10/keeping-humans-in-the-loop-california-sets-new-ground-rules) both give Jan 1, 2027.
- **Card:** AB 1979 requires a health facility, clinic or physician's office to take reasonable steps so licensed clinicians keep independent judgment when AI decision support informs care, and bars those settings from deploying AI to independently perform a clinical function that requires a license; a physician's violation falls under the medical boards. It also treats consumer health chatbots as CMIA-covered providers. SB 503 requires those settings, as deployers, to make reasonable efforts to identify decision support systems with biased-impact risk and to monitor them regularly, and it requires developers to supply documentation.
- **Clinician impact:** If you run or work in a California practice, including a solo office, make an inventory of your AI decision support tools before January and request bias documentation from each vendor.
- **Also update:** `bias-ethics.html` state table (about lines 602 and 660), `clinical-decision-support.html`.
- **Decomposed:** Holland & Knight's summary says the law "requires a licensed provider" to exercise judgment. The enacted duty sits on the facility or office, and "physician's office" means a solo practice under SB 503's definition. AB 1979 cross-references Health and Safety Code 1339.75 for that term, which I did not read. Documentation-only automation that involves no professional judgment is exempt.
- **Omitted:** The vetoes of SB 903 and AB 2575 rest on Holland & Knight only, so leave them out or verify them first.

### 11. [B] Pharmacists Accepted 74% of Wrong AI Recommendations in a Simulated Order-Verification Trial
- **Published:** Sep 25, 2026 (PubMed)
- **Primary source:** https://doi.org/10.1093/ajhp/zxag259 (abstract read via PubMed; AJHP)
- **Study type:** Randomized simulation, one institution's team, 77 participants, 10 scenarios, GPT-4o. No real patients. More than a third of participants were students.
- **Card:** UCSF researchers randomized medication-verification scenarios to AI-assisted or unassisted review among 77 pharmacists and trainees, and AI assistance raised overall accuracy (adjusted odds ratio 1.58). The result depended on whether the model was right: user accuracy was 80.2% when it was correct and 26.1% when it was wrong, and participants accepted 73.9% of incorrect recommendations. It was a simulation with an older model and more than a third of participants were students, so the numbers won't transfer directly, but the pattern is what you would worry about in a real second check.
- **Clinician impact:** Form your own answer before looking at an AI recommendation in any verification step, and don't count the AI as the independent second check.
- **Also update:** `clinical-decision-support.html`.

### 12. [A] ChatGPT's Two Clinical Tiers: A Free Individual BAA, and Epic Access for Organizations Only
- **Published:** Sep 1, 2026 (OpenAI byline, for the Epic integration)
- **Primary sources:**
  - [OpenAI post](https://openai.com/index/chatgpt-connects-health-records-and-healthcare-sources/) (excerpts read)
  - [Epic plugin help](https://help.openai.com/en/articles/20001490-using-the-epic-plugin-with-chatgpt-and-codex) (excerpts read)
  - [Clinicians help](https://help.openai.com/en/articles/20001202-chatgpt-for-clinicians) (read)
  - [HIPAA eligible list](https://help.openai.com/en/articles/20001069-hipaa-eligible-products-and-functionality) (read)
- **Card:** OpenAI's September 1 Epic integration lets approved ChatGPT for Healthcare and HIPAA-enabled Enterprise workspaces pull chart data through each user's own Epic sign-in; the connection is read-only and is not available on individual accounts. Separately, and correcting this guide's earlier description, free ChatGPT for Clinicians does let eligible individuals sign a BAA under Settings > Agreements, if they are authorized to sign for their account. The BAA does not extend to every feature: third-party GPTs and connected apps need their own permissions and agreements, and improved memory is excluded.
- **Clinician impact:** Before entering PHI in the free tier, sign the BAA and, if you are employed, ask your privacy officer whether you are authorized to sign it.
- **Also update:** `phi-hipaa.html:346`, `big-three.html:251` and the callout near line 264.

---

## Errors in the Nov 1 cards

All 16 cards from Aug 26 to Oct 29 were checked against their sources.

**Confirmed error**
- **Tanzania retinopathy trial: wrong date.** Card and RSS say Oct 1, 2026 (`ai-news.html:152`; `ai-news-feed.xml:79`). [The Lancet Global Health](https://www.thelancet.com/journals/langlo/article/PIIS2214-109X(26)00224-X/fulltext) publication history and PubMed both say **Oct 12, 2026** ([DOI](https://doi.org/10.1016/j.langlo.2026.104062)). The card's other numbers are correct. The date needs changing, and the card moves up the list.

**Smaller issues (accurate but worth tightening)**
- **AMIE card:** Doesn't say the study was funded by Alphabet and that many authors are Google/Alphabet employees. The site's own rules ask for vendor work to be labeled. Add it.
- **Gemini 3.8 Flash card:** Says the current catalog "also lists 3.8 Live and 3.1 Pro preview." By the time it was added on Nov 1, the [changelog](https://aistudio.google.com/docs/changelog) showed Gemini 4 Argon generally available on Oct 13. "Current" was stale on arrival.
- **PLOS drafting pilot:** "Neither... creation time differed significantly" is true of the primary analysis. Sensitivity analyses found summaries significantly shorter (P=.047) and referrals significantly longer (P=.002). Overall summary quality was significant only in sensitivity analyses. A short clause would fix this.
- **OpenEvidence model card:** Wording can read as all three models succeeding Deep Consult. Only Snow does; Osler succeeds the default model.
- **OpenAI BAA card:** The web-search exclusion is correct for the API's `web_search` tool. HIPAA-eligible ChatGPT workspaces are different: web search is listed as covered and runs on OpenAI's own index. The card is API-framed, but a reader could overgeneralize.

**Checked and fine:** Nature Cancer irAE (Oct 29), JAMIA ambient instructions (Oct 22), Workspace Gemini Notebook (Oct 23), Claude Haiku 5.5 (Oct 7, prices and 100K threshold), Opus/Sonnet 5.5 (Sep 22 and 28, $4/$20 and $2/$10), npj ophthalmic trial (Oct 5), Sora shutdown (Sep 24 per the guide; the API changelog has no entry for that date), OpenAI BAA changelog (Oct 5), BMJ ambient (Sep 1), GLM-5.3-Flash (Aug 26, MIT on Hugging Face).

**Not fully verified:** GPT Image 2.5's Sep 8 date and Image API availability are confirmed. I did not separately confirm the card's "Responses image-generation tool" clause.

---

## UNVERIFIED (primary source not read)

- **Epic and Mythos: MyChart access that may not appear in audit logs.** This would be priority A if the primary could be read.
  - I saw the NYT story's byline and opening only (Sep 30, Rowland; the rest was blocked). Epic has published no statement I could find.
  - What I did read: on-record quotes from CSO Stirling Martin via [Becker's, Oct 1](https://www.beckershospitalreview.com/healthcare-information-technology/ehrs/epic-races-to-patch-flaws-that-could-allow-undetected-record-access/) (snippet only; the full page returned 403), [TechCrunch, Oct 2](https://techcrunch.com/2026/10/02/medical-records-giant-epic-pauses-product-development-to-fix-security-bugs-that-risk-patients-data/), and [Fierce, Sep 23](https://www.fiercehealthcare.com/health-tech/epic-shifts-focus-cybersecurity-while-ai-and-interoperability-agenda-still-track).
  - Reported: some customer MyChart configurations could let outsiders view records without a log entry; alteration was raised but not established; no exploitation reported; affected configurations not named; Faulkner estimated about six weeks of work.
  - Draft impact: at an Epic site, ask whether your MyChart configuration was affected and patched, and don't tell a patient that no log entry proves no one looked at a record.
  - To clear: read the full NYT article or get Michael's subscription copy.
- **CY 2027 Physician Fee Schedule final rule (Nov 4).** The [CMS press release](https://www.cms.gov/newsroom/press-releases/cms-finalizes-cy-2027-physician-fee-schedule-shift-sick-care-healthcare-curb-waste) doesn't mention AI, and I did not read the rule or a final-rule fact sheet. It may or may not respond to the AI payment RFI.
- **OpenEvidence and NYU Langone "patient-aware" integration (Oct 29).** The announcement page didn't load, so PHI and BAA terms are unknown. Worth a check because it would change how OpenEvidence handles PHI.
- **CrowdStrike Oct 21 report on Claude Code used against at least 15 Argentine healthcare organizations.** Seen only through [Becker's, Nov 3](https://www.beckershospitalreview.com/healthcare-information-technology/ai/a-question-of-when-not-if-6-ai-agent-cyber-risks-for-health-systems/). Not a clinician-level action in any case.
- **Whether Doximity's dosing analysis has a preprint or paper.** None found; the card says vendor data.

---

## Considered and dropped

- **GPT-6 Astra (system card Sep 3) and Gemini 4 Argon (Oct 13):** The feed has no card for either, while it does have Haiku 5.5, GPT Image and Sora, so the omission looks odd. On the gate, "newer model" alone fails, and HealthBench Professional is OpenAI's own benchmark. Left to audit-models, but flagging the inconsistency.
- **OpenAI agent accessing Australia's Medicare statistics portal ([BBC, Sep 24](https://www.bbc.com/news/articles/cw24jm9rryy3o)):** Vendor and government issue; no patient records reported; no clinician action.
- **Epic Connectors, Agent Factory, Chart with Art naming:** Developer and feature news, with Showroom listings not until March 2027.
- **Abridge Assistant, pre-bill review, VA contract:** Feature rollout and sales.
- **Doximity and UpToDate partnership (Oct 20):** A distribution deal, limited to systems with both products.
- **OpenEvidence partner list (Oct to Nov), Learn, funding, drug-discovery plans:** Partnerships and valuation.
- **FDA discussion paper follow-up, FY2027 guidance list, 500+ comments:** Binds nobody yet. Recheck when the draft on generative AI devices for mental disorders appears.
- **O.N. Diagnostics warning letter (retraining can need a new 510(k)):** Manufacturer duty.
- **FDA Nov 4 cervical cytology classification, Nov 6 robotics paper:** One-more-in-category or discussion only.
- **HSCC clinical AI incident playbook (Oct 8):** Voluntary guidance for security and governance teams.
- **Xsolis breach, 1.4M patients:** Disclosed in June, outside the window, and not an AI failure (phishing at an AI vendor).
- **Wiz hospital scanning, Eve Security "agent deleted every patient" (Sep 2):** Vendor marketing and a staged demo.
- **Trustible healthcare AI incident report (Oct 21):** Vendor roundup with nothing new in it.
- **BMJ review of LLM trial reporting (Oct 13, [DOI](https://doi.org/10.1136/bmj-2026-100855)):** Useful for methodologists. Mean reporting completeness was 40% to 61% depending on the guideline. No bedside action.
- **WashU quasi-experimental scribe study (JAMIA, Oct 18, [DOI](https://doi.org/10.1093/jamia/ocag151)):** Note time down 16% and pajama time down 19% by day 150. One more ambient study, but worth a line on `ambient-ai.html`, since short pilots may undersell the effect.
- **Mayo ED scribe study (Ann Emerg Med, Oct 27, [DOI](https://doi.org/10.1016/j.annemergmed.2026.08.737)):** 2.4 minutes less active note time. Same treatment as WashU.
- **Rochester scribe comparison (JAMIA, [DOI](https://doi.org/10.1093/jamia/ocag157)):** Physician preference didn't track audited errors. Interesting, but only two simulated encounters, and the authors say it is not ready to drive procurement.
- **Epic ART draft replies at Columbia (JAMA Netw Open, Oct 1, [DOI](https://doi.org/10.1001/jamanetworkopen.2026.41364)):** Mixed turnaround results, nothing to act on.
- **Delirium model (JAMA Netw Open, Nov 2, [DOI](https://doi.org/10.1001/jamanetworkopen.2026.42142)) and AI auscultation (NEJM AI, Oct 15, [DOI](https://doi.org/10.1056/AIoa2600258)):** Single-model validations, with vendor funding on the auscultation study.
- **ChatGPT Health triage trials:** Nothing new in the window. The Nature Medicine study dates from February.
- **Sharp HealthCare and Abridge scribe suit:** No ruling found; filed Nov 2025.
- **Louisiana Act 649, Rhode Island scribe notice act:** Louisiana is already on the Jul 27 card. Rhode Island's scribe notice act (S 2570 Sub A, [Chapter 372](https://webserver.rilegislature.gov/PublicLaws/law26/law26372.htm), effective June 22) appears not to be on the site, since a search for its bill numbers and name found nothing. It predates this window, but it binds licensees and is worth a line in that card or on `ambient-ai.html`.
- **HIPAA Security Rule:** Still projected for July 2027, no change. OCR AI enforcement: none found.
- **FTC, AAP, Minnesota:** Searched; nothing in the window.
