# V1. Secure Configuration and Maintenance

## Control Objective
Ensure that LLMs, hosted by a model provider or self-hosted, are configured and maintained securely to prevent unauthorized access and leakage of sensitive information.

| # | Requirement | L1 | L2 | L3 |
| - | ---------- | -- | -- | -- |
| 1.1 | Identify any components that store secrets, like API keys, for third-party systems, like hosted LLMs and vector databases, and ensure the secure handling of these credentials according to section V2.10 “Service Authentication” of the OWASP ASVS. |      | ✓ | ✓ |
| 1.2 | For self-hosted LLMs, ensure they are appropriately segregated within the network to prevent direct exposure to end-users unless such access is required. |      | ✓ | ✓ |
| 1.3 | Maintain an up-to-date inventory of all LLM instances and apply regular updates and patches to self-hosted models. |      |      | ✓ |
| 1.4 | Perform and document regular configuration reviews for configuration settings associated with the LLM-powered system.  |      |      | ✓ |
