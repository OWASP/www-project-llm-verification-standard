# Changelog

## Unreleased — 2.1 draft

Not an OWASP release. Source: `catalog/llmsvs-draft.json`. Rendered text: `LLMSVS-v2.1-draft-en.md`.

- Requirements are single “Verify that” outcomes with applicability tags and an evidence note.
- Levels are defined as cumulative. Not Applicable is an explicit result.
- Level 1 includes secret handling, inventory, untrusted context, untrusted output, tool argument checks, and consumption limits.
- Eight v2.0 rows are withdrawn and their identifiers are reserved: 2.7, 2.11, 2.14, 2.15, 5.3, 5.6, 5.7, 5.8.
- New identifiers extend the existing chapters: 1.5, 1.6, 2.19, 2.20, 4.7, 4.8, 4.9, 5.18, 5.19, 5.20, 5.21, 5.22, 5.23, 6.13, 6.14, 6.15, 6.16, 6.17, 7.7, 8.3, 8.4, 8.5.
- Crosswalk to the OWASP LLM Top 10 2026 and the OWASP Agentic Top 10 2026: `mappings/crosswalk.md`.
- Profiles and a worked assessment: `profiles/`, `examples/worked-assessment.md`.
- MITRE ATLAS technique IDs are intentionally absent until they are checked against the current ATLAS release.

## 2.0 — 2026

Markdown release in `LLMSVS-v2.0-en.md`. The numbered requirements carry forward the 0.1 set with editorial corrections, the ASVS crosswalk note, clarifications to 5.5 and 5.10, and chapter-objective clarifications for V3, V4, and V6.

The file previously linked a supporters section that was not in the body, dated the copyright from 2008, and said “(LLM)SVS” in the certification section. Those documentation errors are corrected in the 2.0 file without changing requirement text.

## 0.1 — February 2024

First public text. The markdown copy is `LLMSVS-v1.0-en.md`. The filename says 1.0; the preface of that file says alpha 0.1. The requirement numbers match that publication.
