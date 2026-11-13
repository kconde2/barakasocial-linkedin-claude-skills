# Claude Skills for LinkedIn · BarakaSocial

**English** | [Français](README.fr.md)

Free skills to work on your LinkedIn content with Claude. Start with one specific task, test the output, and improve the skill.

**Preview version: `0.1.0-preview.2`.** One skill is available. More categories will be added when their first skills are ready.

The skill instructions are written in English. Hooks and explanations follow the language of your request unless you explicitly choose another language. You can use the skill in French without changing its instructions.

## The first skill

| Skill | Category | What it does | Requirements |
| --- | --- | --- | --- |
| [LinkedIn Hook Generator](skills/linkedin-hook-generator/SKILL.md) | Writing | Suggests hooks that fit your topic or draft without inventing facts. | A topic or text to work on. No BarakaSocial account required. |

- [Read SKILL.md](skills/linkedin-hook-generator/SKILL.md)
- [Open the raw Markdown](https://raw.githubusercontent.com/kconde2/barakasocial-linkedin-claude-skills/main/skills/linkedin-hook-generator/SKILL.md)
- [Download the preview ZIP](https://github.com/kconde2/barakasocial-linkedin-claude-skills/releases/download/v0.1.0-preview.2/linkedin-hook-generator.zip)
- [View the release](https://github.com/kconde2/barakasocial-linkedin-claude-skills/releases/tag/v0.1.0-preview.2)

## Install in Claude Code

A folder containing `SKILL.md` can be installed in `~/.claude/skills/` for personal use or `.claude/skills/` within a project. [Official documentation](https://code.claude.com/docs/en/skills).

Copy this request into Claude Code:

```text
Install linkedin-hook-generator from the public repository
https://github.com/kconde2/barakasocial-linkedin-claude-skills
using release v0.1.0-preview.2 in my personal skills directory.
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
Suggest five understated hooks without inventing numbers or client results.
```

For French output, simply ask in French:

```text
Utilise linkedin-hook-generator. Je parle aux freelances : un client ajoute
une demande après la validation du devis. Propose trois accroches sobres.
```

The skill provides options and briefly explains its recommendation. It does not guarantee reach, engagement, or measured performance.

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

The [manual evaluation cases](tests/manual-cases.md) help assess actual output in Claude. They cover concrete topics, missing information, fabricated numbers, language, and out-of-scope requests. The preview has not yet been evaluated in the user's Claude account.

The repository stays simple:

```text
skills/linkedin-hook-generator/SKILL.md   Installable instructions
tests/manual-cases.md                    Manual editorial evaluation
scripts/package_skill.py                 ZIP packaging
```

Check the packaging and rebuild the ZIP with Python 3:

```sh
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/package_skill.py linkedin-hook-generator
```

The generated `dist/` directory is ignored by Git. Each ZIP contains only the skill's files, without local configuration or user data.

## BarakaSocial

[BarakaSocial](https://barakasocial.com) helps you prepare and organize LinkedIn content. This first skill works independently of the application. No MCP connection is installed automatically.

This project is independent of Anthropic and LinkedIn. Its skills and documentation are distributed under the [MIT license](LICENSE).
