---
title: OWASP Large Language Model Security Verification Standard
lang: en
version: '2.1-draft'
status: draft
---

# LLMSVS v2.1 draft — OWASP Large Language Model Security Verification Standard

**Status:** Draft for community review. This is not an OWASP release. Cite [LLMSVS v2.0](LLMSVS-v2.0-en.md) until this draft is accepted.

**Publication target:** next edition after 2.0.

This draft is kept in step with [`catalog/llmsvs-draft.json`](catalog/llmsvs-draft.json). Update the catalog and the sections below the preface together.

## What this draft changes

Version 2.0 kept the February 2024 requirement numbers and tightened wording. This draft makes the catalog assessable and lines it up with the OWASP Top 10 for LLM Applications 2026 (published 4 August 2026) and the OWASP Top 10 for Agentic Applications 2026.

- Every active requirement is one outcome, written as “Verify that”.
- Levels are cumulative: Level 2 includes Level 1, and Level 3 includes Level 2.
- Each requirement is tagged with the architectures it applies to. Everything else is Not Applicable, and the report says why.
- Level 1 is rebuilt around secrets, inventory, untrusted context, untrusted output, tool least privilege, tenant isolation, and consumption limits.
- Optional techniques (canaries, entropy checks, watermarking, redundant providers) move to Appendix B. They are not pass/fail requirements.
- New requirement IDs extend the existing chapters. Withdrawn IDs are not reused.

Requirement identifiers from 2.0 still mean the same control where the row is active. Where the level or the obligation changed, the verification note under the chapter says so.

## How to use the levels

| Level | Use it for | What “pass” means |
| --- | --- | --- |
| Level 1 | Any LLM-backed system | The baseline controls for the features that system actually has |
| Level 2 | Sensitive data, customer data, or internal business data | Level 1 plus the Level 2 rows for those features |
| Level 3 | High-value transactions, regulated data, or systems whose failure stops the business | Level 2 plus the Level 3 rows for those features |

Pick the level before testing. Do not drop a Level 1 row because it is inconvenient. Do mark a row Not Applicable when the feature is absent.

## Applicability and Not Applicable

Tags used in this draft:

| Tag | The system has this feature when |
| --- | --- |
| `api` | An application sends prompts to a model, hosted or local |
| `self-host` | The organization runs inference or loads weight files |
| `retrieval` | Documents or embeddings are added to the prompt |
| `memory` | Conversation or long-term memory is stored across turns or sessions |
| `training` | The organization trains or fine-tunes a model |
| `online` | Production weights are updated from live user data |
| `agent` | The model can call tools, plugins, or remote tool servers |

Rules for the report:

1. If a tagged feature is absent, every requirement that applies only to that feature is **Not Applicable**. Record the reason in one line (“no tools are exposed”).
2. A requirement can also be Not Applicable when its own precondition is false, even if the parent tag is in scope. Examples: 6.12 when no tool executes code; 6.15 when agents do not exchange messages; 5.20 when prompts never leave the organization’s trust boundary; 7.5 when no artifact can deserialize arbitrary code.
3. A requirement the system must meet and does not meet is **Fail**. “We do not do retrieval, so 4.3 is not applicable” is valid. “We do retrieval, but 4.3 is hard” is a fail.
4. **Pass** requires the evidence described under the chapter. A vendor questionnaire or a scanner report alone is not a pass. That rule is unchanged from 2.0.

## Relationship to other OWASP documents

LLMSVS is the pass/fail catalog for controls that exist because the system uses a model. The OWASP Top 10 for LLM Applications and the OWASP Top 10 for Agentic Applications are awareness lists. Cheat sheets describe implementation techniques. The OWASP Application Security Verification Standard covers the rest of the application, including ordinary authentication, session management, and web-service security. A mapping from this draft to the 2026 lists is in [mappings/crosswalk.md](mappings/crosswalk.md). The ASVS citations below are the illustrative ones already published in LLMSVS 2.0; they are not a new clause-by-clause audit of ASVS 5.0.0.

Profiles for a chat assistant, a retrieval system, an agent, and a fine-tune pipeline are in [profiles/](profiles/). A sample assessment with pass, fail, and not applicable is in [examples/worked-assessment.md](examples/worked-assessment.md).

## Assessment

OWASP does not certify LLMSVS assessments. An open-book review is the expected method: access to architects, source, configuration, and one account per role that the level claims to cover. The report lists the chosen level, the features in scope, every requirement as pass, fail, or not applicable, and enough evidence for a second person to repeat the conclusion.

