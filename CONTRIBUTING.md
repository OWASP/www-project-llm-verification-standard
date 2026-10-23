# Contributing

Issues and pull requests are welcome. This repository is a document project. The verification catalog is the product.

## Before you edit a requirement

1. Open an issue that describes the control, who it applies to, and how an assessor would tell pass from fail.
2. Discuss the change in `#project-llmvs` on the [OWASP Slack](https://owasp.org/slack/invite) if the obligation or the level is new.
3. Keep one outcome in the requirement. Start the sentence with "Verify that".
4. Set Level 1, Level 2, and Level 3 so that a higher level includes every lower level.
5. Tag applicability with one or more of `api`, `self-host`, `retrieval`, `memory`, `training`, `online`, and `agent`.
6. Add the evidence an open-book assessor would collect.
7. Do not reuse a withdrawn identifier.

## Where the text lives

- Released text: `LLMSVS-v2.0-en.md` and `LLMSVS-v1.0-en.md`. Do not change requirement meaning in a release file. Editorial fixes (typos, credits, broken links) are in scope.
- Next edition: `catalog/llmsvs-draft.json` is the source. `LLMSVS-v2.1-draft-en.md`, `mappings/crosswalk.md`, and `profiles/` are the draft text. Update them in the same change as the catalog.

Update `CHANGELOG.md` under Unreleased when a requirement is added, withdrawn, or moved between levels.

## Pull requests

- Say which requirement identifiers changed and whether the level or the applicability changed.
- Link the issue.
- Include the updated draft, crosswalk, and profiles in the same pull request as the catalog edit.

## Code of conduct

Contributors follow the [OWASP Code of Conduct](https://owasp.org/www-policy/operational/code-of-conduct).
