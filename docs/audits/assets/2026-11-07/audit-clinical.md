> **Lead correction:** C6 below repeats the site's "no BAA" error for ChatGPT for Clinicians. See `docs/audits/2026-11-07-content-audit.md`, corrections 1 and 3.

# Clinical pages content audit: 2026-11-07

Scope: clinical-decision-support.html, ambient-ai.html, ai-search.html, medical-learners.html at HEAD bc3d757. Read-only; no repo changes. All four pages were read in full. Study details come from PubMed records and the publisher pages linked (DOIs given). Line numbers are for the current files.

## Summary

| Page | Verdict | Findings | WRONG | SUPERSEDED | MISSING |
|---|---|---:|---:|---:|---:|
| clinical-decision-support.html | needs edits | 10 | 3 | 4 | 3 |
| ambient-ai.html | needs edits | 9 | 5 | 1 | 3 |
| ai-search.html | needs edits | 3 | 2 | 1 | 0 |
| medical-learners.html | needs edits | 5 | 2 | 0 | 3 |

What the Nov 1 commits changed on these pages (049c6b9, 9ab8102):

- **clinical-decision-support.html:** UpDoc wording and the FDA deadline. Otherwise navigation and the footer.
- **ambient-ai.html:** one October callout and the Dragon licensing paragraph. Otherwise navigation and the footer.
- **ai-search.html:** two new callouts plus meta-description renames.
- **medical-learners.html:** the Gemini Notebook rename only.

So "Updated Nov 2026" currently overstates the review on all four cards.

### Recommended card dates

| Page | Show now | After edits ship | Reason |
|---|---|---|---|
| clinical-decision-support.html | Aug 2026 | Nov 2026 | Last broad pass was Jul 28, plus the Aug 23 FDA paragraph; Nov 1 touched two passages only. |
| ambient-ai.html | Aug 2026 | Nov 2026 | Aug 23 was the last broader pass; Nov 1 added one callout and one licensing paragraph. |
| ai-search.html | Aug 2026 | Nov 2026 | Nov 1 added two top callouts, but the body tools and comparison tables were not reviewed. |
| medical-learners.html | Jul 2026 | Nov 2026 | The Jul 28 citation audit (a9b0f9f) is the last content review; Nov 1 was a rename. |

---

## clinical-decision-support.html: needs edits

### C1. WRONG: FDA "single recommendation" criterion is inverted
- **file:line:** clinical-decision-support.html:1182-1184
- **Claim:** Key non-device criteria include that "the tool should provide a single, clinically appropriate recommendation."
- **Correction:** FDA's reading of Criterion 3 is the reverse. Lists and prioritized lists of options meet it. Software giving a specific output or directive fails it. FDA intends enforcement discretion only where one option alone is clinically appropriate and the software meets all the other criteria. Rewrite to say that, and add that FDA considers automation and time-critical decisions under Criterion 4, because automation bias is greater under urgency.
- **Source:** FDA CDRH town hall transcript on the CDS final guidance, March 11, 2026, https://www.fda.gov/media/191560/download; slides https://www.fda.gov/media/191561/download; guidance page dated January 2026, https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-support-software
- **Clinician impact:** A clinician should treat a tool's single directive as a regulatory flag to check rather than a sign that it qualifies as non-device.

### C2. MISSING: OpenEvidence's "free" is ad-funded, with query-relevant pharma ads
- **file:line:** clinical-decision-support.html:122-129, :375; also ambient-ai.html:135-136, :766. No mention of advertising on any of the four pages.
- **Claim:** "Free" access is recommended as the first thing to do, with no statement of how it is funded.
- **Correction:** Add that OpenEvidence is advertising-funded. Its advertiser site offers "query-relevant, full-screen interstitial engagements to HCPs during a captive moment when they query OpenEvidence about your disease state." Its ad policy (updated March 4, 2026) requires fair balance, bars confusion with clinical content, and bars off-label promotion. Neither source establishes that ads change answers, and the text should say so.
- **Source:** https://ads.openevidence.com/ (undated, read Nov 7); https://www.openevidence.com/policies/ads-policies (March 4, 2026); privacy policy (September 17, 2026) https://www.openevidence.com/policies/privacy
- **Clinician impact:** A clinician choosing between treatments on OpenEvidence should separate adjacent ads from the cited answer and check the citations when a branded therapy is in play.

### C3. SUPERSEDED: OpenEvidence BAA steps conflict with the vendor's own statement
- **file:line:** clinical-decision-support.html:550-556 (conflicts with phi-hipaa.html:366, "free BAA available for covered entities")
- **Claim:** The organization "must sign" a BAA, an authorized signatory completes it online, and individuals without an organizational BAA should stay de-identified.
- **Correction:** OpenEvidence says covered entities "may choose to transmit" PHI under its "standard Business Associate Agreement or other customer-specific agreements." Its April 25, 2025 announcement says covered entities who input PHI "agree" it will be handled under the BAA. Describe that, and keep "confirm with your compliance office." I could not read the BAA itself (see UNVERIFIED), so do not state that the signatory step is gone without checking.
- **Source:** https://www.openevidence.com/security (read Nov 7); https://www.openevidence.com/announcements/openevidence-is-now-hipaa-compliant (April 25, 2025)
- **Clinician impact:** A solo clinician needs the actual route to PHI use before recording or entering patient data, and the current text may send them looking for a form that may not exist.

