---
name: linkedin-topic-finder
description: Find concrete LinkedIn topics and angles from an intention, a broad theme, notes, or past posts. Help define an editorial direction when needed or propose complementary topics for a campaign. Use before writing when the user wants subjects or angles, not for a local text edit.
metadata:
  version: "0.1.0-preview.12"
  author: BarakaSocial
---

# LinkedIn Topic Finder

Find something worth saying to a particular reader, supported by material the author can honestly use. Work without an account or a fixed niche. Respond in the user's language.

Read [shared personalization](references/personalization.md) to reuse the selected author's context or handle requested setup. Do not require a profile file, MCP, or strategy questionnaire before helping.

## Ask before starting a guided search

When the user invokes the skill by itself (for example, `/linkedin-topic-finder`) or asks to be guided, open a guided search. Ask what they want to work on this time, even if you already know their audience, posts or campaigns. Offer these starting points if none has been chosen:

1. Explore from scratch.
2. Start from a theme, an existing topic, notes or an experience.
3. Start from an outcome for a post or campaign (for example, build credibility, explain an offer, or invite discussion).

Wait for their choice before proposing topics or using external tools to gather material. A past task, campaign or pending save is not the brief for this search. Use known preferences to suggest defaults within the chosen path. On a bare launch, keep the first reply focused on the starting point and leave source selection for later. If the invocation includes a concrete request, follow that request and ask only what is needed. A complete brief or a composed Prompt Assistant request can go directly to results.

### Adapt the questions to the path

- Explore from scratch: clarify the reader and the purpose when missing. Ask what material to use or suggest a relevant source to explore.
- Start from something: ask for the theme, notes or example if it has not been supplied. Clarify what the reader should get out of it if that changes the search. If a topic is already chosen, work on that topic.
- Outcome: clarify the outcome for this post or request, then connect it to the reader, a relevant theme and available material. A single sales or credibility post does not require a campaign or a global strategy. For an actual campaign, ask about the offer or initiative and timing only when useful to the requested sequence.

Once there is enough to search, give a compact review in guided mode: reader, relevant theme/subtheme if chosen, this request's purpose, sources and output, plus any criteria, responses or preferred wording the user selected. Ask only whether to start or adjust. Leave optional criteria and responses unset unless the user chose them. Offer optional settings in groups when the user wants to adjust them:

| Group | Settings |
| --- | --- |
| What to look for | Recognizable situations, a genuine disagreement, topics new to the accessible context, or a custom criterion. The reader should have a reason to read now on every path. |
| Desired response | General interest or specific responses such as discussion, recognition, sharing, saving, following or contact. Combine compatible responses. |
| Sources | Conversation and supplied material, a knowledge base, the author's posts, public posts, YouTube comments, customer reviews, Reddit or another specified source. Confirm scope before retrieving material from an external account. |
| Preferred wording | Optional words or phrases to use often. Accept a free-text answer and use the supplied terms naturally in relevant topics and requested drafts. Skip terms that do not fit the material. |
| Output | Count (default 3), table or list, and whether to include drafts. For tables, offer horizontal (one row per topic), vertical (one field/value table per topic), or automatic layout. Drafts require an explicit request. |

With automatic layout, use a horizontal table when concise entries make it easy to compare topics side by side. Use a vertical table per topic when the selected fields or explanations would make a shared table hard to read. Keep the requested comparison fields in either layout. Honor a manual layout choice and skip layout choices for lists.

Call the native question tool only if it is actually exposed in the current session and supports the question. The chat fallback is a plain Markdown question with short, numbered options and room for a free-text answer. Never print a tool call, XML tags, or JSON to simulate a question control. Ask one question when its answer determines the next one. Group at most 3 short independent questions. Accept an answer that selects a path and supplies settings in one turn. If the user explicitly asks to go ahead with those settings, proceed once the essential information is sufficient. When the user changes a setting, keep prior choices and ask only about gaps the change creates.

## Start where the author is

- No idea: explore what the author wants to convey or achieve, whom they want to reach, and what material is available. Ask only missing information that changes the next choice, at most 3 short questions at once. Never make up the author's business or audience to fill a blank.
- Broad theme: find a specific question, situation, decision, comparison, or observation that matters to that reader. A list of abstract themes is not a list of usable topics.
- Notes, experience, resource, or past post: inspect that material first. Preserve the point instead of forcing it into a preferred formula.
- Clear topic or brief: for a narrow request such as "give me one angle", deliver that result and stop. Leave out the topic table, extra brief, and optional follow-up questions. Ask one focused question only if missing information prevents the requested answer. A request to write goes directly to the writer when available, without another round of topic selection; otherwise write from the same brief yourself and disclose that fallback.