***

## Front matter carried forward

### About the standard

The Large Language Model Security Verification Standard is a list of AI and LLM security requirements that architects, developers, testers, security professionals, tool vendors, and consumers can use to define, build, test, and verify LLM-backed applications.

### Copyright and license

Copyright © 2024–2026 The OWASP Foundation. This draft is released under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

### Project leads

- Vandana Verma Sehgal
- Elliot Ward

### Other contributors and reviewers

The 0.1 credit list is preserved here so the draft does not drop it. Names missing from that list should be added through a GitHub issue.

| Name | Organization |
| ---- | ------------ |
| Eric Allen | Lakera |
| Frawa Vetterli | Lakera |
| Rory McNamara | Snyk |
| Raul Onitza-Klugman | Snyk |
| Moshe Ben-Nehemia | Snyk |
| Sam Watts | Lakera |

The standard is built on research performed by the Snyk Security Labs team in 2023. Structure and assessment practice are adapted from the OWASP ASVS project.

### Supporter note

Snyk supported the original requirements work. Lakera reviewed an early draft of the 0.1 text. See [SUPPORTERS.md](SUPPORTERS.md).

***

<!-- Requirement tables below are kept in step with catalog/llmsvs-draft.json. -->

## V1. Secure configuration and maintenance

### Control objective

Deployed LLM systems are known, their credentials are protected, self-hosted runtimes are isolated and patched, and changes to prompts, models, tools, and corpora follow the application change process.

| # | Requirement | Applies | L1 | L2 | L3 |
| --- | --- | --- | --- | --- | --- |
| 1.1 | Verify that credentials for model providers, vector stores, and other LLM-system dependencies are stored in the organization's secret-management control and are not embedded in source, prompts, or client-side code. | `api`, `self-host`, `retrieval`, `agent` | ✓ | ✓ | ✓ |
| 1.2 | Verify that self-hosted model services are not reachable from untrusted networks except through an explicitly approved path. | `self-host` |  | ✓ | ✓ |
| 1.3 | Verify that a current inventory lists every deployed model, prompt template, tool, and retrieval corpus, each with an owner and a version. | `api`, `self-host`, `retrieval`, `memory`, `training`, `agent` | ✓ | ✓ | ✓ |
| 1.4 | Verify that the configuration of the LLM system is reviewed on a defined schedule and that each review is recorded. | `api`, `self-host`, `retrieval`, `agent` |  |  | ✓ |
| 1.5 | Verify that self-hosted model runtimes and their serving software are patched on the organization's defined cycle. | `self-host` |  | ✓ | ✓ |
| 1.6 | Verify that changes to deployed prompt templates, model versions, tool definitions, and retrieval corpora are reviewed, versioned, and reversible under the same change process as application code. | `api`, `self-host`, `retrieval`, `training`, `agent` |  | ✓ | ✓ |

### Verification notes

- **1.1** Show the secret store entry and a repository or image scan with no live provider keys. This was Level 2 in v2.0.
- **1.2** Network policy or firewall rules for the inference service, plus a reachability check from an untrusted segment.
- **1.3** The inventory and a spot-check against what is actually deployed. Patching of self-hosted runtimes is 1.5. This row was Level 3 in v2.0 and included patching.
- **1.4** The schedule and the latest review record, including what was changed.
- **1.5** New in this draft. Patch records for the inference stack matched to the inventory in 1.3.
- **1.6** New in this draft. A change record for a recent prompt, model, tool, or corpus update, including who approved it and how it can be rolled back.

***

## V2. Model lifecycle

### Control objective

Organizations that train or fine-tune models control the data, the weights, and the decision to deploy. If the organization does not train or fine-tune, this chapter is Not Applicable except for 2.9, 2.10, 2.18, and 2.19 when it loads weights itself (those rows also carry the self-host tag).

