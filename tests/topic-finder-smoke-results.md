# Topic Finder preview.10: isolated behavioral checks

Date: 2026-11-15. Runs used independent delegated Codex agents executing the actual skill instructions and explicitly selected synthetic inputs. No live account, network research, real personal profile, paid analysis, or LinkedIn action. This is a recorded smoke check, not an automated model benchmark or a human quality comparison. Model-specific performance cannot be inferred from these few runs.

## Response change and writer handoff

Input 1: a data analyst addresses sales managers and requests 2 subjects colleagues could share. Supplied fictional exercise: A has 20 sales/100 inquiries; B has 30/300. Sources, qualification and periods are unknown. No sales offer.

Observed output:
- S1 compares the meaning of volume and sales/inquiry ratio, without ranking teams.
- S2 proposes 3 checks before comparing results: sources, qualification and periods.
- The recommendation is S2 for its practical use by a recipient. Material is labeled fictional and ratios are 20% and 10%.

Input 2: keep the facts, prioritize debate without attacking teams, choose the best subject and write one post.

Observed: selects S1, reads/applies the writer and hook skills, discloses that use and writes one post without asking for audience or quantity again. The debate concerns whether to publish a provisional ranking or clarify comparability first. It preserves the unknowns and adds no client story or commercial CTA. No files written.

Execution issue: the agent initially looked for a nonexistent hook-finder path, then found the correct hook-generator through the file list. That was corrected during the run; it is not evidence of seamless execution. The resulting post remains explanatory. Its emotional impact has not been tested with readers.

## Campaign subjects and selection boundary

Input: a book for leaders of small web studios about additional requests after mockup approval. Supplied contents: request, effect on deadline, separate quote and written agreement. Ask for 3 sales subjects only; no price/link yet, testimonial, result or urgency. Calm voice.

Observed subjects:
- T1: what to clarify before responding to an additional request.
- T2: demonstrate the book's four-part grid on an explicitly fictional example, still to be constructed.
- T3: distinguish examining the conditions of a request from refusing it.

Recommends T2, proposes a sequence without dates, asks no unnecessary price/link questions and invents no proof. After "I choose T2", retains the subject and constraints without drafting or saving a post.

Limitation: T1 and T2 use the same grid. The distinction between presenting its use and demonstrating an application must remain visible at writing time; this run does not prove a complete campaign will avoid repetition.

## Actual preference persistence

Fixture: a selected temporary version 1 JSON profile for synthetic author Nora, with audience/voice, one pillar, unknown top-level/nested fields and a CTA object containing an unknown property.

Request: save a durable preference for helping sales managers decide, with save/share as desired responses; keep the existing pillar. Replay the same request. Then request debate for one post only. Finally switch to another author, explicitly declining Nora's profile, with a recruitment topic but no lived case.

Observed file changes and assertions:
- Saved `editorial.reader_promise` and two `reader_responses` values.
- Repetition produced identical parsed JSON and identical bytes; no duplicate values.
- Preserved the pillar, unknown nested fields and the whole existing CTA object.
- Temporary response override did not change the file bytes.
- New author's proposal did not reuse Nora's audience/offer or modify the profile; its proposed demonstration was labeled illustrative, without invented results.

The root agent read the actual transcript and validation JSON under the temporary test directory. No production profile was opened. This was an agent-driven instruction execution with Python assertions on the resulting files, not a deterministic implementation of preference merging inside the skill.

## No idea: recover material from past work

Fresh scenario on the campaign test agent: a freelance translator wants export managers to think of her while preparing product sheets. No topic or numerical result. The skill asks for an old or recent exchange and optionally an anonymized document; one example is enough.

The supplied memory: a client requested a literal slogan translation, the translator asked which market it was for, and the country was not yet chosen. The subsequent decision is unknown. The user asks for 2 helpful subjects without ridiculing the client.

