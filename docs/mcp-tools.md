# BarakaSocial MCP tools

[Home](../README.md) · [Français](mcp-tools.fr.md)

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
