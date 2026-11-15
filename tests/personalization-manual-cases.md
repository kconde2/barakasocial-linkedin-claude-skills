# Shared personalization evaluation

Run with each of the three skills, noting client/model/version, available tools, request, actual output and any written files. These scenarios are not automated evaluations. Use synthetic preferences and temporary private paths only. Do not connect real accounts.

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
| Upgrade | Skill ZIP replaced while private profile remains outside installation | Profile remains available to all three skills and is not bundled into the ZIP. |