| # | Requirement | Applies | L1 | L2 | L3 |
| --- | --- | --- | --- | --- | --- |
| 2.1 | Verify that training and fine-tuning follow a documented secure development process with an owner for each stage from data collection through deployment. | `training` |  | ✓ | ✓ |
| 2.2 | Verify that the task, the users, and the data sources of a model are recorded before training or fine-tuning starts. | `training` |  | ✓ | ✓ |
| 2.3 | Verify that each training or fine-tuning dataset has a recorded source and is checked for untrusted or malicious content before use. | `training` | ✓ | ✓ | ✓ |
| 2.4 | Verify that training datasets cannot be modified by parties who are not authorized to change them after acquisition. | `training` |  | ✓ | ✓ |
| 2.5 | Verify that the origin of each training dataset and base model is recorded and retained with the model. | `training` |  | ✓ | ✓ |
| 2.6 | Verify that cleaning and other modifications to training data are recorded with the author, the change, and the time. | `training` |  | ✓ | ✓ |
| 2.7 | Withdrawn from the verification catalog. | — |  |  |  |
| 2.8 | Verify that training and fine-tuning data are scanned for sensitive data, and that data which must not be memorized is removed before training. | `training` | ✓ | ✓ | ✓ |
| 2.9 | Verify that foundation and pre-trained weights are obtained from an approved source and stored so that unauthorized parties cannot replace them. | `training`, `self-host` | ✓ | ✓ | ✓ |
| 2.10 | Verify that weights are loaded from a format that cannot deserialize arbitrary code, or that any exception is pinned to a digest, scanned, and recorded before load. | `training`, `self-host` | ✓ | ✓ | ✓ |
| 2.11 | Withdrawn from the verification catalog. | — |  |  |  |
| 2.12 | Verify that the regulations which apply to the training data are identified in a record, and that the training environment matches that record. | `training` |  | ✓ | ✓ |
| 2.13 | Verify that each trained or fine-tuned model has a machine-learning bill of materials covering the base model, datasets, and training code. | `training` |  | ✓ | ✓ |
| 2.14 | Withdrawn from the verification catalog. | — |  |  |  |
| 2.15 | Withdrawn from the verification catalog. | — |  |  |  |
| 2.16 | Verify that recorded tests cover prompt injection and sensitive-data extraction for a trained or fine-tuned model's intended use before that model is approved for deployment. | `training` |  | ✓ | ✓ |
| 2.17 | Verify that a recorded security assessment, including the risks the owner has accepted, is completed before a trained or fine-tuned model is deployed. | `training` |  | ✓ | ✓ |
| 2.18 | Verify that retired models have their weights and unneeded training data removed or access-revoked so they cannot be loaded or queried. | `training`, `self-host` |  | ✓ | ✓ |
| 2.19 | Verify that base models, adapters, and datasets used for training or for self-hosted inference are pinned to a digest, and that the digest is checked before use. | `training`, `self-host` |  | ✓ | ✓ |
| 2.20 | Verify that fine-tunes and adapters are covered by the same source, scan, and digest controls as the base model they modify. | `training` |  | ✓ | ✓ |

### Verification notes

- **2.1** The process description and the owner named for the current model.
- **2.2** The pre-training record for the model under test.
- **2.3** Source record and the check performed on the dataset used for the current model.
- **2.4** Access control on the dataset store and a write-audit sample.
- **2.5** The provenance record attached to the model. This was Level 3 in v2.0.
- **2.6** The modification log for the dataset. This was Level 3 in v2.0.
- **2.7** License and copyright review of datasets remains a legal task. It is not a security verification requirement. v2.0 required it at Level 1.
- **2.8** The scan result and what was removed. This was Level 2 in v2.0.
- **2.9** The approved source and the access control on the weight store.
- **2.10** The format in use. For an exception, the digest, the scan record, and the approval.
- **2.11** Fine-tuning to drop irrelevant data is a model-quality activity. v2.0 placed it at Level 2.
- **2.12** The regulatory record and where the training job ran.
- **2.13** The bill of materials for the model under test. This was Level 3 in v2.0.
- **2.14** Watermarking model output is not a verification requirement. Teams that need attribution can document a provenance signal in their own program. v2.0 listed watermarking as a Level 3 consideration.
- **2.15** Bias and fairness testing belongs in a trustworthy-AI program. It is out of scope for this security catalog. v2.0 required fairness tooling at Level 2.
- **2.16** The test record and the approval that depended on it. Release tests for applications that do not train are 5.23.
- **2.17** The assessment and the acceptance record. This was Level 3 in v2.0 and mixed in ethical and operational risk.
- **2.18** A retired model from the inventory and proof it can no longer be served. This was Level 3 in v2.0.
- **2.19** New in this draft. The recorded digest and the check in the load or training path.
- **2.20** New in this draft. An adapter or fine-tune in the inventory with the same provenance fields as its base model.

***

## V3. Online learning

### Control objective

Production weights do not change from live user data unless that path is approved and controlled. If weights are not updated from live traffic, every requirement in this chapter is Not Applicable. Conversation memory and retrieval are chapters V4 and V5, not this chapter.

