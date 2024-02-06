# V4. Model Memory and Storage

## Control Objective
Ensure that mechanisms which allow for “memory” or additional knowledge that was not included in the training phase is safely handled. 

| # | Requirement | L1 | L2 | L3 |
| - | ---------- | -- | -- | -- |
| 4.1 | Ensure that mechanisms that implement “Conversational memory” do not mistakenly mix up prior prompts for other users. | ✓ | ✓ | ✓ |
| 4.2 | Ensure that mechanisms which support “long-term” storage appropriately segregate user data to ensure it is not possible to retrieve data pertaining to other users, or inject false records for other users. | ✓ | ✓ | ✓ |
| 4.3 | Ensure that controls exist to detect leakage of sensitive data from internal knowledge bases provided as additional context to the LLM. It should not be possible to coerce the LLM into leaking the contents of the knowledge base. |      | ✓ | ✓ |
| 4.4 | Ensure that external storage components such as vector databases and caches require authentication for consumers. | ✓ | ✓ | ✓ |
| 4.5 | Enforce the principle of least privilege for accessing production storage components, such as vector databases and caches. |      | ✓ | ✓ |
| 4.6 | When updating embeddings within a knowledge base, ensure that an adversary is not able to inject arbitrary documents or otherwise insert false information into the knowledge base. | ✓ | ✓ | ✓ |
