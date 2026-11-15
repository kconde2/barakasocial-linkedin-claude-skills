# Guide: install, use and personalize

[Home](../README.md) · [Français](guide.fr.md)

## Install in Claude Code

A folder containing `SKILL.md` can be installed in `~/.claude/skills/` for personal use or `.claude/skills/` within a project. [Official documentation](https://code.claude.com/docs/en/skills).

To install the current hook source, copy this request into Claude Code. Replace the skill name with `linkedin-post-writer`, `linkedin-post-analyzer`, or `linkedin-profile-optimizer` to install another skill:

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

Sources are at `0.1.0-preview.8` for hooks, writing and analysis and `0.1.0-preview.9` for Profile Optimizer. Neither version has a packaged release yet. The [preview.5 hook ZIP](https://github.com/kconde2/barakasocial-linkedin-claude-skills/releases/download/v0.1.0-preview.5/linkedin-hook-generator.zip) is an older version without shared personalization. To build a ZIP from current sources, see the [contribution guide](contributing.md).

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

## Write a complete post

`linkedin-post-writer` is available as preview source in this repository. Build its ZIP using the [contribution guide](contributing.md) to try it.

```text
Use linkedin-post-writer. Write one post for freelance designers.
A client approved my mockup, then requested 2 additional screens.
I proposed a separate estimate before starting. Keep a direct tone.
Do not invent the client's response or the outcome.
```

It asks whether you want one post or variants only when that choice is missing. It keeps an opening you already selected. Otherwise, it uses `linkedin-hook-generator` when available, selects an opening, and continues writing. It discloses actual use outside the post. Without that skill, it writes the opening itself.

When the material would produce a generic text, it explains what is missing and offers relevant options: add real details, use a shorter form, or set the topic aside. The author chooses the tone. A version that remains limited is presented as a draft to enrich. It never saves, analyzes through a paid service, schedules, or publishes.

## Analyze a post

`linkedin-post-analyzer` requires the BarakaSocial MCP. Without the required tools or access, it explains what is missing and stops instead of inventing an official score. Its preview source is available in this repository; build its ZIP using the [contribution guide](contributing.md) to try it.

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

Personalization is shared behavior, not a separate skill to install. Each candidate ZIP includes `references/personalization.md`, so the skill remains usable on its own.

Ask, for example:

```text
Personalize these LinkedIn skills for me. Reuse what you already know.
Ask only for missing preferences about my audience, tone, and things to avoid.
Use these choices only in this conversation for now.
```

The skill can offer optional setup on first use or respond to an explicit configuration request. It does not require onboarding before working on a sufficiently clear request. It uses `AskUserQuestion` in Claude Code or `request_user_input` / `request_user_input_async` when available and allowed in the current client. Otherwise, it asks in the chat. It never treats silence as an answer or asks again for information already supplied.

Your current instructions take precedence over a saved profile. A preference for one post does not automatically become a permanent setting. Shared preferences guide tone, audience, and presentation; they do not replace BarakaSocial's analysis criteria or grant permission to access an account.

To keep preferences across sessions, ask to save them to a private location you choose. With filesystem access, the suggested location is `~/.config/barakasocial/editorial-profile.json`, outside the repository and installed skill folders. The same file can serve all 4 skills. Skills do not write a profile unless requested, and updates to skill instructions should leave that file intact. Never commit personal profiles or include them in a distribution ZIP.

Without durable storage access, preferences stay in the conversation; the assistant may provide a profile to copy or download, but must not claim it has saved or will automatically remember it. Setup does not change MCP configuration or automatically read personal account data. To configure after installation, explicitly ask to install **and configure** the skill, or configure it on first use; no universal installation questionnaire is assumed.

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
