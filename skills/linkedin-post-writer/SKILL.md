---
name: linkedin-post-writer
description: Write or rework a complete LinkedIn post from notes, an idea, or a draft, with one version or coherent alternatives. Develop a chosen hook into a readable story or argument while preserving the author's facts and voice. Use for full-post writing, not hook-only requests or publishing.
metadata:
  version: "0.1.0-preview.8"
  author: BarakaSocial
---

# LinkedIn Post Writer

Make the reader picture what happens and want to keep reading. Deliver the opening's promise without manufacturing a story.

## Personalization

Read [shared personalization](references/personalization.md) to reuse an author profile or handle setup and preference changes. Configuration is optional and does not require a separate skill or MCP.

## Input and format

Reuse the supplied material, audience, voice, constraints, and previous choices. For a new full-post request, ask whether the user wants one post or variants only if that choice is missing. Never ask again when it is already specified. If variants are requested without a count, state that you will provide three and proceed. A narrow edit stays a narrow edit, without restarting this workflow.

Identify the author's point and the supporting facts. Distinguish supplied events, opinion, inference, and explicitly fictional scenes. Do not impose a personal brand, audience, or belief from another author.

## Choose the opening

Keep an opening the user has already selected. If its promise requires a missing fact, flag the conflict instead of silently changing the choice or inventing the fact.

Otherwise, use `linkedin-hook-generator` if it is available: load and apply its instructions, select the opening that best fits the material, then continue writing without an intermediate approval step. Briefly disclose that actual use and the chosen opening's rationale outside the post. Do not expose unrequested hook candidates.

If the hook skill is absent or cannot be loaded, create the opening directly and continue without installing anything. Do not claim to have used a skill you did not apply. Choose a concrete scene, contrast, consequence, opinion, or useful question already supported by the material, rather than vague suspense. For variants, choose distinct approaches where the facts allow them and adapt each body and ending to its opening.

## Write

1. Preserve the author's point and chosen opening. Let the reader recognize a situation before explaining what it means. Use available people, actions, decisions, and concrete details; an opinion need not become a fabricated anecdote.
2. Make each paragraph advance the story or argument with an event, explanation, consequence, or decision. Connect ideas naturally, vary sentence lengths, and avoid a slogan on every line. Do not impose a fixed length or stretch a post to chase reading time.
3. Deliver what the opening invites the reader to discover. End with an earned observation, consequence, or change of perspective. Include a question or call to action only when requested or genuinely useful, using only supplied destinations and offers. No automatic promotion or BarakaSocial signature.
4. Read the whole post for fidelity, chronology, voice, transitions, repetition, and the opening's promise. Fix specific weaknesses without repeatedly generating more versions.

Write in the language of the request unless the user explicitly chooses another. Prefer natural, active narration; in French, favor narrative present or passé composé when appropriate. Preserve intentional literary effects and exact quotations. Use digits for quantities (2 calls, 6 months), preserving articles such as un client and explicit author preferences. In French, use straight apostrophes, no em dashes, and no comma before et or ou.

## When material is limited

If a central fact promised by the post is missing, ask one focused question or propose a narrower promise. Optional details such as a date or price need not block writing.

If development would remain generic despite a complete structure, explain the specific limitation before drafting. Offer relevant paths: add real material, choose a suitable shorter form, or set the topic aside. Let the author choose the register; do not impose satire. If a limited version is still requested, label it as a draft to enrich rather than a finished post. Do not reject useful opinions merely for lacking a lived scene.

## Output and boundaries

Return one complete post or the requested variants, each clearly separated and easy to copy. Put provenance or necessary reservations outside the post; omit a routine diagnostic or performance score.

Work without an account. Use available, authorized BarakaSocial read tools only when the user requests that context. Disclose missing access and continue with supplied material when possible. Reference posts guide style, not invented experiences or quotations.

Never invent numbers, testimonials, results, emotions, or personal events. Preserve explicit fiction as fiction. No promise of reach, virality, or reading time. This skill does not save drafts, run paid analyses, schedule, or publish; those are separate tasks.
