# V7. Dependency and Component

## Control Objective
Ensure that third-party components and dependencies are safely handled to reduce supply chain risk.

| # | Requirement | L1 | L2 | L3 |
| - | ---------- | -- | -- | -- |
| 7.1 | Utilize Software Composition Analysis (SCA) tools to identify and remediate known vulnerabilities within third-party components used in LLM-powered applications. |      | ✓ | ✓ |
| 7.2 | Ensure that all third-party LLM components are acquired from a trusted source. | ✓ | ✓ | ✓ |
| 7.3 | Ensure a defined vulnerability and patch management process exists for third-party components. |      | ✓ | ✓ |
| 7.4 | Ensure that a Software Bill of Materials (SBOM) exists cataloging third-party components, licenses, and versions. |      | ✓ | ✓ |
| 7.5 | Where unsafe PyTorch models are required, ensure the model is scanned for potentially dangerous Python imports. |      | ✓ | ✓ |
| 7.6 | When hosting LLM components within private package registries, ensure the setup is not susceptible to Dependency Confusion attacks. |      | ✓ | ✓ |
