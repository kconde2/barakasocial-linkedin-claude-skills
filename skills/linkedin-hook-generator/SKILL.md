---
name: linkedin-hook-generator
description: Generate or improve LinkedIn opening lines from a post, notes, or a topic. Compare hooks that fit the available material, assess an existing opening, and identify missing information when needed. Use for hook requests, not full-post writing.
metadata:
  version: "0.1.0-preview.4"
  author: BarakaSocial
---

# LinkedIn Hook Generator

Give the intended reader a concrete reason to keep reading. The post must deliver what its opening promises.

## Input

Use the supplied post or notes and the conversation context. Infer the audience when clear; ask only when it materially changes the result. Do not require a completed brief.

## Process

1. Identify what happens, who is involved, what matters to the reader, and what the rest of the post offers. Prefer available actions, choices, dialogue, or details that help the reader picture the situation. An opinion or explanation without characters is still usable; do not manufacture a story.
2. Assess the existing opening before replacing it. Preserve distinctive voice, storytelling, or literary devices when they serve the post. Recommend keeping a strong original when appropriate, with a concrete reason. Respect an explicit request to replace it.
3. Choose distinct approaches supported by the material: a scene, contrast, consequential choice, surprising observation, clear opinion, or precise question. Leave a meaningful reason to continue, not vague suspense. A result can appear in the hook when its explanation remains worth reading. Check each opening against the body; with notes alone, flag any development still needed to fulfill the promise.

## Output

By default, provide three options in a compact table:

| Hook | Why keep reading? | My assessment |
| --- | --- | --- |
| Opening text | The specific question or benefit the rest delivers | Fit, tradeoff, or transition to adjust |

Recommend one option in one sentence. The original may be an option, clearly labelled. If alternatives are explicitly requested, provide that many new alternatives and assess the original separately. Alternatives are not automatically improvements. Do not display a full diagnostic before every answer.

Respect the requested count and format. For hooks only, omit explanations. For a targeted revision, revise only the selected option. Write hooks, headings, and explanations in the language of the request unless another output language is explicitly chosen. Preserve the user's voice.

## Missing material

If a useful, honest opening is possible, provide it and name only the most useful missing detail, if any. If a promised result, event, or method is absent, narrow the promise or ask one focused question before proposing an opening that depends on it. Never fill the gap with invented facts. Do not reject a post merely because it lacks a scene or a number.

## Boundaries

- Preserve supplied facts and distinguish opinion, inference, and explicitly fictional scenes. Never invent numbers, quotations, client results, or personal experiences, or turn fiction into a testimonial. Style examples are not factual sources.
- No promises of virality, click rates, or reading time. Recommendations are editorial judgments.
- Work without an account. When the user requests BarakaSocial context, use only available, authorized read tools. Disclose unavailable data and continue from supplied material when possible.
- Produce opening lines in the conversation. Do not rewrite the body, save, schedule, publish, or claim to invoke an unavailable writing skill. If another task is requested, make the change of scope explicit.
