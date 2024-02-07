# V2. Model Lifecycle

## Control Objective
Ensure that the Machine Learning (ML) lifecycle for models used within LLM-powered systems considers the various security threats from dataset curation, model training, and validation.  

| # | Requirement | L1 | L2 | L3 |
| - | ---------- | -- | -- | -- |
| 2.1 | Ensure that the lifecycle of machine learning models is integrated into the existing Secure Software Development Lifecycle (SSDLC). Defined processes should exist and be available for each stage of the lifecycle of ML models. |      | ✓ | ✓ |
| 2.2 | Document user stories defining the requirements and use cases for any new ML model being produced. |      | ✓ | ✓ |
| 2.3 | Ensure that model training resources and datasets are acquired from trustworthy sources and validated for correctness or free from malicious data.  | ✓ | ✓ | ✓ |
| 2.4 | Ensure that model training resources and datasets are properly secured from unauthorized modification once acquired. |      | ✓ | ✓ |
| 2.5 | Ensure that the source of any training resources and datasets is documented. |      |      | ✓ |
| 2.6 | Ensure that any data cleaning or other modifications to the original training resources are tracked and auditable to reduce the risk of data poisoning from an insider threat. |      |      | ✓ |
| 2.7 | Ensure that the intellectual property rights of model training resources and datasets are checked to avoid potential license or copyright infringement issues. Ensure this process is documented and auditable. | ✓ | ✓ | ✓ |
| 2.8 | Ensure that model training resources are audited for sensitive data (such as PII, internal company data, etc.) and cleaned before training to mitigate sensitive data exposure in model responses. |      | ✓ | ✓ |
| 2.9 | Ensure secure acquisition and storage of foundational or pre-trained models. | ✓ | ✓ | ✓ |
| 2.10 | Where possible, prefer secure model formats such as SafeTensors over formats that use unsafe serialization, like PyTorch’s Pickle format. | ✓ | ✓ | ✓ |
| 2.11 | Ensure that foundational models are fine-tuned to limit irrelevant data points which may lead to poor model performance. |      | ✓ | ✓ |
| 2.12 | Check regulatory obligations to ensure compliance when handling and processing model training data. |      | ✓ | ✓ |
| 2.13 | Ensure that a ML Bill-of-Materials (BOM) is produced for each model. |      |      | ✓ |
| 2.14 | Consider watermarking techniques for model responses when model theft is a concern, or the output of the model needs to be identifiable. |      |      | ✓ |
| 2.15 | Ensure tooling to detect biases and ensure fairness are integrated into the ML models lifecycle. |      | ✓ | ✓ |
| 2.16 | Ensure security tooling to detect LLM vulnerabilities such as injection attacks, jailbreak attempts and other abuse are integrated into the ML models lifecycle. |      | ✓ | ✓ |
| 2.17 | Before a model is finalized for deployment, conduct a thorough risk assessment to understand potential security, ethical, and operational risks. This assessment should guide the decision-making process regarding the deployment of the model. |      |      | ✓ |
| 2.18 | Ensure there is a clear plan for decommissioning models that are no longer in use. This includes securely erasing data, model parameters, and any sensitive information associated with the model to prevent unauthorized access or misuse. |      |      | ✓ |
