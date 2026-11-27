# Guide: install, use and personalize

[Home](../README.md) · [Français](guide.fr.md)

## Install in Claude Code

A folder containing `SKILL.md` can be installed in `~/.claude/skills/` for personal use or `.claude/skills/` within a project. [Official documentation](https://code.claude.com/docs/en/skills).

To install the current hook source, copy this request into Claude Code. Replace the skill name with `linkedin-topic-finder`, `linkedin-post-writer`, `linkedin-post-analyzer`, or `linkedin-profile-optimizer` to install another skill:

```text
Install linkedin-hook-generator from the public repository
https://github.com/kconde2/barakasocial-linkedin-claude-skills
using the main branch in my personal skills directory.
Copy the entire skill folder, including references/.
Read its SKILL.md before installing. If a skill with the same name already exists,
compare its origin and contents before replacing it.
Do not modify my other skills or my MCP configuration.
```

In Codex, you can request the same installation into your Codex skills. Storage locations and configuration tools depend on the client.

The source path is `skills/linkedin-hook-generator/SKILL.md`. After installation, explicitly ask to use `linkedin-hook-generator` or invoke `/linkedin-hook-generator` in Claude Code.

## Install in Claude

Each ZIP includes `SKILL.md` and the 2 shared personalization references. The Topic Finder is on preview.12. The other skills are on preview.10. Download the skill you want:

- [linkedin-topic-finder](https://github.com/kconde2/barakasocial-linkedin-claude-skills/releases/download/v0.1.0-preview.12/linkedin-topic-finder.zip)
- [linkedin-hook-generator](https://github.com/kconde2/barakasocial-linkedin-claude-skills/releases/download/v0.1.0-preview.10/linkedin-hook-generator.zip)
- [linkedin-post-writer](https://github.com/kconde2/barakasocial-linkedin-claude-skills/releases/download/v0.1.0-preview.10/linkedin-post-writer.zip)
- [linkedin-post-analyzer](https://github.com/kconde2/barakasocial-linkedin-claude-skills/releases/download/v0.1.0-preview.10/linkedin-post-analyzer.zip)
- [linkedin-profile-optimizer](https://github.com/kconde2/barakasocial-linkedin-claude-skills/releases/download/v0.1.0-preview.10/linkedin-profile-optimizer.zip)

To build a ZIP from source, see the [contribution guide](contributing.md).

Once you have the desired ZIP, upload it through **Customize > Skills** using the option to add a skill. Required capabilities and controls may vary by workspace. [Official instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

Pasting the instructions into a conversation lets you try them. It does not create a persistent installation in every client.

## Try it

```text
Use linkedin-hook-generator.
My audience is freelancers. My topic: a client adds requests after approving
an estimate. My point: define the scope before starting the work.
Suggest understated hooks without inventing numbers or client results.
```

For French output, simply ask in French:

```text
Utilise linkedin-hook-generator. Je parle aux freelances : un client ajoute
une demande après la validation du devis. Propose trois accroches sobres.
```

By default, the skill compares three hooks in a compact table: the opening, the reason to keep reading, and its editorial assessment. It then recommends one option. You can request another count or format. If your existing opening already works well, it can recommend keeping it rather than replacing it for the sake of change. It does not guarantee reach, engagement, or measured performance.

## How it works

| You provide | The skill does | You receive |
| --- | --- | --- |
| A complete post | Checks the opening and what the body actually delivers. | Three hooks in a comparison table and one recommendation, which may be to keep the original. |
| Notes or a topic | Uses the available material without inventing a story. | Supported openings and, if needed, one focused question or a missing detail to develop. |
| Feedback on one option | Revises the selected opening while preserving the facts. | A targeted revision, without rewriting the whole post. |

It selects angles already present in your material: identification, contrast, consequence, injustice, discovery, dilemma, or practical value. These are choices, not a checklist to force into every post.

It favors natural, active narration. In French, that means narrative present or passé composé when appropriate, while preserving chronology and intentional literary effects. Quantities use digits (2 calls, 6 months); articles and exact quotations are preserved.

No account or MCP is required. If you explicitly request BarakaSocial context, the skill uses only available, authorized read tools and discloses missing access. It does not rewrite the body, save a draft, schedule, or publish.

## Find topics or prepare a campaign

[LinkedIn Topic Finder](../skills/linkedin-topic-finder/README.md) starts with your intent, reader, and available material. It can help define a direction when necessary without a setup questionnaire for every request.

```text
Use linkedin-topic-finder. I write for small-agency leaders.
My material: [notes or resources]. I want something useful to save and send to a colleague.
Suggest 3 concrete topics with angles and supporting material. Do not write yet.
```

It separates the author's goal, reader benefit, and desired response. Topics can come from experience, attributed observations, questions, resources, or authorized research. Illustrations stay labeled as such. Missing substance becomes a research need instead of an invented fact.

For a campaign, ask for complementary subjects around your offer and audience. No fixed post count or funnel sequence is required. Choosing a topic does not start writing. Ask to write the selected topic: the writer reuses the brief without repeating discovery. Without the writer installed, the assistant can draft from the same brief when requested.

## Write a complete post

Download the [linkedin-post-writer preview.10 ZIP](https://github.com/kconde2/barakasocial-linkedin-claude-skills/releases/download/v0.1.0-preview.10/linkedin-post-writer.zip) to try it.

```text
Use linkedin-post-writer. Write one post for freelance designers.
A client approved my mockup, then requested 2 additional screens.
I proposed a separate estimate before starting. Keep a direct tone.
Do not invent the client's response or the outcome.
```

It asks whether you want one post or variants only when that choice is missing. It keeps an opening you already selected. Otherwise, it uses `linkedin-hook-generator` when available, selects an opening, and continues writing. It discloses actual use outside the post. Without that skill, it writes the opening itself.

When the material would produce a generic text, it explains what is missing and offers relevant options: add real details, use a shorter form, or set the topic aside. The author chooses the tone. A version that remains limited is presented as a draft to enrich. It never saves, analyzes through a paid service, schedules, or publishes.

## Analyze a post

`linkedin-post-analyzer` requires the BarakaSocial MCP. Without the required tools or access, it explains what is missing and stops instead of inventing an official score. Download the [linkedin-post-analyzer preview.10 ZIP](https://github.com/kconde2/barakasocial-linkedin-claude-skills/releases/download/v0.1.0-preview.10/linkedin-post-analyzer.zip) to try it.

```text
Use linkedin-post-analyzer. Analyze this draft without saving anything.
Keep the text unchanged and identify the most useful improvement:
[paste the post]
```

The default route reads `get_analysis_criteria`, evaluates the chosen text, and calls `preview_post_analysis` without saving a diagnostic. When the user explicitly asks to save the diagnostic, it uses `submit_post_analysis` instead. For a post identified in BarakaSocial, it reads the current text with `get_post`; a pasted revision is not silently substituted for the stored version.

The model in the user's client produces the editorial evaluation. BarakaSocial calculates the official score from that evaluation; it is not a second independent AI review or a prediction of reach. An analysis request does not rewrite the text. Correction is a separate requested scope, and the skill distinguishes the version scored from a later revision.

Several reviewers may contribute only when explicitly requested and supported by the client. They inspect the same text with complementary scopes, and the main agent combines their actual findings into one evaluation. It does not invent reviewers, average imaginary scores, or run repeated scoring loops. The skill never creates, edits, schedules, or publishes a post. Saving a diagnostic does not save a post.

## Improve a LinkedIn profile

[LinkedIn Profile Optimizer](../skills/linkedin-profile-optimizer/README.md) works from supplied text or screenshots without an account. When you request the stored BarakaSocial profile, it can use `get_linkedin_profile` and reports the retrieval date when available. That copy may include local changes and is not a live LinkedIn read.

```text
Use linkedin-profile-optimizer. Review my headline and About for startup founders looking for a freelance developer. Suggest changes without inventing results:
[paste the current sections]
```

Choose headline, About, banner or a combination. Experience provides evidence without being rewritten. Approve the proposed elements and receive a summary table and copyable text. An available image tool can generate or edit the requested banner; otherwise the output is a clearly labeled brief. Unseen elements are not assessed. Apply the changes yourself on LinkedIn. No official score or account save.

<a id="personalize-the-3-skills"></a>
## Personalize the skills

Personalization is shared behavior, not a separate skill to install. Each candidate ZIP includes `references/personalization.md` and `references/profile-schema.md`, so the skill remains usable on its own.

Ask, for example:

```text
Personalize these LinkedIn skills for me. Reuse what you already know.
Ask only for missing preferences about my audience, tone, and things to avoid.
Use these choices only in this conversation for now.
```

The skill can offer optional setup on first use or respond to an explicit configuration request. It does not require onboarding before working on a sufficiently clear request. It uses `AskUserQuestion` in Claude Code or `request_user_input` / `request_user_input_async` when available and allowed in the current client. Otherwise, it asks in the chat. It never treats silence as an answer or asks again for information already supplied.

Your current instructions take precedence over a saved profile. A preference for one post does not automatically become a permanent setting. Shared preferences guide tone, audience, and presentation; they do not replace BarakaSocial's analysis criteria or grant permission to access an account.

To keep preferences across sessions, ask to save them to a private location you choose. With filesystem access, the suggested location is `~/.config/barakasocial/editorial-profile.json`, outside the repository and installed skill folders. The same file can serve all 5 skills. Skills do not write a profile unless requested, and updates to skill instructions should leave that file intact. Never commit personal profiles or include them in a distribution ZIP.

Without durable storage access, preferences stay in the conversation; the assistant may provide a profile to copy or download, but must not claim it has saved or will automatically remember it. Setup does not change MCP configuration or automatically read personal account data. To configure after installation, explicitly ask to install **and configure** the skill, or configure it on first use; no universal installation questionnaire is assumed.

The profile can also retain an editorial direction, pillars, expertise, offers, and preferred reader responses. These fields are optional; old profiles remain usable without migration. Link preferences are not LinkedIn reach rules. Campaign goals and one-post choices remain temporary unless explicitly saved. Updates preserve unknown fields. Different authors use distinct profiles.

### Build and retain shared context

The Topic Finder helps define the reader's world: situations, aspirations, constraints, questions, decision criteria, and reported or hypothesized emotions. It reuses the selected profile and memory genuinely available in the client, labeling inferences instead of presenting an interpretation as your settled belief.

After establishing useful new context, it offers to save the named information. Accepting that offer authorizes the described write. Declining or not answering leaves the information in the conversation. Other skills can then read the same private file without repeating the interview.

```text
Use linkedin-topic-finder. Reuse my editorial profile and available context.
Help clarify my readers' world, then suggest 3 topics.
Separate observations from hypotheses and offer to retain the useful context.
Do not write a post yet.
```

The [shared schema](../skills/linkedin-topic-finder/references/profile-schema.md) retains version 1 and adds optional `editorial.reader_world` and `editorial.author_perspectives` fields. Each entry keeps an ID, content, origin, and reported/inferred basis, plus a recording date when available. Repeating an identical save creates no duplicates.

The profile holds useful summaries, not entire client exchanges. Proposed topics, drafts, and one-post objectives stay in the conversation. Without filesystem access, the skill can return JSON to retain without claiming it was saved.

## Update

Downloaded versions do not automatically update from this repository.

In Claude Code:

```text
Compare my linkedin-hook-generator skill with the latest published release at
https://github.com/kconde2/barakasocial-linkedin-claude-skills/releases
Explain the changes, then update it while preserving my local adaptations.
If my skill comes from another repository, flag that before replacing it.
Do not modify other skills or the MCP configuration.
```

In Claude, download the new version's ZIP and replace the installed version through the skill management interface.


### Topic Finder: preview.12

Preview.12 adds themes and audience → idea or post outcome → treatment → topics. Recurring ideas remain optional. Use the versioned ZIP linked above. Updates are manual and keep the private profile separate from the skill.
