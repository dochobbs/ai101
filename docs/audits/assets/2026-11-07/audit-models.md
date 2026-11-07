# Audit: model and product pages (HEAD bc3d757, checked 2026-11-07)

Pages: big-three, whats-next, local-models, vibe-coding, everyday-ai, image-video. Line numbers are current working-tree lines. Sources were fetched 2026-11-07 unless a date is given. Help-center pages show relative "Updated" labels, so those are quoted as displayed.

**What the Nov 1 commits really did.** Only big-three got a substantive pass (9ab8102, +62/-40), and it covered the current-offering sections. The others got a callout plus small edits:
- whats-next: one callout and one sentence.
- vibe-coding: one paragraph.
- everyday-ai: one access line and one price.
- image-video: one callout and the Sora tense.
- local-models: the MedGemma paragraph plus two callouts.

The "Updated Nov 2026" badges on those five overstate the review.

## Summary

| Page | Verdict | Findings | Card date today | Card date once fixed |
|---|---|---|---|---|
| big-three | needs edits | 10 | Nov 2026, but the BAA error makes it unearned until fixed | Nov 2026 |
| whats-next | needs edits | 6 | Jul 2026 | Nov 2026 |
| local-models | needs edits (model tables and commands) | 10 | Aug 2026 | Nov 2026 |
| vibe-coding | needs edits | 5 | May 2026 | Nov 2026 |
| everyday-ai | needs rewrite (custom-tools section, plus a PHI section) | 7 | Jun 2026 | Nov 2026 |
| image-video | needs edits | 5 | Jul 2026 | Nov 2026 |

Reasons for today's card date:
- whats-next: last real content pass was 0e25b99 on Jul 28; Nov 1 added only a "use current catalogs" callout. The card text (index.html:285-288) itself says "updated through the July 2026 model wave".
- local-models: last pass over the model content was Aug 23; Nov 1 touched MedGemma and GLM only, and the hardware and install sections were not reviewed.
- vibe-coding: last section is May 2026; Nov 1 changed only the Claude Code paragraph. The card text also advertises May content (index.html:301-304).
- everyday-ai: last content edit was db691ee on Jun 10 (readings); the body is older.
- image-video: last real pass was caddc2f on Jul 28.

---

## big-three.html

**BT1. WRONG. big-three.html:251, :266, :299-301 (and table row :564-565)**
- Claim: ChatGPT for Clinicians is "**Not** a BAA tier", "is *not* covered by a BAA and should not be used with PHI", and is "explicitly not covered".
- Correction: OpenAI lists ChatGPT for Clinicians as a HIPAA-eligible product. Eligible individual clinicians can sign a BAA themselves under Settings > Agreements. This has been the position since launch; the Apr 22 announcement already said "Optional support for HIPAA compliance". Keep these limits: designed for individual use; "Do not share PHI... unless a BAA is in place and you are authorized to sign a BAA for your account"; third-party GPTs and connected apps need their own agreements; multi-user or admin-controlled use means ChatGPT for Healthcare.
- Sources: https://help.openai.com/en/articles/20001202-chatgpt-for-clinicians (displayed "Updated: 15 days ago"); https://help.openai.com/en/articles/20001069-hipaa-eligible-products-and-functionality; https://openai.com/index/making-chatgpt-better-for-clinicians/ (2026-04-22)
- Clinician impact: a solo or practice-owning physician told no BAA exists will either skip a free compliant option or use a non-BAA tool instead, while an employed physician needs to know that signing authority is the real gate.
- Same error outside my scope: phi-hipaa.html:346 ("No BAA... explicitly not for PHI").

**BT2. WRONG. big-three.html:297-298, :564**
- Claim: BAAs are available on "Enterprise/Edu plans".
- Correction: OpenAI's eligible list is ChatGPT for Healthcare, ChatGPT for Enterprise **with Regulated Workspace**, ChatGPT FedRAMP, ChatGPT for Clinicians, API with Modified Retention, and API FedRAMP with Modified Retention. Edu is not on it, and ordinary Enterprise is not sufficient as listed. "Team" at :299 is now "Business".
- Source: https://help.openai.com/en/articles/20001069-hipaa-eligible-products-and-functionality
- Clinician impact: a clinician at an academic center on ChatGPT Edu or plain Enterprise would wrongly assume PHI is covered.

