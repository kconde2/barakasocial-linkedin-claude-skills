# Claude Skills for LinkedIn · BarakaSocial

**English** | [Français](README.fr.md)

Free skills to work on your LinkedIn content with Claude. Start with one specific task, test the output, and improve the skill.

**Source preview: `0.1.0-preview.7` for all 3 skills. No packaged GitHub release for this version yet.** The published hook release remains `0.1.0-preview.5`; it does not include the new shared personalization. Build the candidate ZIPs below to test them locally.

Give it a complete post or rough notes. It works with the material you have and asks a focused question only when necessary.

The skill instructions are written in English. Hooks and explanations follow the language of your request unless you explicitly choose another language. You can use the skill in French without changing its instructions.

## Skills

| Skill | Category | What it does | Requirements |
| --- | --- | --- | --- |
| [LinkedIn Hook Generator](skills/linkedin-hook-generator/SKILL.md) | Writing | Suggests hooks that fit your topic or draft without inventing facts. | A topic or text to work on. No BarakaSocial account required. |
| [LinkedIn Post Writer](skills/linkedin-post-writer/SKILL.md) | Writing | Writes one complete post or coherent variants from your material. | Notes or a draft. No account or other skill required. |
| [LinkedIn Post Analyzer](skills/linkedin-post-analyzer/SKILL.md) | Analysis | Reviews a post using current BarakaSocial criteria and its official score calculation. | A post and a connected BarakaSocial MCP account. |

