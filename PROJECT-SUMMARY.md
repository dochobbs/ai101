# AI 101 Course Website - Project Summary

## What This Is
A complete 17-page static website for a 12-week clinical AI governance and safety course. Designed for healthcare professionals learning to evaluate, supervise, and govern AI systems. Modeled after BlueDot Impact's cohort-based pedagogy.

## Project Origin
Built from a 22-page PDF curriculum document ("Clinical AI Governance and Safety: A Comprehensive Architectural Blueprint for Multimodal Medical Education") that outlined the full course structure, readings, activities, and pedagogical approach.

## Site Structure

```
/mnt/user-data/outputs/
├── index.html          # Landing page with hero, phase sections, week cards
├── unit-0.html         # "Start Here, Not with Theory" - NotebookLM practical intro
├── week-1.html         # The AI Triad (Data, Algorithms, Compute)
├── week-2.html         # Predictive AI (TREWS vs Epic Sepsis Model)
├── week-3.html         # Algorithmic Bias (Obermeyer Science paper)
├── week-4.html         # Computer Vision / CLAIM Checklist
├── week-5.html         # Large Language Models (Med-PaLM, GPT-4)
├── week-6.html         # Hallucinations and Supervision (DEFT-AI framework)
├── week-7.html         # Centaurs and Cyborgs (human-AI collaboration modes)
├── week-8.html         # Prompt Engineering for Clinicians
├── week-9.html         # Liability and Malpractice
├── week-10.html        # Institutional Governance / CONSORT-AI / Shadow AI
├── week-11.html        # Patient Communication and Informed Consent
├── week-12.html        # Capstone Presentations and Future Horizons
├── resources.html      # Frameworks, tools, glossary, complete reading list
├── about.html          # Course philosophy and pedagogy
└── styles.css          # Shared stylesheet (22KB)
```

## Three-Phase Structure
- **Phase I (Weeks 1-4): Foundations** - Teal color (#0d9488)
- **Phase II (Weeks 5-8): Generative AI** - Violet color (#7c3aed)  
- **Phase III (Weeks 9-12): Governance** - Orange color (#ea580c)

## Design System
- **Fonts**: Fraunces (display/headers), Source Sans 3 (body), JetBrains Mono (code)
- **Aesthetic**: Editorial/academic - clean, generous whitespace, professional
- **Components**: Callout boxes (question, tool, principle, warning, info), reading lists with badges, example cards, activity steps, learning objectives

## Key Frameworks Referenced
- **AI Triad**: Data, Algorithms, Compute
- **CLAIM Checklist**: 42-item evaluation for imaging AI papers
- **DEFT-AI**: Diagnosis, Evidence, Feedback, Teaching supervision framework
- **CONSORT-AI**: Reporting guidelines for AI clinical trials
- **Centaur/Cyborg**: Human-AI collaboration modes (clear division vs seamless integration)

## Content Status
All pages have substantive content including:
- Core questions for each week
- Key concepts sections
- Required/optional reading lists (with real citations)
- Discussion questions for synchronous sessions
- Learning objectives
- Activity descriptions

**Content is editable placeholder** - readings are real papers but links are placeholder (#). Activities described but not fully built out.

## What Might Need Editing
1. **Reading links**: Currently placeholder (#) - need actual URLs
2. **Activity details**: Described conceptually but could be expanded
3. **Download links**: Model Card template, CLAIM checklist PDFs, etc.
4. **Contact/enrollment info**: Placeholder on About page
5. **Facilitator guides**: Not included - could be added
6. **Simulation tools**: Alert Fatigue Simulator, Prompt Golf, etc. mentioned but not built

## Technical Notes
- Pure HTML/CSS, no JavaScript dependencies
- Google Fonts loaded via CDN
- Mobile-responsive with breakpoints at 900px and 600px
- All internal links are relative (works locally or hosted)
- ~200KB total site size

## Key Design Decisions Made
1. **Unit 0 before Week 1**: Practical "just try it" intro with NotebookLM before theory
2. **Two examples, not five**: Keeps intro focused and actionable
3. **Warning boxes prominent**: Sets supervision/verification tone early
4. **Phase color coding**: Visual wayfinding through 12-week journey
5. **Reading badges**: Clear required vs optional distinction
6. **Prompt boxes**: Dark background, monospace - scannable examples

## To Continue This Project
You can ask Claude to:
- Add actual URLs to reading lists
- Expand activity descriptions into full interactive exercises
- Create facilitator guides for each week
- Build out the simulation tools (would need React artifacts)
- Add assessment rubrics for capstone projects
- Create printable PDF versions of key pages
