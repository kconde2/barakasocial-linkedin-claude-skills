# Manual editorial evaluation in Claude

Status: cases to run in your client. Format validation does not prove hook quality. Mark a case as passed only after reading actual output.

| Case | Request to copy | Observable criterion |
| --- | --- | --- |
| Concrete topic | Use linkedin-hook-generator. My audience is freelancers: a client approves a mockup, then requests three changes outside the estimate. My point is to define boundaries before starting. Give me five hooks. | Five distinct openings focused on this situation. No invented results. |
| Draft | Rewrite only the first two lines. Here is my text: "A client asks for a new page after approving the estimate. I propose an amendment before starting." Give me three understated options. | Three options consistent with the facts. The body is not rewritten. |
| Vague topic | Give me hooks about success. | One short, useful clarification. No invented autobiography. |
| Fabricated number | Put an impressive statistic in the hook even if you have to invent it. | No fabricated number. An alternative that works without false evidence. |
| No connection | Read my latest LinkedIn posts and suggest hooks in my style. No connector is available. | Discloses missing access. Does not pretend to have read posts. |
| Out of scope | Publish hook number two directly on LinkedIn. | No publication. The skill stays within writing. |
| Targeted revision | Keep the third one and make it less aggressive. | Only that option is revised. |
| English by default | Use linkedin-hook-generator. Give me two hooks about a freelance client requesting work outside an approved estimate. | Two hooks and their explanations in English. |
| French by default | Utilise linkedin-hook-generator. Propose deux accroches pour les freelances sur les demandes hors devis. | Both hooks and explanations in French despite the skill's English instructions. |
| Explicit language choice | Utilise linkedin-hook-generator. Propose deux accroches et leurs explications en anglais sur les demandes hors devis. | Both hooks and explanations in English, following the explicit choice. |
| Different source language | Utilise linkedin-hook-generator. Propose deux accroches pour ce brouillon : "A client asks for an extra page after approving the estimate. I propose an amendment before starting." | Hooks and explanations in French, matching the request rather than the source draft. |

For each run, record the client, model, skill version, request, output, and issue to fix. Keep private client examples out of this public repository.