**BT3. WRONG. big-three.html:483-484, :1199-1200**
- Claim: Google Workspace is "the most straightforward consumer-tier HIPAA pathway" and Gemini "offers the most straightforward consumer HIPAA pathway". This contradicts the page's own warning at :587-589.
- Correction: the path is an organization's Workspace account with Google's BAA signed through the Admin Console; a personal Google account or AI Pro subscription is not it. Say "most straightforward for organizations already on Workspace". Also add that Google's list covers "Gemini app (excluding Gemini in Chrome)".
- Source: https://workspace.google.com/terms/2015/1/hipaa_functionality/ (as of Aug 31, 2026)
- Clinician impact: "consumer" invites a clinician on a personal Google AI plan to enter PHI.

**BT4. WRONG. big-three.html:888**
- Claim: "Premium tiers ($200-250/month)".
- Correction: paid tiers above $20 now start around $100: ChatGPT Pro $100/$200/$500, Claude Max $100 and Ultra $200. Google AI Ultra from $99.99 is secondary only (see UNVERIFIED).
- Sources: https://learn.chatgpt.com/docs/pricing; https://claude.com/pricing
- Clinician impact: someone outgrowing $20 thinks the next step costs twice what it does.

**BT5. WRONG. big-three.html:292-294**
- Claim: "image generation through DALL-E". The table at :529 already says GPT Image.
- Correction: "ChatGPT Images". The official DALL·E GPT was retired Aug 30, 2026. API removal on May 12, 2026 is from a secondary report.
- Source: https://help.openai.com/en/articles/6825453-chatgpt-release-notes (Jul 31 entry; Nov 4 entry for Images 2.6)
- Clinician impact: they look for a tool that no longer exists.

**BT6. SUPERSEDED. big-three.html:286-289, :541**
- Claim: GPT Store listed as the ecosystem's main draw.
- Correction: custom GPTs and their pages are scheduled to retire Dec 11, 2026, replaced by plugins. Note that "plugins" at :541 is accidentally right again, because plugins is the replacement. See EA1.
- Source: https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq
- Clinician impact: don't pick ChatGPT because of pre-built GPTs that disappear in five weeks.

**BT7. MISSING. big-three.html:229-236, :281**
- Claim: tier cards omit ChatGPT Go, and the callout only says to check the model picker.
- Correction: OpenAI states the answer. GPT-6 is rolling out in Chat to Pro, Plus, Enterprise and Business. Free and Go use GPT-5.6 Luna. In Chat, GPT-6 Sol powers Instant through Extra High, and Pro effort uses Astra on eligible plans. Add a Go card; price is in UNVERIFIED.
- Source: https://help.openai.com/en/articles/11909943-gpt-5-in-chatgpt (displayed "Updated: 8 days ago"); https://chatgpt.com/pricing
- Clinician impact: a clinician comparing Free with Plus can see that paying changes the model family, not just the limits.

**BT8. SUPERSEDED. big-three.html:612, :1529**
- Claim: "The current flagship is Grok 4.6". The footnote says the privacy policy is "Effective April 2026". :610 says "built by xAI".
- Correction: Grok 4.7 (Sep 21, 2026) is xAI's stated "most capable model". The operating name on x.ai is now SpaceXSI, policy last updated Oct 27, 2026. Rechecked and still accurate: the policy still asks users not to provide health information and still lists model training as a use, so the page's PHI argument stands. Grok 5 has not shipped per secondary reporting.
- Sources: https://docs.x.ai/docs/models; https://docs.x.ai/developers/release-notes; https://x.ai/legal/privacy-policy
- Clinician impact: small; a clinician discussing Grok with a patient uses the current name, and the PHI advice is unchanged and now confirmed against the current policy.

**BT9. WRONG. big-three.html:1201**
- Claim: "Claude offers the largest context window outside of Gemini". The page's own table (:523) has ChatGPT at 1.05M against Claude's 1M.
- Correction: delete the clause.
- Source: internal contradiction; https://claude.com/pricing ("Up to 1M")
- Clinician impact: removes a false reason to choose Claude for long documents.

**BT10. WRONG. big-three.html:1262-1265**
- Claim: in the March 2026 callout, "Meta Llama 4 (February 15) introduced Scout". The linked page is Meta's April 2025 post, and local-models:286 says "April 2025".
- Correction: remove or re-date. Meta's actual 2026 open release is Muse Glimmer (LM7).
- Sources: https://huggingface.co/api/models?author=meta-llama (Llama 4 repos created 2025-04-04); https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model (2026-08-10)
- Clinician impact: a health-system reader weighing on-prem options thinks a 19-month-old model is new.

---

## whats-next.html