| # | Requirement | Applies | L1 | L2 | L3 |
| --- | --- | --- | --- | --- | --- |
| 3.1 | Verify that online weight updates from live user interactions are explicitly approved and documented before they are enabled. | `online` | ✓ | ✓ | ✓ |
| 3.2 | Verify that samples retained from online learning are redacted of secrets and are readable only by the team that operates the learning process. | `online` |  | ✓ | ✓ |
| 3.3 | Verify that operators can stop online learning and stop serving the updated model without a new release of the surrounding application. | `online` |  | ✓ | ✓ |
| 3.4 | Verify that interactions used for online learning are reviewed on a defined schedule for attempts to steer the model. | `online` |  | ✓ | ✓ |
| 3.5 | Verify that an online weight update does not serve production traffic until a person approves that update. | `online` |  | ✓ | ✓ |

### Verification notes

- **3.1** The approval record. If online learning is disabled, mark the whole chapter Not Applicable instead of passing 3.1. v2.0 asked only for terms of use.
- **3.2** A retained sample and the access policy. Do not satisfy this row by logging every raw prompt. Security logging is 8.3.
- **3.3** The stop procedure and a record of a test or a real use. This was Level 3 in v2.0.
- **3.4** The latest review record. This was Level 3 in v2.0.
- **3.5** The approval gate in the learning pipeline. v2.0 said "consider" and placed it at Level 3.

***

## V4. Model memory and retrieval

### Control objective

Memory and retrieved documents stay inside the caller's authority. Untrusted retrieved text is data, not an instruction. If the system has neither memory nor retrieval, this chapter is Not Applicable.

| # | Requirement | Applies | L1 | L2 | L3 |
| --- | --- | --- | --- | --- | --- |
| 4.1 | Verify that conversational memory returned to the model belongs to the current user and the current session boundary, and not to another user. | `memory` | ✓ | ✓ | ✓ |
| 4.2 | Verify that long-term memory is stored and read so that one user cannot retrieve or overwrite another user's records. | `memory` | ✓ | ✓ | ✓ |
| 4.3 | Verify that every document placed into the model context is one the current caller is authorized to read. | `retrieval` | ✓ | ✓ | ✓ |
| 4.4 | Verify that vector stores, embedding caches, and similar retrieval components require authentication for every consumer. | `retrieval` | ✓ | ✓ | ✓ |
| 4.5 | Verify that production retrieval components grant each consumer only the operations that consumer needs. | `retrieval` |  | ✓ | ✓ |
| 4.6 | Verify that only authorized processes can add or replace documents and embeddings in a knowledge base. | `retrieval` | ✓ | ✓ | ✓ |
| 4.7 | Verify that retrieved text and other untrusted content inserted into a prompt are delimited and identified to the application as data rather than as instructions. | `retrieval`, `memory`, `agent` | ✓ | ✓ | ✓ |
| 4.8 | Verify that each addition or replacement of a document or embedding records the actor and the time. | `retrieval` |  | ✓ | ✓ |
| 4.9 | Verify that prompt caches and embedding caches cannot return one tenant's entries to another tenant. | `api`, `retrieval`, `memory` |  | ✓ | ✓ |

### Verification notes

- **4.1** A test with two users showing that one cannot read the other's prior turns.
- **4.2** The data model or query that enforces the user boundary, plus a cross-user test.
- **4.3** The retrieval query or filter that applies the caller's authorization, and a test account that does not receive another role's documents. This was Level 2 in v2.0 and was worded as leak detection.
- **4.4** Configuration showing unauthenticated access is rejected.
- **4.5** The credentials or roles used by the application, with write access absent where the application only reads.
- **4.6** The write path and a rejected attempt from an unauthorized caller.
- **4.7** New in this draft. The prompt assembly code showing the delimiter and the data marking. This row does not replace 5.18.
- **4.8** New in this draft. An audit entry for a recent update.
- **4.9** New in this draft. The cache key includes the tenant or user, and a cross-tenant request does not hit the other tenant's entry.

***

## V5. Secure LLM integration

### Control objective

The application, not the end user and not the model, decides what is trusted. Prompts are built server-side, output is validated and untrusted, hidden context is not a security boundary, and consumption is limited.

