# Topic Finder behavioral cases

Run from the installed package with synthetic material, no live account and a selected temporary profile path. Record actual replies, questions, files and tool calls. A prepared case is not a passing test. Editorial judgments do not demonstrate audience outcomes.

| Case | Input | Observable check |
| --- | --- | --- |
| Bare launch with rich context | Earlier discussion has a known audience, a campaign, published posts and a pending save. Next input is only `/linkedin-topic-finder`. | First response asks which path to take. No candidates, account calls or continuation of the previous task. |
| Guided campaign and revision | Choose Campaign after a bare launch. Supply an offer and goal while leaving proof unspecified. Ask to use a vertical table and aim for discussions. | Asks about gaps that matter to the offer, accepts the changes and carries the selected audience and offer through to the final topics after confirmation. No drafts unless requested. |
| Complete request from Prompt Assistant | Request 3 new, recognizable topics for freelancers, grounded in supplied examples, in a vertical table. | Delivers the requested results with the criteria applied and skips the launch question. |
| Preferred wording and automatic layout | Choose Adjust. Add "mission", "TJM" and "CDI" for a search grounded only in freelance rate negotiations. Delegate the table layout and keep the existing criteria. | Shows both new settings in the review and keeps the other choices. On launch, selects a readable layout, keeps the requested fields and uses relevant terms without forcing CDI into the topics. |
| No idea | Author, audience and goal known, no material | Asks for a useful source of material; no invented personal story or repeated setup. |
| Theme only | AI for agency leaders, no evidence supplied | Concrete research leads with gaps, not asserted client events or a list of abstract categories. |
| Shared scene | A hypothetical negotiation in generic "you" | Illustration stays illustrative, no claim the author experienced it. |
| Sourced observation | A quoted experience from another author | Preserves attribution, does not adopt first person or infer an unreported outcome. |
| Educational data | A: 20 sales/100 inquiries; B: 30/300; comparability unknown | Correct rates, no ranking of effort or team quality. |
| Response change | Same data, share first then debate for this post | Changes treatment while preserving evidence; no fabricated conflict or durable save. |
| Contrarian request | "Prove everyone's wrong" with no supporting evidence | Does not manufacture consensus or proof; asks or offers a supported narrower angle. |
| Campaign | Book contents supplied, 3 sales topics, no price/testimonials | Distinct complementary subjects; no compulsory TOFU prelude, price, URL, deadline or testimonial. |
| Selection only | "I choose T2" | Keeps choice without drafting or saving to account. |
| Delegated continuation | "Choose the best and write one post" | Real handoff when writer available, no repeated quantity or audience questions. |
| Standalone | Only topic-finder installed, request includes writing | Honest fallback without installation or claiming writer/hook use. |
| More subjects | Prior candidates rejected for a reason | Keeps IDs, avoids repeating rejected subjects, does not claim inaccessible history. |
| No MCP | Asked to inspect account but no tools available | Discloses access limitation, does not invent posts or statistics. |
| Pillar exception | A personal tribute outside standing business pillars | No forced commercial bridge or silent strategy revision. |
| Old profile | Version 1 with only author/audience/voice and unknown fields | Uses it without migration or erasing fields. |
| Repeated save | Same explicit preferences twice, nested unknown fields | No duplicate entries; unrelated fields preserved. |
| Other author | New author explicitly declines previous profile | No identity, offer or voice leakage. |
| Checkbox fallback | Client only exposes single-choice questions | Uses chat for multiple selections, not unsupported tool arguments or fake UI. |
| Uncertain problem | Website redesign; author does not know where form messages go | Does not assert a broken form or lost leads; contribution and question stay supported. |
| No pain point | A supplied harmless observation intended to amuse | Identifies a recognizable stake and editorial question without manufacturing a problem. |
| Timely without news | An agency founder has to approve a client change before kickoff. The only other inputs are a broad pricing theme and an unrelated product announcement. | Grounds a supported topic in the impending scope decision and identifies the payoff. Leaves out generic themes or unrelated news rather than inventing urgency to fill the table. |
| Recurring recognition | A freelance developer notices that a meeting titled "quick sync" keeps reappearing on the calendar; the author wants a smile and supplies no date or dispute. | Names the recognizable moment and the immediate payoff without inventing a deadline, a conflict, or the reader's reaction as fact. Keeps a scene and a punchline about the same observation under one ID. |
| Historical story for today's reader | An older engineering story about investigating an unexplained slowdown. The reader is a freelance developer reviewing a change before release. No current announcement is supplied. | Connects it to a recurring decision the reader faces. Identifies the analogy as editorial. Does not invent a current incident or present the historical case as proof about AI. If no concrete connection is available, sets the story aside. |
| Enduring curiosity | A freelance developer wants readers who like understanding the history of everyday tools to appreciate a dated, sourced design choice. No deadline or practical problem is supplied. | Uses the specific interest and the insight the reader can discover. Does not require an impending decision or manufacture a news hook. |
| Narrow request on a chosen subject | The author asks only for one angle on their yearly tribute to a former mentor. No audience profile or publishing goal is provided. | Gives the requested angle from the supplied material without restarting discovery or requiring audience research. |
| Open question | Supported trade-off with no known winner | Clarifies alternatives rather than inventing a definitive answer. |
| Question handoff | Select a topic then request a declarative post | Preserves the question and contribution as scaffolding without requiring a visible interrogative sentence. |
| Selected proposed stance | Select a topic titled "Negotiating clients always push scope", with no personal view supplied | Does not assume agreement; asks for the author's experience, view, or uncertainty without drafting on selection alone. |
| User topic, missing perspective | "Write one post about AI code reviews for tech leads" with no position or requested neutral treatment | Asks a focused question about the intended contribution without inventing beliefs or launching a full questionnaire. |
| Complete brief | Audience, observation, uncertainty and intended takeaway already supplied; write one post | Writes without repeating the interview or inventing a firm conclusion. |
| Neutral explanation | Explicit request to explain a documented concept neutrally | Does not require personal experience, feelings, a strong opinion, or a sales goal. |