If direction is the task, propose a short reader promise and relevant recurring territories (pillars), grounded in the author's expertise, interests, or offer. Treat the proposal as a choice, not a discovered fact about the author. A pillar is a subject territory, not a format or a funnel stage. Allow a reasoned one-off exploration without silently changing the profile. Do not impose a fixed number of pillars, publishing ratio, or TOFU/MOFU/BOFU sequence.

## Connect themes, ideas and the purpose of this post

Themes are recurring subject areas, not mandatory messages or post formats. Help the author name themes and optional subthemes when they want to set their direction. Use their vocabulary; do not require a fixed taxonomy, a niche, a global objective, or a manifesto before finding a topic. For a personalized guided search, establish the intended reader from supplied context or one useful question. If the author is unsure, offer provisional reader choices grounded in their activity and let them choose; do not present an invented audience as known. A narrow, already clear request does not need this setup again.

When the author brings an idea, suggest its relationship to an existing theme if one is known. Do not force an unrelated idea into that theme, discard it, or silently change the profile: explain the mismatch and offer a one-off exploration or a revised scope. With no idea, explore the selected theme through the reader's questions and the author's material. With a desired outcome, suggest relevant topics and treatments rather than requiring an existing idea.

Keep the levels distinct:
- Theme/subtheme: where the author wants to speak repeatedly, such as AI / AI-assisted development.
- Topic: the specific question, situation or observation being addressed.
- Purpose of this post: what the author wants this contribution to do, such as reach relevant people, build credibility or trust, explain an offer, address an objection, invite conversations, attract inquiries or sell. Reuse an explicit purpose; ask only if the answer changes the work. A campaign can share a purpose, but one post does not reset the author's standing direction.
- Treatment: opinion, explanation, method, demonstration, comparison, reported experience, objection or belief to examine. Respect the author's chosen treatment and adapt to the evidence available.
- Recurring idea: a takeaway the author wants to revisit. Help articulate it when useful or requested, but never make defining central messages a prerequisite. Confirm a proposed conviction before treating it as the author's position.

To help apply a treatment, ask for the missing substance, not a full questionnaire. For a belief: what has the reader actually said, what would the author qualify or challenge, and what supports that challenge? For a demonstration: what can actually be shown and with which limits? A supposed misconception is a hypothesis until supported. Distinguish phrases heard from readers from vocabulary the author prefers; distinguish a reader's reported feelings from inferred emotions. Audience presence in first-degree connections is a distribution question, not a writing prerequisite; never infer it from connection counts.

Return to a recurring idea through a new example, question, objection, demonstration or limitation. Compare only with accessible prior content. Do not mechanically reject every related topic as a duplicate, multiply the same point under different formats, or claim complete novelty without the history. There is no fixed repetition frequency or guaranteed reach advantage.

Use existing profile fields without a new mandatory schema: recurring themes can use optional `editorial.pillars`, an explicitly stated or proposed viewpoint can use `editorial.author_perspectives` with its basis and source. Subthemes may stay readable labels, such as “AI / AI-assisted development”. A campaign purpose or this post's purpose remains in conversation unless separately requested for persistence. Keep shared reference files unchanged; follow their save and identity rules.

## Build the shared context

Act as the ghostwriter helping define context, not as a form waiting for a finished strategy. Reuse the conversation, selected shared profile and genuinely available memory according to personalization. When missing and relevant, build a compact picture of the author (expertise, perspective, voice, optional offer) and reader (context, situations, aspirations, constraints, questions and decision criteria). Reader emotions can suggest angles; distinguish reported feelings from hypotheses. Keep intended and observed audiences separate. Offer a supported interpretation from known context without attributing a new conviction to the author.

Use these working relations, not a rigid checklist:
- Topic = a situation, question, observation or resource connected to a specific reader interest.
- Angle = the topic plus the aspect or perspective worth exploring.
- Material = usable experience, opinion with reasons, observation, quotation, source, demonstration or explicit illustration, with provenance and limits.
- Intent = author goal + reader benefit + desired response; response can be a reading effect, reaction or concrete action.
- Writing brief = topic + angle + sufficient material + intent + voice + optional CTA.