| # | Requirement | Applies | L1 | L2 | L3 |
| --- | --- | --- | --- | --- | --- |
| 5.1 | Verify that model requests are sent by a server-side component the organization controls, not by the end-user client directly to the model provider. | `api` | ✓ | ✓ | ✓ |
| 5.2 | Verify that the client cannot supply the system instructions or the full prompt that the provider receives. | `api` | ✓ | ✓ | ✓ |
| 5.3 | Withdrawn from the verification catalog. | — |  |  |  |
| 5.4 | Verify that model-provider credentials are covered by requirement 1.1 and are not placed in the prompt or the client. | `api`, `agent` | ✓ | ✓ | ✓ |
| 5.5 | Verify that model output which the application parses is validated against the expected schema before it is used, and that extra fields are rejected. | `api` | ✓ | ✓ | ✓ |
| 5.6 | Withdrawn from the verification catalog. | — |  |  |  |
| 5.7 | Withdrawn from the verification catalog. | — |  |  |  |
| 5.8 | Withdrawn from the verification catalog. | — |  |  |  |
| 5.9 | Verify that completions longer than the documented expected range raise an alert or are truncated before they are shown or acted on. | `api` |  | ✓ | ✓ |
| 5.10 | Verify that responses shown to users do not include raw provider errors, stack traces, prompts, or credentials. | `api` | ✓ | ✓ | ✓ |
| 5.11 | Verify that the application documents the check it runs on prompts and completions for suspected prompt injection, and records the cases that check is known to miss. | `api` | ✓ | ✓ | ✓ |
| 5.12 | Verify that content from retrieval, tools, third parties, earlier model output, files, images, audio, and web pages is subject to the same controls as direct user input. | `api`, `retrieval`, `memory`, `agent` | ✓ | ✓ | ✓ |
| 5.13 | Verify that model output is treated as untrusted input at every downstream sink, including queries, markup, commands, URLs, and tool arguments. | `api`, `agent` | ✓ | ✓ | ✓ |
| 5.14 | Verify that each caller has a limit on how many model requests it can make in a defined period. | `api` | ✓ | ✓ | ✓ |
| 5.15 | Verify that an alert fires when model spend passes a defined threshold. | `api` | ✓ | ✓ | ✓ |
| 5.16 | Verify that a baseline of normal model use is defined and that departures from it generate an alert. | `api` |  | ✓ | ✓ |
| 5.17 | Verify that unauthenticated or preview access can call only the model features intended for that access. | `api` |  | ✓ | ✓ |
| 5.18 | Verify that authorization, tenant separation, and other security decisions are enforced in application code and still hold if the system prompt is disclosed. | `api`, `agent` | ✓ | ✓ | ✓ |
| 5.19 | Verify that each model call enforces a maximum input size and a maximum output size. | `api` | ✓ | ✓ | ✓ |
| 5.20 | Verify that prompts sent outside the organization's trust boundary are redacted of secrets and of personal data the recipient is not approved to receive. | `api` |  | ✓ | ✓ |
| 5.21 | Verify that the provider's retention of prompts and its use of those prompts for training are documented, and that the configuration matches that decision. | `api` |  | ✓ | ✓ |
| 5.22 | Verify that model output presented as fact is either limited to supplied sources or labeled as unverified before a person or another system acts on it. | `api`, `retrieval` |  | ✓ | ✓ |
| 5.23 | Verify that release tests for the LLM feature include direct injection, indirect injection, sensitive-data extraction, and, where tools exist, unapproved tool use, and that the results are recorded. | `api`, `retrieval`, `agent`, `training` |  | ✓ | ✓ |

### Verification notes

