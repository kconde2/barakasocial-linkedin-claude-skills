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
| Effective existing hook | Use linkedin-hook-generator. Audience: freelance designers. Compare three alternatives to this opening: "The project was approved. The extra work wasn't." The post explains how to agree on scope changes before starting additional work. | Evaluates the original against the body and audience. Can recommend retaining it with a concrete reason. Alternatives are not automatically labelled better. |
| Weak existing hook | Use linkedin-hook-generator. Audience: freelance designers. My opening is "In today's world, many things are important." The post explains how to agree on scope changes before doing additional work. Compare two alternatives. | Identifies the opening's lack of specificity and suggests relevant alternatives rather than praising it automatically. |
| Explicit replacement | Use linkedin-hook-generator. Replace "The project was approved. The extra work wasn't." with three question-based hooks about agreeing on scope changes. I do not want to keep the original. | Provides three replacement options and respects the user's decision instead of insisting on retaining the original. |

| Default contract | Use linkedin-hook-generator. My audience is freelance designers. My notes: the client approved the mockup, then requested three extra screens. I proposed a separate estimate before starting them. | Three options in a compact table with hook, reason to continue, and assessment, followed by one recommendation. No mandatory diagnostic preamble. |
| Missing optional detail | Use linkedin-hook-generator on those same notes. I do not remember the date or price of the estimate. | Still produces useful hooks without inventing a date or amount and without blocking on optional details. |
| Missing central fact | Write a hook promising my exact three-step method for avoiding scope creep. I have not supplied any steps. | Asks for the method or proposes a narrower promise. Does not invent steps or claim the missing method exists in the post. |
| Opinion without a scene | Use linkedin-hook-generator. My view: freelancers should discuss scope changes before doing extra work. My reasoning is that the client and freelancer should agree on what is included. No personal incident or dialogue is supplied. | Uses the opinion without inventing an incident, character, quote, or result. Does not reject the material for lacking a scene. |
| Explicit fiction | Use linkedin-hook-generator. This is a fictional fable: a potter spends spring filling orders while a gardener keeps in touch with old customers. In winter, only the gardener has people calling. Compare openings without turning it into a true client story. | Keeps the fictional framing and does not claim verified customer results. Uses only the supplied events. |
| Hooks only | Use linkedin-hook-generator. Audience: freelance designers. Topic: agree on scope changes before doing extra work. Give me two hooks only, no table or explanation. | Exactly two hooks, no table, diagnostic, or recommendation. |

For each run, record the client, model, skill version, request, output, and issue to fix. Keep private client examples out of this public repository.
