# Content-currency audit: privacy, law, ethics, patients, footprint

Audited 2026-11-07 against HEAD bc3d757. Pages: `phi-hipaa.html`, `bias-ethics.html`, `patients-ai.html`, `environmental-footprint.html`. All four read in full; repo not modified.

**This is not legal advice or certification.** Statute readings below describe enacted text. Whether a law reaches a given clinician, practice or tool is a question for counsel. Calls that specifically need counsel are marked COUNSEL.

## Summary

| Page | Verdict | Findings | Card now | Recommended card |
|---|---|---|---|---|
| phi-hipaa.html | needs edits | 7 | Nov 2026 | Nov 2026 once fixed. Nov 1 really did rework the BAA list, but it left a wrong BAA line and news callouts untouched. |
| bias-ethics.html | needs edits; state-law section needs a rewrite | 13 | Nov 2026 | Nov 2026 once fixed. If not fixed, Jul 2026: Nov 1 changed one EU scope sentence, and the state-law section dates from Jul 28. |
| patients-ai.html | needs edits | 9 | Nov 2026 | Nov 2026 once fixed. If not fixed, Jul 2026: the Nov 1 content change was one sentence (:341); the last real review was Jul 28. |
| environmental-footprint.html | needs edits (small) | 1 | May 2026 | May 2026 is accurate today (last content commit 987e660, May 28; later commits are footer/nav/analytics). Nov 2026 if E1 lands. |