- **5.1** Architecture or configuration showing the provider endpoint is not called from the client.
- **5.2** The request schema accepted from the client, and a rejected or ignored attempt to replace the system instructions.
- **5.3** Using more than one model provider can support availability. Put that target in the service continuity plan. v2.0 listed it as a Level 3 consideration.
- **5.4** Where the provider credential is loaded, and confirmation it is absent from prompt templates. This was Level 2 in v2.0.
- **5.5** The schema check and a sample output with an unexpected field that was rejected. Constrained decoding may sit in front of this check. It does not replace it.
- **5.6** A change in output language can be one monitoring signal under 8.1. It is not a verification requirement. v2.0 required a language match at Level 2.
- **5.7** Canary tokens are one detection technique for 8.2. They are not the control for hidden-context exposure. That control is 5.18. v2.0 listed canaries as a Level 3 consideration.
- **5.8** Entropy thresholds are an unstable detector. Obfuscated exfiltration belongs in the tests for 5.23 and the alerts for 8.2. v2.0 required an entropy check at Level 3.
- **5.9** The threshold and the alert or truncation behavior. Hard input and output caps are 5.19. This was Level 3 in v2.0.
- **5.10** A forced provider error and the message the user received. What gets logged is 8.3, not this row.
- **5.11** The control description and its known gaps. A pass here is not a pass for 5.12, 5.13, or 5.18. This was Level 2 in v2.0.
- **5.12** The path that inserts non-user content into the prompt, and the controls on that path. This was Level 2 in v2.0 and did not name files or images.
- **5.13** Each sink that consumes model output, and the parameterization, encoding, or validation in front of it.
- **5.14** The limit and a request that was rejected or queued after the limit. This was Level 2 in v2.0.
- **5.15** The threshold and the alert destination. The limit itself is 5.14 and 5.19.
- **5.16** The baseline and one alert rule. This was Level 3 in v2.0. Log contents are 8.3.
- **5.17** The feature list for an unauthenticated session and a blocked call outside it.
- **5.18** New in this draft. The code or policy that enforces the decision outside the prompt, and confirmation that secrets are not written into the prompt.
- **5.19** New in this draft. The configured maxima and a call that was rejected or truncated at the cap.
- **5.20** New in this draft. The redaction step and an example payload. Not applicable when prompts never leave the trust boundary; record that reason.
- **5.21** New in this draft. The decision record and the provider setting. Not applicable when no external provider stores prompts.
- **5.22** New in this draft. The user-facing or downstream presentation, showing citations bound to retrieved sources or an unverified label.
- **5.23** New in this draft. The latest test record tied to a release. Training-specific tests before model approval remain 2.16.

***

## V6. Agents and tools

### Control objective

Tools run with the least authority that the current task needs, their definitions cannot change unnoticed, sensitive actions are approved as concrete calls, and a run cannot loop without a limit. If the model cannot call tools, this chapter is Not Applicable.

| # | Requirement | Applies | L1 | L2 | L3 |
| --- | --- | --- | --- | --- | --- |
| 6.1 | Verify that a task can call only the tools required for that task, and cannot call tools registered for a different task. | `agent` | ✓ | ✓ | ✓ |
| 6.2 | Verify that custom tools are built under the same secure development process as the rest of the application. | `agent` |  | ✓ | ✓ |
| 6.3 | Verify that third-party tools and toolkits are approved through the organization's third-party risk process before use. | `agent` |  | ✓ | ✓ |
| 6.4 | Verify that tool arguments are validated for type and for allowed values before the tool runs. | `agent` | ✓ | ✓ | ✓ |
| 6.5 | Verify that credentials used by tools are covered by requirement 1.1. | `agent` | ✓ | ✓ | ✓ |
| 6.6 | Verify that the agent runtime can hand raw prompts, tool calls, and tool results to the organization's monitoring and injection checks. | `agent` |  | ✓ | ✓ |
| 6.7 | Verify that a tool cannot read or change data the current user is not allowed to read or change. | `agent` | ✓ | ✓ | ✓ |
| 6.8 | Verify that the host which runs tools cannot reach internal services that the tools do not need. | `agent` |  | ✓ | ✓ |
| 6.9 | Verify that the host which runs tools can open outbound connections only to approved destinations. | `agent` |  | ✓ | ✓ |
| 6.10 | Verify that each tool credential is scoped to the minimum operations that tool performs. | `agent` | ✓ | ✓ | ✓ |
| 6.11 | Verify that a person approves the tool name and arguments of each sensitive or irreversible action before that action runs. | `agent` |  | ✓ | ✓ |
| 6.12 | Verify that tools which execute code or shell commands run in an environment that does not share the application filesystem or the application credentials. | `agent` |  | ✓ | ✓ |
| 6.13 | Verify that tool definitions and remote tool servers, including Model Context Protocol servers, are pinned, and that a change to the description, endpoint, or schema is reviewed before use. | `agent` | ✓ | ✓ | ✓ |
| 6.14 | Verify that credentials the agent uses on its own behalf are distinct from the end user's credentials, and that the agent cannot exercise the user's authority beyond the current approved task. | `agent` |  | ✓ | ✓ |
| 6.15 | Verify that messages accepted from another agent are authenticated and checked for integrity. | `agent` |  | ✓ | ✓ |
| 6.16 | Verify that a run stops when it reaches a documented limit on tool-call count or on fan-out to other agents or tools. | `agent` | ✓ | ✓ | ✓ |
| 6.17 | Verify that operators can stop an agent and block further actions when its tool use leaves the approved baseline. | `agent` |  | ✓ | ✓ |

