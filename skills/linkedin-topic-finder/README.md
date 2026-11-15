# LinkedIn Topic Finder

[← All skills](../../README.md) · [Français](README.fr.md)

Find concrete topics and angles for your readers from an intention, a theme, notes, or existing work. Prepare one post or complementary subjects for a campaign without inventing experiences.

**Requires:** your context or material, completed through a few useful questions if needed. No BarakaSocial account required.

[Install](#install) · [Use](#use) · [Copyable examples](#examples) · [Personalize](#personalize)

<a id="install"></a>
## Install this skill

In Claude Code or Codex, copy this request:

```text
Install linkedin-topic-finder in my personal skills for this client.
Repository: https://github.com/kconde2/barakasocial-linkedin-claude-skills
Folder: skills/linkedin-topic-finder
Use the repository version and copy SKILL.md with the entire references/ folder.
Read the instructions before installing. If this skill already exists,
compare its origin and contents before replacing it.
Preserve my personal preferences and MCP configuration.
```

**ZIP import:** preview.10 has no packaged release yet. Build an archive from these sources using the [contribution guide](../../docs/contributing.md). Import the whole package, including its reference file. [Installation options](../../docs/guide.md).

<a id="use"></a>
## Use the skill

```text
Use linkedin-topic-finder. I write for small-agency leaders.
A client approved a mockup, then requested 2 more screens. I offered a separate estimate; I do not know their response yet.
Suggest 3 topics that help readers recognize this situation or discuss the trade-off. Do not write the posts yet.
```

You receive a short table with stable IDs, topics/angles, why the reader would care, and available material or gaps. Goals and intended responses appear when they help you choose. The editorial question and supported contribution guide the selected brief without cluttering every row. A problem is optional. The skill recommends an option without claiming it will perform. Ask for a different count or format if useful.

Whether you bring a topic or choose a proposed ID, the assistant reuses what you already said. If needed, it asks what you think, noticed, experienced, or want to explore. Selecting a topic does not endorse a proposed conclusion. No repeated interview when the material is sufficient, and no forced opinion, personal story, or sales pitch.

Choose a topic, then ask to write it. If `linkedin-post-writer` is available, it receives the same decisions without another discovery questionnaire. Otherwise, the assistant can draft from the brief when requested. Selecting a topic alone does not start writing.

The skill can also help define your readers' world and offer to retain it in your shared private profile. It reuses known context and distinguishes observations from hypotheses. [See shared context and saving](../../docs/guide.md#build-and-retain-shared-context).

<a id="examples"></a>
## Ready-to-copy requests

Replace placeholders with your information. These are chat requests, not terminal commands.

### I have no idea

```text
Use linkedin-topic-finder. I work in [field] and want to reach [people] for [purpose].
Help me find material in my past work, observations, questions, or resources. Ask only what is missing before suggesting topics. Do not invent my experience.
```

### Turn a theme into specific topics

```text
Use linkedin-topic-finder. Theme: [theme]. Reader: [reader].
What I can support: [notes or resources]. I want something worth saving and sending to a colleague.
Propose 3 specific angles. Flag any missing evidence.
```

### Prepare a sales campaign

```text
Use linkedin-topic-finder. Prepare topics for 3 sales posts about [offer] for [audience].
Here is what it actually provides: [contents and limits]. Available evidence: [material].
Propose complementary angles without invented testimonials or urgency. No writing or scheduling yet.
```

### Change the response, then write

```text
Keep my material and audience. For this post only, prioritize a useful discussion instead of saving.
Choose the best supported topic and write one post using linkedin-post-writer if available. Do not save this preference.
```

### Find topics in my account

```text
Use linkedin-topic-finder. Read my BarakaSocial posts through available MCP tools to find 3 new angles for [audience and goal].
Read the selected posts before proposing reuse. Explain missing access or metrics. Do not save or publish anything.
```

Account access is optional and depends on the connected tools. External research, if used, is attributed; examples and hypotheses stay distinct from verified facts. No automated audience messages, paid analysis, idea saving, or publication.

<a id="personalize"></a>
## Personalize

Reuse the same private author profile as the other skills. Configure only what helps: audience, goal, voice, expertise, optional pillars, offers, or desired reader responses. A campaign is temporary unless you explicitly ask to retain its settings.

```text
Personalize these skills for [author and audience]. My direction is [direction].
I want readers to [response]. Keep these choices in this conversation for now.
```

[Shared preferences](../../docs/guide.md#personalize-the-skills) · [Skill instructions](SKILL.md)