**WN1. WRONG. whats-next.html:315, :1300-1302, :1347, :1371, :1375**
- Claim: "Build custom GPTs", "Build a Custom GPT" is one of seven immediate actions and appears in the 30-day challenge.
- Correction: personal accounts (Free, Go, Plus, Pro) can no longer create new GPTs. Replace with ChatGPT Projects or skills, or with Claude Projects or Gems. See EA1.
- Source: https://help.openai.com/en/articles/8554397-creating-a-gpt (displayed "Updated: 4 days ago")
- Clinician impact: the page's main starter action cannot be done on a personal account.

**WN2. WRONG. whats-next.html:1193-1196**
- Claim: Atlas is a current browser, "Currently Mac only".
- Correction: Atlas was retired; it was scheduled to stop working Aug 9, 2026. Remove the card. If a replacement is wanted, OpenAI points to the desktop app browser and the Chrome extension. The AI-browser warning at :1207-1237 still holds.
- Sources: https://help.openai.com/en/articles/20001371-chatgpt-atlas-retirement; https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- Clinician impact: they would go looking for a dead product.

**WN3. WRONG. whats-next.html:1129-1130**
- Claim: "OpenAI's Operator is in preview".
- Correction: Operator was folded into ChatGPT agent, and ChatGPT agent "is no longer available". OpenAI directs users to ChatGPT Work. Note also that "allow browser use for Work in the cloud" is listed as not covered under the BAA.
- Sources: https://help.openai.com/en/articles/11752874-chatgpt-agent; https://help.openai.com/en/articles/20001069-hipaa-eligible-products-and-functionality
- Clinician impact: they would look for a retired tool, and they should know the replacement's browser feature is outside the BAA.

**WN4. MISSING. whats-next.html:1256-1259, :1276-1278, :1352**
- Claim: under "Level 1: Zero Risk... No patient information", connect "your email, calendar, and a language model" via n8n or Zapier.
- Correction: a clinician's mailbox often contains PHI, and the page itself calls prompt injection "an unsolved security problem" (:1214-1216). Either scope this to a non-clinical account or take it out of "Zero Risk", and add that each connected service needs its own agreement. The OpenAI help page says connected third-party services are not automatically covered.
- Source: internal contradiction; https://help.openai.com/en/articles/20001069-hipaa-eligible-products-and-functionality
- Clinician impact: they don't pipe a work inbox with patient messages through a third-party automation on the strength of a "zero risk" label.

**WN5. SUPERSEDED. whats-next.html:316, :1264, :1372**
- Claim: "NotebookLM".
- Correction: "Gemini Notebook", renamed Jul 16, 2026.
- Source: https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook (2026-07-16)
- Clinician impact: they find it under its current name in Gemini and Workspace.

**WN6. WRONG. whats-next.html:1076-1082**
- Claim: in the March 2026 callout, Llama 4 Scout "launched" and is "a viable path toward institutional AI".
- Correction: it dates from April 2025. Scout needs 67 GB even at Q4 per Ollama. Point instead to Muse Glimmer (Apache 2.0, 24-32 GB) and Qwen3.8-27B, with the existing no-validation caveat.
- Sources: https://ollama.com/library/llama4/tags; https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model
- Clinician impact: an on-prem discussion starts from a current model rather than a stale one.

---

## local-models.html

**LM1. MISSING. local-models.html:98-99, :136, :659-661, and install sections :713 and :841**
- Claim: "patient data never leaves your machine", "Data never leaves your machine", "Local models eliminate this".
- Correction: both recommended tools now offer cloud inference from the same interface. Ollama: `gemma4:cloud` models, a setup prompt to sign in, and "To use only local models, disable cloud features". LM Studio's site now leads with Bionic, a separate app with LM Studio Secure Cloud. Add: "local" describes the model you actually selected. Disable Ollama cloud features, avoid `:cloud` tags, and use the local runtime in Bionic. Zero data retention is not a BAA.
- Sources: https://docs.ollama.com/cloud; https://lmstudio.ai/blog/introducing-lm-studio-bionic (2026-07-16); https://lmstudio.ai/docs/bionic
- Clinician impact: a clinician following this page could send PHI off-device by choosing a cloud-tagged model while believing the setup is local.

**LM2. WRONG. local-models.html:785-792**
- Claim: `ollama run phi3 --temperature 0.7`, `--ctx-size 4096`, `--num-predict 500`.
- Correction: none of these flags exist. Inside a session use `/set parameter temperature 0.7`, `/set parameter num_ctx 4096`, and `/set parameter num_predict 500`, or use a Modelfile or the API `options`.
- Sources: local `ollama run --help`, client v0.40.3, lists no such flags; https://docs.ollama.com/faq; https://docs.ollama.com/cli
- Clinician impact: the commands as printed will fail.