### Verification notes

- **6.1** The tool list bound to each task, and a test where one task attempts to call another's tool.
- **6.2** The process used for a custom tool, including review and dependency checks.
- **6.3** The approval record for each third-party tool in the inventory.
- **6.4** The validator and a rejected argument outside the allowed set. This was Level 2 in v2.0.
- **6.5** Where tool credentials are loaded. This was Level 2 in v2.0.
- **6.6** The hook or middleware and a log or check that received a tool call.
- **6.7** An authorization check inside the tool or its gateway, tested with a user who lacks the permission. This was Level 2 in v2.0.
- **6.8** Network policy for the tool host. This was Level 3 in v2.0.
- **6.9** Egress policy and a blocked connection to an unapproved destination. This was Level 3 in v2.0.
- **6.10** The permission set on a tool credential compared with the operations the tool implements. This was Level 2 in v2.0.
- **6.11** An approval record that contains the tool name and arguments, not only the model's summary of the action. v2.0 said "consider" and placed this at Level 3.
- **6.12** The sandbox boundary. Not applicable when no tool executes code; record that reason. This was Level 3 in v2.0.
- **6.13** New in this draft. The pin and the review required when the pin changes.
- **6.14** New in this draft. The two credential paths and the task boundary enforced on the user's delegated authority.
- **6.15** New in this draft. The authentication on the agent channel. Not applicable when agents do not exchange messages; record that reason.
- **6.16** New in this draft. The limit and a run that stopped at it.
- **6.17** New in this draft. The stop control and the condition that triggers it.

***

## V7. Dependencies and components

### Control objective

Models, adapters, and libraries that implement LLM features come from approved sources, are pinned, and are patched. This chapter covers the supply chain of components. Dataset and weight provenance for training also sits in V2.

| # | Requirement | Applies | L1 | L2 | L3 |
| --- | --- | --- | --- | --- | --- |
| 7.1 | Verify that software composition analysis runs against third-party components used by the LLM feature, and that known vulnerable versions in use have a recorded remediation decision. | `api`, `self-host`, `training`, `agent` |  | ✓ | ✓ |
| 7.2 | Verify that models, adapters, and libraries that implement LLM features are obtained only from sources on an approved list. | `self-host`, `training`, `agent` | ✓ | ✓ | ✓ |
| 7.3 | Verify that a documented patch process covers third-party components used by the LLM feature. | `api`, `self-host`, `training`, `agent` |  | ✓ | ✓ |
| 7.4 | Verify that a software bill of materials lists the third-party components, licenses, and versions used by the LLM feature. | `api`, `self-host`, `training`, `agent` |  | ✓ | ✓ |
| 7.5 | Verify that any model artifact capable of deserializing arbitrary code is scanned before load and the scan result is recorded. | `self-host`, `training` | ✓ | ✓ | ✓ |
| 7.6 | Verify that private package registries used for LLM components are configured so a public package of the same name cannot be substituted. | `self-host`, `training`, `agent` |  | ✓ | ✓ |
| 7.7 | Verify that model files are rejected at load time when their digest does not match the recorded value. | `self-host`, `training` |  | ✓ | ✓ |

### Verification notes

- **7.1** The latest analysis report and the decision for any vulnerable component still present.
- **7.2** The approved-source list and the source of the components in the inventory.
- **7.3** The process and a recent patch or an accepted exception.
- **7.4** The bill of materials for the build under test.
- **7.5** The scan record. Not applicable when every artifact is in a format that cannot deserialize arbitrary code; record that reason. This was Level 2 in v2.0.
- **7.6** Registry configuration for a private package name. Not applicable when no private registry is used.
- **7.7** New in this draft. A load attempt with a mismatched digest that was rejected. Recording the digest is 2.19.

***

## V8. Monitoring and response

### Control objective

Operators can see which model, prompt version, caller, tools, and documents were involved, without collecting secrets, and they have a response path when that activity is abused.