- [Read SKILL.md](skills/linkedin-hook-generator/SKILL.md)
- [Open the raw Markdown](https://raw.githubusercontent.com/kconde2/barakasocial-linkedin-claude-skills/main/skills/linkedin-hook-generator/SKILL.md)
- [Download the previously published hook ZIP (preview.5)](https://github.com/kconde2/barakasocial-linkedin-claude-skills/releases/download/v0.1.0-preview.5/linkedin-hook-generator.zip)
- [View the published hook release (preview.5)](https://github.com/kconde2/barakasocial-linkedin-claude-skills/releases/tag/v0.1.0-preview.5)

## Install in Claude Code

A folder containing `SKILL.md` can be installed in `~/.claude/skills/` for personal use or `.claude/skills/` within a project. [Official documentation](https://code.claude.com/docs/en/skills).

To install the previously published hook version, copy this request into Claude Code:

```text
Install linkedin-hook-generator from the public repository
https://github.com/kconde2/barakasocial-linkedin-claude-skills
using release v0.1.0-preview.5 in my personal skills directory.
Read its SKILL.md before installing. If a skill with the same name already exists,
compare its origin and contents before replacing it.
Do not modify my other skills or my MCP configuration.
```

The source path is `skills/linkedin-hook-generator/SKILL.md`. After installation, explicitly ask to use `linkedin-hook-generator` or invoke `/linkedin-hook-generator` in Claude Code.

## Install in Claude

Download the skill ZIP and upload it through **Customize > Skills** using the option to add a skill. Required capabilities and controls may vary by workspace. [Official instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

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

`linkedin-post-writer` is available as preview source in this repository. Build its ZIP with the command below to try it.

```text
Use linkedin-post-writer. Write one post for freelance designers.
A client approved my mockup, then requested 2 additional screens.
I proposed a separate estimate before starting. Keep a direct tone.
Do not invent the client's response or the outcome.
```

It asks whether you want one post or variants only when that choice is missing. It keeps an opening you already selected. Otherwise, it uses `linkedin-hook-generator` when available, selects an opening, and continues writing. It discloses actual use outside the post. Without that skill, it writes the opening itself.

When the material would produce a generic text, it explains what is missing and offers relevant options: add real details, use a shorter form, or set the topic aside. The author chooses the tone. A version that remains limited is presented as a draft to enrich. It never saves, analyzes through a paid service, schedules, or publishes.

## Analyze a post

`linkedin-post-analyzer` requires the BarakaSocial MCP. Without the required tools or access, it explains what is missing and stops instead of inventing an official score. Its preview source is available in this repository; build its ZIP below to try it.

```text
Use linkedin-post-analyzer. Analyze this draft without saving anything.
Keep the text unchanged and identify the most useful improvement:
[paste the post]
```

The default route reads `get_analysis_criteria`, evaluates the chosen text, and calls `preview_post_analysis` without saving a diagnostic. When the user explicitly asks to save the diagnostic, it uses `submit_post_analysis` instead. For a post identified in BarakaSocial, it reads the current text with `get_post`; a pasted revision is not silently substituted for the stored version.

The model in the user's client produces the editorial evaluation. BarakaSocial calculates the official score from that evaluation; it is not a second independent AI review or a prediction of reach. An analysis request does not rewrite the text. Correction is a separate requested scope, and the skill distinguishes the version scored from a later revision.

Several reviewers may contribute only when explicitly requested and supported by the client. They inspect the same text with complementary scopes, and the main agent combines their actual findings into one evaluation. It does not invent reviewers, average imaginary scores, or run repeated scoring loops. The skill never creates, edits, schedules, or publishes a post. Saving a diagnostic does not save a post.

## Personalize the 3 skills

Personalization is shared behavior, not a fourth skill to install. Each candidate ZIP includes `references/personalization.md`, so the skill remains usable on its own.

Ask, for example:

```text
Personalize these LinkedIn skills for me. Reuse what you already know.
Ask only for missing preferences about my audience, tone, and things to avoid.
Use these choices only in this conversation for now.
```

The skill can offer optional setup on first use or respond to an explicit configuration request. It does not require onboarding before working on a sufficiently clear request. It uses `AskUserQuestion` in Claude Code or `request_user_input` / `request_user_input_async` when available and allowed in the current client. Otherwise, it asks in the chat. It never treats silence as an answer or asks again for information already supplied.

Your current instructions take precedence over a saved profile. A preference for one post does not automatically become a permanent setting. Shared preferences guide tone, audience, and presentation; they do not replace BarakaSocial's analysis criteria or grant permission to access an account.

To keep preferences across sessions, ask to save them to a private location you choose. With filesystem access, the suggested location is `~/.config/barakasocial/editorial-profile.json`, outside the repository and installed skill folders. The same file can serve all 3 skills. Skills do not write a profile unless requested, and updates to skill instructions should leave that file intact. Never commit personal profiles or include them in a distribution ZIP.

Without durable storage access, preferences stay in the conversation; the assistant may provide a profile to copy or download, but must not claim it has saved or will automatically remember it. Setup does not change MCP configuration or automatically read personal account data. To configure after installation, explicitly ask to install **and configure** the skill, or configure it on first use; no universal installation questionnaire is assumed.

## BarakaSocial MCP tools

Hooks and writing work without mandatory tools. They may use authorized MCP reads when the user requests account context. Analysis requires the connected BarakaSocial MCP. Availability depends on the tools exposed by the connector in the user's client.

The table lists relevant available tools. Hooks and writing use optional reads rather than a mandatory call sequence; the analyzer follows its criteria-and-score workflow described above.

| Need | Tools | Purpose |
| --- | --- | --- |
| Prepare writing | `get_writing_brief` | Retrieve the public method and optionally authorized personal context for the topic. |
| Respect the author's voice | `get_writing_context`, `get_config_profile` | Read authorized preferences and style examples. |
| Understand the author | `get_linkedin_profile` | Read the profile stored in BarakaSocial without calling LinkedIn. |
| Find supporting material | `find_reference_posts`, `list_posts`, `get_post` | Find the account's posts and read selected references. |
| Start from an idea | `list_ideas`, `get_idea`, `prepare_post_from_idea` | Read an idea and optionally its authorized writing context and references. No post is created. |
| Check the text | `lint_post` | Check mechanical rules without saving, calling an LLM, or consuming credits. |
| Analyze | `get_analysis_criteria`, `preview_post_analysis`, `submit_post_analysis`, `get_post_analysis` | Read criteria, calculate a score from the client's evaluation, save or retrieve a diagnostic. |

### Skill boundaries

| Skill | Intended use |
| --- | --- |
| `linkedin-hook-generator` | Openings from supplied text. Optional MCP reads to enrich context. |
| `linkedin-post-writer` | A post or variants from supplied material. Optional MCP reads and use of the hook skill when available. |
| `linkedin-post-analyzer` | Requires MCP. Preview by default; saves a diagnostic only when explicitly requested. |

For analysis, the client model produces the evaluation according to `get_analysis_criteria`. BarakaSocial then applies its official calculation through `preview_post_analysis` or `submit_post_analysis`. These tools do not invoke the server's internal analysis model. `submit_post_analysis` saves the diagnostic with `mcp-client` provenance. `get_post_analysis` reads an existing diagnostic without running an analysis. This workflow consumes no credits.

The tools `save_post`, `update_post`, `schedule_post`, `prepare_post_image`, `confirm_post_image`, and `cancel_post_image` also exist. They remain outside all 3 skills' scope. Their presence in the connector does not authorize automatic saving, scheduling, or changes. This catalogue does not make every tool a mandatory step or authorize an action outside the requested scope.

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

## Test and contribute

A [three-case isolated behavioral smoke check](tests/behavior-smoke-results.md) covered missing MCP, actual profile persistence, and a temporary preference override. It does not validate native client dialogs or connected MCP paths.

The [manual evaluation cases](tests/manual-cases.md) help assess actual output in Claude. They cover concrete topics, missing information, fabricated numbers, language, and out-of-scope requests. The preview has not yet been evaluated in the user's Claude account.

The [writer evaluation cases](tests/writer-manual-cases.md) cover format choices, optional hook coordination, missing material, and factual fidelity. These are manual scenarios, not automated proof of writing quality.

The [analyzer cases](tests/analyzer-manual-cases.md) cover MCP availability, preview versus saved diagnostics, version fidelity, and real reviewer provenance. The [personalization cases](tests/personalization-manual-cases.md) cover interactive questions, scoped preferences, and honest persistence. These cases require behavioral execution; their presence is not a passing evaluation.

The repository stays simple:

```text
skills/linkedin-hook-generator/SKILL.md   Installable instructions
tests/manual-cases.md                    Manual editorial evaluation
skills/linkedin-post-writer/SKILL.md      Installable writing instructions
tests/writer-manual-cases.md              Writer evaluation
skills/linkedin-post-analyzer/SKILL.md    Analysis instructions
skills/*/references/personalization.md   Shared personalization guidance in each ZIP
tests/analyzer-manual-cases.md           Analyzer evaluation
tests/personalization-manual-cases.md    Personalization evaluation
scripts/package_skill.py                 ZIP packaging
```

Check the packaging and rebuild the ZIP with Python 3:

```sh
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/package_skill.py linkedin-hook-generator
python3 scripts/package_skill.py linkedin-post-writer
python3 scripts/package_skill.py linkedin-post-analyzer
```

The generated `dist/` directory is ignored by Git. Each ZIP contains only the skill's files, without local configuration or user data.

## BarakaSocial

[BarakaSocial](https://barakasocial.com) helps you prepare and organize LinkedIn content. Hooks and writing work independently of the application. Analysis requires the BarakaSocial MCP. No MCP connection is installed automatically.

This project is independent of Anthropic and LinkedIn. Its skills and documentation are distributed under the [MIT license](LICENSE).
