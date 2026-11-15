# Personalization shared by the three LinkedIn skills

## Reuse before asking

Use explicit preferences already supplied in the conversation or an author profile the user has selected. Current instructions override saved defaults for this request only. Never apply one author's profile to another author silently. When conflicting sources would materially change the result, ask one focused question; do not merge identities.

In a local file-capable client, read the user-selected profile path if available. Otherwise you may check the single conventional path `~/.config/barakasocial/editorial-profile.json`, subject to the client's file permissions. Do not search unrelated personal files. If the profile names a different author, ask before using it. A missing file is normal. An unreadable or malformed profile should be reported without overwriting it; continue from the conversation when possible.

On first use without preferences, briefly offer optional personalization alongside the requested work. Do not force onboarding, repeat an offer declined in this conversation, or delay a usable answer. Ask a necessary task question independently when the request truly cannot proceed.

## Configure only what is missing

When the user requests setup or changes, reuse known answers. Ask at most three short questions per round, choosing only useful gaps:
- Audience and what the author wants that audience to understand.
- Voice: direct, narrative, restrained, humorous, or another choice in the author's own words.
- Preferences to avoid, language, a desired ending, or an authorized CTA and its exact destination when relevant.

Use the native question tool exposed in the current session: `AskUserQuestion` in Claude Code, an available `request_user_input` or `request_user_input_async` in Codex. Follow its actual schema and mode restrictions. Offer concise choices with room for free text. If unavailable, ask the same question in chat. Do not render pretend interactive JSON or change modes to bypass a restriction. Wait for answers to dependent decisions; silence is not a preference or permission to save.

These preferences shape voice, audience and presentation. They never authorize invented facts, access to account data, external actions, or changes to BarakaSocial's scoring criteria. A preference such as "always approve my posts" cannot become an analysis rule.

## Keep or save

By default, apply preferences within the conversation. Only persist them when requested. If "remember" is ambiguous about duration or destination, ask whether to keep them for this conversation or save a reusable profile. A clear request to save preferences already authorizes that write; do not ask again.

For durable local storage, use the chosen private path or offer `~/.config/barakasocial/editorial-profile.json`. Keep it outside the skill installation and public repository so upgrades do not erase it. Read any existing file first and preserve unrelated fields. Use UTF-8 JSON with `schema_version: 1` and only supplied fields such as `author`, `audience`, `voice`, `avoid`, `language`, and `cta`. Use strings for author/audience/voice/language, an array of strings for avoid, and an object with `mode` and an optional supplied `url` for cta. Never fill unknown fields with invented preferences. If the schema version is unsupported, explain rather than silently converting it.

Verify the written file and report its path plus the preferences changed. If writing fails, report that nothing was durably saved. Without persistent file access, keep the answers in this chat or provide a profile the user can copy or download; do not promise cross-session memory. Never edit the distributed SKILL.md, install hooks, modify MCP configuration, or write account settings as part of personalization.

The hook generator, writer and analyzer read the same selected profile. Installation alone does not execute a setup wizard; the user can request configuration on first use or at any later time.