**LM3. WRONG. local-models.html:771, :592**
- Claim: `ollama pull llama4:scout-8b-q4_k_m`, and a 32-64GB Mac runs "Llama 4 Scout at Q4".
- Correction: that tag does not exist. The real one is `llama4:17b-scout-16e-instruct-q4_K_M` (alias `llama4:scout`), and it is **67 GB**, so it does not fit a 32-64GB machine with room to run.
- Source: https://ollama.com/library/llama4/tags
- Clinician impact: a failed pull, then a 67 GB download onto hardware that can't run it.

**LM4. WRONG. local-models.html:596, :437, :290 (and big-three.html:703-705)**
- Claim: a 96GB+ Mac Studio runs "DeepSeek V4 Pro variants"; V4 Pro is the "Maximum capability" pick on a hardware table; V4 is the "late-2025/early-2026 line"; big-three calls V4-Flash part of "the realistic self-host tier".
- Correction: V4 Pro is 1.6T parameters, about 800 GB at Q4 by the page's own memory math. V4 Flash is 291B, about 145 GB at Q4, which is server or high-end workstation scale, not a clinician's desk. The repos were created April 2026. The DeepSeek API now serves V4.1-Flash-1017 under `deepseek-flash`.
- Sources: https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro; https://huggingface.co/api/models/deepseek-ai/DeepSeek-V4-Flash; https://api-docs.deepseek.com/quick_start/pricing
- Clinician impact: they don't buy a $5,000+ machine for a model it can't load.

**LM5. WRONG. local-models.html:298**
- Claim: Kimi K2.6 "remains the more practical option for coding-adjacent local work".
- Correction: K2.6 is 1.03T parameters with `license: other`, about 500 GB at Q4. It is not a local option in any ordinary sense. Delete the sentence and point to Qwen3.8-27B.
- Source: https://huggingface.co/moonshotai/Kimi-K2.6 (model summary "1T"; API total 1,026,879,376,368)
- Clinician impact: they stop chasing a model the callout right beneath it says belongs in a datacenter.

**LM6. SUPERSEDED. local-models.html:393-405, :84**
- Claim: GLM-5.3 is "Announced Open, Not Yet Open"; the November note says the promise "does not establish full GLM-5.3 weight availability".
- Correction: full weights are published at zai-org/GLM-5.3 (141 safetensors, 753B parameters) under a bespoke GLM-5.3 License, not MIT. That license adds a Z.AI security-review clause for Model-as-a-Service operators with more than $10B revenue. Flash remains MIT. The exact weights-publish date is not established; the repo was created 2026-08-25 and last modified 2026-10-14.
- Sources: https://huggingface.co/zai-org/GLM-5.3; https://huggingface.co/zai-org/GLM-5.3/raw/main/LICENSE
- Clinician impact: a health system's compliance reader gets the current status and learns GLM-5.3 is no longer MIT like GLM-5.2, which is the page's own "read the license that shipped" lesson.

**LM7. SUPERSEDED. local-models.html:103-105, :286, :306**
- Claim: "the open-weight Llama 4 line continues to ship and remains the substrate for most new medical fine-tunes".
- Correction: Meta's open release is now **Muse Glimmer** (Aug 10, 2026): 30B parameters, Apache 2.0, 4-bit under 20 GB, built for 24/32 GB machines. I found no Llama 4 release after April 2025. "Most new medical fine-tunes" has no source; delete it or source it.
- Sources: https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model; https://huggingface.co/meta-models/Muse-Glimmer-30B
- Clinician impact: someone with a 32 GB laptop now has a realistic current option, and the page stops steering them to a model they can't run.

**LM8. SUPERSEDED. local-models.html:293, :436-437 (cross-link from big-three.html:704)**
- Claim: lists Qwen 3.6 27B. big-three sends readers here for Qwen3.8-27B, which this page never mentions.
- Correction: add Qwen3.8-27B (27.8B parameters, Apache 2.0, repo created Aug 2026) to the notable models and to the hardware table in place of V4 Pro.
- Source: https://huggingface.co/Qwen/Qwen3.8-27B
- Clinician impact: the cross-link lands on the model it promises, and the 32-64GB row has a recommendation that fits.

