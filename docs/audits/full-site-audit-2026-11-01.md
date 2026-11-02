# Full site audit and second content pass — November 1, 2026

**Prepared for owner review as v1.16. Not a publication receipt.** The baseline
was live v1.15, repository main `c663696`. The deployed content receipt remains
unchanged in `latest.json`; proposed changes are recorded separately.

## Coverage and evidence

- Fetched all 30 tracked root HTML routes, including the `30-days.html` redirect.
  Every deployed response matched the baseline repository source. Checked local
  destinations, fragments, duplicate IDs, image alt attributes, language and
  canonical metadata. No missing internal pages or fragments at baseline.
- Checked 560 distinct external URLs. 484 returned HTTP 200; five content URLs
  repeatedly returned 404; two additional 404s were harmless font preconnect
  origins. The other 69 results were blocked or indeterminate (403, 429, 999,
  challenge/redirect responses or network errors), not confirmed dead links.
  [Baseline inventory and unresolved URLs](assets/2026-11-01/link-baseline.json).
- Rendered all 29 nonredirect pages in Chromium at 1440×1000 and 390×844, before
  and after. Inspected saved desktop/mobile screenshots for eight representative
  pages: home, Start Here, PHI/HIPAA, Big Three, news, contribution, Claude Code
  and GitHub. Also inspected targeted table, form and failed-icon-service cases.
- Tested shared menus, expanded state and Escape; keyboard entry/skip behavior;
  course progress persistence; and navigation with the Lucide request blocked.
  No form submission, chatbot conversation or patient information was used.
- Read primary sources for the highest-risk privacy/regulatory assertions,
  stale product descriptions and the second catch-up window, August 24–November 1.
  This is broad technical coverage and risk-prioritized factual verification,
  not a revalidation of every historical sentence or a WCAG certification.

## Findings and proposed repairs

P1 means high consequence for privacy or regulatory interpretation. P2 means
material usability, freshness or maintenance risk. All repairs below are in the
review branch; they have not been verified in production.

| Priority | Finding | Proposed disposition |
| --- | --- | --- |
| P1 | Consumer health-app use was conflated with a covered entity's unauthorized disclosure. | Distinguish individual app use from a clinician's continuing HIPAA duties; cite HHS FAQ 2079. |
| P1 | Claude's BAA table contradicted the PHI page; blanket Cowork exclusions were stale. | Explain HIPAA-ready Enterprise, required configuration, and separate local/cloud Code and Cowork scope. Individual/Team plans are not covered by the product name. |
| P1 | Blanket Notebook exclusion omitted the Cloud Enterprise product. | Distinguish ordinary Gemini Notebook from Gemini Notebook Enterprise on Google's Cloud BAA list. |
| P1 | OpenAI API eligibility was reduced to a ZDR-only rule. | Describe executed BAA, eligible organization/account, feature and retention configuration; distinguish live internet search from specifically covered offline/cache-only modes. |
| P1 | August news gave a June UpDoc clearance date, and categorical first-LLM claims exceeded FDA evidence. | Preserve the correct December 23, 2025 date in the main module; correct news/RSS chronology, describe provider-directed insulin management, attribute the first claim to the vendor. |
| P1 | EU AI Act scope incorrectly used training on EU patient data as a standalone territorial trigger. | Replace with Article 2 market/deployment/output scope and distinguish separate privacy law. |
| P1 | Contribution form lacked a title and put its PHI reminder below a 1,941px iframe. | Put the fictional-data-only warning before entry, label the iframe, lazy-load it, provide a direct form link. |
| P2 | MedGemma history omitted the January 2026 1.5 4B release and made global validation/SOTA claims. | Add the release, update the variant table and qualify readiness for the intended use case. |
| P2 | Stale current examples remained outside Big Three. | Correct About, prompting, ordinary Gemini plan naming, patient-model assignments, image/video and What's Next; distinguish dated historical blocks from current guidance. |
| P2 | GLM weights status was frozen before the August 26 release. | Add GLM-5.3-Flash publisher weights and MIT license; distinguish the full model and hardware/clinical-readiness limits. |
| P2 | Five external content URLs repeatedly returned 404. | Replace two OpenAI release paths, Dragon reseller pricing, Spotify episode and FTC guide with relevant first-party/publisher destinations; correct unsupported adjacent wording. |
| P2 | 27 mobile menus lacked expanded/controlled state, Escape behavior, and failed when the icon CDN was unavailable. | Shared local navigation script, ARIA state, Escape with focus return, and an inline SVG menu icon independent of the CDN. |
| P2 | Keyboard bypass and several metadata labels were inaccessible. | Add skip links and main targets to all 29 content pages, visible focus, reduced-motion scrolling, darker selected light-background labels. Preserve code-block colors. Broader contrast review remains below. |
| P2 | RSS duplicated one story, omitted four HTML stories, and linked an unlinked warning to a missing fragment on the old domain. | Remove the duplicate from both representations, add the actual warning ID and canonical permalink, generate all 119 feed entries from HTML with unique stable GUIDs. Weekly checks now catch drift; imprecise historical dates do not acquire invented days. |
| P2 | Retired module references and stale card dates obscured the topic structure. | Replace exercise module numbers with topic names, add fictional-case guidance, refresh dates only for substantive content changes. |
| P2 | Catch-up missed clinically relevant studies and product changes. | Add the eight primary-source items below, retaining comparator, supervision and outcome limitations. |
| P2 | Three pages scrolled horizontally on mobile. | Contain search comparison tables; constrain course grid tracks and wrap long inline commands and definition terms. Confirmed all three at 390px after repair. |

