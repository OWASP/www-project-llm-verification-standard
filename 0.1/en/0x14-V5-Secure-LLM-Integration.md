# V5. Secure LLM Integration

## Control Objective
Establish controls that enable safe interactions and operations between application components and LLMs. 

| # | Requirement | L1 | L2 | L3 |
| - | ---------- | -- | -- | -- |
| 5.1.1 | Ensure that prompts to LLMs are issued from a trusted server-side component. | ✓ | ✓ | ✓ |
| 5.1.2 | Ensure that prompts to LLMs are constructed server-side, rather than accepting the complete prompt directly from the client. | ✓ | ✓ | ✓ |
| 5.1.3 | Ensure that user prompts are properly validated to exclude special characters, keywords, separators, etc. [\[1\]](#hou_yi), [\[2\]](#contest), [\[3\]](#struq) | ✓ | ✓ | ✓ |
| 5.1.4 | Ensure that user prompts are protected against semantic-based prompt injections, such as completion attacks, ignore attacks and important task attacks. [\[1\]](#hou_yi), [\[2\]](#contest), [\[4\]](#ign_prev_prompt), [\[5\]](#agent_dojo) | ✓ | ✓ | ✓ |
| 5.1.5 | Ensure that user-supplied URLs undergo safety checks to prevent indirect prompt injection. [\[6\]](#greshake_et_al), [\[7\]](#real_world_llm_sec) | ✓ | ✓ | ✓ |
| 5.1.6 | Ensure that proper protections are in place to prevent meta-prompt leakage, e.g. canary tokens, guardrails, input and output filtering, etc. [\[8\]](#nemo_guardrails) |   | ✓ | ✓ |
| 5.1.7 | Ensure that appropriate LLM guards are used to scan prompts and compilations to help detect potential prompt injection attacks. |      | ✓ | ✓ |
| 5.1.8 | Ensure that prompts are scanned for suspicious, harmful or banned sequences of words. [\[1\]](#hou_yi), [\[7\]](#real_world_llm_sec), [\[9\]](#context_inj) |    | ✓ | ✓ |

## V5.2 Context Security

This section deals primarily with defenses against context injection attacks. In context injection attacks, an entire context is fed to the LLM, rather than a single prompt. Reference for all requirements: [\[9\]](#context_inj)

| # | Requirement | L1 | L2 | L3 |
| - | ---------- | -- | -- | -- |
| 5.2.1 | Ensure that the application protects user context against word anonymization (replacing harmful/banned words with other words). | ✓ | ✓ | ✓ |
| 5.2.2 | Ensure that the application protects user context from acceptance elicitation attacks, i.e. the LLM should not accept users' claims about previously received messages from the LLM. | ✓ | ✓ | ✓ |
| 5.2.3 | Ensure that chat histories are stored server-side and their integrity is regularly verified. |    |    | ✓ |
| 5.2.4 | Check that inputs from various sources, e.g. user, system, administrator, are segregated from each other and do not influence one another. |    |    | ✓ |

## V5.3 LLM Access Control

This section deals with proper access controls to and from the LLM module in an application.

| # | Requirement | L1 | L2 | L3 |
| - | ---------- | -- | -- | -- |
| 5.3.1 | Ensure that the output of LLM completions is considered to be untrusted by any subsequent system. For example, if using the LLM response within a SQL query, the query should not be constructed by concatenating parts of the LLM response but should follow section V5.3.4 of the OWASP ASVS and use parmeterized queries. | ✓ | ✓ | ✓ |
| 5.3.2 | Ensure that all prompts are considered to be untrusted and subjected to any deployed security controls. Reflecting stored data, data from third-party APIs, or the response from previous prompt compilations may lead to indirect prompt injections and must be subjected to the same controls as prompts containing direct user input. |      | ✓ | ✓ |
| 5.3.3 | Ensure that the principle of least privilege is respected with respect to the LLM's internal APIs, functions and network access. [\[10\]](#portswigger), [\[11\]](#ahom) |      | ✓ | ✓ |
| 5.3.4 | Ensure any functionality that allows anonymous users to preview features is properly restricted to allow only the necessary features. |      | ✓ | ✓ |
| 5.3.5 | Ensure that credentials for LLM providers are securely handled according to section V2.10 “Service Authentication” of the OWASP ASVS. |      | ✓ | ✓ |
| 5.3.6 | Consider the use of redundant LLM accounts and providers to avoid single points of failure and ensure application availability. |      |      | ✓ |

## V5.4 LLM Output Security

This section deals with protecting and monitoring the output of the LLM module.

| # | Requirement | L1 | L2 | L3 |
| - | ---------- | -- | -- | -- |
| 5.4.1 | Ensure that the output format and properties of the data returned from the LLM match the expected structure and properties. Specifically, when a response is expected in JSON, the result should not only be in valid JSON format, but also undergo schema validation to ensure it contains all the expected JSON fields and does not include any unnecessary or extraneous properties. | ✓ | ✓ | ✓ |
| 5.4.2 | Ensure that the application properly suppresses any exceptions and error messages when interacting with the LLM. LLM errors may inadvertently leak the prompt and should not be visible to the client. | ✓ | ✓ | ✓ |
| 5.4.3 | Ensure that LLM output is scanned for suspicious, harmful or banned content. [\[7\]](#real_world_llm_sec), [\[9\]](#context_inj) |    | ✓ | ✓ |
| 5.4.4 | Ensure that the output language of the LLM response matches the expected language. |      | ✓ | ✓ |
| 5.4.5 | Perform length checks on LLM completions to verify that the response length is within an expected range. For example, a response that is significantly longer than the normal output length might indicate the completion is including additional, unexpected data. |      |      | ✓ |
| 5.4.6 | Check the entropy of LLM responses to detect encoded data which aims to circumvent additional checks, such as bypassing canary tokens. |      |      | ✓ |

## V5.5 Cost Control

This section deals with ensuring that LLM costs stay within appropriate limits.

| # | Requirement | L1 | L2 | L3 |
| - | ---------- | -- | -- | -- |
| 5.5.1 | Ensure that cost alerts are active within LLM provider configurations to be alerted when costs exceed expectations. | ✓ | ✓ | ✓ |
| 5.5.2 | Ensure that systems that result in LLM calls have appropriate API rate limiting to avoid excessive calls to LLMs, which may result in unexpected and excessive LLM costs. |      | ✓ | ✓ |
| 5.5.3 | Ensure that the LLM is not able to perform computationally heavy tasks. [\[12\]](#taxonomy) |      | ✓ | ✓ |

## References

<a id="hou_yi">\[1\] https://arxiv.org/pdf/2306.05499</a>

<a id="contest">\[2\] https://arxiv.org/pdf/2311.16119</a>

<a id="struq">\[3\] https://arxiv.org/pdf/2402.06363</a>

<a id="ign_prev_prompt">\[4\] Ignore Previous Prompt attacks: https://arxiv.org/pdf/2211.09527</a>

<a id="agent_dojo">\[5\] https://arxiv.org/pdf/2406.13352</a>

<a id="greshake_et_al">\[6\] https://arxiv.org/pdf/2302.12173</a>

<a id="real_world_llm_sec">\[7\] https://arxiv.org/pdf/2402.18649</a>

<a id="nemo_guardrails">\[8\] https://github.com/NVIDIA/NeMo-Guardrails</a>

<a id="context_inj">\[9\] https://arxiv.org/pdf/2405.20234v1</a>

<a id="portswigger">\[10\] https://portswigger.net/web-security/llm-attacks#exploiting-llm-apis-functions-and-plugins</a>

<a id="ahom">\[11\] https://cybersecurity.ahomcybersecurity.xyz/readme/web-app-pentesting-notes/llm-attacks/exploiting-llm-apis-functions-and-plugins</a>

<a id="taxonomy">\[12\] https://arxiv.org/pdf/2311.11415</a>