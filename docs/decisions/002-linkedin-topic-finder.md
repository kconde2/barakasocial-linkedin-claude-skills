# 002 - LinkedIn Topic Finder

Status: implemented locally as preview.10; human editorial comparison and target-client evaluation pending. Framing approved on 2026-11-15 with the request to begin implementation after reviewing the author's private note about finding subjects. No commit, push, release, application change, or live account action is included.

## Purpose

Add one public skill for concrete topics and angles, including optional direction-setting and campaign subjects. Reuse the existing writer and optional hook skill. Generalize the process rather than an author's niche, preferred emotional register, or funnel allocation.

## Questions and decisions

| Réf. | Question | Proposition | Décision |
| --- | --- | --- | --- |
| Q1 | ~~What is the new public skill?~~ | P1: `linkedin-topic-finder` handles subjects, angles and campaign proposals according to the request. | Approved in the implementation request. |
| Q2 | ~~How should reader responses affect the work?~~ | P1: distinguish author intent, reader benefit and response; optional multiple choices or free text guide material search and writing. | Approved: save, share, debate and other intentions. |
| Q3 | ~~Must every post have a lived scene or fit a pillar?~~ | P1: prefer concrete support without forcing experience, conflict or a commercial bridge; allow supported opinions, resources and explicit illustrations. | Retained for the general-purpose V1. The private author's heuristics are not universal evidence. |
| Q4 | ~~How should writing continue?~~ | P1: explicit writing request passes the same brief to the existing writer, with a standalone fallback if absent. Selection alone stays a selection. | Retained in the approved V1 scope. |
| Q5 | ~~Where should preferences live?~~ | P1: extend the selected private profile with optional fields; current campaign and one-post choices stay temporary unless explicitly saved. | Retained in the approved shared-personalization scope. |
| Q6 | ~~Should this include a visual skill?~~ | P1: defer visual work. | Explicitly deferred by the user. |
| Q7 | ~~Must every topic identify a problem and answer a question?~~ | P1: require a precise editorial question and supported contribution; a problem is optional. Preserve uncertainty and allow unresolved alternatives. Do not force the question into the published text. | Approved by Kaba in the follow-up discussion. |
| Q8 | ~~How do proposed and user-supplied topics become the author's post?~~ | P1: reuse existing material; ask focused follow-ups only for a missing contribution. Topic selection is not endorsement of a conclusion. Keep the selection table short and do not require a stance, emotion, story, or sales goal. | Approved by Kaba in the ghostwriter workflow discussion. |

## What the research changes

The author's note suggests seeking material in past experiences, observations, attributed phrases, outside resources and questions rather than polishing an empty opening. Reuse those source options and honest attribution. Do not import claims that personal stories guarantee reach, that abstraction is always weak, or that a generic second-person scene is automatically factual. An idea can be a useful starting point; missing support becomes research or a question.

Examples from other creators and training materials informed the distinction between intention, subject, form and response. They do not establish causal performance. No proprietary template text, personal archive, private research corpus or local CLI dependency is distributed in this package.

## Contract

Entry points: no idea, theme, material, existing topic, or campaign goal. Reuse what is known and ask only consequential missing questions. Direction-setting is optional. No fixed funnel, posting cadence, pillar count, or guaranteed reaction.

Output: a short selection table with stable IDs, topic/angle, reader relevance, and available material or gaps. Add goal/response when useful for choosing. Keep the editorial question, supported contribution and provenance in the reasoning and selected brief. Recommend a supported choice. A requested campaign connects complementary subjects; it does not schedule them.

Handoff: author intent, reader, response/benefit, topic/angle/stake/question/contribution/promise, material with provenance and gaps, voice, optional opening/CTA and campaign role. These remain ordinary conversation context, not a required data-entry form. The writer does not require the finder or repeat its questions.

Persistence: version 1 profiles keep existing fields and accept optional `editorial` fields and `cta.placement`. Unknown nested fields are preserved. No automatic author merge, campaign save, or personal data in public files. Instruction copies stay identical so each ZIP is self-contained. All package versions advance to preview.10 because their shared reference changes; the hook, analyzer and optimizer core workflows remain unchanged.

## Validation and limits

- [x] Read the private source note and distinguish reusable decisions from author-specific or unsupported claims.
- [x] Add the fifth skill to distribution tests and observe missing-package failures before implementation.
- [x] Implement Topic Finder, writer handoff and the optional shared fields.
- [x] Add bilingual installation and usage pages, catalogue entries and guides.
- [x] Run isolated behavioral checks for campaign proposals, response changes and actual preference persistence.
- [x] Check question/contribution handoff on an untested contact form without inventing a malfunction or requiring visible questions.
- [ ] Compare writer-only and finder-plus-writer outputs with human readers using identical inputs and shuffled presentation order.
- [ ] Exercise native multi-select controls, real connected MCP reads and installation in the target clients.

See [behavioral results](../../tests/topic-finder-smoke-results.md) and [remaining scenarios](../../tests/topic-finder-manual-cases.md). Archive tests establish packaging integrity, not writing quality. Agent trials establish observed behavior in those runs, not reliable audience outcomes or universal model compliance.

## Follow-up framing: reader world, material and intent

The user requested explicit definitions and composable formulas before further changes. The [French working map](002-editorial-map.fr.md) separates reader context, subject, angle, material, author intent, reader response and optional CTA. Kaba approved this follow-up framing and implementation, including reuse of available memory, labeled inferences and an explicit offer to save useful shared context.

| Réf. | Question | Proposition | Décision |
| --- | --- | --- | --- |
| Q9 | ~~Should the process be mapped with definitions and formulas?~~ | P1: write a Markdown working map covering subjects, sources of material, intentions and possible actions. | Explicitly requested. Document created. |
| Q10 | ~~How should structured reader knowledge be shared?~~ | P1: extend the selected private profile minimally, keeping observations, hypotheses and provenance distinct; topic candidates remain in conversation. | Approved by Kaba. Implemented as optional version 1 arrays `reader_world` and `author_perspectives` under `editorial`, with provenance and reported/inferred basis. |

- [x] Create the working map with a synthetic example and responsibility/storage mapping.
- [x] Validate the follow-up framing with Kaba.
- [x] Implement the approved schema, context reuse, inference boundaries and save offer.
- [x] Record independent end-to-end and persistence trials in [reader-world results](../../tests/reader-world-smoke-results.md), including actual files and limits.