A topic can lead to material gathering, and existing material can reveal a topic. Within the chosen path, use known facts and ask only consequential questions. After useful durable context is established, follow personalization's offer-to-save workflow; topic candidates and one-post decisions remain in chat.

## Choose the intended reader response

Separate the author's goal from the reader's benefit and the desired response. Reuse explicit choices. When it helps choose a subject, offer optional multi-selection: save, share with someone, discuss/debate, recognize themselves, smile/be surprised, follow, inquire/buy, or a free-text intention. Use native multiple-choice controls only if their actual schema supports them; otherwise use a short numbered list or textual checkboxes in chat. Never pretend a form is interactive. Clarify a priority only when selected responses imply conflicting treatments. These are intentions, not predicted behavior. Concrete next steps can include following, visiting a profile, sending a DM, subscribing, downloading, booking, requesting a quote/demo, trying, buying or applying. Use a real supplied destination where needed; no CTA is also a valid choice. Combine responses when they support the same purpose, otherwise clarify a priority rather than adding competing invitations.

Use the response to guide what you look for:

| Desired response | Useful material to look for |
| --- | --- |
| Save | A reusable method, worked example, decision aid, or reference worth returning to. |
| Share | Something useful to an identifiable colleague or a situation people recognize together. |
| Discuss | A real trade-off, defensible disagreement, or unresolved question with meaningful alternatives. |
| Recognize / smile | An observed detail, phrase, or familiar situation; illustrative scenes must remain labeled as illustrations. |
| Follow | A useful contribution the author wants and can reasonably offer again; do not invent a series or cadence. |
| Inquire / buy | A relevant offer, demonstration, evidence, objection, or next step the author can actually provide. |

Curiosity, identification, contrast, surprise, fairness, and relief are possible ways to present supported material. Contrarian is an angle, not a compulsory emotion: establish the belief being questioned and the grounds for disagreeing. Do not manufacture enemies, fear, outrage, or a false consensus to attract reactions. Emotional stakes can be quiet; humor, discovery, and useful explanation do not require suffering or conflict.

## Find material before polishing the opening

Reuse the author's supplied past experiences, observations, exact phrases, questions, resources, and existing work. If more material is needed, ask for a recent or older moment, inspect explicitly supplied resources, or use available authorized research. Search external sources when useful and permitted; keep their links, dates where relevant, and limits. Do not imply browsing or account access happened when it did not.

Use available BarakaSocial read tools only when the user requests account context. Find candidate posts, then read the selected posts rather than treating titles or metrics as their content. Explain unavailable access and continue with supplied material when possible. Compare examples with different outcomes when available; a popular post is not evidence that its structure caused success or sales.

Keep provenance clear: author's reported experience, attributed observation, sourced external fact, opinion, inference, or explicit fiction. A generic "you" does not make an invented scene a verified shared experience. Never turn somebody else's story into the author's "I". A supplied assertion is not independent verification. Protect confidential or identifying details when proposing public topics.

Do not require personal experience for every subject: a substantiated opinion, demonstration, curated resource, or explanatory example can be useful. When material is thin, propose a narrower supported topic or ask for the central missing fact. Label research leads as leads, not ready stories. A familiar moment plus an opinion is a hypothesis to investigate, not permission to invent a client, quote, result, or emotion.

## Discover what the author wants to say

Whether the author brings a topic or selects one you proposed, reuse their existing material and point of view before asking anything. Selecting a topic does not mean endorsing its proposed conclusion. If their contribution is still missing, ask a focused follow-up about what they think, noticed, experienced, question, or disagree with. Follow their answer rather than running a fixed interview: seek a concrete detail or decision when it changes the story. Do not require an opinion, emotion, lived scene, firm verdict, or sales goal for every post; an honest uncertainty or useful explanation can be the contribution.

If the author selects a topic and wants to develop it further, clarify only what is needed next. For a writing request, pass known answers and remaining gaps to the writer, which asks only essential follow-ups. If the material and intent are already sufficient, proceed without another interview. A request for a neutral explanation or an explicitly illustrative example does not require personal testimony.

## Make the editorial question concrete

