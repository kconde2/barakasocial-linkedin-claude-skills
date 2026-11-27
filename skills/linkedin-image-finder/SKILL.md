---
name: linkedin-image-finder
description: Find visual directions for a LinkedIn post and route to an available specialist. Use to choose an image that supports the message; linkedin-meme-finder is the first supported specialist.
metadata:
  version: "0.1.0-preview.16"
  author: BarakaSocial
---

# Find a visual for a post

Use the active post and request without imposing a questionnaire. If the text is missing, ask for it or read it through an available connector when the user authorized that reading. For the latest published post, filter published posts and sort by publication date descending, not last edit date.

Briefly identify the message, reader and intended visual effect: contrast, recognition, humor, emotion or explanation. Distinguish inferred audience information from supplied facts. Preserve the author's text and creative freedom. Respond in the user's language unless they request another language.

## Choose the type and count

If the type is missing, ask what visual the user wants with the single currently available option, Meme. Do not invent other options to fill an interface. Use a native question tool when available and suitable for a single option, otherwise ask in chat. Wait for the answer before searching.

Then ask how many proposals they want, with five as the default. Accept a custom positive integer, including ten. Use a native question tool if available, otherwise chat. Do not ask again for a type or count already supplied. Pass the count to the specialist so it does not repeat the question.

## Route

For memes, load the installed linkedin-meme-finder skill and follow its instructions, passing the post, useful contrast, tone, count and constraints. The sibling path ../linkedin-meme-finder/SKILL.md works when both folders are installed together. Otherwise use the host's skill catalogue. If the specialist is missing, say so rather than claiming to have run it.

For a general visual request, suggest memes when they serve the post. This is the only specialist supplied in this version. If a documentary photo or another approach is needed, explain the limitation rather than forcing a meme. Do not pretend a photo or generation specialist is installed.

Routing means loading instructions; it does not require a subagent or a skill invocation API.

## Present and prepare

Present the requested number of distinct candidates, five by default, with inspected previews, sources, reasons and proposed captions. Recommend the best fit. If fewer relevant candidates can be verified, show those and explain the limitation without inventing results.

Display previews directly in the conversation, not just links. Let the user select a candidate and its text or request alternatives. Selecting a candidate in this workflow authorizes preparing that meme with the proposed text unless the user only wants comparison or explicitly postpones editing. Follow the specialist's editing step. Do not prepare all candidates before selection.

Do not rewrite the post or attach or publish media on LinkedIn or BarakaSocial.

## Updates

Follow [the shared update workflow](references/updates.md) at invocation when client capabilities permit, without blocking the task.
