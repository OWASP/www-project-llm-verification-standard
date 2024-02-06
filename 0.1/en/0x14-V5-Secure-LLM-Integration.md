# V5. Secure LLM Integration

## Control Objective
Establish controls that enable safe interactions and operations between application components and LLMs. 

| # | Requirement | L1 | L2 | L3 |
| - | ---------- | -- | -- | -- |
| 5.1 | Ensure that prompts to LLMs are issued from a trusted server-side component. | ✓ | ✓ | ✓ |
| 5.2 | Ensure that prompts to LLMs are constructed server-side, rather than accepting the complete prompt directly from the client. | ✓ | ✓ | ✓ |
| 5.3 | Consider the use of redundant LLM accounts and providers to avoid single points of failure and ensure application availability. |      |      | ✓ |
| 5.4 | Ensure that credentials for LLM providers are securely handled according to section V2.10 “Service Authentication” of the OWASP ASVS. |      | ✓ | ✓ |
| 5.5 | Ensure that the output format and properties of the data returned from the LLM match the expected structure and properties. Specifically, when a response is expected in JSON, the result should not only be in valid JSON format, but also undergo schema validation to ensure it contains all the expected JSON fields and does not include any unnecessary or extraneous properties. | ✓ | ✓ | ✓ |
| 5.6 | Ensure that the output language of the LLM response matches the expected language. |      | ✓ | ✓ |
| 5.7 | Consider using canary tokens in LLM prompts and check whether LLM completions contain the canary word to detect prompt leakage attacks. |      |      | ✓ |
| 5.8 | Check the entropy of LLM responses to detect encoded data which aims to circumvent additional checks, such as bypassing canary tokens. |      |      | ✓ |
| 5.9 | Perform length checks on LLM completions to verify that the response length is within an expected range. For example, a response that is significantly longer than the normal output length might indicate the completion is including additional, unexpected data. |      |      | ✓ |
| 5.10 | Ensure that the application properly suppresses any exceptions and error messages when interacting with the LLM. LLM errors may inadvertently leak the prompt and should not be visible to the client. | ✓ | ✓ | ✓ |
| 5.11 | Ensure that appropriate LLM guards are used to scan prompts and compilations to help detect potential prompt injection attacks. |      | ✓ | ✓ |
| 5.12 | Ensure that all prompts are considered to be untrusted and subjected to any deployed security controls. Reflecting stored data, data from third-party APIs, or the response from previous prompt compilations may lead to indirect prompt injections and must be subjected to the same controls as prompts containing direct user input. |      | ✓ | ✓ |
| 5.13 | Ensure that the output of LLM completions is considered to be untrusted by any subsequent system. For example, if using the LLM response within a SQL query, the query should not be constructed by concatenating parts of the LLM response but should follow section V5.3.4 of the OWASP ASVS and use parmeterized queries. | ✓ | ✓ | ✓ |
| 5.14 | Ensure that systems that result in LLM calls have appropriate API rate limiting to avoid excessive calls to LLMs, which may result in unexpected and excessive LLM costs. |      | ✓ | ✓ |
| 5.15 | Ensure that cost alerts are active within LLM provider configurations to be alerted when costs exceed expectations. | ✓ | ✓ | ✓ |
| 5.16 | Define baselines for normal LLM interactions and monitor and alert when abnormal LLM interactions are detected.  |      |      | ✓ |
| 5.17 | Ensure any functionality that allows anonymous users to preview features is properly restricted to allow only the necessary features. |      | ✓ | ✓ |
