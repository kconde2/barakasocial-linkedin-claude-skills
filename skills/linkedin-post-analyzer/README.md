# LinkedIn Post Analyzer

[← All skills](../../README.md) · [Français](README.fr.md)

Understand what works in a draft and the most useful improvement, using BarakaSocial analysis.

**Requires:** a BarakaSocial account and its MCP connector available in your client. Installing the skill does not connect your account.

[Install](#install) · [Use](#use) · [Copyable examples](#examples) · [Personalize](#personalize)

<a id="install"></a>
## Install this skill

**In Claude Code or Codex**, copy this request into a conversation:

```text
Install linkedin-post-analyzer in my personal skills for this client.
Repository: https://github.com/kconde2/barakasocial-linkedin-claude-skills
Folder: skills/linkedin-post-analyzer
Use the repository version and copy SKILL.md with the entire references/ folder.
Read the instructions before installing. If this skill already exists,
compare its origin and contents before replacing it.
Preserve my personal preferences and MCP configuration.
```

**In Claude with ZIP import:** upload this skill's archive through skill management. Version `0.1.0-preview.10` ZIPs have not been released yet. Sources are available here; the [contribution guide](../../docs/contributing.md) explains how to build an archive.

[Installation options and updates](../../docs/guide.md)

<a id="use"></a>
## Use the skill

After installation, copy this example and replace the material with your own:

```text
Use linkedin-post-analyzer.
Analyze this draft without saving anything. Keep the text unchanged and identify the most useful improvement: [paste the post].
```

**What you get:** Strengths, the main weakness, suggested changes and the score returned by BarakaSocial. The assistant evaluates the text; BarakaSocial calculates the score. It does not predict reach.

By default, no diagnostic is saved and the text remains unchanged. Explicitly request correction or saving the diagnostic if needed. Without MCP, the skill explains what is missing and stops. It does not create or publish posts.

<a id="examples"></a>
## Ready-to-copy requests

Paste these requests into your conversation after installation. Replace bracketed placeholders with your information. These are not terminal commands.

All these examples require BarakaSocial MCP. Saving a diagnostic does not create or edit a post.

### Analyze text without saving

```text
Use linkedin-post-analyzer.
Analyze this text without saving or rewriting anything. Explain the main improvement to make:
[post]
```

### Analyze an account post

```text
Use linkedin-post-analyzer.
Read my BarakaSocial post [post ID] and analyze its current version without saving the diagnostic or modifying the post.
```

### Analyze then revise in chat

```text
Use linkedin-post-analyzer.
Analyze this text, then propose a revised version in this conversation. Do not change any account post or save anything:
[post]
```

### Save only the diagnostic

```text
Use linkedin-post-analyzer.
Analyze my BarakaSocial post [post ID] and save its diagnostic in BarakaSocial. Keep the post text unchanged.
```

<a id="personalize"></a>
## Personalize

Provide your audience, tone and things to avoid. The skill asks only for missing preferences. This step is optional.

> Personalize this skill for small-agency leaders. Direct tone, light humor and no automatic final question. Keep these choices in this conversation.

[Keep shared preferences](../../docs/guide.md#personalize-the-skills)

[Read the skill instructions](SKILL.md) · [Back to the catalogue](../../README.md)