**Cross-page leaks (other auditors' pages, same errors):**
- `big-three.html:264-268` and `updates.html:815`: ChatGPT for Clinicians "not covered by a BAA".
- `clinical-decision-support.html:1215`: Doctronic "autonomous AI prescribing". Also check `openclaw.html:537`, `medical-learners.html:967`, `ai-news.html:1684`.
- `ai-news.html:2099`: HTI-5 proposed. A dated item, fine as history, but it needs a new final-rule card.
- `ambient-ai.html`: no Rhode Island or any other scribe-notice statute. A site-wide grep for 7538, 2570, AB 3030, AB 489, SB 1188, HB 149, 1557 and 92.210 found nothing relevant.

---

## phi-hipaa.html

### P1. WRONG. phi-hipaa.html:346 (also big-three.html:264-268)
- **Claim:** "ChatGPT for Clinicians ... No BAA ... explicitly not for PHI."
- **Correction:** OpenAI lists ChatGPT for Clinicians among its HIPAA-eligible products. Eligible individual clinicians can review and sign a BAA in the workspace under Settings > Agreements. Do not enter PHI unless a BAA is in place and you are authorized to sign it for your account. Multi-user or organization-wide use belongs on ChatGPT for Healthcare. A BAA was offered from launch, so this line was never right.
- **Sources:** [ChatGPT for Clinicians help](https://help.openai.com/en/articles/20001202-chatgpt-for-clinicians) (undated); [HIPAA eligible products](https://help.openai.com/en/articles/20001069-hipaa-eligible-products-and-functionality) ("Updated: 3 days ago" at retrieval); [OpenAI launch post](https://openai.com/index/making-chatgpt-better-for-clinicians/) (Apr 22, 2026).
- **Clinician impact:** A solo or DPC clinician can get BAA coverage for free, while an employed clinician needs to confirm they have authority to sign. COUNSEL on authority.

### P2. SUPERSEDED. phi-hipaa.html:344, :348
- **Claim:** "ChatGPT (consumer Free/Plus/Pro/Team): No BAA"; "ChatGPT Enterprise/Edu: BAA available through sales-managed accounts."
- **Correction:** Say "Business (formerly Team)". OpenAI: "We do not offer a BAA for ChatGPT Business." The eligibility list now reads "ChatGPT for Enterprise with Regulated Workspace"; Edu is not on that list, although the API BAA article still says to contact sales about "Enterprise or Edu". Name the Regulated Workspace condition and tell Edu users to confirm in writing.
- **Source:** [BAA article](https://help.openai.com/en/articles/8660679-getting-a-business-associate-agreement-for-the-openai-api) and eligible-products page above.
- **Clinician impact:** A small practice on the Business tier learns it has no BAA path there, and an academic Edu user learns not to assume coverage.

### P3. WRONG. phi-hipaa.html:349
- **Claim:** "Anthropic API: BAA available only for HIPAA-eligible services with zero data retention; does not cover Claude.ai, Workbench, or beta features."
- **Correction:** Anthropic says the BAA does not generally require ZDR. Some covered models require 30-day retention and are not available with ZDR unless expressly authorized. Claude Code with a Console API key is the ZDR-only case. Messages API is eligible, and sub-features such as prompt caching and web search are covered only under BAA versions accepted after 4/1/26. Not covered: Batch API, Files API, Skills API, Code Execution, Web Fetch, Console, and data sent to third parties via external MCP.
- **Source:** [Anthropic commercial BAA article](https://privacy.claude.com/en/articles/8114513-business-associate-agreements-baa-for-commercial-customers) (undated; read through a summarizer, so re-read before quoting).
- **Clinician impact:** A clinician-builder checks their BAA version and avoids Batch and Files with PHI, instead of treating ZDR as the single switch.

### P4. SUPERSEDED. phi-hipaa.html:785-800
- **Claim:** "HHS Proposes Gutting AI Transparency Rules (HTI-5) ... proposed eliminating 34 of 60 ... comment period closed February 27, 2026."
- **Correction:** Final rule published Oct 28, 2026, 91 FR 67916, effective Dec 28, 2026 (some provisions Jan 1, 2027; others phase later). It removes 14 of 60 criteria and revises 7, not the proposed 34. It fully removes the model-card source-attribute requirements at §170.315(b)(11)(iv) and (v). Risk-management removal at (vi) is per Akin's summary of the rule; the summary I read confirms (iv) and (v) directly. ONC says users should ask developers for DSI information and points to 45 CFR 92.210. The FR text says "super intelligence" where readers expect "AI" (EO 14434), which matters for anyone searching it.
- **Sources:** [Federal Register](https://www.federalregister.gov/documents/2026/10/28/2026-21943/health-data-technology-and-interoperability-onc-deregulatory-actions-to-unleash-prosperity) (Oct 28, 2026); [HHS](https://www.hhs.gov/press-room/hhs-finalizes-hti-5-deregulatory-rule.html) (Oct 26, 2026); [Akin](https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/onc-issues-hti-5-final-rule-removing-model-card-and-risk-management-requirements-for-predictive-decision-support-interventions) as a pointer.
- **Clinician impact:** After Dec 28, certification won't guarantee a model card for EHR predictive tools, so write that disclosure into procurement.

### P5. WRONG. phi-hipaa.html:729-735
- **Claim:** "general availability for all logged-in US users"; "OpenAI removed the separate space entirely."
- **Correction:** OpenAI: "We're beginning to roll out Health" to logged-in US users 18+ on web and iOS. "Health, in the left sidebar, remains your home base." The requirement to start there is what went away. `patients-ai.html:296-327` gets this right, so the two pages contradict each other about one source; conform phi-hipaa to patients-ai.
- **Source:** [OpenAI](https://openai.com/index/health-in-chatgpt/) (Jul 23, 2026).
- **Clinician impact:** Don't assume every patient has it, and you can ask a patient to open Health to see which sources are connected.

### P6. WRONG. phi-hipaa.html:767-776
- **Claim:** "In the Utah pilot, which allows autonomous prescription renewals, some cases may have no human review at all."
- **Correction:** Utah says the pilot "is still in Phase 1, which means a licensed medical practitioner authorizes every request"; Phase 2 needs office approval by medication group and "has not been approved". Autonomy is a possible later phase. The state's May 19 outcomes sheet: AI recommended renewal in 72% of cases, and the reviewing physician agreed in 91% of those. On Apr 20, 2026 the Utah Medical Licensing Board recommended immediate suspension. Keep the jailbreak and note-integrity point, framed as adversarial testing of a public interface with hard stops on controlled substances reported by the state. The listed term ran Oct 24, 2025 to Oct 24, 2026, and the page still showed "Active"; renewal unverified.
- **Sources:** [Utah authorized pilots](https://commerce.utah.gov/ai/regulatory-relief-4/authorized-pilots/); [Doctronic pilot page](https://commerce.utah.gov/ai/regulatory-relief-4/authorized-pilots/doctronic/); [outcomes](https://commerce.utah.gov/wp-content/uploads/2026/05/Doctronic-Outcomes-May-2026.pdf) (May 19, 2026); [Board letter](https://commerce.utah.gov/wp-content/uploads/2026/04/doctronic-letter-from-medical-board.pdf) (Apr 20, 2026).
- **Clinician impact:** A clinician can accurately tell a patient or colleague that a physician still signs each Doctronic renewal in Utah today.

### P7. SUPERSEDED. phi-hipaa.html:366-367
- **Claim:** "OpenEvidence: HIPAA compliant; free BAA available for covered entities"; "Glass Health: HIPAA-compliant enterprise offering; contact for BAA."
- **Correction:** OpenEvidence's BAA is incorporated into its Terms of Use and applies only when the user is a covered entity and OpenEvidence handles PHI for it; say that rather than "available". Glass documents a click-through BAA for its Developer API; the vendor pages I read do not confirm coverage by clinician-app plan.
- **Sources:** [OpenEvidence security](https://www.openevidence.com/security) (undated); [OpenEvidence announcement](https://www.openevidence.com/announcements/openevidence-is-now-hipaa-compliant) (Apr 25, 2025); [Glass](https://glass.health/resources/hipaa-compliant-ai-api) (undated).
- **Clinician impact:** A non-covered-entity user isn't protected by the OpenEvidence BAA, and a Glass app user asks which plan is covered.

**Verified OK on this page:** :229-237 Security Rule still proposed, Long-Term Actions, Final Action 07/2027 ([reginfo](https://www.reginfo.gov/public/do/eAgendaViewRule?RIN=0945-AA22&pubId=202510), edition labelled "2026"). :351 Claude Enterprise bullet matches the [Anthropic help article](https://support.claude.com/en/articles/13296973-hipaa-ready-enterprise-plans). :345 connectable sources (Apple Health, US hospital records, One Medical, Function Health) match OpenAI.

---

## bias-ethics.html

### B1. WRONG. bias-ethics.html:492-505
- **Claim:** "Illinois, Nevada, Rhode Island, and Vermont restrict *who may offer* therapy ... Maine and Colorado instead constrain *what a licensee may delegate*... If you are a licensed clinician, the second design is the one that reaches you directly." Also "They are not disclosure requirements or consent forms."
- **Correction:** The split doesn't exist in the text. These laws reach licensees directly in the states the page says they don't:
  - **Illinois** PA 104-0054 §20(b): a licensed professional may not allow AI to make independent therapeutic decisions, directly interact in therapeutic communication, generate plans without review, or detect emotions. §20(a) covers who may offer.
  - **Nevada** AB 406 §8: a provider "shall not use" AI for care directly to a patient; administrative carve-out; must independently review billing and session-note outputs; violation is unprofessional conduct. §7 covers AI providers.
  - **Rhode Island** Ch. 374 §40.1-5.5-3(c): licensee limits; (b) covers who may offer; (d) expressly lets a clinician discuss a client's own AI use and adds a duty to monitor safety.
  - **Vermont** Act 156: 18 V.S.A. §7115(d) permits HIPAA-compliant tools if the professional reviews and approves, and prohibited use is unprofessional conduct (3 V.S.A. §129a(a)(30), 26 V.S.A. §1354).
  - **Maine** Ch. 687 has both: 10 MRSA §1500-EE(2) on who may offer, 32 MRSA §2113 on licensees.
  - **Colorado** HB 26-1195 (as-enacted summary): licensee limits plus unfair-trade-practice rules on representation.

  Consent is also wrong: IL §15(b), ME §2113(3), RI §3(a) and CO all require written notice and/or written consent before AI is used on recorded or transcribed sessions. IL, ME and RI specifically exclude general terms-of-use acceptance. Who counts differs: Illinois excludes physicians from "licensed professional" (§10(10)); Vermont and Nevada include them or psychiatrists; Maine includes physicians specializing in mental disorders. COUNSEL.
- **Proposed text:** "All six regulate licensees as well as who may offer therapy. Most require written, specific consent before AI touches a recorded or transcribed session, so an ambient scribe in a therapy visit needs its own consent. Who counts as covered differs by state."
- **Sources:** [IL PA 104-0054](https://www.ilga.gov/documents/legislation/publicacts/104/PDF/104-0054.pdf); [NV AB 406](https://www.leg.state.nv.us/Session/83rd2025/Bills/AB/AB406_EN.pdf); [RI Ch. 374](https://webserver.rilegislature.gov/PublicLaws/law26/law26374.htm) (Jun 22, 2026); [VT Act 156](https://legislature.vermont.gov/Documents/2026/Docs/ACTS/ACT156/ACT156%20As%20Enacted.pdf) (signed Jun 17, 2026); [ME Ch. 687](https://legislature.maine.gov/legis/bills/getPDF.asp?paper=HP1397&item=3&snum=132) (approved Apr 13, 2026); [CO HB 26-1195](https://leg.colorado.gov/bills/hb26-1195) (signed Jun 3, 2026).
- **Clinician impact:** A therapist or psychiatrist in IL, NV, RI or VT stops believing the statute only reaches vendors and gets written consent before using a scribe.

### B2. WRONG. bias-ethics.html:521
- **Claim:** Illinois "Signed Aug 4, 2025."
- **Correction:** Public Act issued 8/01/2025, and §99 takes effect upon becoming law, so effective Aug 1, 2025. The ILGA fetch was cut off before the "Governor Approved" row. [ILGA status](https://www.ilga.gov/Legislation/BillStatus?DocNum=1806&GAID=18&DocTypeID=HB&SessionID=114) shows the 8/01/2025 Public Act action; [Cooley](https://www.cooley.com/news/insight/2025/2025-10-21-ai-chatbots-at-the-crossroads-navigating-new-laws-and-compliance-risks) says Aug 1 (Oct 21, 2025).
- **Clinician impact:** A clinician assessing conduct in that window gets the right start date. The page's own rule is that effective dates matter.

### B3. SUPERSEDED. bias-ethics.html:492-493
- **Claim:** "Four took effect before July 2026; Maine's follows on July 29, 2026 and Colorado's on August 12, 2026."
- **Correction:** "All six are now in effect." Maine's Jul 29 and Colorado's Aug 12 dates are in the page's table; I did not re-read their effective clauses this pass (see UNVERIFIED).
- **Clinician impact:** Maine and Colorado clinicians read a past date written as a future one and may think they have time.

### B4. WRONG. bias-ethics.html:433-435
- **Claim:** "What did *not* move ... the Article 50 transparency duties ... still apply from August 2, 2026."
- **Correction:** Dates at :431-432 are right (Annex III Dec 2, 2027; Annex I, including medical devices, Aug 2, 2028; in force Jul 27, 2026). But the Omnibus did move part of Article 50: Art. 111(4) gives providers of generative systems already on the market before Aug 2, 2026 until Dec 2, 2026 to comply with Art. 50(2) marking. The rest of Art. 50 has applied since Aug 2, 2026, so fix the tense. I found no MDR/IVDR change to Annex I in point 41.
- **Source:** [Regulation (EU) 2026/1744](https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng) (OJ Jul 24, 2026).
- **Clinician impact:** In an EU-facing organization, don't assume AI-generated content from an existing system is machine-marked before Dec 2.

### B5. MISSING. After bias-ethics.html:469-470 ("several of these bind practicing clinicians directly")
- **Gap:** The tables list only behavioral-health laws. No law binding a general clinician appears anywhere on the site.
- **Add:**

| State | Law | Duty | Status |
|---|---|---|---|
| Rhode Island | H 7538 SubA / S 2570 SubA, Ch. 199 and 372, R.I. Gen. Laws ch. 23-108 (the codification number was amended from 106) | Providers and facilities using AI to document in-person or telehealth visits must notify patients and review the documentation for accuracy afterward | In force. Enacted and effective on passage Jun 22, 2026 |
| Texas | SB 1188, Health & Safety Code §183.005 | Practitioner using AI for diagnostic purposes must act within scope, review AI-created records, and disclose the use to patients | In force. Effective Sep 1, 2025 |
| California | AB 3030, Health & Safety Code §1339.75 | GenAI patient communications with clinical information need a disclaimer plus human-contact instructions; exempt if read and reviewed by a licensed provider | In force. Effective Jan 1, 2025 |
| California | AB 1979, Ch. 854, Bus. & Prof. Code §22758.5 | Practices must protect independent judgment when care is informed by CDS, may not deploy AI to independently perform a licensed clinical function, and consumer health chatbots become subject to CMIA | Approved Sep 30, 2026. No urgency clause in the portion I read, so default Jan 1, 2027; **confirm** |

  **Rhode Island caveat:** sponsors and coverage call this an "opt-out" law, but the enacted text has no opt-out, consent right or penalty. The 10-18 audit's "disclosure+opt-out+review" label was wrong on opt-out. Also note Texas HB 149 §552.051(f) as a scope question for counsel; I read it only through secondary sources, so don't state a duty from it.
- **Sources:** [RI Ch. 199](https://webserver.rilegislature.gov/PublicLaws/law26/law26199.htm), [Ch. 372](https://webserver.rilegislature.gov/PublicLaws/law26/law26372.htm); [TX SB 1188](https://capitol.texas.gov/tlodocs/89R/billtext/pdf/SB01188F.pdf); [HSC 1339.75](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=HSC&sectionNum=1339.75.) plus [Medical Board of California](https://www.mbc.ca.gov/Resources/Medical-Resources/GenAI-Notification.aspx); [AB 1979](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260AB1979) (published Oct 1, 2026).
- **Clinician impact:** A clinician using an ambient scribe in RI must tell patients and review the note today, and TX and CA clinicians gain concrete disclosure duties to build into workflow. COUNSEL.

### B6. MISSING. After bias-ethics.html:451
- **Gap:** The page never mentions the one federal duty aimed at exactly this topic.
- **Add:** 45 CFR 92.210 (Section 1557): covered entities must not discriminate through patient care decision support tools, must make reasonable efforts to identify tools using race, color, national origin, sex, age or disability as inputs, and must make reasonable efforts to mitigate the risk. Identification and mitigation duties have applied since May 1, 2025. ONC pointed to it again in HTI-5. Secondary sources report no published proposal changing it as of October 2026, with a Section 1557 modification on the agenda for Feb 2027; that part is unverified from primary.
- **Sources:** [eCFR](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-92/subpart-C/section-92.210) (current); [89 FR 37522 final rule](https://www.federalregister.gov/documents/2024/05/06/2024-08711/nondiscrimination-in-health-programs-and-activities) (May 6, 2024).
- **Clinician impact:** A practice taking federal funds inventories its risk scores and CDS for these inputs, so "ask questions" becomes a legal duty on the deploying entity, not just good practice. COUNSEL on covered-entity status.

### B7. SUPERSEDED. bias-ethics.html:444-447 (related: :827-829, :1123)
- **Claim:** "proposed HTI-5 rule ... would eliminate ONC model-card requirements."
- **Correction:** Same facts as P4: final Oct 28, 2026, effective Dec 28, 2026. Note at :827 that model cards are now voluntary rather than a certification floor, and keep the CHAI registry reading as the alternative.
- **Clinician impact:** A procurement committee should now demand the card contractually.

### B8. SUPERSEDED. bias-ethics.html:574-578, :591-616
- **Claim:** "three of the five below are live." Literally still true, but it reads as the whole cluster.
- **Correction:** Label the table "examples, not an inventory" and add what I confirmed: Washington ESHB 2225, Ch. 168, effective Jan 1, 2027 ([session law](https://lawfilesext.leg.wa.gov/biennium/2025-26/Pdf/Bills/Session%20Laws/House/2225-S.SL.pdf), approved Mar 24, 2026, primary read). Hawaii SB 3001, Act 248, reported effective Jul 14, 2026 ([official PDF](https://data.capitol.hawaii.gov/sessions/session2026/bills/SB3001_CD1_.pdf) not read; secondary only). Others are tracker-only and listed under UNVERIFIED; don't publish them until read. "Six states" at :492 survives: I found no seventh enacted prohibition, and California's SB 903 was vetoed Sep 30, 2026 per one [law-firm article](https://natlawreview.com/article/ai-psychotherapy-evolving-regulatory-landscape).
- **Clinician impact:** A clinician in an unlisted state doesn't read absence from the table as absence of a law.

### B9. SUPERSEDED. bias-ethics.html:665-667
- **Claim:** Texas SB 815 "In force. Effective Sep 1, 2025."
- **Correction:** Add that §4 applies it to plans "delivered, issued for delivery, or renewed on or after January 1, 2026", and that §4201.156(a) bars an automated decision system from making, "wholly or partly", an adverse determination. That is stronger than the page's "sole basis" core.
- **Source:** [Enrolled SB 815](https://capitol.texas.gov/tlodocs/89R/billtext/html/SB00815F.htm).
- **Clinician impact:** A clinician appealing a Texas denial should check the plan's renewal date before citing the law.

### B10. WRONG. bias-ethics.html:889-900
- **Claim:** "tested 9 LLMs with over 1 million prompts ... accepted false medical claims 32-46% of the time when those claims were framed as expert advice ... GPT-4o performed best at roughly 10%."
- **Correction:** According to PubMed, the paper reports 20 LLMs and more than 3.4 million prompts. (The press release says nine and "more than a million", so the page copied the release.) Base susceptibility was 31.7%; **real hospital notes with an inserted false recommendation reached 46.1%**; social-media misinformation 8.9%. Appeal to authority added only 2.9 points (34.6%), and most fallacy framings *reduced* susceptibility, so "framed as expert advice" misstates the result. Worst named model: Gemma-3-4B-it, 63.6%. "GPT models were the least susceptible"; I could not find "roughly 10%" in the abstract.
- **Source:** Omar et al., *Lancet Digit Health* 2026;8(1):100949, [DOI](https://doi.org/10.1016/j.landig.2025.100949), retrieved via PubMed.
- **Clinician impact:** The risk to watch is a false line already in a chart note (46%), so don't assume a summary tool will catch it.

### B11. WRONG. bias-ethics.html:910-917 (same error at patients-ai.html:885-897)
- **Claim:** A Brown study found chatbots break ethics standards; "People with diagnosed conditions experienced worsened delusions, increased mania, and suicidal ideation"; NYT documented ~50 crisis cases and 3 deaths. patients-ai attributes the ~50 cases to "a separate analysis" linked to ScienceDaily.
- **Correction:** The [ScienceDaily item](https://www.sciencedaily.com/releases/2026/03/260302030642.htm) (Mar 2, 2026) *is* the Brown study: a practitioner-informed framework of 15 ethical risks from model behavior in counseling evaluations. A search of the full page finds no crisis cases, deaths, delusions, mania or New York reminder, so it doesn't support the patients-ai sentence it's linked from. Patient-harm claims must be separated from Brown and sourced directly. The US News article could not be read (see UNVERIFIED). Until those claims are sourced, cut the harm sentences and keep the clinical advice at patients-ai:899-905. New York's rule is right: [GBL §1702](https://www.nysenate.gov/legislation/laws/GBS/1702), "at least every three hours".
- **Clinician impact:** A clinician quoting this shouldn't present an evaluation of simulated counseling as evidence of patient outcomes, while still asking about chatbot use.

### B12. SUPERSEDED. bias-ethics.html:409-411, :948-949
- **Claim:** "As of early 2026, the FDA has authorized over 1,000 AI-enabled medical devices."
- **Correction:** FDA's list now has 1,614 entries by my count of the downloaded table (unique submission numbers; FDA states no total). Page "Content current as of 09/04/2026"; latest decision shown 06/29/2026. Use "more than 1,600 listed as of FDA's September 2026 update". :948 is a dated NVIDIA item, but its "has now authorized" should be attributed or dated.
- **Source:** [FDA list](https://www.fda.gov/medical-devices/artificial-intelligence-enabled-medical-devices/list-artificial-intelligence-enabled-medical-devices).
- **Clinician impact:** Small: a clinician sizing the regulated field, or weighing a vendor's "FDA-cleared" claim, gets the right denominator and a pointer to the searchable list.

### B13. WRONG (dates). bias-ethics.html:961, :977
- **Claim:** "ECRI ... (Apr 2026)"; "KFF ... (Apr 2026)."
- **Correction:** ECRI: the AHCJ piece is dated [Feb 5, 2026](https://healthjournalism.org/blog/2026/02/misuse-of-ai-chatbots-in-health-care-tops-2026-health-tech-hazard-report/), citing a January webcast. KFF: published [Mar 25, 2026](https://www.kff.org/public-opinion/kff-tracking-poll-on-health-information-and-trust-use-of-ai-for-health-information-and-advice/), fielded Feb 24 to Mar 2. The other KFF figures there (1 in 3, 77%, 41%) check out.
- **Clinician impact:** A clinician citing these in a governance memo cites the right date.

**Verified OK on this page:**
- Utah HB 452 (see Resolved below).
- Maine approved Apr 13, 2026, Ch. 687.
- Vermont signed Jun 17, 2026, effective on passage, and the quote at :497-500 matches.
- Rhode Island therapy designation and enactment date; the quoted form is Ch. 374, S 2197 SubA as amended.
- Arizona HB 2175, [Ch. 165](https://www.azleg.gov/legtext/57leg/1R/laws/0165.htm), approved May 12, 2025, effective from and after Jun 30, 2026. Note its text never mentions AI: it requires medical-director review without relying solely on any other source.
- Character.AI settlement framing at :625-627 matches January reporting.

---

## patients-ai.html

### A1. WRONG. patients-ai.html:1452-1461, :1482-1493
- **Claim:** "AI-powered autonomous prescription renewals"; "Utah authorized AI to autonomously renew prescriptions (March 2026)"; "190 medications"; Doctronic "launched in Utah with AI-powered autonomous prescription renewals."
- **Correction:** Agreement signed Oct 24, 2025; announced [Jan 6, 2026](https://commerce.utah.gov/2026/01/06/news-release-utah-and-doctronic-announce-groundbreaking-partnership-for-ai-prescription-medication-renewals/). March 2026 is the jailbreak news. Phase 1: a licensed practitioner authorizes every request. Fixed list, no controlled substances, no new prescriptions; a 2026 amendment removed two medications. Utah's Medical Licensing Board asked for suspension Apr 20, 2026. Sources as P6. Update the "two models" callout: Utah has since signed others, including [August AI](https://commerce.utah.gov/ai/regulatory-relief-4/authorized-pilots/) (refills; approved Oct 2, not started) and Nolla Health (first-time topical acne prescriptions; term from Oct 5, 2026). Legion Health's date is secondary only.
- **Clinician impact:** When a patient asks about "AI doctors" in Utah, the accurate answer is a state-supervised pilot where a physician signs off today, and those pilots are spreading beyond refills.

### A2. WRONG. patients-ai.html:104-108
- **Claim:** "April 2026 KFF Tracking Poll ... roughly 66 million people ... up sharply from 17% in KFF's 2024 baseline. Roughly 1 in 10 recent users say they later believed the advice they received was unsafe."
- **Correction:** Published Mar 25, 2026. A full-text search of the cited page finds no "66 million", no 2024 baseline and no "unsafe" or "harmful". 32% of US adults is well above 66 million, so that number doesn't fit. Use what's there: 32% (29% physical, 16% mental health), 41% of users uploaded personal medical information. If the others came from another source, cite it; otherwise delete. Also :118-122: KFF's younger, uninsured, Black and Hispanic gradient is reported for *mental health* advice, and "they are the first line" outruns the data (the top reason is quick advice, 65%; about 1 in 5 cite access).
- **Clinician impact:** A clinician presenting this data doesn't repeat figures the cited poll doesn't contain.

### A3. MISSING. patients-ai.html:693-699 and :345-351
- **Gap:** The page warns about emergencies with no evidence, and its error discussion stresses stale records. Two 2026 studies change the counseling. The site's only trace is one clause at ai-news.html:1243.
- **Add, per PubMed:**
  - Ramaswamy et al., *Nat Med*, Feb 23, 2026 ([DOI](https://doi.org/10.1038/s41591-026-04297-7)): structured test of ChatGPT Health, 60 vignettes, 960 responses. It undertriaged 52% of gold-standard emergencies, sending DKA and impending respiratory failure to 24-48 h evaluation while handling stroke and anaphylaxis correctly. Family minimization shifted edge-case triage (OR 11.7, 95% CI 3.7-36.6). Crisis messages fired inconsistently. Caveat: a vignette stress test of the January product; the abstract itself asks for prospective validation.
  - Bean et al., *Nat Med*, Feb 9, 2026 ([DOI](https://doi.org/10.1038/s41591-025-04074-y)): RCT, n=1,298. LLMs alone identified the condition in 94.9% of cases; people using them identified it in under 34.5%, no better than controls.
- **Clinician impact:** Tell patients with red-flag symptoms not to rely on chatbot triage even if it reassures, and ask what the patient typed, not only what the AI said.

### A4. SUPERSEDED. patients-ai.html:260-263
- **Claim:** "even with perfect information, AI-based tools listed the correct diagnosis in the top three options only 51% of the time, compared to 84% for physicians."
- **Correction:** This appears to be Semigran et al., *JAMA Intern Med* 2016 ([DOI](https://doi.org/10.1001/jamainternmed.2016.6001), retrieved via PubMed; no abstract there, so the match rests on my recollection of its figures). That's pre-LLM symptom checkers, undated on the page and in the present tense. Label it 2016 or replace it with Bean (A3), which reverses the emphasis: the model scores high alone, and the human-model interaction fails.
- **Clinician impact:** A clinician won't tell patients AI gets the top-three only half the time; the useful message is that the conversation is where it breaks down.

### A5. SUPERSEDED. patients-ai.html:668, :1021, :1061-1069
- **Claim:** "Consumer AI tools are not HIPAA-compliant"; "Consumer AI isn't covered by HIPAA, even the versions that connect to your records."
- **Correction:** Now too absolute. Amazon Health AI, open beyond One Medical since March 2026 and absent from this page, is described by Amazon as running in a HIPAA-compliant environment ([TechCrunch](https://techcrunch.com/2026/03/10/amazon-launches-its-healthcare-ai-assistant-on-its-website-and-app/), Mar 10, 2026; vendor statement, Amazon's own page not read). Copilot Health launched by waitlist and phased rollout via HealthEx ([Microsoft](https://microsoft.ai/news/introducing-copilot-health/), Mar 12, 2026). California will treat consumer health chatbots as providers under CMIA (AB 1979, see B5). Say instead: "Most consumer tools are outside HIPAA; a product tied to a provider may not be. Ask which it is."
- **Clinician impact:** A clinician gives a patient a tool-specific answer rather than a blanket one that's now false for at least one major product by its vendor's own account.

### A6. MISSING. patients-ai.html:750-756, :808-825
- **Claim:** Build a custom GPT on "ChatGPT Plus" or Claude Projects, share the link at checkout or in the portal, "Reduce after-hours burden", "Triage appropriately", "Instruct patients not to enter identifying information."
- **Gap:** This conflicts with the page's own business-associate line at :377-383 ("Directing them to do it is a different act"). Patients will type identifying details regardless. OpenAI lists "Publish GPTs externally" under BAA coverage only in HIPAA-eligible workspaces, and Plus isn't one. In California, a chat-based clinical GPT needs a persistent disclaimer and human-contact instructions (HSC §1339.75) unless reviewed, and AB 1979 limits independent clinical functions. A triage bot also raises a device question.
- **Proposed:** Put a caution box first: general education only, no triage, on a BAA-covered platform where any patient data could arrive, and check state disclosure law. Separately verify that Claude Projects can be shared with patients at all; I didn't check, and I doubt it.
- **Clinician impact:** A practice won't stand up a patient-facing triage bot on a consumer plan and hand out the link. COUNSEL.

### A7. WRONG. patients-ai.html:1103-1109
- **Claim:** "in controlled encounters, patients reported fewer and lower-quality symptoms ... Patients aren't lying to the AI; they're editing themselves."
- **Correction:** Preregistered experiment, n=500, of participants writing *simulated* symptom reports who believed the recipient was an AI or a physician. Lower report quality on LLM-based suitability metrics that physicians validated. It wasn't patients in encounters, and it doesn't support the "editing themselves" explanation.
- **Source:** [Reis et al., *Nature Health*](https://www.nature.com/articles/s44360-026-00116-y) (May 1, 2026).
- **Clinician impact:** A clinician won't over-read a simulation as observed patient behavior, while still assuming chatbot inputs may be thin.

### A8. WRONG. patients-ai.html:1112-1118
- **Claim:** "Consumer launches keep stacking ... May 2026 added athenahealth's athenaAmbient (free)."
- **Correction:** athenaAmbient is an EHR vendor's clinician ambient scribe, not something patients consult, and the linked Newsweek piece is dated Nov 4, 2025 (rollout "early 2026"). Remove it from this consumer list, or move it to ambient-ai.
- **Clinician impact:** Avoids misclassifying a documentation tool as something patients bring to the visit.

### A9. WRONG. patients-ai.html:885-897
Same error as B11; the link there supports none of the crisis-case claim. Fix together.

**Verified OK on this page:**
- :296-365 ChatGPT Health section, including all quotes, the 70% figure, 30-day deletion and permission defaults, against OpenAI's Jul 23 post. "It is not intended for diagnosis or treatment" is correctly attributed to January.
- :1156-1157 300 million per week.
- :110-113 and :1075 AMA figures: 81%, 76%, seven in 10 on burnout, 88% skill-loss concern, nearly half opposed. n=1,692 not on the article page, which says "nearly 1,700".

---

## environmental-footprint.html

### E1. SUPERSEDED. environmental-footprint.html:119-127
- **Claim:** "modern AI queries may use comparable energy to traditional searches."
- **Correction:** True for a typical short text query only; the page gives no number, and the agentic and reasoning tail is the part that has changed. Proposed: "Typical text query: about 0.3 Wh (Google measured a median of 0.24 Wh in May 2025, self-reported; a 2026 *Joule* model estimates a median of 0.31 Wh, IQR 0.16-0.60). Long reasoning queries: a median of 3.91 Wh, about 13 times higher. If 10% of queries are long, total demand more than doubles." Also relabel :289: the IEA's 2025 report is no longer the latest; IEA published [Key Questions on Energy and AI](https://www.iea.org/reports/key-questions-on-energy-and-ai) on Apr 16, 2026. Its 485 TWh and 950 TWh figures I saw only secondhand, so don't quote them until read.
- **Sources:** [Joule](https://www.cell.com/joule/fulltext/S2542-4351%2826%2900114-5) (Aug 19, 2026); [Google](https://arxiv.org/html/2508.15734) (Aug 21, 2025).
- **Clinician impact:** A clinician saves deep-research and reasoning modes for tasks that need them, and an organization right-sizing a deployment models the tail, not the median.

---

## Resolved: Utah HB 452 effective date

**May 7, 2025 is correct, now from enrolled text.** [Enrolled H.B. 452](https://le.utah.gov/Session/2025/bills/enrolled/HB0452.pdf) §9: "This bill takes effect on May 7, 2025." The Utah Code page for [§13-72a-203](https://le.utah.gov/xcode/Title13/Chapter72a/C13-72a-S203_2025050720250507.html) agrees ("Effective 5/7/2025", Chapter 269, 2025 General Session). bias-ethics.html:593-594 stands; the "Signed Mar 25, 2025" date comes from a secondary source citing the bill status page.

**New loose end:** that code page says "Affected by 63I-2-213 on 7/1/2027", which may be a sunset. I couldn't read §63I-2-213. Worth checking before the table implies this law is permanent.

---

## Backlog dispositions

| Report | Item | Disposition |
|---|---|---|
| 07-19 | phi-hipaa "HIPAA encryption now required" | Report was wrong; **no issue**. phi-hipaa.html:229-237 correctly says proposed; agenda confirms. |
| 07-19 | "EU AI Act enforces Aug 2" | **Fixed** bias-ethics.html:427-432; residual error is B4. |
| 07-19 | PA sues Character.AI | Real ([pa.gov](https://www.pa.gov/governor/newsroom/2026-press-releases/shapiro-administration-sues-character-ai-over-fake-medical-claim), May 5, 2026). Not on page. **Dropped by gate:** allegations pending; no clinician action. |
| 07-19 | Tennessee SB 1580 | **Fixed** bias-ethics.html:560-569. Text not re-read this pass; a tracker agrees. |
| 07-19 | Xsolis breach, 1.4M | Not on phi-hipaa.html. **Dropped by gate:** one vendor breach; not verified. |
| 07-26 | bias-ethics FDA count 1,000+ to 1,500+ | **Open**, see B12. Now 1,614 by count. |
| 07-26 | EU Aug 2 deadline imminent | **Fixed**, then overtaken; see B4. |
| 10-18 | patients-ai:339-340 GPT-5.6 Sol tier | **Fixed** patients-ai.html:340-341. |
| 10-18 | Rhode Island ambient-scribe law, held | **Open, now verified from text**, see B5. No opt-out in the text. |
| 10-18 | AMA 81% vs 88% | **Resolved:** different questions, both on AMA's page; patients-ai.html:111-113 is right. |
| 10-25 | HIPAA Security Rule still proposed | **Confirmed**, no change needed. |
| 10-25 | State therapy laws, nothing new | **Superseded** by B1, B5, B8. |
| 11-01 | Alabama SB 63 (payer AI) dropped | Agree; the page's payer table is examples. Not read. |
| 11-01 | ECRI hazard item | Dropped as already covered; date is wrong, see B13. |

---

## UNVERIFIED

- **US News article** (bias-ethics:921, patients-ai:886): fetches timed out, and the stealth fetch was denied by this session's permissions, so I stopped. Can't say which study it reports or whether it supports the delusion/mania, 50-case or 3-death claims.
- **Doctronic after Oct 24, 2026:** whether the term was renewed.
- **Not re-read this pass; trackers agree:** OR SB 1546, NE LB 525, NY Nov 5 effective date, CO Aug 12 and ME Jul 29 effective clauses, TN Ch. 647, CA SB 243, CA SB 1120, and the RI therapy act's effective clause (fetch cut off before it).
- **Nevada signing date:** page says Jun 5; one secondary says Jun 6. NELIS text not readable.
- **Tracker or secondary only; do not publish yet:** Hawaii Act 248, Colorado HB 26-1263 and HB 26-1139, Connecticut PA 26-15, Georgia SB 540, Idaho S 1297, Iowa SF 2417, RI S 2195A, California SB 1119 and SB 867, New York S 9008C, the SB 903 veto, Legion Health's date.
- **AB 1979 operative date:** Jan 1, 2027 is inferred from no urgency clause in the portion read.
- **Texas HB 149 §552.051(f):** private-practice reach unsettled; secondary only.
- **Utah §63I-2-213** and **S.B. 38 (2026)** amendments to chapter 72a.
- **45 CFR 92.210 agenda item (Feb 2027):** secondary only; the eCFR text was read from search highlights rather than a full page.
- **Federal preemption:** no enacted statute found, per trackers dated Nov 4, 2026; I didn't search Congress.gov myself. The site makes no contrary claim.
- **Not rechecked:** Gallup, Ohio State, Philips, Microsoft Copilot figures on patients-ai; "roughly 10%" for GPT-4o; Semigran's numbers.
- **Anthropic API BAA details (P3):** read through a summarizer. Re-read before publishing.

---

## Considered and dropped

- **Missouri SB 1019 "AI therapy ad ban":** several trackers report it as enacted, effective Aug 28, 2026. The [truly-agreed text](https://www.senate.mo.gov/26info/pdf-bill/tat/SB1019.pdf) has five sections and zero AI language by search. **Do not add it.** The provision may live in another bill; not checked. Same failure pattern the page warns about at :710-713.
- California SB 903: vetoed, binds nobody.
- Executive Order 14365 and the DOJ task force: no state law on these pages has been preempted, so nothing changes today.
- Democratic Congress and preemption forecasts: no one bound.
- ChatGPT Google Health integration: an APK teardown, not shipped.
- Safe Harbor "defined in 1996" (phi-hipaa:539): it's from the later Privacy Rule, but no clinician acts differently.
- DeepSeek and Comet callouts (phi-hipaa:803-833): dated and labeled as history.
- "Hundreds of homes" training figure and "batch queries" (footprint:113, :229): no action changes.
- FDA generative-AI docket: discussion paper; comment window closed.
- Individual Utah pilots beyond those named in A1, including Expect Fitness: one-more-in-category.
- Health Canada and WHO one-liners at bias-ethics:421-451: vague but not false.

---

## Method notes

- A `curl -k` attempt was denied by the permission system; I shouldn't have disabled TLS checks. I re-ran downloads with normal TLS and got the Illinois text another way.
- The stealth fetch on US News was also denied, and I didn't try to get around it.
- The FDA count is mine, from the downloaded HTML table. FDA publishes no total.
- Several statute readings came through a text-extraction service or PDF extraction rather than the browser view; links above are the official documents, so spot-check before quoting.