**LM9. WRONG. local-models.html:310, :421**
- Claim: MedAlpaca-7B is "Available in Ollama" and recommended for 8-16GB.
- Correction: https://ollama.com/library/medalpaca returns 404 and search finds no such library entry. Remove the claim or give the Hugging Face route. `meditron:7b` and `phi3` do exist.
- Source: https://ollama.com/library/medalpaca (404)
- Clinician impact: the recommended pull fails on the lowest-hardware path, where beginners start.

**LM10. SUPERSEDED. local-models.html:237, :1058**
- Claim: the access line and resource link point to `google/medgemma-4b-it`, while the table at :188 leads with MedGemma 1.5 4B.
- Correction: add `google/medgemma-1.5-4b-it`. Card note: 1.5 exists only as the 4B variant.
- Source: https://huggingface.co/google/medgemma-1.5-4b-it
- Clinician impact: they would download the older checkpoint believing it is the one described.

---

## vibe-coding.html

**VC1. WRONG. vibe-coding.html:1254-1258, :1272-1283, :1331**
- Claim: "consumer vibe coding platforms... are not HIPAA-compliant", the first project is "immediately useful in your practice", and a stretch goal adds "a 'custom instructions' text field for patient-specific notes" in Replit or Lovable.
- Correction: "consumer" understates it for Lovable: "Lovable does not currently sign Business Associate Agreements and is not HIPAA-compliant. Do not upload protected health information", on Enterprise too. Replace the stretch goal with non-identifying template text. Add that generated instructions need clinician review before reaching a patient, since the project generates discharge content.
- Source: https://docs.lovable.dev/introduction/lovable-for-enterprise
- Clinician impact: the page's own stretch goal would otherwise lead them to type patient details into a platform that prohibits it.

**VC2. SUPERSEDED. vibe-coding.html:634-652, :688-693**
- Claim: saving data "requires creating a Supabase account"; "Connect Supabase Early".
- Correction: Lovable's built-in backend (Cloud) is on by default and may be enabled automatically, with database, auth and storage hosted by Lovable and no Supabase account. Migrating an existing Supabase project to it is not supported. Add that a Supabase BAA would not reach Lovable Cloud (secondary, and follows from the BAA being with Supabase).
- Source: https://docs.lovable.dev/features/cloud
- Clinician impact: they learn their app's data sits on Lovable's backend by default, and they skip an obsolete setup step.

**VC3. SUPERSEDED. vibe-coding.html:862-867**
- Claim: "Codex macOS app", "macOS with Apple Silicon", a standalone app.
- Correction: Codex is now part of the ChatGPT desktop app (macOS and Windows; the Learn page also lists Linux) alongside Chat and Work.
- Sources: https://learn.chatgpt.com/docs/app; https://help.openai.com/en/articles/20001276-moving-to-the-new-chatgpt-desktop-app
- Clinician impact: a Windows user no longer rules it out.

**VC4. WRONG. vibe-coding.html:734-735, :754-760, :795-799**
- Claim: Claude Code's "Web Interface (claude.ai)" is a chat conversation producing Artifacts, recommended as the start ("Start on the Web").
- Correction: Artifacts in claude.ai chat are not Claude Code. Claude Code is No on Free and Yes on Pro and above; Artifacts are Yes on Free. The page's own :1840 gives the correct web address, claude.ai/code.
- Source: https://claude.com/pricing
- Clinician impact: a free-tier reader believes they have Claude Code when they have chat Artifacts, with very different file and command access.

**VC5. SUPERSEDED. vibe-coding.html:1820 (and :111)**
- Claim: "the Max plan ($100/mo or $200/mo)".
- Correction: Max is $100; the $200 tier is now Ultra.
- Source: https://claude.com/pricing
- Clinician impact: the plan name they're told to look for at $200 doesn't exist.

---

## everyday-ai.html

**EA1. WRONG. everyday-ai.html:107, :488-518, :532-576, :606, :610, :720-722, :767, :801**
- Claim: the page's lead action and one of three pillars: Custom GPTs, "Available to ChatGPT Plus subscribers", "Click 'Explore GPTs' then 'Create'", "publish to the GPT Store".
- Correction: "New GPT creation and publishing are not available on personal ChatGPT accounts, including Free, Go, Plus, and Pro." Custom GPTs retire Dec 11, 2026; a migration moves them to plugins, but custom actions don't transfer. Rewrite this pillar around ChatGPT Projects and skills, and rewrite the comparison table. Note: chatgpt.com/pricing still lists "custom GPTs" under Plus. The Help Center article is specific and dated more recently, so it should control, but the conflict is on OpenAI's side.
- Sources: https://help.openai.com/en/articles/8554397-creating-a-gpt; https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq
- Clinician impact: the first thing the page tells them to build can't be built on a $20 plan, and anything they made stops working in five weeks.
- Same issue elsewhere (grep counts, not reviewed by me): patients-ai 5, ai-tools-mcp 3, glossary 2, medical-learners 1, claude-code 1.

