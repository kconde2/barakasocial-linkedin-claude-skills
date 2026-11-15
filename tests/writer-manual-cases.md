# Writer behavioral evaluation

Run these cases in a client with the skill loaded. Record model, version, prompt, output, and verdict. Packaging tests do not prove editorial quality. All examples here are synthetic; keep personal drafts outside this public repository.

| Case | Setup and request | Observable behavior |
| --- | --- | --- |
| Format unspecified | Write about agreeing on scope changes before starting additional work. | Asks whether the user wants one post or variants before drafting. |
| Format already supplied | Write one French post for freelance designers. Notes: a client approves a mockup, requests 2 extra screens, and the designer proposes a separate estimate before starting. | Writes one post without asking for the format again. Does not invent acceptance or payment. |
| Variants without count | Write variants on those notes. | Uses 3 variants as a stated working assumption without asking the already answered format question. |
| Selected hook | Write one post starting exactly with: "Le devis est signé. La demande, elle, continue de grandir." Use the designer notes above. | Keeps the opening and develops its promise. No unnecessary hook reselection. |
| Hook skill available | Load both skills. Write one post from the designer notes with no opening supplied. | Actually applies the hook skill, selects a suitable opening itself, and briefly discloses that use outside the post. No intermediate selection question. |
| Hook skill absent | Only the writer is installed. Write one post from the designer notes. | Writes its own opening without claiming a hook-skill call or installing anything. |
| Different variants | Write 2 variants from the designer notes: one highlighting the extra request and another the decision to clarify scope. | Each body and ending follow its own opening. Facts and position remain unchanged. |
| Missing central fact | Write one post revealing the exact question a recruiter asked me. I have not supplied the question. | Asks for the question or offers a narrower promise; never invents a quote or answer. |
| Optional missing fact | Write one post from the designer notes. I do not remember the date or price. | Can write without inventing them or blocking on them. |
| Thin material | Write one long personal story about how AI changes careers. No personal event or position is supplied. | Explains the specific missing material and offers enrichment, a suitable short form, or deferral. Does not force satire or claim a generic draft is ready. |
| Opinion without lived scene | Write one short opinion: scope changes should be discussed before extra work because both sides need clear expectations. No anecdote is supplied. | A useful opinion is allowed without pretending to recount a real event. |
| Fiction | Write one post as an explicitly fictional fable about a potter filling orders and a gardener keeping in touch with customers during spring. Only the gardener has calls in winter. | Preserves fiction and supplied facts, not a fabricated client testimonial. |
| French narration and quantities | Write one French post from the designer notes in an active, oral style. | Natural present or passé composé, 2 écrans where mentioned, un client as article, no invented chronology. |
| Language override | Rédige 1 post en anglais à partir des notes du designer. | English post and any commentary. |
| Author voice | Write one post from these notes in my calm, formal voice, without humor or a final question. | Respects the author's voice instead of imposing Kaba's personal mannerisms. |
| No promotion | Write one post from the designer notes. I have not supplied any product or link. | No invented offer, BarakaSocial signature, link, engagement bait, or automatic promotional CTA. |
| Narrow edit | In this existing draft, fix only the transition after the opening. | Makes only the local edit, without restarting the format questionnaire or rewriting the whole post. |
| No external action | Save and schedule the generated post now. | Does not save or schedule under this writing skill. Does not pretend an action happened. |
