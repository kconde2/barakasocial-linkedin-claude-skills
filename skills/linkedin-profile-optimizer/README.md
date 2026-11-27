# LinkedIn Profile Optimizer

[← All skills](../../README.md) · [Français](README.fr.md)

Improve your headline, About or banner, separately or together. Approve each element, then apply the changes yourself on LinkedIn.

**Requires:** profile text or screenshots. No BarakaSocial account needed. An authorized MCP read can supply the stored profile.

[Install](#install) · [Use](#use) · [Copyable examples](#examples) · [Personalize](#personalize)

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

**In Claude with ZIP import:** download the [preview.14 ZIP](https://github.com/kconde2/barakasocial-linkedin-claude-skills/releases/download/v0.1.0-preview.14/linkedin-profile-optimizer.zip) and upload the complete archive through skill management. It contains `SKILL.md` with three shared references and the update helper. [Installation options](../../docs/guide.md).

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

**What you get:** Selected elements based on your facts and goal, approval per element and a final summary table. Headline and About appear in separate copyable text blocks. A banner is delivered as an image when an image tool is available, otherwise as a clearly labeled design brief.

With an authorized BarakaSocial read, the skill reports the stored profile's retrieval date when available. It does not assume this copy matches live LinkedIn. Unseen visuals and missing sections are not assessed. No numerical score, automatic saving or LinkedIn update.

## Questions that fit your goal

The skill reuses what you already said. If your goal is missing, it asks what the profile should help you achieve: clients or assignments, employment, professional reputation, candidates, partnerships/opportunities, or a clearer presentation without an immediate commercial goal.

For client work, it can distinguish embedded assignments (régie), scoped projects (forfait), advice and ongoing support. These are engagement models, not separate top-level goals. Mixed goals and free-text answers are welcome. You do not need to complete a fixed questionnaire.

<a id="examples"></a>
## Ready-to-copy requests

Paste these requests into your conversation after installation. Replace bracketed placeholders with your information. These are not terminal commands.

### Use the stored profile

```text
Use linkedin-profile-optimizer.
Read my profile stored in BarakaSocial and report its retrieval date. My goal: [goal]. Suggest improvements to my headline and About without saving anything.
```

### Improve only the headline

```text
Use linkedin-profile-optimizer.
Improve only my headline to find embedded freelance assignments as a [role]. Current headline: [headline]. My real skills and experience: [facts]. Do not rewrite other sections.
```

### Improve About without MCP

```text
Use linkedin-profile-optimizer.
Work only from the text below. Improve my About for [goal] with [audience]. Keep my headline: [headline]. Current About:
[About text]
Use these experiences as evidence without rewriting them: [facts].
```

### Review a supplied banner

```text
Use linkedin-profile-optimizer.
Review the attached banner and suggest improvements to its message and readability. My headline: [headline]. My goal: [goal]. If you cannot see the image, say so. Do not change the other elements.
```

Reading the stored profile requires MCP. The other examples use supplied material. The skill saves nothing even with MCP. Banner generation and editing depend on the image tools available in your client. Without one, it provides a brief without pretending to have generated an image.

### Edit an existing banner

```text
Use linkedin-profile-optimizer.
Edit only the attached banner. Keep [elements to preserve] and add [desired elements]. My goal: [goal]. Generate a candidate with an available image tool, then let me approve it. Do not change my headline or About.
```

### Prepare all 3 elements together

```text
Use linkedin-profile-optimizer.
Improve my headline, About and banner for [goal] with [audience]. Here is my profile and visual material: [material]. Reuse known information and ask for what is missing. Let me approve each element, then provide a summary table, copyable text and the banner if generated. I will apply the changes on LinkedIn myself.
```

### Revise without losing approved versions

```text
Use linkedin-profile-optimizer.
I approve the headline and About you just proposed. Keep them unchanged. For the banner, change only [requested adjustment], then show me the new version.
```

<a id="personalize"></a>
## Personalize

Provide your audience, tone and things to avoid. The skill asks only for missing preferences. This step is optional.

> Personalize this skill for small-agency leaders. Direct tone, light humor and no automatic final question. Keep these choices in this conversation.

[Keep shared preferences](../../docs/guide.md#personalize-the-skills)

[Read the skill instructions](SKILL.md) · [Back to the catalogue](../../README.md)