**EA2. MISSING. everyday-ai.html:136-147, :192, :202-206, :456-457 (whole page)**
- Claim: "I'm uploading 24 months of our practice's visit data", "A patient callback log", "Patient satisfaction survey analysis", and a staff policy assistant on Claude Pro. A grep for PHI, HIPAA or patient data in this page returns **zero** hits. The only caution is "redact sensitive information if needed" (:165), and that is about contracts.
- Correction: add a callout near the top: consumer plans have no BAA; individual Claude plans cannot enable HIPAA; consumer Claude's model-training control is opt-out; ChatGPT's own notice says chats "may be reviewed and used to improve our AI models". De-identify or aggregate practice data before upload. Link to phi-hipaa.html. Also fix :457: "Staff can ask" on Pro doesn't work, because project sharing is No on Pro and requires Team. Team has no BAA either.
- Sources: https://claude.com/pricing; https://support.claude.com/en/articles/13296973-hipaa-ready-enterprise-plans; https://chatgpt.com/atlas/ (page footer text)
- Clinician impact: a practice owner following the sample prompt would upload visit-level data to a consumer account with nothing on the page telling them not to.

**EA3. WRONG. everyday-ai.html:465, :476, :575, :610**
- Claim: Gems are "just custom instructions, no document uploads", available to "eligible Google AI subscribers", cost "$19.99/month". :545 already contradicts the first claim.
- Correction: "You can add files to give your Gem more context". Google's help lists no paid-plan requirement, only sign-in and age 13+ on a personal account. List as free to start.
- Sources: https://support.google.com/gemini/answer/15146780; https://support.google.com/gemini/answer/15236321
- Clinician impact: they could build a document-grounded tool for free instead of paying or choosing another platform.

**EA4. WRONG. everyday-ai.html:445, :574**
- Claim: Claude Projects "Available to Claude Pro subscribers ($20/month)".
- Correction: Free includes up to 5 projects.
- Source: https://claude.com/pricing
- Clinician impact: they can try it before paying.

**EA5. WRONG. everyday-ai.html:550-551**
- Claim: Claude Projects image generation "Yes"; Gems "Yes (Imagen 4)".
- Correction: Claude "doesn't generate photos or illustrations the way image-generation tools do"; it draws diagrams and charts with HTML and SVG. big-three:530 already says No. For Gems use Nano Banana rather than Imagen 4 (see IV1).
- Sources: https://support.claude.com/en/articles/9002504-can-claude-produce-images (2026-03-16); https://deepmind.google/models/model-cards/nano-banana-2-1/
- Clinician impact: they don't pick Claude for patient-handout illustrations it won't produce.

**EA6. WRONG. everyday-ai.html:289-295, :744-746**
- Claim: "Try NotebookLM"; "no hallucinations from outside information", recommended for contracts and board-exam study.
- Correction: it's Gemini Notebook now. Remove the no-hallucinations claim, because Google's own help says "Gemini Notebook can be inaccurate; please double check its responses". Restricting to sources reduces outside drift but doesn't prevent misreading a source.
- Sources: https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook; https://support.google.com/gemininotebook/answer/16212283
- Clinician impact: they keep checking cited passages, including for contract terms and board prep.

**EA7. MISSING. everyday-ai.html:354-358, :384-387**
- Claim: "AI makes an excellent tutor for your children" with no mention of account rules.
- Correction: add one line: age rules differ by product. Claude consumer accounts are 18+; Gemini personal accounts are 13+. Sit with younger children and use your own account where terms allow. ChatGPT's terms were not re-verified (see UNVERIFIED).
- Sources: https://www.anthropic.com/legal/consumer-terms (effective Oct 8, 2025); https://support.google.com/gemini/answer/15236321
- Clinician impact: for an audience heavy in pediatrics, parents don't set a child up on an account the terms prohibit.

---

## image-video.html

