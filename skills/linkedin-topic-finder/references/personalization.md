# Personalization shared by the LinkedIn skills

## Reuse before asking

Reuse relevant information already supplied in the conversation, the selected profile, or memory genuinely available and authorized in the current client. Do not claim access to past conversations or external memory you cannot read. External account/document reads still require the applicable authorization. Current statements take precedence over older memory; resolve consequential identity or factual conflicts before reuse. Current instructions override saved defaults for this request only. Never apply one author's profile to another author silently. When conflicting sources would materially change the result, ask one focused question; do not merge identities.

In a local file-capable client, read the user-selected profile path if available. Otherwise you may check the single conventional path `~/.config/barakasocial/editorial-profile.json`, subject to the client's file permissions. Do not search unrelated personal files. If the profile names a different author, ask before using it. A missing file is normal. An unreadable or malformed profile should be reported without overwriting it; continue from the conversation when possible.

On first use without preferences, briefly offer optional personalization alongside the requested work. Do not force onboarding, repeat an offer declined in this conversation, or delay a usable answer. Ask a necessary task question independently when the request truly cannot proceed.

Keep explicit author choices and reported observations distinct from contextual inferences. Infer cautiously from identifiable premises when it helps propose a direction or topic; label the interpretation as a hypothesis rather than the author's settled belief. Do not demand reconfirmation of every remembered fact. Ask only when uncertainty changes the next decision, and never turn a remembered reader concern into the author's lived event.

## Configure only what is missing

When the user requests setup or changes, reuse known answers. Ask at most three short questions per round, choosing only useful gaps:
- Audience and what the author wants that audience to understand.
- Voice: direct, narrative, restrained, humorous, or another choice in the author's own words.
- Preferences to avoid, language, a desired ending, or an authorized CTA and its exact destination when relevant.
- When useful, build the reader's world: situations, aspirations, constraints, questions, decision criteria and emotions. Reuse supplied observations and propose labeled hypotheses for gaps. Separate the audience the author wants to reach from the audience actually observed.
- When useful to the task: the author's goal, recurring subject territories, expertise or offer, and the intended reader benefit/response. Accept free-text intentions; no mandatory funnel or setup checklist. Distinguish a subject pillar from a format, emotion, or funnel stage.

Use the native question tool exposed in the current session: `AskUserQuestion` in Claude Code, an available `request_user_input` or `request_user_input_async` in Codex. Follow its actual schema and mode restrictions. Offer concise choices with room for free text. If unavailable, ask the same question in chat. Do not render pretend interactive JSON or change modes to bypass a restriction. Wait for answers to dependent decisions; silence is not a preference or permission to save.

For reader responses, allow multiple choices only when the actual tool supports them; otherwise use a numbered list or textual checkboxes in chat. Reuse known answers and clarify priority only if choices conflict. A preference for debate or surprise never establishes a fact, guarantees engagement, or licenses invented conflict.

These preferences shape voice, audience and presentation. They never authorize invented facts, access to account data, external actions, or changes to BarakaSocial's scoring criteria. A preference such as "always approve my posts" cannot become an analysis rule.

## Keep or save

By default, apply context within the conversation. After establishing useful new durable context, briefly offer to save it to the shared private profile, naming what would be saved and any inferences. Do not interrupt a ready writing task, repeat a declined/unanswered offer within the conversation, or silently save. A direct save request or acceptance of that concrete offer authorizes the specified write; do not ask again. A bare request to use the skill or configure preferences is not consent to persist them. If "remember" is ambiguous about duration or destination, ask whether to keep them for this conversation or save a reusable profile. A clear request to save preferences already authorizes that write; do not ask again.

For durable local storage, use the chosen private path or offer `~/.config/barakasocial/editorial-profile.json`. Read [the shared version 1 schema](profile-schema.md) when saving or interpreting structured reader/author entries. It defines existing preferences plus optional `editorial.reader_world` and `editorial.author_perspectives`, with provenance and a reported/inferred distinction. Save only relevant, authorized summaries; do not copy a user's private corpus into the public skill. Preserve old fields, unknown properties and stable IDs. Repeated identical setup must not create duplicates or rewrite unchanged dates. Use a selected private path per author.

Campaign goals, timing, a chosen topic, a brief, and one-post response choices stay in conversation unless the user explicitly asks to persist them. They do not silently replace the standing editorial direction. Keep persistent preferences separate from post evidence and generated drafts. A profile revision does not authorize account updates.

Verify the written file and report its path plus the preferences changed. If writing fails, report that nothing was durably saved. Without persistent file access, keep the answers in this chat or provide a profile the user can copy or download; do not promise cross-session memory. Never edit the distributed SKILL.md, install hooks, modify MCP configuration, or write account settings as part of personalization.

The topic finder, hook generator, writer, post analyzer and profile optimizer read the same selected profile. Installation alone does not execute a setup wizard; the user can request configuration on first use or at any later time.
