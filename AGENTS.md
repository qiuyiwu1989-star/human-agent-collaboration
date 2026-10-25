# Maintaining this library

- This repository stores reusable collaboration methods, not private task records or shared credentials.
- Keep skills model-independent and portable. Use standard SKILL.md frontmatter; optional platform metadata belongs in agents/.
- Preserve user intent. Simple requests must not be expanded into mandatory interviews, committees, or long workflows.
- Add methods backed by concrete use cases. Do not add empty categories to claim coverage of every domain.
- Keep the skill entrypoint concise; link conditional detail from references. Avoid forced dependencies between skills.
- Distinguish structural checks, behavioral evaluation, independent review, and real-world outcomes in every validation report.
- Before publishing changes, inspect the diff for unintended content and verify relative links and skill frontmatter. Never include local absolute paths, secrets, private materials or copied third-party articles.
- For behavioral evaluation, use evaluations/scenarios.md or a fresh realistic task. Keep generated evaluation artifacts outside the repository unless explicitly selected as public evidence.

- Structured records live in skills/collaboration-library/references/catalog.json. Keep IDs stable; update affected cards when source methods change. Regenerate index.md with scripts/build_index.py and run the repository tests. Examples and evaluation prompts must never be promoted to observed success without public outcome evidence.