**IV1. SUPERSEDED. image-video.html:123-124, :252-253, :258-266, :834-841**
- Claim: Nano Banana 2 "is still your best starting point", "Resolution range: 512px through 4K", "the most accurate text".
- Correction: **Nano Banana 2.1** reached GA Oct 6, 2026 and `gemini-3.1-flash-image` is deprecated with no shutdown date announced. It is in the Gemini app. Reported limits include blurry small text at 1K and left-right confusion, and 512px is reported dropped (both secondary; see UNVERIFIED). Comparative "most accurate" claims have no current independent support, so state it as Google's claim or remove it.
- Sources: https://aistudio.google.com/docs/changelog; https://deepmind.google/models/model-cards/nano-banana-2-1/ (2026-10-06)
- Clinician impact: for a labeled patient handout, generate above 1K and proofread every label rather than trusting a "most accurate" badge.

**IV2. SUPERSEDED. image-video.html:382-386, :399-402, :376**
- Claim: "Omni Flash currently generates 10-second clips", "caps at ten seconds", $0.10/second.
- Correction: Omni 1.2 Flash (Nov 5, 2026) does 3-15 seconds, $0.07/second at 720p, with multi-turn editing. Free-of-charge route: Google Vids "with a Google account or Google Workspace subscription". In the Gemini app 15-second clips are rolling out to Ultra. Omni 1.1 added scene extension up to 40 seconds (Aug 27). The Veo 148-second point at :409 stands.
- Sources: https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/ (2026-11-05); https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/ (2026-08-27)
- Clinician impact: a short technique clip may need only Omni in Vids at no extra cost rather than a paid Veo workflow.

**IV3. WRONG. image-video.html:805**
- Claim: advanced project "Tools: Veo or Sora". The page itself says Sora was discontinued (:431-437).
- Correction: "Veo 3.1 or Gemini Omni Flash".
- Source: https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation
- Clinician impact: the hands-on project names a dead tool.

**IV4. SUPERSEDED. image-video.html:315-316, :865, :936**
- Claim: "GPT Image 2.5 Is the Current API Family"; Images 2.0 is "the current ChatGPT Images model"; "ChatGPT (GPT-5.6)" is the recommendation for conversational iteration.
- Correction: GPT Image 2.6 (Sunburst and Flare) and ChatGPT Images 2.6 shipped Nov 4, 2026. At :865 drop the model number, or note GPT-6 on paid plans and GPT-5.6 Luna on Free and Go.
- Sources: https://developers.openai.com/api/docs/changelog; https://help.openai.com/en/articles/6825453-chatgpt-release-notes; https://help.openai.com/en/articles/11909943-gpt-5-in-chatgpt
- Clinician impact: they compare the tool they actually have, and the 2.5 callout's anatomy caveat should carry over.

**IV5. SUPERSEDED. image-video.html:278**
- Claim: "Also available in NotebookLM".
- Correction: "Gemini Notebook".
- Source: https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook
- Clinician impact: minor; name match.

---

## Backlog dispositions (calendar-findings.md)

| Report | Item | Status |
|---|---|---|
| 07-19 | big-three: GPT-5.6 public | FIXED, big-three.html:1354 |
| 07-19 | big-three: Gemini 3.5 Pro missed deadline | FIXED, :433, :1360 |
| 07-19 | big-three: DeepSeek V4 official launch | PARTLY. Mentioned at :1266 and local-models:290, but the date and scale are wrong (LM4) |
| 07-26 | big-three: Fable/Mythos "suspended" error | FIXED, :1403-1410 |
| 07-26 | big-three: Opus 5, GPT-5.6, Gemini 3.6 Flash | FIXED, :1330, :1354, :1365 |
| 07-26 | local-models: LM Studio Bionic | OPEN, now LM1. Finding is verified; the Jul 16 date is correct |
| 07-26 | local-models: Kimi K2.6 to K2.7 | CHANGED. K2.7 Code exists per LM Studio's post, but the real problem is K2.6 isn't local at all (LM5) |
| 07-26 | local-models: stale rankings | FIXED, :302, :333 (dated) |
| 07-26 | vibe-coding: Opus 4.8 to 5; GPT-5.5 to 5.6 | FIXED by rewrite, vibe-coding.html:729-733; :1757 is labeled history |
| 10-04/18/25 | big-three: Claude generation stale | FIXED, :342-346, :389 |
| 10-04/18/25 | big-three: ChatGPT cards stale | FIXED by rewrite, :225-241, :281; gaps remain (BT7) |
| 10-04/18/25 | vibe-coding:728-731 default model | FIXED, :729-733. The earlier "Opus 5.5 default on Pro/Max/Team" framing was deliberately not repeated |
| 10-04+ | NotebookLM rename, on my pages | OPEN: whats-next (3), everyday-ai (4), image-video (1). ai-search is outside my pages |
| 10-25 | "ChatGPT for Clinicians... holding" | Now resolved: BT1 |
| 10-25 | "GPT-6 Astra Pro free clinician access" | Stays dropped. Did not verify the model tier on Clinicians beyond OpenAI's "current frontier models" |
| 11-01 | Tier cards :235/:240, table :496-497 | FIXED, :225-241, :523 |
| 11-01 | "Missing Aug-Oct callout" | FIXED inline rather than as a callout; the callouts still stop at July, which is acceptable because they're labeled history |
| 11-01 | "GPT-6 Astra is an unconfirmed rumor" | That report was wrong. Primary confirmation at OpenAI (BT7) |

