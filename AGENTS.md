# Repository rules

## Skill language and behavior

- Write SKILL.md instructions and descriptions in English. Respond to users in their requested language. Examples may demonstrate another language when explicitly useful.
- Preserve the validated workflow when translating. Do not add product behavior during a language-only change.
- Keep French and English user documentation aligned. Use straight apostrophes in French, no em dashes and no comma before et, ou, ni, mais, donc, or or car.
- The catalogue Install link points to each skill's installation section, not directly to a ZIP. Keep ZIP downloads on the skill's page. Explain required companion skills.
- Never publish or attach media to LinkedIn through these skills. Respect each skill's boundaries and the user's scope.

## Distribution

- Keep AGENTS.md and repository README pages outside installed ZIPs.
- Package complete skill folders with required references and scripts. Verify reproducible archives and run the tests before publication.
- Existing published archives are immutable. Assign a new version to changed skills and keep matching source tags, ZIP URLs and documentation.
- Preserve catalog release history and verify downloaded published bytes before activating a catalogue entry.
- Legacy skills use updates.json. Visual skills use image-updates.json because legacy clients reject unknown skill names. Preserve separate caches and helper allowlists.
- Keep helper copies identical within each family. Do not imply image viewing or editing is available in every client. Record actual test limitations.
- Commit and publish only on explicit user request. Permission to publish one batch does not authorize later batches. Do not merge an application PR unless requested.

## Checks

Run `python3 -m unittest discover -s tests -p 'test_*.py'`, package changed skills with scripts/package_skill.py and build the relevant candidate catalogue. Update public catalogue only after published asset verification. Never package user posts, credentials or private profiles.
