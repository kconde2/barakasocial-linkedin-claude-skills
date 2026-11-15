# Behavioral smoke check: 2026-11-15

Candidate: 0.1.0-preview.7. Evaluator: a separate Codex subagent; exact model identifier not recorded. Three scenarios were run in one isolated evaluation context, not three fresh client sessions. Only synthetic material and a temporary profile were used. No live MCP, account, network call, or personal installation.

| Scenario | Request | Observed result |
| --- | --- | --- |
| Missing MCP | Analyze the designer draft in BarakaSocial without saving; no BarakaSocial tools available | Explained the missing connection and stopped without a diagnostic, fabricated score, or remote save. |
| Save preferences | Configure for small-agency leaders, restrained tone, no final question; explicitly save to a temporary JSON file containing an author, language, and unknown extension field | Actually read, updated and reread the file. Preserved author, language and extension.keep. Did not ask redundant questions. |
| Temporary override | Use that profile, write one ironic post with an exact selected hook and the designer facts; no client reply supplied | Kept the hook, used the requested temporary tone, invented no client response, and left profile bytes unchanged. |

The main agent inspected the temporary profile and checked equality with its pre-writing snapshot. The profile remained 219 bytes with SHA-256 `2b9111e824d49ae7c16486894501c888461515c14fe7bdca5fa59a4ae28cae18`.

No blocking defect was observed in these three cases. This is limited model-driven behavioral evidence, not a benchmark of writing quality or proof of client UI/MCP integration. Native question dialogs, connected preview/submit paths, failure recovery, and the remaining manual cases still require evaluation with mocked services in the target clients.
