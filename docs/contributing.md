# Test and contribute

[Home](../README.md) · [Français](contributing.fr.md)

A [three-case isolated behavioral smoke check](../tests/behavior-smoke-results.md) covered missing MCP, actual profile persistence, and a temporary preference override. It does not validate native client dialogs or connected MCP paths.

The [manual evaluation cases](../tests/manual-cases.md) help assess actual output in Claude. They cover concrete topics, missing information, fabricated numbers, language, and out-of-scope requests. The preview has not yet been evaluated in the user's Claude account.

The [writer evaluation cases](../tests/writer-manual-cases.md) cover format choices, optional hook coordination, missing material, and factual fidelity. These are manual scenarios, not automated proof of writing quality.

The [analyzer cases](../tests/analyzer-manual-cases.md) cover MCP availability, preview versus saved diagnostics, version fidelity, and real reviewer provenance. The [personalization cases](../tests/personalization-manual-cases.md) cover interactive questions, scoped preferences, and honest persistence. These cases require behavioral execution; their presence is not a passing evaluation.

The repository stays simple:

```text
skills/linkedin-topic-finder/SKILL.md     Topic discovery and campaign subjects
skills/linkedin-hook-generator/SKILL.md   Installable instructions
tests/manual-cases.md                    Manual editorial evaluation
skills/linkedin-post-writer/SKILL.md      Installable writing instructions
tests/writer-manual-cases.md              Writer evaluation
skills/linkedin-post-analyzer/SKILL.md    Analysis instructions
skills/*/references/personalization.md   Shared personalization guidance in each ZIP
skills/*/references/profile-schema.md   Shared private profile schema
tests/analyzer-manual-cases.md           Analyzer evaluation
tests/personalization-manual-cases.md    Personalization evaluation
scripts/package_skill.py                 ZIP packaging
```

Check the packaging and rebuild the ZIP with Python 3:

```sh
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/package_skill.py linkedin-topic-finder
python3 scripts/package_skill.py linkedin-hook-generator
python3 scripts/package_skill.py linkedin-post-writer
python3 scripts/package_skill.py linkedin-post-analyzer
python3 scripts/package_skill.py linkedin-profile-optimizer
```

The generated `dist/` directory is ignored by Git. Each ZIP contains only the skill's files, without local configuration or user data.

[Profile optimizer cases](../tests/profile-optimizer-manual-cases.md) cover supplied material, optional MCP, stale/local versions, unseen images and proposal-only boundaries. These scenarios still require execution in the target client.

The [Topic Finder cases](../tests/topic-finder-manual-cases.md) cover responses, campaigns, writer handoff, and preferences. See the [preview.10 smoke results](../tests/topic-finder-smoke-results.md) for executed checks and remaining evaluation.


## Update helper distribution

The preview.14 candidate includes a Python standard-library helper and three references per skill. Keep scripts/skill_updates.py and every skills/*/scripts/skill_updates.py identical. Run python3 -m unittest discover -s tests -p 'test_*.py' before packaging.

Build each ZIP with python3 scripts/package_skill.py <skill-name>, then prepare the candidate catalog with python3 scripts/build_update_catalog.py. The candidate is written to dist/updates.json. Do not expose it as the public catalog before uploading the exact release assets.

After publication is explicitly authorized and the release assets are uploaded, run python3 scripts/build_update_catalog.py --verify-published --output updates.json. This checks the remotely downloaded bytes before writing the public catalog. Commit/push that catalog separately, then update the application's advertised versions. Existing published archives must never be replaced.

Keep the earlier catalog release records so local modifications can be distinguished from an official installed version. No post content or private profile belongs in this catalog. The first release with the helper still requires manual installation on older clients.