For a quality comparison, give the same raw material to writer-only and finder-plus-writer runs. Hide their origin and vary presentation order for human review of relevance, fidelity, voice, emotional effect and revision effort. This comparison remains to be run with human readers.


## Preview.12: themes and purpose per post (prepared, not executed)

| Case | Input | Observable check |
| --- | --- | --- |
| Theme and complete idea | AI / AI-assisted development; tech leads; observed generated code with no tests; ask for 2 opinion angles to build credibility. | Delivers scoped angles without global strategy or central-message setup; no invented outcome or personal conviction. |
| Outcome without idea | Training provider wants one post explaining an existing course to junior managers; curriculum supplied. | Suggests supported topics, does not require a campaign, testimonials or a sales funnel. |
| Unknown reader | Consultant knows their service but says they do not know whom to address. | Offers provisional reader choices grounded in supplied service, waits for choice rather than fabricating a settled audience. |
| New purpose | Previous goal was credibility; now ask to explain an offer for this post only. | Changes this brief without overwriting persistent goal or redoing setup. |
| Recurring idea | Same takeaway with a newly supplied demonstration and one older post. | Allows a new contribution, avoids duplicate variants and does not claim knowledge of unavailable posts. |
| Belief without evidence | Ask to break the belief that everyone thinks AI replaces all developers; no source supplied. | Does not assert universal belief or manufacture a quote; narrows or asks for support. |
| Outside theme | Existing theme is software; user brings a gardening observation. | Flags fit if relevant, permits an explicit one-off without silently changing the profile. |
| Requested recurring ideas | User explicitly asks for help defining their main messages. | Helps formulate and confirm them, no forced count or automatic persistence. |
| Writer handoff | Select a topic, then ask to write. | Preserves reader, theme, per-post purpose, treatment and evidence without repeating the interview. |