| P2 | Deployment check searched the whole changelog, so an old release heading could falsely satisfy a receipt. | Require the live footer release to match the published receipt; regression tests cover a historical match with a different current footer. |

## Eight additional news items

These are eight additional stories beyond the eight published earlier today.
One duplicate historical story was removed, so the net HTML count increases by
seven. The final HTML/RSS inventory is 119 unique stories.

| Published | Source | Interpretation retained |
| --- | --- | --- |
| October 8 | [AMIE prospective feasibility](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736%2826%2901535-7/abstract) | 114 enrolled, 98 completed; physician supervision, no prespecified safety stops, one hallucination. Feasibility is not clinician replacement or outcome benefit. Publisher publication-history date used; later metadata explained. |
| October 5 | [OpenAI API changelog](https://developers.openai.com/api/docs/changelog) | Eligible-organization BAA setup does not cover every account, endpoint, tool or retention mode. |
| October 5 | [Ophthalmic history-taking RCT](https://www.nature.com/articles/s41746-026-03232-x) | 172 patients, single center; higher history score with median 11.2 vs 3.1 minutes. No general diagnostic-superiority or outcome claim. |
| October 1 | [Tanzanian retinopathy pathway RCT](https://doi.org/10.1016/j.langlo.2026.104062) | 2,378 participants; true-referable attendance 35.9% vs 18.2%. Immediate results and counseling were bundled, so this is not an isolated effect of image grading. |
| September 24 | [Sora API retirement](https://developers.openai.com/api/docs/guides/video-generation) | Retirement is past, not an upcoming deadline; no assumed replacement. |
| September 8 | [GPT Image 2.5](https://developers.openai.com/api/docs/guides/image-generation) | Image-production capability is not medical illustration validation or consumer-plan entitlement. |
| September 1 | [Multisite ambient-scribe study](https://doi.org/10.1136/bmjcdh-2026-000008) | Four hospitals, 58 clinicians; before/after comparison and no randomized causal attribution. |
| August 26 | [GLM-5.3-Flash](https://z.ai/blog/glm-5.3-flash) | Publisher weights and MIT license verified; 320B-scale availability is not ordinary laptop feasibility or clinical validation. |

Additional correction sources: [Anthropic Enterprise scope](https://support.claude.com/en/articles/13296973-hipaa-ready-enterprise-plans),
[Google Cloud HIPAA services](https://docs.cloud.google.com/docs/security/compliance/hipaa),
[OpenAI data controls](https://developers.openai.com/api/docs/guides/your-data),
[FDA clearance](https://www.accessdata.fda.gov/cdrh_docs/pdf25/K253281.pdf),
[FDA device review](https://www.accessdata.fda.gov/cdrh_docs/reviews/K253281.pdf),
[EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng),
[MedGemma model card](https://developers.google.com/health-ai-developer-foundations/medgemma/model-card),
[Dragon Copilot licensing](https://www.microsoft.com/licensing/guidance/Dragon-Copilot),
[OpenAI Work security](https://learn.chatgpt.com/docs/enterprise/chatgpt-work-cloud-security).
The HHS FAQ and remaining publisher references are linked at the corrected text.

## Verification

- Nine Python unit tests pass, including shared-source RSS identifiers,
  idempotent generation, no fabricated publication days, and valid local warning
  permalinks. `python3 scripts/sync_news_feed.py --check` confirms 119 items.
- Final static check: all 30 root pages have zero missing local targets, missing fragments or duplicate IDs. [Results](assets/2026-11-01/local-final.json).
- Full browser confirmation: no JavaScript page errors across 58 page/viewport
  combinations. All 27 mobile menus opened with expanded state and closed with
  Escape. With the icon CDN aborted, the menu still opened and no page error
  occurred. Both courses retained progress after reload.
- The first confirmation found remaining long-command/definition overflow in
  both courses. A targeted repair and fresh-page recheck confirmed width=390 and
  scrollWidth=390 on both courses, search, contribution and home. Fresh keyboard
  Tab reaches the skip link and Enter focuses main on all five.
- Saved browser observations: [before](assets/2026-11-01/browser-before.json),
  [confirmation](assets/2026-11-01/browser-after.json),
  [final targeted recheck](assets/2026-11-01/browser-final-targeted.json).
- Ran the Impeccable detector once on changed interface targets. It returned
  existing accent-card/style, small-text and static contrast warnings rather
  than a clean certification. Incumbent typography and callout styling are
  intentionally preserved. The known pale metadata labels were darkened;
  remaining phase-colored small labels merit a separate computed-style and
  assistive-technology pass. Static inherited-color warnings are not accepted
  as proof of a rendered 1:1 color pair. No redesign or automated score is claimed.

## Selected visual evidence

| Case | Baseline | Proposed |
| --- | --- | --- |
| Mobile course width/progress | [Claude Code before](assets/2026-11-01/course-before.png) | [Claude Code after](assets/2026-11-01/course-after.png) |
| Optional icon outage | [Menu unavailable](assets/2026-11-01/icons-before.png) | [Menu opens](assets/2026-11-01/icons-after.png) |
| Contribution entry | Warning was below the iframe in baseline source | [Warning and fallback before entry](assets/2026-11-01/form-after.png) |
| Search comparison table | Wrapper forced 600px page width | [Contained horizontal table](assets/2026-11-01/table-after.png) |

## Work still requiring attention

1. The 69 blocked/indeterminate URLs require provider-specific or interactive
   verification; they are retained in the evidence inventory. HTTP 200 itself
   also does not verify an article's claims.
2. Claude cloud's own issue credential, primary-source egress, and adoption of
   the new hosted routine instructions still need a successful research-run
   receipt. The independent GitHub check does not repair those capabilities.
3. Complete assistive-technology, zoom/reflow, cross-browser and computed-color
   coverage remains open; course sidebars are long on mobile, though the skip
   link now bypasses them. No full WCAG compliance claim is made.
4. Third-party chatbot/form authorization, retention and outgoing payloads were
   not privacy-audited. No submission or real patient data was used.
5. State-law inventories, historical country-block notices and every older
   research/vendor claim were not independently revalidated. Keep dated history
   distinct from current advice; this report does not provide blanket legal or
   clinical approval.
6. Production must be checked after an owner-approved merge. The v1.16 footer,
   changelog and pending-review record in this branch are proposed release
   content, not evidence that publication already occurred.
