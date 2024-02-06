# V3. Real Time Learning

## Control Objective
Establish controls to reduce the risks associated with real time learning within LLM systems, where the models are continuously fine-tuned based on user interactions in real time.

| # | Requirement | L1 | L2 | L3 |
| - | ---------- | -- | -- | -- |
| 3.1 | Define clear terms of use and guidelines for interacting with the model and make users aware of acceptable and unacceptable behaviors. | ✓ | ✓ | ✓ |
| 3.2 | Ensure continuous monitoring of the model's performance and interactions. This includes logging all inputs and outputs (where appropriate, with consideration to the potential sensitivity of the data) in real time to quickly identify and address any inappropriate or unexpected behavior. |      | ✓ | ✓ |
| 3.3 | Create clear protocols for immediate intervention in case the model starts displaying undesirable behavior. This should include the ability to quickly take the system offline if necessary. |      |      | ✓ |
| 3.4 | Regularly analyze user interactions to identify and mitigate attempts to manipulate the model into inappropriate behavior. |      |      | ✓ |
| 3.5 | Consider using an incremental learning approach where the model can be updated in increments with human approval. |      |      | ✓ |
