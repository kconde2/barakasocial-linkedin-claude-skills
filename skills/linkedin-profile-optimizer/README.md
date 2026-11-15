# LinkedIn Profile Optimizer

[← All skills](../../README.md) · [Français](README.fr.md)

Make your LinkedIn profile clearer for the people you want to reach. Get focused findings and copyable rewrites.

**Requires:** profile text or screenshots. No BarakaSocial account needed. An authorized MCP read can supply the stored profile.

[Install](#install) · [Use](#use) · [Personalize](#personalize)

<a id="install"></a>
## Install this skill

**In Claude Code or Codex**, copy this request into a conversation:

```text
Install linkedin-profile-optimizer in my personal skills for this client.
Repository: https://github.com/kconde2/barakasocial-linkedin-claude-skills
Folder: skills/linkedin-profile-optimizer
Use the repository version and copy SKILL.md with the entire references/ folder.
Read the instructions before installing. If this skill already exists,
compare its origin and contents before replacing it.
Preserve my personal preferences and MCP configuration.
```

**In Claude with ZIP import:** upload this skill's archive through skill management. Version `0.1.0-preview.8` ZIPs have not been released yet. Sources are available here; the [contribution guide](../../docs/contributing.md) explains how to build an archive.

A client card that only supports `SKILL.md` cannot install this complete package. Use the ZIP or a file-capable client; do not silently omit `references/`.

[Installation options and updates](../../docs/guide.md)

<a id="use"></a>
## Use the skill

After installation, copy this example and replace the material with your own:

```text
Use linkedin-profile-optimizer.
Review my headline and About for startup founders looking for a freelance developer. Keep my claims factual and flag missing evidence:
[paste the current sections]
```

**What you get:** A review table grounded in your material and up to 3 priorities with ready-to-copy rewrites. You can also ask for just one section.

With an authorized BarakaSocial read, the skill reports the stored profile's retrieval date when available. It does not assume this copy matches live LinkedIn. Unseen visuals and missing sections are not assessed. No numerical score, automatic saving or LinkedIn update.

## Questions that fit your goal

The skill reuses what you already said. If your goal is missing, it asks what the profile should help you achieve: clients or assignments, employment, professional reputation, candidates, partnerships/opportunities, or a clearer presentation without an immediate commercial goal.

For client work, it can distinguish embedded assignments (régie), scoped projects (forfait), advice and ongoing support. These are engagement models, not separate top-level goals. Mixed goals and free-text answers are welcome. You do not need to complete a fixed questionnaire.

<a id="personalize"></a>
## Personalize

Provide your audience, tone and things to avoid. The skill asks only for missing preferences. This step is optional.

> Personalize this skill for small-agency leaders. Direct tone, light humor and no automatic final question. Keep these choices in this conversation.

[Keep shared preferences](../../docs/guide.md#personalize-the-skills)

[Read the skill instructions](SKILL.md) · [Back to the catalogue](../../README.md)
