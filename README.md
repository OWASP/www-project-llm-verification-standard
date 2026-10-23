---
layout: col-sidebar
title: OWASP Large Language Model Security Verification Standard
tags: llm, verification, ai, security
level: 2
type: documentation
pitch: An open standard for designing, building, and verifying the security of applications that use large language models.
---

## About

OWASP Large Language Model Security Verification Standard

The OWASP Large Language Model Security Verification Standard (LLMSVS) is a catalog of security requirements for applications that use large language models. Architects, developers, testers, and security teams use it to agree what “verified” means for an LLM feature. It does not replace the OWASP Application Security Verification Standard for the rest of the application.

**Current release:** [LLMSVS v2.0 (English)](https://github.com/OWASP/www-project-llm-verification-standard/blob/main/LLMSVS-v2.0-en.md)

**Next-edition draft, for review:** [LLMSVS v2.1 draft](https://github.com/OWASP/www-project-llm-verification-standard/blob/main/LLMSVS-v2.1-draft-en.md)

The draft is not a release. Cite v2.0 until the project accepts a newer edition.


[![OWASP Incubator](https://img.shields.io/badge/owasp-incubator-blue.svg)](https://owasp.org/www-project-llm-verification-standard/)
[![Creative Commons License](https://img.shields.io/github/license/OWASP/www-project-llm-verification-standard)](https://creativecommons.org/licenses/by-sa/4.0/ "CC BY-SA 4.0")

## Introduction

The primary aim of the OWASP Large Language Model Security Verification Standard (LLMSVS) Project is to provide an open security standard for systems which leverage artificial intelligence and Large Language Models.

The standard provides a basis for designing, building, and testing robust LLM backed applications, including architectural, model lifecycle, model training, model operation and integration, model storage and monitoring concerns.

**Please [log issues](https://github.com/OWASP/www-project-llm-verification-standard/issues) if you find any bugs or if you have ideas. We may subsequently ask you to [open a pull request](https://github.com/OWASP/www-project-llm-verification-standard/pulls) based on the discussion in the issue.**

## Classification and audience

**Classification:** Documentation

**Audience:**

* Builders
* Breakers
* Defenders

## Project leaders

The project is led by [Vandana Verma Sehgal](https://github.com/vermava) and [Elliot Ward](https://github.com/mowzk). Reviewers of the first edition are credited in the standard. Supporters are listed in [SUPPORTERS.md](SUPPORTERS.md).

## Standard documents (Markdown)

- **[LLMSVS v2.0 (English)](LLMSVS-v2.0-en.md)** — current release. Cite this edition.
- **[LLMSVS v2.1 draft (English)](LLMSVS-v2.1-draft-en.md)** — proposed next edition. Not a release. Kept in step with [`catalog/llmsvs-draft.json`](catalog/llmsvs-draft.json).
- **[LLMSVS v1.0 (English)](LLMSVS-v1.0-en.md)** — markdown copy of the February 2024 **0.1** text. The filename says 1.0; the requirement numbers match that first publication.
- **[Changelog](CHANGELOG.md)**
- **[Crosswalk](mappings/crosswalk.md)**, **[profiles](profiles/)**, and a **[worked assessment](examples/worked-assessment.md)** for the draft.

`main` contains the 2.0 release and the in-progress draft together. Create a git tag when 2.0 should stay frozen while the draft continues on `main`.

## Repository and community

* [GitHub repository](https://github.com/OWASP/www-project-llm-verification-standard)
* [Releases (changelog)](https://github.com/OWASP/www-project-llm-verification-standard/releases)
* [Join OWASP Slack](https://owasp.org/slack/invite)
* [#project-llmvs on Slack](https://owasp.slack.com/messages/C06MDJG0KBK)

## Standard Objectives

The requirements were developed with the following objectives in mind:

1. **Develop and Refine Security Guidelines**: Consolidate general objectives, including community involvement and standard evolution, into a comprehensive set of security guidelines for AI and LLM-based systems.
2. **Address Unique Security Challenges of LLMs**: Focus specifically on the unique functional and non-functional security challenges presented by Large Language Models.
3. **Guide Development Teams in Secure Practices**: Provide detailed guidance to development teams for implementing robust security measures in LLM-based applications.
4. **Assist Security Teams in Audits and Penetration Testing**: Offer methodologies and standards for security teams to conduct effective security audits and penetration tests on LLM-backed systems.
5. **Establish and Update Security Benchmarks**: Create and regularly update security benchmarks to align with the latest advancements in AI and cybersecurity.
6. **Promote Best Practices in LLM Security**: Encourage the adoption of industry best practices in securing LLM-based systems.
7. **Align Security Expectations Among Stakeholders**: Establish a common understanding of security expectations among developers, security professionals, vendors, and clients.


## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). Requirement changes go in the draft catalog, not in the 2.0 release file. Contributors follow the [OWASP Code of Conduct](https://owasp.org/www-policy/operational/code-of-conduct).


## License

The entire project content is under the **[Creative Commons Attribution-Share Alike v4.0](LICENSE.md)** license.