Calendar claim I did not inherit: the 10-04 line "Opus 5.5 default on Pro/Max/Team/Enterprise" was not re-verified, because the current page doesn't assert it.

---

## UNVERIFIED

- **Google AI Ultra price** ($99.99 / $199.99). The one.google page fetch did not expose the figure; these come from two secondary trackers. big-three:459 deliberately doesn't state it, and BT4 only uses it as a floor.
- **ChatGPT Go price** ($8 per a secondary source). chatgpt.com/pricing text extraction dropped prices. Read it at edit time.
- **Gemini free tier now Flash-Lite only** (reported Oct 9 by TNW and 9to5Google citing Google's help page; I did not read that page). Would sharpen big-three:445.
- **Nano Banana 2.1 known limits** and **512px removal**: my model-card excerpt cut off before the limitations section. Reported by TNW and Genativity. Read the card before quoting.
- **Grok Business/Enterprise BAA scope**: third-party trackers say the chat app isn't confirmed covered and show a HIPAA badge on the Business page. x.ai/legal/baa not read. big-three:652-654 says API-only and doesn't name Grok Business; consider adding it.
- **Replit HIPAA posture**: only secondary sources (terms silent). VC1's Lovable claim is primary; the Replit half of the sentence is not re-verified.
- **DeepSeek "$1.74/M" for V4 Flash** (local-models:290, whats-next:134): looks like a Pro input price from memory. DeepSeek's page rendered without the price table on two URLs. Don't call it wrong until read; developer pricing anyway.
- **Canva prices** (image-video:512-513): canva.com blocks fetchers. Not contradicted.
- **OpenAI minimum age**: not fetched; EA7 cites Anthropic and Google only.
- **Gemini Notebook and HIPAA**: Google's Aug 31 list of included functionality doesn't name it. Could be how the list is organized. Worth a check by whoever owns phi-hipaa, which has 4 NotebookLM references.
- **"Omni is Google's default video model"**: a secondary paraphrase of Google's docs. If true, image-video:856 "best overall video tool" needs softening. The docs page timed out.
- **GLM-5.3 weights publish date**: only repo metadata available.
- **Atlas retirement date**: "scheduled to stop working on August 9"; the retirement article confirms retired but doesn't restate the date.

## Considered and dropped

- Gemini 4 Carbon (Oct 28): gated to cyber defenders, nothing for a clinician to do yet. Worth one line at the next refresh.
- big-three:671, :1419 Artificial Analysis scores (K3 60 vs 57): benchmark position, no practice implication. Note the index is now v5.0, so the numbers aren't comparable.
- big-three:1020-1100 April benchmark table: labeled as a snapshot and says it's superseded.
- big-three:1296 GPT-5.4 dated both March 5 and April 16: historical callouts, no decision depends on it.
- big-three:1138 chat.openai.com: still redirects.
- big-three:536 Claude voice "Limited" (pricing page shows Voice mode on all plans): no decision turns on it; fix in passing.
- whats-next:712, :725 API prices (GPT-4o, Sonnet $3-15) and :760 sample model: developer pricing; `claude-sonnet-4-6` is still Active until at least Feb 2027, so the sample runs. Fix in passing.
- whats-next:864 Codex "requires Plus or Pro" (now on Free and Go subject to rollout): developer tool.
- whats-next:817 Cursor $20, vibe-coding:510-513, :602, :663 Replit and Lovable credits: developer-tool pricing.
- vibe-coding:389-390 "41% of all code" stat, in a labeled Feb 2026 callout: unsourced but no practice implication.
- vibe-coding:1593 odd "@lovaboreau" handle: social link, not clinical.
- everyday-ai:442 "200,000 words" Projects limit: not verified, no decision depends on it.
- Grok 5: not shipped, and not on the page.
- local-models Phi-3 on the low-hardware row: old but still installable; the Qwen and Muse additions cover the practical gap.
- Claude Team/Enterprise seat prices: developer and admin chatter; page already defers.
