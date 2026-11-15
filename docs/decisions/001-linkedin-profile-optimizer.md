# 001 - LinkedIn Profile Optimizer

Status: **Implemented locally; target-client evaluation pending**. Framing approved by Kaba with "ok go" on 2026-11-15. Q1-Q3 use P1. Goal-based routing (Q4-Q6) was approved with "oui c'est ça go" after expanding the objectives below.

## Purpose

Prepare a fourth public skill, `linkedin-profile-optimizer`, to help someone make their LinkedIn profile understandable and relevant to the people they want to reach. Deliver an evidence-based review and usable rewrites. Do not promise reach, ranking or conversions.

## Verified starting point

Taplio offers a skill with this name. It reviews the headline, About, banner, photo, Featured section and experience. Its output uses section ratings and three prioritized rewrites. It requires its MCP even though the skill explicitly says that connector cannot read or edit the LinkedIn profile: the user must supply the actual profile sections.

Source inspected on 2026-11-15: [Taplio's skill](https://github.com/TaplioOfficial/taplio-linkedin-claude-skills/blob/main/skills/linkedin-profile-optimizer/SKILL.md). This is a comparison of documented behavior, not a test of Taplio's application. Its prescriptive formulas and claims about search suppression are not adopted as established facts.

BarakaSocial already exposes the following capabilities, confirmed in the connector descriptions and application source (`appli2/app/services/mcp/tools/config_tools.ts` and `appli2/app/services/mcp/linkedin_profile_context_service.ts`):

| Need | Existing capability | Boundary |
| --- | --- | --- |
| Read the stored profile | `get_linkedin_profile` | Returns current local headline and summary, avatar, imported details and `lastRetrievedAt`. No live LinkedIn call. Fields inside imported details may be absent. |
| Read voice preferences | `get_config_profile` | Optional authorized context. Not a substitute for the actual profile or the user's current goal. |
| Save proposed text locally | `update_linkedin_profile` | Only headline and summary, with application limits of 220 and 2600 characters. Explicit request required. Does not update LinkedIn. |
| Apply changes on LinkedIn | User action in `/config/profile` | Outside agent execution. The agent never writes to LinkedIn. |

No additional MCP tool is needed for the proposed first version. Do not reuse post-analysis tools to calculate a profile score: their rubric is for posts.

The existing application decision `001-profil-linkedin-positionnement-et-offres.md` reserves synchronization to the application and removes separate positioning/offers settings. Questions about audience and goals here are conversation context, not a proposal to restore those settings.

## Questions and decisions

| Réf. | Question | Proposition | Décision |
| --- | --- | --- | --- |
| Q1 | ~~How should the skill obtain the profile?~~ | **P1:** Work from supplied text/screenshots without an account. Optionally read the stored profile through MCP when the request authorizes it. | P1 (validated: "ok go") |
| Q2 | ~~What should the first result contain?~~ | **P1:** A short positioning interpretation, an evidence table, up to 3 priorities and ready-to-copy rewrites. Qualitative findings rather than an arbitrary numeric score. | P1 (validated: "ok go") |
| Q3 | ~~Should this first version save changes?~~ | **P1:** Review and proposals only. **P2:** Also allow explicitly requested local headline/summary saving through the existing tool, with clear separation from LinkedIn synchronization. | P1 (validated: "ok go") |
| Q4 | ~~How should questions adapt to the professional goal?~~ | **P1:** Identify the primary goal only if missing: clients/assignments, employment, reputation, candidates, partnerships/opportunities or clarity without an immediate commercial goal. Separate engagement models (régie, forfait, advice/support) from objectives. For mixed goals, ask which is primary. Do not infer the goal from being in IT. | P1 (validated: "oui c'est ça go") |
| Q5 | ~~How much questioning is useful?~~ | **P1:** Reuse known information. Ask one decision at a time or up to 3 related short questions using the available native question tool, with a chat fallback. Stop once the next recommendation is supported. | P1 (validated: "oui c'est ça go") |
| Q6 | ~~Should this iteration add account-writing tools?~~ | **P1:** No. Existing profile reads are sufficient. Keep Q3's proposal-only scope; discuss local saving separately if a concrete need emerges. | P1 (validated: "oui c'est ça go") |
| Q7 | ~~Which elements should the next version work on?~~ | **P1:** Headline, About and banner, individually or together. Experience is supporting material, not a rewrite target. Clarify banner versus portrait only when the request is ambiguous. | P1 validated: manual application for every element; implemented in preview.9 locally. |
| Q8 | ~~How should image work operate?~~ | **P1:** For a requested banner, inspect supplied/accessible imagery, reuse the requested message and assets, then use an available image tool to create or edit it. If unavailable, provide a clearly labeled design brief, never claim an image was generated. | P1 validated: manual application for every element; implemented in preview.9 locally. |
| Q9 | ~~How should individual validation work?~~ | **P1:** Choose the elements first, establish a shared direction, then propose and validate each selected element. Preserve approved elements unless a later requested change creates a conflict to resolve. Finish with approved text and a banner file when generated. | P1 validated: manual application for every element; implemented in preview.9 locally. |
| Q10 | ~~Should validating text also save it?~~ | **P1:** No. Validation selects the deliverable; this version never saves profile edits, even with MCP. The user applies all selected elements manually on LinkedIn. Existing MCP writes only local headline/About, not experience or banner. No LinkedIn writes. | P1 validated: manual application for every element; implemented in preview.9 locally. |

## Proposed input and output

Input: current profile material, intended audience and desired visitor action (for example understand expertise, contact, follow or apply for a role). Ask only for missing information that affects the requested work. A headline-only request stays headline-only.

1. State what the supplied profile communicates and distinguish that interpretation from the user's stated goal. Resolve a consequential mismatch before rewriting around a new positioning.
2. Review only visible or actually returned sections. Missing is not the same as weak. Label the review partial when appropriate. An image URL alone is not evidence that the image was inspected.
3. Explain findings through clarity, specificity, supporting evidence, consistency and ease of taking the intended next step. Tie each finding to supplied material. These are editorial criteria, not measured conversion effects.
4. Recommend up to 3 changes with an original excerpt, a proposed replacement and a short reason. Retain effective wording. Never invent experience, clients, outcomes, qualifications or numbers. Ask for missing proof instead.
5. Match the requested language and voice. Apply supplied preferences without requiring a setup questionnaire. Avoid imposing a sales formula on every profession.

Suggested result table:

| Section | Observed material | Finding | Priority | Proposed change |
| --- | --- | --- | --- | --- |
| Headline | Exact excerpt | Specific issue or strength | High / medium / low | Rewrite or keep |
| About | Exact excerpt | Specific issue or strength | High / medium / low | Rewrite or keep |
| Banner | Inspected image or supplied brief | Finding or not assessed | As justified | Image candidate or labeled brief |

Follow the table with copyable text for the selected changes. Never imply that an audit updated the account. State the stored profile's retrieval date when available and distinguish local edits from the live LinkedIn profile.

## Implementation tasks after framing approval

- [x] Inspect Taplio's actual skill and distinguish its connector requirements from its capabilities.
- [x] Verify existing BarakaSocial profile tools without reading any user's personal data.
- [x] Confirm the framing and record Q1-Q3 decisions.
- [x] Write a concise English SKILL.md in the public repository.
- [x] Reuse the optional personalization behavior without duplicating a setup wizard.
- [x] Add English and French description, installation and usage pages plus catalogue links.
- [x] Verify packaging and supporting-file installation requirements. Do not promise single-file card installation for a folder-based package.
- [ ] Exercise supplied-profile/no-MCP, stored/stale profile, missing visuals, thin evidence, headline-only and changed-positioning cases.
- [ ] Verify that no post-analysis call, account write or LinkedIn write occurs in the proposal-only workflow. If Q3 P2 is chosen, test local saving with mocked tools and explicit scope.
- [x] Propose a commit after review. Kaba subsequently authorized committing and pushing this lot with "poush le skill". No packaged release is requested.

## Local validation

- SKILL.md frontmatter and naming validator passed.
- Four distribution tests passed across all 4 skills: exact installed files, reproducibility, identical personalization contract and path traversal rejection.
- Local documentation links and anchors checked successfully. All four ZIPs rebuilt locally as preview.8; no release published.
- Skill instructions reviewed against the existing read-only workflow and application boundaries. Fifteen behavioral cases are documented in `tests/profile-optimizer-manual-cases.md` but have not been executed in a target client. No claim of verified MCP behavior or writing quality is made.
- No personal account reads, account writes or LinkedIn calls performed.

## Next iteration: goal-based questions

Status: **Approved and implemented locally; behavioral evaluation pending**. Six goal families are included in SKILL.md. The proposal-only scope remains unchanged.

### Documented facts and editorial implications

Checked on 2026-11-15:

- [LinkedIn Recruiter search guide](https://business.linkedin.com/hire/resources/talent-acquisition/how-to-use-linkedin-recruiter) documents combining search filters and Boolean keywords. Its keyword search can use the whole profile.
- [LinkedIn's skills filter documentation](https://www.linkedin.com/help/recruiter/answer/a593647) describes both explicitly listed skills and evidence drawn from other profile sections. Its search can recognize alternative names for a skill. This does not establish keyword repetition as a ranking tactic.
- [LinkedIn AI Search FAQ](https://www.linkedin.com/help/recruiter/answer/a1676640) documents searches based on titles, location, experience and skills, with capabilities varying by product. These are search capabilities, not a guarantee that rewriting a headline produces more leads.

Editorial recommendation derived from those capabilities: for embedded IT work, use a recognizable role and truthful relevant skills, supported by experience. Review headline, experience and skills together. Do not reduce the review to stuffing terms into the headline or promise a ranking boost.

For scoped projects, prioritizing the buyer's problem, a concrete deliverable and supporting cases is our proposed editorial approach. It is not presented as a LinkedIn algorithm rule or a measured conversion finding. Both branches still need recognizable expertise and credible evidence.

### Approved decision tree

```text
Known goal? -> Reuse it; do not ask again.
Missing consequential goal? -> What should this profile help you achieve?
|
+-- Clients / assignments -> régie, forfait, advice or ongoing support
+-- Salaried employment -> target role, fit and possible career change
+-- Professional reputation -> audience, subjects and evidence
+-- Attract candidates -> actual needs, project and reasons to join
+-- Partners / opportunities -> counterpart and kind of collaboration
+-- Clarity without a commercial goal -> current activity and trajectory
+-- Free text / mixed goals -> preserve intent; clarify priority if needed

Only ask missing details that change the recommendation.
Then: available evidence -> up to 3 priorities -> copyable proposals.
```

Follower growth is not automatically a business objective. Clarify the desired purpose if missing and respect growth itself when that is explicitly the goal. Native question tools remain optional and their schema limits determine how choices are presented.

Questions are a means to choose a useful review, not compulsory onboarding. A user already asking for React freelance work in an embedded team does not need to choose the same goal again. A hypothetical keyword found in a target posting is not evidence the person has that skill. Optional target postings supplied by the user can inform vocabulary; unsupported qualifications remain questions, not profile claims.

### Next iteration tasks

- [x] Verify LinkedIn's documented recruiter search capabilities.
- [x] Propose routing and distinguish documented facts from editorial recommendations.
- [x] Validate Q4-Q6 and close this additional framing with Kaba.
- [x] Add concise routing instructions without changing the personalization contract or write boundaries.
- [ ] Exercise régie, forfait, salaried, mixed and already-specified goals with synthetic material.

The evaluation matrix now contains 28 manual scenarios, including all 6 goal families, overlapping engagement models, confidential searches and restricted question tools. These cases are prepared, not reported as executed. Preview.8 remains an unpublished working version.

## Section-by-section flow: approved and implemented locally

The user wants headline and About improvements plus optional banner generation/editing, individually or coherently together. Experience remains evidence. The published preview.8 reviews more sections and does not generate images. The approved flow is implemented as preview.9. Kaba authorized committing and pushing this lot with "ok go push"; no packaged release was requested.

Approved flow:

```text
Selected elements known? -> Use them.
Otherwise -> Headline / About / Banner / All three
Goal known? -> Reuse it, otherwise use goal routing.
Collect only missing material for the selected elements.
For a banner: current image if available, exact desired text,
required elements and visual preferences not already supplied.
Develop a shared direction when multiple elements are selected.
Propose -> user validates or requests changes -> keep approved version.
Deliver a summary table, separate copyable text blocks and actual image if generated.
User manually applies all changes on LinkedIn; no profile saving through MCP.
```

No mandatory restart or complete audit for a banner-only request. No portrait retouching inferred from a request for a banner. Image inspection and generation depend on actual client tools and access; do not imply all models have them. Before image production, verify current format guidance from LinkedIn rather than hardcoding unverified dimensions. Check legibility, cropping and the avatar overlap in the resulting banner when possible. A generated banner is a deliverable, not an uploaded LinkedIn asset.

No new MCP is necessary to create proposals or generate a local image using a client tool. Existing `update_linkedin_profile` accepts only headline and summary. Experience editing and banner upload are not exposed by that tool. Adding storage or synchronization capabilities would be a separate implementation decision, not a prerequisite for this flow.

Tasks:
- [x] Add bilingual copyable usage requests to each of the 4 skill pages, scoped to current capabilities.
- [x] Explicitly distinguish current banner review from future image generation in the examples.
- [x] Validate Q8-Q10 and close this flow framing.
- [x] Narrow optimizer deliverables to headline/About/banner and keep experience as reference.
- [x] Implement optional image-tool use and per-element validation after framing approval.
- [x] Add behavioral cases for selected elements, unavailable image tools, revisions and preserving approved text. Cases are prepared; target-client execution remains pending.

### Delivery decisions for preview.9

Headline and About are delivered in separate plain-text code blocks below a summary table. Copy controls are provided by the client when supported, not promised by the skill. The table contains only selected elements with their actual approval state and manual next action. A real image/file output is required before calling the banner generated; a brief is labeled separately. Generation uses the client image tool directly when requested and sufficiently specified, then the user can validate or revise it. The final reminder states that neither BarakaSocial nor LinkedIn was updated. Kaba authorized the commit and push for this lot with "ok go push".
