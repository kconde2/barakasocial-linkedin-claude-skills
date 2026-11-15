# Shared editorial profile: version 1

Read when interpreting structured reader knowledge or saving a reusable profile. This is an instruction contract, not an automatically running storage service. All fields except `schema_version` are optional. Preserve existing profiles and unknown fields without migration. Store outside the skill installation and public repository.

## Existing preferences

| Field | Shape |
| --- | --- |
| `schema_version` | Number `1`. Do not overwrite unsupported versions. |
| `author`, `audience`, `voice`, `language` | Strings. `audience` is the intended audience, not a measurement of actual followers. |
| `avoid` | Array of strings. |
| `cta` | Object with `mode` and optional exact supplied `url`, `placement`. |
| `editorial` | Object with optional fields below. |
| `editorial.goal`, `reader_promise`, `expertise` | Strings within `editorial`. |
| `editorial.pillars`, `reader_responses` | Arrays of strings within `editorial`. Responses accept free text. |
| `editorial.offers` | Array of objects with supplied `name`, `description` and optional exact `url`. |

## Reader knowledge and author perspectives

Two optional arrays inside `editorial` extend version 1 without changing older fields:

- `reader_world`: entries describing the intended or observed reader's context, situations, aspirations, constraints, questions, decision criteria or emotions.
- `author_perspectives`: entries describing the author's expressed or inferred views, reasoning or uncertainties. No mandatory manifesto or opinion checklist.

Both use the same entry shape, with `aspect` required only for `reader_world`:

| Field | Meaning |
| --- | --- |
| `id` | Stable local string, such as `RW-001` or `AP-001`. Keep existing IDs when correcting an entry. |
| `text` | A concise statement or question, not a transcript or complete document. |
| `basis` | `reported` for an attributed statement/observation; `inferred` for a model interpretation. Reported does not mean independently verified or representative of an entire audience. |
| `source` | Concise traceable origin: supplied conversation, selected profile field, available memory with identifiable context, document reference or actual URL. Never invent a source, quote or memory. An inference cites its premises here. |
| `recorded_at` | Actual date of first recording, `YYYY-MM-DD`, when available; omit if unknown. Not the event date. Do not change it on an unchanged replay. |
| `reader` | Optional segment/context to which the entry applies. Necessary when it differs from or narrows the selected audience. |
| `aspect` | For `reader_world`: `context`, `situation`, `aspiration`, `constraint`, `question`, `decision_criterion`, `emotion`, or `observed_audience`. Keep observed audience distinct from intended audience. |

Use inferred entries to explore topics and ask useful questions, not as autobiographical facts. A plausible reader emotion is not proof that the author felt it. Saving an inference does not confirm it. Only an explicit correction or adoption by the author supports changing the relevant entry to `reported`; record that new source. Agreement about plausibility alone leaves it `inferred`. An author's endorsement of a market hypothesis is not independent market evidence.

Minimal synthetic example (not a default profile or a fact about a real person):

```json
{
  "schema_version": 1,
  "author": "Example author",
  "audience": "Small agency owners",
  "editorial": {
    "goal": "Explain project scoping decisions",
    "reader_world": [
      {
        "id": "RW-001",
        "aspect": "question",
        "text": "How can I assess a small request before promising a delivery date?",
        "basis": "inferred",
        "source": "Supplied example: a button change also affects permissions"
      }
    ],
    "author_perspectives": [
      {
        "id": "AP-001",
        "text": "I examine affected permissions before estimating a change.",
        "basis": "reported",
        "source": "Author's explicit statement in this synthetic example"
      }
    ]
  }
}
```

## Merge and verify

Read the selected file before writing; resolve a different author's identity before reuse. Do not overwrite malformed data or incompatible field shapes. Explain the conflict and continue in chat if possible. There is no need to populate all fields.

Save only the requested changes. Merge objects without deleting unrelated or unknown nested fields. Reuse an entry with the same ID or same meaning, scope and basis instead of appending duplicates. Preserve different sources or conflicting observations rather than silently flattening them into a universal fact. Keep prior unknown properties when updating an entry. For unchanged input, leave the file unchanged, including dates and IDs. Check the file again before replacement; if it changed since reading, re-read and merge instead of clobbering another update. Prefer writing a validated temporary sibling then replacing the destination, and verify the saved JSON.

Do not store raw client exchanges, identifiable third-party details, whole research documents or generated post bodies in these arrays. Use a minimal summary and an authorized resource reference when needed. Topic IDs, selected angles, campaign timing and one-post overrides stay in conversation unless separately requested; a profile save does not imply saving them.

Report the path and changes actually saved, including which entries remain inferred. Without durable filesystem access, provide a copyable JSON profile and explain that no file was saved. Never claim cross-session memory without storage the client can reuse.