### C4. WRONG: Doctronic described as autonomously renewing prescriptions
- **file:line:** clinical-decision-support.html:1216-1218, :1222 (compare medical-learners.html:968, "AI-assisted")
- **Claim:** Doctronic "deployed an AI system that autonomously renews prescriptions."
- **Correction:** Utah's regulator says the pilot is in Phase 1, where all requests require authorization by a licensed practitioner. It also reports hard stops against unauthorized controlled-substance dispensing and describes the red-team findings as vulnerabilities under adversarial use. Reporting through September found 2,317 requests, fewer than 600 completed by the AI, and physician review of those renewals. Rewrite as "designed to move toward autonomous renewal; human authorization in the current phase." Keep the jailbreak lesson. Utah's scope count is 191 drugs per Fierce, not 190.
- **Source:** https://commerce.utah.gov/ai/regulatory-relief-4/authorized-pilots/doctronic/ (undated status update, about three months into the pilot); https://commerce.utah.gov/wp-content/uploads/2026/05/Doctronic-Outcomes-May-2026.pdf (May 2026); KUER, October 22, 2026, https://www.kuer.org/health/2026-10-22/utah-ai-prescription-pilot-doctronics; Fierce, August 10, 2026, https://www.fiercehealthcare.com/ai-and-machine-learning/deep-dive-doctronics-ai-prescription-refill-pilot-program-utah
- **Clinician impact:** A clinician answering a patient or colleague can say correctly that a physician still authorizes these renewals in the current phase.

### C5. SUPERSEDED: "Doximity GPT" is now Doximity Ask
- **file:line:** clinical-decision-support.html:393-399. Grep count of "Doximity GPT": 1 here, 1 at resources.html:249 (its link goes to /gpt), and uncommitted videos.html:405 ("GPT", not to be published). Doximity's own old /gpt/ page still says "DoxGPT"; its current product pages say Ask.
- **Correction:** Rename to Doximity Ask. Say it is free with a verified account, and that Doximity says users can include PHI in prompts. Add that UpToDate-based answers are rolling out alongside Ask, but only to clinicians at health systems that use both products. This is not free UpToDate for everyone. Label Doximity's homepage NOHARM ranking as vendor-presented if it is mentioned at all.
- **Source:** https://www.doximity.com/ask/overview; https://support.doximity.com/hc/en-us/articles/55381817186195-Doximity-Ask-FAQs; https://www.wolterskluwer.com/en/news/doximity-wolters-kluwer-uptodate-doximity-ask (October 20, 2026); https://support.doximity.com/hc/en-us/articles/56694248433299-Doximity-UpToDate
- **Clinician impact:** A clinician looking for the tool by the page's name won't find it, and could wrongly assume Doximity now gives them UpToDate.

### C6. MISSING: ChatGPT for Clinicians from the general-purpose section and BAA table
- **file:line:** clinical-decision-support.html:402-425, :593-603
- **Claim:** General-purpose tools "lack the curated knowledge bases and citation infrastructure"; the BAA table lists ChatGPT for Healthcare only.
- **Correction:** Add ChatGPT for Clinicians, launched April 22, 2026: free for verified US physicians, NPs, PAs and pharmacists, with OpenAI describing cited clinical search. Add a BAA row matching big-three.html:249-268 and phi-hipaa.html:346 (no BAA), and qualify the "lack citations" sentence.
- **Source:** https://openai.com/index/making-chatgpt-better-for-clinicians/ (April 22, 2026). The no-BAA status comes from the site's own pages; it was not reconfirmed on OpenAI's page in this pass.
- **Clinician impact:** A clinician reading only this page would not know a free clinician-branded ChatGPT exists, or that its verification does not make it safe for PHI.

### C7. SUPERSEDED: CME note predates the July 28 CE/MOC platform
- **file:line:** clinical-decision-support.html:447-448, :497-499 (ai-search.html:961-968 already covers the launch)
- **Claim:** "Free AMA PRA Category 1 Credits for verified NPI users."
- **Correction:** Say physicians, NPs and PAs can earn accredited CE from their own searches by documenting reflection, through AKH joint providership, with MOC through "select certifying boards" and tracking in CME Passport. Link openevidence.com/cme and tell readers to check their own board. The July 28 announcement text I read does not itself say "AMA PRA Category 1" (see UNVERIFIED).
- **Source:** https://www.openevidence.com/announcements/openevidence-launches-new-education-platform-offering-continuing-education-ce-and-maintenance-of-certification-moc-credit (July 28, 2026)
- **Clinician impact:** Credit requires documented reflection, and MOC depends on the clinician's board, so the clinician should confirm both before relying on it.

