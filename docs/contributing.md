# Test and contribute

[Home](../README.md) · [Français](contributing.fr.md)

A [three-case isolated behavioral smoke check](../tests/behavior-smoke-results.md) covered missing MCP, actual profile persistence, and a temporary preference override. It does not validate native client dialogs or connected MCP paths.

The [manual evaluation cases](../tests/manual-cases.md) help assess actual output in Claude. They cover concrete topics, missing information, fabricated numbers, language, and out-of-scope requests. The preview has not yet been evaluated in the user's Claude account.

The [writer evaluation cases](../tests/writer-manual-cases.md) cover format choices, optional hook coordination, missing material, and factual fidelity. These are manual scenarios, not automated proof of writing quality.

The [analyzer cases](../tests/analyzer-manual-cases.md) cover MCP availability, preview versus saved diagnostics, version fidelity, and real reviewer provenance. The [personalization cases](../tests/personalization-manual-cases.md) cover interactive questions, scoped preferences, and honest persistence. These cases require behavioral execution; their presence is not a passing evaluation.

The repository stays simple:

```text
skills/linkedin-hook-generator/SKILL.md   Installable instructions
tests/manual-cases.md                    Manual editorial evaluation
skills/linkedin-post-writer/SKILL.md      Installable writing instructions
tests/writer-manual-cases.md              Writer evaluation
skills/linkedin-post-analyzer/SKILL.md    Analysis instructions
skills/*/references/personalization.md   Shared personalization guidance in each ZIP
tests/analyzer-manual-cases.md           Analyzer evaluation
tests/personalization-manual-cases.md    Personalization evaluation
scripts/package_skill.py                 ZIP packaging
```

Check the packaging and rebuild the ZIP with Python 3:

```sh
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/package_skill.py linkedin-hook-generator
python3 scripts/package_skill.py linkedin-post-writer
python3 scripts/package_skill.py linkedin-post-analyzer
```

The generated `dist/` directory is ignored by Git. Each ZIP contains only the skill's files, without local configuration or user data.
