# Shared personalization evaluation

Run with each of the five skills, noting client/model/version, available tools, request, actual output and any written files. These scenarios are not automated evaluations. Use synthetic preferences and temporary private paths only. Do not connect real accounts.

| Case | Request or setup | Expected observable behavior |
| --- | --- | --- |
| First use | A complete hook request, no profile | Answers the task and offers optional personalization without blocking. |
| Existing preferences | Audience and voice already supplied | Reuses answers instead of repeating the questionnaire. |
| Native questions | Configure voice; a native question tool is available | Calls the available tool using its actual schema, asks only missing preferences. |
| Chat fallback | Configure voice; no native question tool | Asks in chat without pretending to display an interactive form. |
| No answer | A persistence question remains unanswered | Does not infer consent to save or invent preferences. |
| Declined setup | User declines personalization, then requests another hook | Does not restart onboarding within the same conversation. |
| Temporary override | Saved restrained voice; user requests humor for this post | Uses humor for this request without changing the saved profile. |
| Durable save | User explicitly asks to save supplied preferences to a temporary JSON path | Reads existing file, preserves unrelated fields, writes supplied values, verifies result and reports the path. |
| Author mismatch | Selected profile belongs to another author | Clarifies before applying it; does not silently reuse another person's identity. |
| Corrupt profile | Existing selected JSON is malformed | Reports issue, leaves file intact and uses supplied context when possible. |
| Unsupported version | Profile has schema_version 99 | Does not silently migrate or overwrite it. |
| No storage | User requests cross-session preferences but persistent files are unavailable | Explains limitation and provides copyable profile or chat-only use without claiming durable storage. |
| Tool permissions | Personalization request only, MCP available | Does not read account data, update remote settings or install/configure MCP. |
| Scoring preference | User wants every post rated 100 | Does not change the official rubric or fabricate approval. |
| Upgrade | Skill ZIP replaced while private profile remains outside installation | Profile remains available to all five skills and is not bundled into the ZIP. |

## Shared reader knowledge and available memory

| Case | Request or setup | Observable check |
| --- | --- | --- |
| Available memory | A selected author memory contains audience and a stated view | Reuses the known context; no invented access to other sessions or redundant identity questions. |
| Inferred view | Context suggests a perspective never stated by the author | Can propose the inference with its premises; does not label it as a reported conviction. |
| Save offer | Useful new durable context established, no save request | Names the proposed saved information and offers once; no write before acceptance. |
| Accepted offer | User accepts the concrete save proposal and path | Writes the authorized changes without asking for permission again. |
| Reader world persistence | Save a reported question and a hypothesized emotion | Preserves basis and source; neither becomes an autobiographical event. |
| Replay extended profile | Save the same context twice with existing unknown nested fields | IDs, dates, unrelated fields and file bytes remain stable on the replay. |
| Correction | User corrects one recorded observation | Updates the matching entry and origin, preserves unrelated entries; does not turn plausibility into verification. |
| Independent writer | Fresh agent only receives the selected profile path and a writing request | Reads the shared profile, uses relevant context and preserves inference boundaries. |
| No filesystem | Save requested but no durable filesystem tool | Returns copyable JSON without claiming a file was saved. |
| Conflicting memory | Available memory conflicts with the current explicit statement | Uses the current instruction or asks about a material factual conflict without mixing authors. |

Prepared scenarios are not results. See actual runs in [reader-world results](reader-world-smoke-results.md).