Observed: T1 proposes clarifying the target market before requesting the translation; T2 proposes making an undecided market explicit in the brief. The reply preserves the unknown ending, treats the second angle as a possible recommendation rather than a proven method, and notes that the source concerns a slogan rather than claiming it appeared on a product sheet. No post, personal profile read, network call or file write. Both angles still concern the same missing information; broader diversity would require more material.

## Editorial question and uncertain problem

Follow-up isolated agent run after adding the editorial question/contribution contract. Input: a freelance developer is asked to redesign an aging website; the interlocutor does not know where form messages arrive. The developer has not tested the form and does not know the outcome. Request: 2 topics to share with an associate, choose the strongest and write one short post with no interrogative sentence or added event/result.

Observed: the agent read the finder, writer, hook and their shared references. S1 distinguishes missing information from a malfunction; S2 adds message routing to the redesign brief. It selects S1 and produces a declarative post. It explicitly avoids claiming a broken form or lost inquiries and preserves the absence of testing and outcome. No repeated setup questions, personal profile access, network call or file write.

The table expressed the editorial question as a declarative point to clarify, consistent with the user's no-interrogative constraint. This checks that the reasoning can survive without a literal question in the post. The resulting text is cautious and explanatory; this run does not establish emotional impact or audience interest. Humor and unresolved debate scenarios remain prepared rather than tested for this refinement.

Both changed skill entrypoints passed the validator. The 4 distribution tests passed again and the finder/writer ZIPs were rebuilt after the refinement.

## Not established

Native checkbox behavior, connected MCP behavior, target-client installation, universal model adherence, higher engagement, emotional effect, or sales. Human evaluation must compare the actual texts and revision effort, not merely the presence of requested sections. Prepared scenarios in [the manual matrix](topic-finder-manual-cases.md) remain pending unless a run is described here.

## Distribution checks before the reader-world extension

Four automated tests passed across all 5 skills: exact archive contents, reproducibility, identical shared reference, and path traversal rejection. All 5 entrypoints passed the skill validator. All 196 local documentation links and anchors resolved. All 5 ZIPs were built locally; no release or push was performed. Final instruction review clarified that the writer's prohibition concerns invented facts, not explicitly requested fiction. No target-client fiction test is claimed.

The later shared-schema extension and end-to-end trials are documented in [reader-world results](reader-world-smoke-results.md).

## Why read it now? Local preview.11

Date: 2026-11-18. Fresh Claude Code sessions read the local skill and received synthetic material. No account, MCP, web research, or preference save was requested.

- **Pending quote:** a small-agency leader must approve a quote after a request for 2 more screens with the same delivery date. The model tied its proposed angles to that decision and excluded a broad leadership note and an unrelated product announcement. It flagged the missing author criteria and still offered some follow-up questions alongside the selection.
- **Recurring recognition:** a freelance developer sees the same "quick sync" each Monday. Early runs split the observation into multiple formats. After the shortlist rule was tightened, the model proposed one ID and placed format alternatives under it. It did not assert the meeting's duration. Calling recurrence and short duration a contradiction is a weak editorial inference that still needs human judgment.
- **Historical illustration:** a fictional story from 2008 about a slowdown was supplied for a freelancer deciding whether to release a change. The model retained it for that specific decision and kept it fictional. It left out an unrelated old rescue story and a recent outdoor announcement. The recommendation did not require a new technology story or claim that the suspected slowdown had been measured.
- **Enduring curiosity:** a fictional example about removing a save icon once autosave existed produced one topic for readers interested in design history. The model treated curiosity as the reason to read and retained the fictional provenance.
- **Chosen tribute:** an initial run answered a request for one angle with the topic table and 3 questions. After clarifying the direct path, the final run gave the requested angle without a selection table or follow-up questions. It still inferred that the habit lasted a year from the annual tribute; the author would need to confirm that chronology before drafting.

The runs check whether the reason to read is visible and connected to the inputs. They do not establish whether a reader would stop scrolling.