### C8. MISSING: Prospective evidence, against "standard of care" language
- **file:line:** clinical-decision-support.html:297-298 ("becoming part of the standard of care"); evidence list at :1509-1593
- **Correction:** Soften :298 to "increasingly common" and add the Nature Medicine prospective study. It is a DECIDE-AI stage 1 observational evaluation in one tertiary ED (1,138 patients over 4 weeks; not randomized). Adoption fell from 68% to 30%. Expert review rated 99 of 100 sampled outputs appropriate. Length of stay did not differ (4.9 h in both). The authors say the findings "do not justify clinical deployment" at this stage.
- **Source:** According to PubMed: Leibovitch et al., Nat Med, August 19, 2026, [DOI](https://doi.org/10.1038/s41591-026-04601-5). The study is already on ai-news.html:289 but not on this page.
- **Clinician impact:** A clinician should not treat LLM decision support as an expected standard, since prospective data so far show appropriate sampled outputs with no length-of-stay benefit.

### C9. WRONG: "First time" claim for Abridge contradicts the page itself
- **file:line:** clinical-decision-support.html:1235-1236 (versus :361-362; also ambient-ai.html:1526-1530, which is limited to scribe vendors and can stay)
- **Claim:** "This is the first time a clinical AI company has wired first-tier peer-reviewed journals directly into a CDS engine at the point of care."
- **Correction:** Delete the sentence or limit it to "scribe-grounded," because the same page already credits OpenEvidence with NEJM and JAMA content partnerships.
- **Source:** Internal contradiction; https://www.fiercehealthcare.com/ai-and-machine-learning/jama-signs-multi-year-deal-openevidence-inform-ai-powered-medical-search (already cited at ai-search.html:1026)
- **Clinician impact:** A clinician comparing tools should not choose Abridge's CDS for a journal-content exclusivity it does not have.

### C10. SUPERSEDED: Glass access claims, and "future" integration that has shipped
- **file:line:** clinical-decision-support.html:133-134, :457-461, :1370-1375, :1390-1391; ambient-ai.html:770
- **Correction:**
  - Glass publishes Lite (free, limited), Starter $20, Pro $90 and Max $200, with EHR integration on Max. One Glass page says NPI-verified US clinicians get unlimited free use, while others describe Lite as limited, so tell readers to confirm the current plan. Ambient :770's "EHR integration for patient context" needs the Max qualifier.
  - Replace the "Nuance DAX" naming at :1390 and rewrite the "future" framing: Epic's Chart with Art and Dragon with UpToDate already embed these functions.
- **Source:** https://glass.health/compare; https://glass.health/resources/best-ai-medical-scribe (both undated; read Nov 7); https://www.epic.com/epic/post/real-results-right-now-how-epic-ai-is-reducing-costs-improving-care-and-helping-patients/ (March 10, 2026)
- **Clinician impact:** A clinician may be able to ask IT for an embedded option now rather than wait, and should not expect free Glass to write into the EHR.

---

## ambient-ai.html: needs edits

### A1. WRONG: Upcoding claim overstates the sources, and the citation is wrong
- **file:line:** ambient-ai.html:1489-1500 (the PHTI link at :1495 goes to an AHA market scan)
- **Claim:** "Three coordinated publications in April 2026," including JAMA Health Forum, "all found" scribes "consistently suggest higher-acuity E&M codes than coders would assign from the same encounter."
- **Correction:** Remove that sentence and retitle "crisis." What I could verify:
  - JAMA Health Forum ran a Viewpoint and a commentary on January 9, 2026. The commentary says these points "have not been addressed empirically."
  - PHTI's April 2026 report is an Industry Insight from a Chatham House workshop. It reports one system's 5% rise in Level 5 and 7% in Level 4 established-patient visits, and payer responses including algorithmic downcoding.
  - UCSF cohort: +0.04 RVU per encounter, +1.81 RVU per week, no increase in denials. The authors leave upcoding unresolved.
  - WashU interrupted time series: +2% wRVU at day 150.
  - Mayo orthopaedics, single site with blinded audit of 200 encounters: ambient visits were coded higher than dictation visits by providers (3.11 vs 2.82) and by the auditor (3.24 vs 2.96). In both arms the provider level was below the auditor level, the reverse of the page's claim. Accuracy was 68% vs 74%.
- **Source:** https://www.phti.org/wp-content/uploads/2026/04/PHTI-Administrative-AI-Current-Use-and-Potential-Impact.pdf (April 2026); Fierce on PHTI, April 13, 2026, https://www.fiercehealthcare.com/ai-and-machine-learning/ai-speeding-prior-authorizations-while-driving-higher-costs-health-systems; https://jamanetwork.com/journals/jama-health-forum/fullarticle/2843726 (January 9, 2026); https://doi.org/10.1001/jamahealthforum.2025.5771. According to PubMed: [UCSF, JAMA Netw Open](https://doi.org/10.1001/jamanetworkopen.2025.53233); [WashU, JAMIA, Oct 18, 2026](https://doi.org/10.1093/jamia/ocag151); [Arias, JAAOS, Aug 31, 2026](https://doi.org/10.5435/JAAOS-D-26-00442).
- **Clinician impact:** A clinician should verify that each code is supported by what was actually done and expect payer scrutiny, rather than assume the scribe overcodes relative to a coder.

### A2. WRONG: JAMA study unit and strength
- **file:line:** ambient-ai.html:1447-1452
- **Claim:** "Per clinician per day," "the strongest controlled evidence."
- **Correction:**
  - It is an observational difference-in-differences study, normalized to 8 scheduled patient hours: 13.4 minutes less EHR time (3.0%) and 16.0 less documentation time (10.0%).
  - Time outside work hours did not change significantly. Adoption added 0.49 visits per week. The authors call this modest.
  - Randomized data are the stronger design and already sit on this page.
  - Add the later patient-side result: a UC Davis difference-in-differences study of 31,917 surveys found no evidence that scribes worsened or enhanced patient experience. Page :284-288 reports clinician-side satisfaction only.
- **Source:** https://jamanetwork.com/journals/jama/fullarticle/2847319 (April 1, 2026). According to PubMed: [Taylor et al., JAMIA, Sept 2026](https://doi.org/10.1093/jamia/ocag103).
- **Clinician impact:** A clinician should expect about a 10% cut in documentation time, not a large recovery of after-hours work.

### A3. WRONG: One trial presented as three, with wrong dates and a conclusion the authors do not draw
- **file:line:** ambient-ai.html:162-168, :1219, :1489, :1503, :1513-1517; same claim at ai-news.html:2066-2069
- **Claim:** "Nabla outperforms DAX" (Feb 2026); "NEJM AI Lukac RCT (2026)"; "Afshar RCT (May 2026)"; "Vendor choice matters."
- **Correction:**
  - Both RCTs were published November 26, 2025 in NEJM AI. The Lukac link at :163 and :1514 is the July 2025 preprint; use DOI 10.1056/AIoa2501000. Fix the "May 2026 ... Two NEJM RCTs" heading.
  - Lukac: Nabla had −9.5% time-in-note versus control (P=0.02), and DAX had no significant change. The scribes were used in only 33.5% and 29.5% of visits, so "72,000 encounters" overstates exposure.
  - The 7.8% Nabla-vs-DAX result appears in the preprint, not the published abstract. The published conclusion says clinicians "reported that performance was similar across the two distinct platforms" and that secondary burnout findings need confirmation.
  - For "vendor choice," cite the Duke crossover trial, which masks products as A and B (160 clinicians; B better by 3.19 min/day in notes).
- **Source:** https://ai.nejm.org/doi/full/10.1056/AIoa2501000; https://ai.nejm.org/doi/full/10.1056/AIoa2500945 (both November 26, 2025). According to PubMed: [preprint](https://doi.org/10.1101/2025.07.10.25331333); [Chowdhury et al., JAMIA, May 2026](https://doi.org/10.1093/jamia/ocag018).
- **Clinician impact:** A clinician picking a scribe should pilot it locally rather than treat a brand ranking as settled.

### A4. MISSING: Consent litigation, plus a script that promises deletion
- **file:line:** ambient-ai.html:643-685 and script at :682-685
- **Correction:**
  - Add that proposed class actions are pending against Sharp HealthCare (San Diego Superior Court, filed November 26, 2025) and against Sutter and MemorialCare (N.D. Cal., filed April 8, 2026), all involving Abridge, which is not a defendant. Label the allegations unproven.
  - The Sharp complaint alleges that notes stated patients were advised and consented when that did not happen, and that the vendor retained recordings for 30 days.
  - Practice change: never let a template attest to consent you did not obtain.
  - Change the script's "The recording is deleted after the notes are generated" to a fill-in matching your tool's real retention. Page :587 already says retention varies.
- **Source:** Medscape, January 16, 2026, https://www.medscape.com/viewarticle/health-system-sued-over-ai-scribe-technology-patient-consent-2026a10001k7; Medscape, April 16, 2026, https://www.medscape.com/viewarticle/patients-sue-two-more-health-systems-over-ai-scribe-use-lack-2026a1000bwq; complaint, https://www.alstonprivacy.com/wp-content/uploads/2026/04/US_DIS_CAND_4_26cv3012_d13525803e781_COMPLAINT_Class_against_All_Defendants_Filing_fee_-1.pdf; status tracker (secondary), https://ailawsuittracker.com/cases/saucedo-v-sharp-healthcare-25cu063632c/. According to PubMed: [The Consent Gap, NEJM AI, Sept 2026](https://doi.org/10.1056/AIltr2600505) (title only read).
- **Clinician impact:** A clinician should say the retention facts accurately, get consent for real, and remove any auto-inserted consent line that isn't true.

### A5. MISSING and WRONG: Rhode Island's law, and the state tally
- **file:line:** ambient-ai.html:643, :654-661, :1397
- **Claim:** 38 + DC one-party states and 11 all-party states. That sums to 49 states. Nevada is listed as all-party and Oregon is omitted.
- **Correction:**
  - Add Rhode Island: providers using AI to document visits must notify patients and review the documentation for accuracy. Enacted and effective June 22, 2026 (H 7538 Sub A and S 2570 Sub A).
  - Replace the hard counts with "about a dozen; rules differ for in-person and phone." Per the Reporters Committee (2021) and Justia: Oregon requires all participants be informed for in-person conversations, Nevada's all-party rule is for phone calls, and Connecticut's civil rule is for phone calls. Say "check your state," because ambient capture is usually in person.
- **Source:** https://webserver.rilegislature.gov/PublicLaws/law26/law26199.htm; https://webserver.rilegislature.gov/PublicLaws/law26/law26372.htm; Sheppard Mullin, August 28, 2026, https://www.sheppard.com/insights/blogs/rhode-island-becomes-first-state-to-require-ai-scribe-disclosure-and-opt-out-process (its "opt-out" headline is not in the enacted text I read); https://www.rcfp.org/introduction-to-reporters-recording-guide/; https://www.justia.com/50-state-surveys/recording-phone-calls-and-conversations/
- **Clinician impact:** A clinician in Rhode Island or Oregon reading this page could miss a legal duty to notify patients.

### A6. SUPERSEDED: Order-drafting chronology, and Epic missing from the vendor grid
- **file:line:** ambient-ai.html:722-772, :1534-1553, :1588
- **Claim:** "June 2026 Update: The Scribe Starts Drafting Orders," framed around Abridge as a category change.
- **Correction:**
  - Epic released AI Charting on February 4, 2026. It drafts notes and "queues up orders based on the conversation," and Epic says clinicians review before orders are placed. Epic now calls it Chart with Art. Add it to the grid.
  - New boundary to add: Ambience said on September 23, 2026 that its Care Gap Advisor can pend an order from a guideline gap for signature. That origin is the chart rather than the conversation.
  - Boundary result: I found no vendor announcing orders placed without clinician signature, so :1588's "no order-placing autonomy" framing still holds as of November 7.
- **Source:** https://www.epic.com/epic/post/epic-ai-charting-rolls-out-alongside-an-expanding-set-of-built-in-ai-capabilities/ (February 4, 2026); https://www.healthcaredive.com/news/epic-rolls-out-ai-charting-art-notetaking-documentation-scribe/811462/ (February 5, 2026); https://www.ambiencehealthcare.com/blog/introducing-ambience-chorus-%E2%80%94-part-2-system-of-action (September 23, 2026)
- **Clinician impact:** A clinician on Epic may already see queued orders, and should read each pended order as a proposal, including ones never spoken in the visit.

### A7. WRONG: Freed and Heidi pricing
- **file:line:** ambient-ai.html:750, :754
- **Claim:** Freed "$99/month ... Free tier available (3 notes/week)." Heidi "$99/month ... Free tier available."
- **Correction:**
  - Freed's page shows Starter $39 (40 notes/month), Core $79 (unlimited), Premier $119 monthly or $104 on the cheaper billing, and a 7-day free trial. I saw no free tier.
  - Heidi's current pricing page shows plans but no dollar figures in the text I could read. Secondary reports cite $150 monthly or $110 annually for Clinician (checked by the reporter October 20, 2026), with a free plan carrying sponsored content and de-identified training under September 29, 2026 terms. Link to Heidi's page instead of quoting $99, and check those terms before publishing the free-plan caveat.
- **Source:** https://www.getfreed.ai/pricing (read Nov 7); https://www.heidihealth.com/en-us/pricing (read Nov 7); secondary: https://medaidirectory.com/blog/heidi-health-review-2026
- **Clinician impact:** An independent clinician budgeting from this page gets the wrong price and would expect a Freed free tier that its pricing page does not show.

### A8. MISSING: Doximity Scribe in "Prioritize This" and the vendor grid
- **file:line:** ambient-ai.html:130-139, :747-771
- **Correction:** Add Doximity Scribe: free for US physicians, NPs, PAs and medical students with a verified account, and described by Doximity as HIPAA compliant. Note that free tools are not free of tradeoffs: OpenEvidence is ad-funded (C2), and the clinician should confirm BAA terms for any tool used to record patients.
- **Source:** https://www.doximity.com/clinicians/scribe (read Nov 7)
- **Clinician impact:** An independent clinician deciding whether to pay $79 or more can test a free option first.

### A10. WRONG: Christ Hospital result mislabeled as ambient AI
- **file:line:** ambient-ai.html:1463-1467
- **Claim:** A 69% vs 46% early lung cancer rate is called "ambient AI's most important clinical contribution."
- **Correction:** Epic describes Art extracting incidental findings from radiology results and driving follow-up. That is not ambient listening. The figure is a vendor-reported single-hospital rate compared with a national average, with no control group or study design given. Label it so and remove the ambient framing. Numbering skips A9 deliberately; see Considered and dropped.
- **Source:** https://www.epic.com/epic/post/real-results-right-now-how-epic-ai-is-reducing-costs-improving-care-and-helping-patients/ (March 10, 2026)
- **Clinician impact:** A clinician should not expect a scribe rollout to improve lung cancer stage at detection.

---

## ai-search.html: needs edits

### S1. WRONG: Suggests using Perplexity Health on patients' records
- **file:line:** ai-search.html:272-273
- **Claim:** "The same capability is a useful research surface for clinicians querying their own patients' records."
- **Correction:** Delete the sentence. Perplexity describes "connectors to your personal health data" for a person's own records. Its announcement describes no clinician workflow and no BAA. Replace with: "It is built for a patient's own data; do not connect or enter your patients' records."
- **Source:** https://www.perplexity.ai/hub/blog/introducing-perplexity-health (March 19, 2026)
- **Clinician impact:** The current sentence could prompt a clinician to put PHI into a consumer tool, so they should not do this.

### S2. WRONG: Search defaults and plan requirements
- **file:line:** ai-search.html:667, :684-685, :623, :674 (:656 already contradicts :684 on the same page)
- **Claim:** Models don't search "unless you specifically ask"; Claude search "Requires Pro"; Gemini Deep Research needs an "Advanced" subscription.
- **Correction:**
  - Anthropic says that in the new Claude experience there is no toggle and "Claude searches the web when it helps." Its help page also gives web fetch guidance for free accounts.
  - Say tools may search automatically, so look for citations and a search indicator.
  - Change Gemini "Advanced" to the current Google AI plan names, matching big-three.html:455. Remove Claude's Pro requirement.
- **Source:** https://support.claude.com/en/articles/10684626-enabling-and-using-web-search (October 7, 2026). Per-vendor ChatGPT defaults not rechecked; page :656 already says automatic.
- **Clinician impact:** A clinician may wrongly believe an answer is training-data only or pay for a feature they already have, and should check for citations instead.

### S3. SUPERSEDED: AI Overview accuracy rests on a marketing-firm number
- **file:line:** ai-search.html:347-349, :456-459, :467-469, :485, :492-494, :898
- **Claim:** Perplexity 13% vs AI Overviews 26% from a 2025 Wordstream study; "13-26% error rates in current studies"; follow-up requires a new search; health Overviews link to authoritative sources.
- **Correction:**
  - Label Wordstream as a non-clinical marketing comparison and stop calling it current.
  - Add the October 29, 2026 preprint (arXiv, not peer reviewed) on 3,611 health questions: 44.4% of the top five results were cited, an estimated 56.7% of cited statements were supported by their cited page, 38.2% of physician-rubric points were earned, and 22.2% contained a specific anticipated harmful claim where the rubric named one. It also found 93.4% had no factual error on the general check, and that commercial publishers were over-represented.
  - Add that Google removed some health Overviews after the January 2026 Guardian investigation.
  - Fix the "new search required" row: Common Sense Media's July 2026 assessment reports an "Ask Anything" box routing from Overviews into AI Mode.
- **Source:** https://arxiv.org/abs/2610.39339 (October 29, 2026); https://www.theguardian.com/technology/2026/jan/11/google-ai-overviews-health-guardian-investigation (January 11, 2026); https://www.theverge.com/news/860356/google-pulls-alarming-dangerous-medical-ai-overviews (Google's response, January 11, 2026); https://institute.commonsensemedia.org/sites/default/files/risk-assessments/csm-ai-risk-assessment-google-search-07142026_0.pdf (July 14, 2026)
- **Clinician impact:** A clinician should warn patients that an Overview's citation may not support its statement, and should open the source before relying on it.

---

## medical-learners.html: needs edits

### L1. MISSING and WRONG: Published residency-application rules, and "often detectable"
- **file:line:** medical-learners.html:383-387 (workflow at :363-378)
- **Claim:** AI-written content is "generic and often detectable"; the page cites no application rule.
- **Correction:**
  - Quote AAMC: AI is "acceptable for brainstorming, proofreading or editing the personal statement, but the final submission should represent your own work."
  - Add that AAMC says ERAS does not use AI to analyze applications and Thalamus does not determine whether essays were AI-written, but Thalamus Cortex does read personal statements with AI for certain characteristics.
  - Replace "detectable" with the real risks: plagiarism investigation and accuracy duties. The NRMP requires complete and accurate information.
  - Add AMA's advice that AI is a poor source for deadlines and program facts, and that a human should be the last reader.
- **Source:** https://www.ama-assn.org/medical-students/preparing-residency/how-use-ai-residency-applications-learn-rules-road (September 9, 2026; quotes the AAMC language); https://www.aamc.org/services/use-artificial-intelligence-aamc-service-programs (undated); https://www.nrmp.org/wp-content/uploads/2025/09/2026-Policy-Highlights-Applicants.pdf
- **Clinician impact:** A learner can use AI within the published rule and stop relying on a detection risk the application services say they do not apply.

### L2. MISSING: First bedside RCT on student ChatGPT use
- **file:line:** medical-learners.html:279-282, :880
- **Correction:** Add the RCT in final-year students at four academic hospitals (73 analyzed, ChatGPT GPT-4o vs no aids, minimal training). Overall clinical exam score did not differ (66.7 vs 68.2), and 37% reported distraction, with no preferential benefit for weaker students. It measures assessed performance with the tool, in a middle-income setting, not long-term learning. :880's "direct evidence does not yet exist" is the Perspective's statement, so keep the attribution and add this next to it.
- **Source:** According to PubMed: Saloojee et al., Med Teach, online April 20, 2026 (issue 48(11)), [DOI](https://doi.org/10.1080/0142159X.2026.2652061)
- **Clinician impact:** A student should not assume bringing a chatbot to the bedside improves performance without structured training.

### L3. MISSING: Built-in study modes
- **file:line:** medical-learners.html:576-626
- **Correction:** Add ChatGPT study mode (Socratic questions and knowledge checks; launched July 29, 2025 on Free, Plus, Pro and Team), Gemini Guided Learning, and Claude's Learning Mode. Say evidence is thin and vendor-run: Google's own University of Tokyo statistics RCT reported 8.1 vs 5.3 percentage-point gains in one session, not in medicine.
- **Source:** https://openai.com/index/chatgpt-study-mode/ (July 29, 2025); https://blog.google/products-and-platforms/products/education/guided-learning/ (August 6, 2025); https://blog.google/products-and-platforms/products/education/guided-learning-uk-japan/ (November 3, 2026); Inside Higher Ed on Claude's Learning Mode, https://www.insidehighered.com/news/tech-innovation/artificial-intelligence/2025/08/07/understanding-value-learning-fuels-chatgpts (August 7, 2025)
- **Clinician impact:** A learner following this page's "build, don't bypass" advice should turn on the mode that asks questions rather than gives answers.

### L4. WRONG: Gemini Notebook "only works with what you upload"
- **file:line:** medical-learners.html:571-573
- **Correction:** It answers from the sources in the notebook, but Fast Research and Deep Research can pull in web sources, which the user selects and imports. Tell students to check what they imported, because "my curriculum only" holds only if they kept it that way.
- **Source:** https://support.google.com/gemininotebook/answer/16215270 (read Nov 7); https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-deep-research-file-types/ (November 13, 2025)
- **Clinician impact:** A student should review the source panel before assuming a study guide reflects only course material.

### L5. WRONG: Philips self-report framed as "measured"
- **file:line:** medical-learners.html:974-979
- **Claim:** "The upside, measured ... found AI already saves clinicians the equivalent of 16+ working days."
- **Correction:** Change to "A vendor survey: clinicians report." The Philips release describes perspectives from health professionals, and time savings are reported by respondents. Compare the JAMA result in A2 (16 minutes per 8 patient hours). Philips sells healthcare technology, so say it is vendor-sponsored.
- **Source:** https://www.philips.com/a-w/about/news/archive/standard/news/press/2026/philips-future-health-index-2026-ai-is-already-saving-clinicians-time-and-delivering-measurable-impact-in-healthcare.html (June 9, 2026)
- **Clinician impact:** A trainee should not plan around a 16-day saving, because it is self-reported vendor survey data rather than measured time.

---

## Backlog dispositions

Calendar reports, Jul 19 to Nov 1. Verified against current files.

| Item | Origin | Status | Evidence |
|---|---|---|---|
| NotebookLM renamed Gemini Notebook, lines 7, 12 and current references | 07-19, 10-04, 10-18, 10-25 | FIXED | ai-search.html:7, :12, :83-84; medical-learners.html:537. Remaining uses at ai-search.html:631-638 are a callout dated February 2026 and acceptable as history. |
| OpenEvidence EvidenceGrade + NYP deployment | 07-19 | FIXED | ai-search.html:938-958 |
| Perplexity "SPACE" | 07-19 | Dropped | Not identifiable from the note; medical-learners.html:665 covers Spaces. No gate reason found. |
| npj study: 2/3 of Epic hospitals live | 07-19 | Dropped | Not on the page (grep none); adoption statistic fails the gate. |
| Abridge x Northwestern + Eli Lilly | 07-19 | Dropped | Not on the page; partnership news fails the gate. |
| Dragon Copilot agentic pivot | 07-19 | FIXED in general form | ambient-ai.html:177-179, :1534-1553; see A6 for order-specific gaps. |
| Rhode Island ambient-scribe law ("Holding") | 10-18 | OPEN, now verified from enacted text | See A5. The report's "opt-out" element is not in the enacted text I read. |
| Sutter/MemorialCare recording suit ("single mention") | 10-18 | OPEN, now verified | See A4. The 10-18 pointer to ambient-ai.html:1390 is stale; the current consent summary is :1397 and does not cover litigation. |
| AMA 81% vs 88% conflict | 10-18 | FIXED; not a conflict | medical-learners.html:107-113. AMA report verified: 81% awareness or use; 88% any skill-loss concern, a different question. Fielded Jan 15 to Feb 2, 2026, n=1,692. |
| ChatGPT for Clinicians, unconfirmed | 10-25 | Partly OPEN | Confirmed on OpenAI's page, April 22, 2026. On big-three and phi-hipaa but not the CDS page; see C6. |
| GPT-6 Epic integration | 10-25 | Not assessed | Not checked here; belongs to the models audit. |
| Regenstrief x Suki, Oct 24 ambient explainer | 11-01 | Dropped | Stays dropped; nothing on the page becomes wrong. |
| OpenEvidence Darwin | 11-01 | FIXED | ai-search.html:89 |
| FDA comment deadline | 11-01 commit | FIXED | clinical-decision-support.html:1332-1334 |
| Dragon reseller price | 11-01 commit | FIXED | ambient-ai.html:728-733 |

## FDA link result

clinical-decision-support.html:1335 is **live and correct. No change is required.** On November 7 the URL returned HTTP 200 for GET and HEAD, with both default and browser user agents, and I read the page through a separate fetcher. Its text matches the site's description: discussion purposes only, docket FDA-2026-N-7874, feedback by October 19, 2026.

The press release at :1336 also returned 200 (August 18, 2026). The PDF at https://www.fda.gov/media/194242/download returned 200 as application/pdf. FDA's October 13 reminder keeps the same date, and I found no extension.

The weekly check's 404 was not reproducible. The only 404 I could produce came from appending "-comments" to the slug, which is my guess at a truncated-title URL. The title actually ends "Request for Feedback," and FDA truncates the slug at "and-request." I can't say what the weekly checker requested, because the 404 record is not in the files I searched. Optional: add the PDF link as a second route.

## UNVERIFIED

- **openevidence.com/cme and /policies/baa** returned 403 to fetchers. This is anti-bot, not a dead link. A stealth fetch was denied by the permission system, so I did not retry or work around it. A third-party registry quotes the BAA as incorporated into the Terms of Use, last updated February 5, 2025, but I did not read it directly. Whether a signatory step still exists (C3), whether AMA PRA Category 1 still applies, and which boards count for MOC (C7, ai-search.html:966) all need a logged-in or browser check by Michael.
- **Status of Sharp's October 23, 2026 demurrer:** a tracker reports a minute order issued but gives no ruling. No ruling read.
- **Whether any Doctronic medication group has moved to Phase 2** by November 7, and whether the pilot contract was renewed in October. Latest human-review evidence is KUER, October 22.
- **"41 sec/note" at ambient-ai.html:1219:** not in the published abstract; full text not read.
- **72,000 encounters:** the two scribe arms total 48,349 visits; the control-arm count was not read. Total is plausible.
- **Heidi dollar prices** and terms: from secondary sources.
- **Missouri:** RCFP lists in-person all-party; Justia was not checked for Missouri, so I did not put it in the A5 correction.
- **npj Digital Medicine billing paper (ambient-ai.html:1494):** could not identify it; only "scaling" and "general practice" npj papers surfaced.
- **Not re-verified on these pages:** athenaAmbient no-cost status; Dragon 100K and 600+ counts; Abridge recognition items; Plaud, Granola and Suki compliance claims; Perplexity quotas and deep-research table numbers (ai-search.html:211, :585-624); Lancet Digital Health per-model figures at clinical-decision-support.html:1208-1210 (press release confirms 9 models, over a million prompts, Feb 9; not the percentages); NYU Nature Medicine details at ai-search.html:925-934; "QuizGPT" (medical-learners.html:706); UpToDate and DynaMed access details.

## Considered and dropped

- **A9, Abridge 150+ vs 300+ systems and Dragon "order-of-magnitude jump" (ambient-ai.html:738, :1544, :1523):** internally inconsistent and the second compares unlike units, but scale figures change no clinician decision. Fix when editing.
- **OpenEvidence 40% / 65,000 / 15M vs 20M (clinical-decision-support.html:127, :358-366; ai-search.html:1039):** adoption statistics, gated out; align if touched.
- **OpenEvidence "first AI to score 100% on USMLE" (clinical-decision-support.html:369):** vendor benchmark, framed as headlines; candidate for a "vendor-reported" label only.
- **Perplexity valuation and query counts (ai-search.html:148-151):** valuation, gated out.
- **Perplexity Model Council names Opus 4.7 and GPT-5.5 in a February callout (ai-search.html:228-229):** model naming, passed to the models audit.
- **Perplexity 93.9% SimpleQA (ai-search.html:549):** a non-clinical benchmark; no decision turns on it.
- **Bunkerhill/CMS and "lockstep" with an ECG citation (clinical-decision-support.html:1248-1253):** one-more clearance and a citation mismatch; gated out, low priority.
- **"Code Interpreter" and "Extended Thinking" feature names (medical-learners.html:587, :620):** cosmetic.
- **Doximity's NOHARM homepage ranking:** vendor-presented benchmark, not added as a finding.
- **Doximity and OpenEvidence lawsuit dismissal (Oct 16):** company dispute; no clinician action.
- **Utah's October pilots (Nolla, August AI, Expect Fitness):** not launched; one more entrant.
- **New ambient papers (JMIR, JGIM, JCO OP, trainee competency framework in npj, Oct 12):** titles reviewed only; no page claim becomes wrong. The npj trainee framework may merit a future learner-page read.
- **AI-INFOCARE RCT (NEJM AI, Oct 15, 2026; [DOI](https://doi.org/10.1056/AIoa2600136)):** a patient-facing previsit summary in one neurosurgical clinic with no clear scribe or CDS claim to fix; better suited to news.
- **ACR x OpenEvidence patient fact sheets (Nov 6):** partnership news.