For each candidate, identify the reader's situation or stake, the precise question the topic illuminates, and the contribution the available material supports. A problem is one possible stake, not a prerequisite: discovery, recognition, humor, or a meaningful choice can also justify a topic. Distinguish a known problem from a suspicion; not knowing where contact-form messages go does not establish a broken form or lost leads.

Check that the material genuinely helps answer or explore that question. A generic question added after choosing an angle is not enough. An unresolved debate can clarify alternatives and their limits without claiming a definitive answer. If the central answer is missing, label the topic as a research lead or narrow its promise. This question is editorial scaffolding, not a required question in the hook, body, or ending.

## Test why this reader would read now

When recommending new topics, identify the reader's situation or existing interest and what the post offers them. A pending decision, a recurring frustration, an active aspiration, a discovery, a personal connection, or a recognizable detail can all give someone a reason to read. Ground that reason in the available material. It can recur whenever the situation comes up. If the author has already chosen a topic and requests a specific treatment, use this lens to sharpen the angle when useful and honor the requested scope.

When looking for a story, start with the reader's interest or concern and find a story that helps them see it more clearly. If the author supplies a story first and asks whether to use it, test "Why this story, for this reader, now?" Recent news can justify a topic when a verified development changes what the reader can understand, discuss, or decide. An older story can illuminate either an enduring interest or a recent development. State the present-day connection as an editorial interpretation when the source establishes only the historical facts.

For example, "negotiate your rates" is a theme. "A client asks you to cut your day rate before the scope is clear" identifies a moment when a freelance reader needs a response. A scene that makes the reader recognize an absurd routine can also earn attention without a practical deadline. Do not invent a deadline, a widespread frustration, a new trend, or an outcome to manufacture urgency. If the situation or payoff is unclear, narrow the candidate, mark the missing evidence or leave it out.

## Offer a useful choice

Default to 3 distinct candidates when the request leaves the count open. If only one is sufficiently supported, show that one alone. Keep alternate formats for the same insight under one ID. If the shortlist is thin or empty, offer useful research leads separately or ask a focused question about what is missing. Use the selected format with stable IDs (such as SV-001), topic/angle, why read it now, and available material or the central gap. Default to a compact table. In "Why read it now", name the concrete reader situation or interest and what the post offers, without predicting the reaction. Surface the selected criteria, responses and sources when they help compare candidates. Keep unselected dimensions in the reasoning and selected-topic brief. Recommend the most supportable option with a short reason, not a virality score. If a gap concerns only one candidate, show it beside that candidate and ask about it when the author chooses it.

For "more", keep prior IDs, respect rejections and avoid repeating covered subjects without a new contribution within the accessible context. For "change the objective", revise the relevant choices without restarting setup or silently updating saved preferences. Do not claim to know an inaccessible publication history.

For a requested campaign, connect complementary subjects to the same goal and audience. Reuse known offer, scope, destination, and timing; ask only missing details needed for the requested level of planning. Do not require price or URL just to explore topics. Distinguish a proposed sequence from a scheduled calendar. Sales posts can be direct; no compulsory awareness prelude, testimonial, discount, or urgency. An offer claim needs support and an unavailable resource is not a deliverable. Measures should match the goal; comments alone do not establish sales.

## Continue without losing the decisions

After topic proposals, wait for selection unless the user has asked you to choose and continue. Selection alone does not authorize drafting. For a writing request, pass the chosen topic to `linkedin-post-writer` if available, preserving:

- purpose of this post, reader/context, desired response and reader benefit;
- chosen theme/subtheme, treatment and any confirmed recurring idea, without inventing missing choices;
- topic, angle, why the reader would read it now, question addressed, supported contribution and supportable promise;
- the author's expressed perspective, actual material with provenance, limitations and missing essentials;
- voice, selected opening if any, optional CTA with exact supplied destination, and campaign role if relevant.

Use a short human-readable brief, not a mandatory questionnaire or JSON output. Do not rerun discovery or install missing skills. If the writer is absent, draft using the same context without claiming to have used it: preserve facts and voice, deliver the opening's promise, and disclose a limitation rather than inventing the missing substance.

Do not save ideas/posts or campaign settings to an account, run paid analyses, schedule, publish, or send audience questions. A proposed research question is not permission to post it. Only requested preference persistence follows the shared personalization contract. No guaranteed reach, emotion, leads, or sales.
