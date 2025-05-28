# V2. Model Lifecycle

## Control Objective
Ensure that the Machine Learning (ML) lifecycle for models used within LLM-powered systems considers the various security threats from dataset curation, model training, and validation.  

## V2.1 Training Data Security

Measures for securing the LLM's training data.

| # | Requirement | L1 | L2 | L3 |
| - | ---------- | -- | -- | -- |
| 2.1.1 | Ensure that model training resources and datasets are acquired from trustworthy sources and validated for correctness or free from malicious data.  | ✓ | ✓ | ✓ |
| 2.1.2 | Ensure that the intellectual property rights of model training resources and datasets are checked to avoid potential license or copyright infringement issues. Ensure this process is documented and auditable. | ✓ | ✓ | ✓ |
| 2.1.3 | Ensure that model training resources are audited for sensitive data (such as PII, internal company data, etc.) and cleaned before training to mitigate sensitive data exposure in model responses. |      | ✓ | ✓ |
| 2.1.4 | Ensure that model training resources and datasets are properly secured from unauthorized modification once acquired. |      | ✓ | ✓ |
| 2.1.5 | Ensure that the source of any training resources and datasets is documented. |      |      | ✓ |
| 2.1.6 | Ensure that any data cleaning or other modifications to the original training resources are tracked and auditable to reduce the risk of data poisoning from an insider threat. |      |      | ✓ |

## V2.2 Lifecycle Planning

Ensure that the LLM's lifecycle is planned while taking security considerations into account.

| # | Requirement | L1 | L2 | L3 |
| - | ---------- | -- | -- | -- |
| 2.2.1 | Check regulatory obligations to ensure compliance when handling and processing model training data. |      | ✓ | ✓ |
| 2.2.2 | Ensure that foundational models are fine-tuned to limit irrelevant data points which may lead to poor model performance. -> Don't see security relevance. Remove? |      | ✓ | ✓ |
| 2.2.3 | Ensure that the LLM is regularly fine-tuned to incorporate defenses against the most recent vulnerabilities, e.g. new prompt or context inejction techniques. [\[1\]](#fine_tune_def) |      | ✓ | ✓ |
| 2.2.4 | Ensure that the LLM is fine-tuned to only output verified and truthful information. [\[1\]](#fine_tune_def) |      | ✓ | ✓ |
| 2.2.5 | Ensure that a ML Bill-of-Materials (BOM) is produced for each model. |      |      | ✓ |
| 2.2.6 | Consider watermarking techniques for model responses when model theft is a concern, or the output of the model needs to be identifiable. |      |      | ✓ |
| 2.2.7 | Before a model is finalized for deployment, conduct a thorough risk assessment to understand potential security, ethical, and operational risks. This assessment should guide the decision-making process regarding the deployment of the model. |      |      | ✓ |
| 2.2.8 | Consider implementing a clear plan for decommissioning models that are no longer in use. This includes securely erasing data, model parameters, and any sensitive information associated with the model to prevent unauthorized access or misuse. |      |      | ✓ |

## V2.3 Integration of Model Lifecycle into Secure Software Development Lifecycle

Ensure that planning out the LLM lifecycle is in line with and taken into account within the organization's Secure Software Development Lifecycle (SSDLC).

| # | Requirement | L1 | L2 | L3 |
| - | ---------- | -- | -- | -- |
| 2.3.1 | Ensure that the lifecycle of machine learning models is integrated into the existing Secure Software Development Lifecycle (SSDLC). Defined processes should exist and be available for each stage of the lifecycle of ML models. |      | ✓ | ✓ |
| 2.3.2 | Document user stories defining the requirements and use cases for any new ML model being produced. |      | ✓ | ✓ |

## V2.4 Model Storage and Tooling

Ensure that LLMs are stored in a secure manner, with additional security tooling integrated into the models.

| # | Requirement | L1 | L2 | L3 |
| - | ---------- | -- | -- | -- |
| 2.4.1 | Ensure secure acquisition and storage of foundational or pre-trained models. | ✓ | ✓ | ✓ |
| 2.4.2 | Where possible, prefer secure model formats such as SafeTensors over formats that use unsafe serialization, like PyTorch’s Pickle format. | ✓ | ✓ | ✓ |
| 2.4.3 | Ensure tooling to detect biases and ensure fairness are integrated into the ML models lifecycle. |      | ✓ | ✓ |
| 2.4.4 | Ensure security tooling to detect LLM vulnerabilities such as injection attacks, jailbreak attempts and other abuse are integrated into the ML model's lifecycle. |      | ✓ | ✓ |

## References

<a id="fine_tune_def">\[1\] https://arxiv.org/pdf/2410.21337v1</a>