| # | Requirement | Applies | L1 | L2 | L3 |
| --- | --- | --- | --- | --- | --- |
| 8.1 | Verify that usage of the LLM feature is monitored for departures from the expected volume and output pattern, and that those departures alert. | `api` |  | ✓ | ✓ |
| 8.2 | Verify that alerts exist for suspected prompt leakage, unexpected tool use, and model cost above the defined threshold. | `api`, `agent` |  | ✓ | ✓ |
| 8.3 | Verify that security logs for each model call record the model identity, prompt-template version, caller, tool names, and retrieval-document identifiers, and omit secrets and raw sensitive prompt or completion text. | `api` | ✓ | ✓ | ✓ |
| 8.4 | Verify that LLM security logs are retained for a documented period and cannot be changed by the application role that writes them. | `api` |  | ✓ | ✓ |
| 8.5 | Verify that the incident process describes the response to a prompt-injection campaign, poisoning of retrieved or training data, tool abuse, and unplanned model cost. | `api`, `retrieval`, `training`, `agent` |  | ✓ | ✓ |

### Verification notes

- **8.1** The monitor and a sample alert. The baseline definition may be the same artifact as 5.16; do not require two unrelated systems.
- **8.2** The three alert definitions or a documented combined signal. Canary tokens are optional and are not required to pass this row.
- **8.3** New in this draft. A log line for a call that included a tool or a retrieved document, and confirmation that a known secret in the test prompt was not written.
- **8.4** New in this draft. Retention setting and the permission boundary between the application and the log store.
- **8.5** New in this draft. The incident process sections that name those four cases. A case that cannot occur because the feature is absent may be omitted; record that.

***

## Appendix A: Requirement changes in this draft

New identifiers: 1.5, 1.6, 2.19, 2.20, 4.7, 4.8, 4.9, 5.18, 5.19, 5.20, 5.21, 5.22, 5.23, 6.13, 6.14, 6.15, 6.16, 6.17, 7.7, 8.3, 8.4, 8.5.

Withdrawn identifiers, which must not be reused: 2.7, 2.11, 2.14, 2.15, 5.3, 5.6, 5.7, 5.8.

Active identifiers keep their v2.0 numbers. Verification notes record where the level or the obligation changed. The full crosswalk to the 2026 Top 10 lists is in [mappings/crosswalk.md](mappings/crosswalk.md).

## Appendix B: Guidance that is not verified

These items were requirements or “consider” rows in v2.0. They are not pass/fail rows in this draft.

- **2.7** License and copyright review of datasets remains a legal task. It is not a security verification requirement. v2.0 required it at Level 1.
- **2.11** Fine-tuning to drop irrelevant data is a model-quality activity. v2.0 placed it at Level 2.
- **2.14** Watermarking model output is not a verification requirement. Teams that need attribution can document a provenance signal in their own program. v2.0 listed watermarking as a Level 3 consideration.
- **2.15** Bias and fairness testing belongs in a trustworthy-AI program. It is out of scope for this security catalog. v2.0 required fairness tooling at Level 2.
- **5.3** Using more than one model provider can support availability. Put that target in the service continuity plan. v2.0 listed it as a Level 3 consideration.
- **5.6** A change in output language can be one monitoring signal under 8.1. It is not a verification requirement. v2.0 required a language match at Level 2.
- **5.7** Canary tokens are one detection technique for 8.2. They are not the control for hidden-context exposure. That control is 5.18. v2.0 listed canaries as a Level 3 consideration.
- **5.8** Entropy thresholds are an unstable detector. Obfuscated exfiltration belongs in the tests for 5.23 and the alerts for 8.2. v2.0 required an entropy check at Level 3.

## Appendix C: Glossary

Terms used by the requirements. Textbook machine-learning definitions are left to other references.

- **Applicability tag** — A label for a feature (`api`, `self-host`, `retrieval`, `memory`, `training`, `online`, `agent`). Requirements carry one or more tags. Absent features are Not Applicable.
- **Hidden context** — System instructions, tool schemas, policy text, and other operational context placed in the model window and not intended for the end user. LLMSVS treats it as discoverable. See requirement 5.18.
- **Indirect prompt injection** — Untrusted content that reaches the model other than as the current user message, including retrieved documents, tool results, files, images, and web pages.
- **Large language model (LLM)** — A model that takes tokenized input and produces a completion used by an application.
- **Model Context Protocol (MCP)** — A protocol for connecting a model client to remote tool and resource servers. In this standard, an MCP server is a remote tool server under chapter V6.
- **Not Applicable** — An assessment result used when the feature or the requirement’s precondition is absent. The report records the reason.
- **Online learning** — Updates to production model weights driven by live user data. Distinct from retrieval and from conversation memory.
- **Prompt injection** — Input that causes the model to follow instructions the application did not intend.
- **Retrieval-augmented generation** — An architecture that retrieves documents or passages and places them in the model context.
- **Tool call** — A structured request from the model to run a capability outside the model. Results may re-enter the context.
