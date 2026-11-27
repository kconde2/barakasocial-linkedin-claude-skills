# LinkedIn Post Writer

[← All skills](../../README.md) · [Français](README.fr.md)

Turn your notes or draft into a complete LinkedIn post while keeping your facts and voice.

**Requires:** a topic, notes or a draft. No BarakaSocial account needed.

[Install](#install) · [Use](#use) · [Copyable examples](#examples) · [Personalize](#personalize)

<a id="install"></a>
## Install this skill

**In Claude Code or Codex**, copy this request into a conversation:

```text
Install linkedin-post-writer in my personal skills for this client.
Repository: https://github.com/kconde2/barakasocial-linkedin-claude-skills
Folder: skills/linkedin-post-writer
Use the repository version and copy SKILL.md with the entire references/ folder.
Read the instructions before installing. If this skill already exists,
compare its origin and contents before replacing it.
Preserve my personal preferences and MCP configuration.
```

**In Claude with ZIP import:** download the [preview.14 ZIP](https://github.com/kconde2/barakasocial-linkedin-claude-skills/releases/download/v0.1.0-preview.14/linkedin-post-writer.zip) and upload the complete archive through skill management. It contains `SKILL.md` with three shared references and the update helper. [Installation options](../../docs/guide.md).

[Installation options and updates](../../docs/guide.md)

<a id="use"></a>
## Use the skill

After installation, copy this example and replace the material with your own:

```text
Use linkedin-post-writer.
Write one post: a client approves my mockup, then requests 2 extra screens. I propose a separate estimate. Keep a direct tone and do not invent the outcome.
```

**What you get:** One post or coherent variants, according to your request. A chosen opening is preserved. Missing essential material is flagged rather than invented.

The skill responds in the requested language. It does not save or publish posts.

<a id="examples"></a>
## Ready-to-copy requests

Paste these requests into your conversation after installation. Replace bracketed placeholders with your information. These are not terminal commands.

### Write one post

```text
Use linkedin-post-writer.
Write one post for [audience] from these notes:
[notes]
Voice: [voice]. Do not invent facts. If the material is too thin, explain what is missing.
```

### Compare alternatives

```text
Use linkedin-post-writer.
Suggest 3 versions with distinct angles. Preserve my facts and voice. Use linkedin-hook-generator if available, then choose a fitting hook for each version:
[draft]
```

### Develop an approved hook

```text
Use linkedin-post-writer.
Keep this hook: [approved hook]. Write one post from this material:
[facts and notes]
If the material cannot deliver the hook's promise, flag it.
```

### Write a selected topic

```text
Use linkedin-post-writer. Write one post from the topic I selected with linkedin-topic-finder.
Keep the audience, intent, desired response, and evidence in the brief. Do not restart topic discovery.
```

The writer also works without Topic Finder. Discussion, saving, or sales goals guide the substance without forcing a final question or promotion.

<a id="personalize"></a>
## Personalize

Provide your audience, tone and things to avoid. The skill asks only for missing preferences. This step is optional.

> Personalize this skill for small-agency leaders. Direct tone, light humor and no automatic final question. Keep these choices in this conversation.

[Keep shared preferences](../../docs/guide.md#personalize-the-skills)

[Read the skill instructions](SKILL.md) · [Back to the catalogue](../../README.md)
