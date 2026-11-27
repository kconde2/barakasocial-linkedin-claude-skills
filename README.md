# Claude Skills for LinkedIn · BarakaSocial

**English** | [Français](README.fr.md)

Find topics and openings, write or review a post, or improve your profile. Seven free skills that work from your material and respond in your language.

[Skills](#skills) · [Installation](#installation) · [Personalization](#personalization) · [Documentation](#documentation)

## Skills

Open a skill's page for its description, installation instructions and usage example.

| I want to… | Skill | Install | BarakaSocial account |
| --- | --- | --- | --- |
| Find topics or prepare a campaign | [Topic Finder](skills/linkedin-topic-finder/README.md) | [Install](skills/linkedin-topic-finder/README.md#install) | Not required |
| Find a better opening | [Hook Generator](skills/linkedin-hook-generator/README.md) | [Install](skills/linkedin-hook-generator/README.md#install) | Not required |
| Turn notes into a complete post | [Post Writer](skills/linkedin-post-writer/README.md) | [Install](skills/linkedin-post-writer/README.md#install) | Not required |
| Understand what to improve in a draft | [Post Analyzer](skills/linkedin-post-analyzer/README.md) | [Install](skills/linkedin-post-analyzer/README.md#install) | Required, with the MCP connector |
| Improve my LinkedIn profile | [Profile Optimizer](skills/linkedin-profile-optimizer/README.md) | [Install](skills/linkedin-profile-optimizer/README.md#install) | Optional |
| Find a visual for my post | [Image Finder](skills/linkedin-image-finder/README.md) | [Install](skills/linkedin-image-finder/README.md#install) | Not required |
| Find and prepare a meme | [Meme Finder](skills/linkedin-meme-finder/README.md) | [Install](skills/linkedin-meme-finder/README.md#install) | Not required |

The analyzer uses BarakaSocial's current criteria and score calculation. A score does not predict reach. None of these skills publishes posts.

## Installation

1. Open the page of the skill you want.
2. Copy its **Install this skill** request into Claude Code or Codex.
3. Try the usage example on that same page with your own material.

**Using Claude with ZIP import?** Download [Topic Finder preview.14](https://github.com/kconde2/barakasocial-linkedin-claude-skills/releases/download/v0.1.0-preview.14/linkedin-topic-finder.zip) or find the other skill ZIPs in the [installation guide](docs/guide.md).

## Personalization

Tell the assistant your audience, tone and preferences. It asks only for what is missing. Configuration is optional and shared across the 5 skills.

> Personalize these LinkedIn skills for small-agency leaders. Direct tone, light humor and no automatic final question. Use these preferences in this conversation.

[Keep preferences for later](docs/guide.md#personalize-the-skills)

## Documentation

- [User guide](docs/guide.md): installation, examples, personalization and updates.
- [MCP tools](docs/mcp-tools.md): available tools and analysis workflow.
- [Testing and contributing](docs/contributing.md): evaluation cases and ZIP packaging.

Built by [BarakaSocial](https://barakasocial.com). Free under the [MIT license](LICENSE). Independent of Anthropic and LinkedIn.


### Topic Finder: preview.12

Preview.12 adds themes and audience → idea or post outcome → treatment → topics. Recurring ideas remain optional. Use the versioned ZIP linked above. Updates are manual and keep the private profile separate from the skill.
