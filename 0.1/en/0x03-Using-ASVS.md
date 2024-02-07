# Utilizing the LLMSVS
The OWASP LLMSVS serves several key purposes:

- **Assisting Development Teams**: guide teams in developing and maintaining secure LLM-powered applications.

- **Framework for Security Teams**: assist security teams in setting requirements, guiding security audits, and conducting penetration tests against LLM-powered systems.

- **Aligning Security Benchmarks**: establish a common ground for security service providers, vendors, and clients regarding security expectations.

## Security Verification Layers
The LLMSVS categorizes security verification into three distinct levels, each tailored to different levels of security assurance:

1. **LLMSVS Level 1 - Basic Security**: This level is aimed at applications with lower security risk and focuses on fundamental security controls for any LLM-powered system.

2. **LLMSVS Level 2 - Moderate Security**: This level is ideal for applications handling sensitive data, offering a balanced approach to security that meets the needs of most applications. These applications may range from personal assistants, APIs processing customer data, or systems processing internal company data.

3. **LLMSVS Level 3 - High Assurance Security**: This level provides the most extensive security measures for the most critical applications involving sensitive data or high-value transactions. These applications may range from business critical applications that are essential for business operation, systems which handle financial transactions, or systems which fall under specific industry regulations such as those which process patient or healthcare data. 

Each level of the LLMSVS provides a set of specific security requirements, mapping these to essential security features and practices necessary for building and operating robust LLM-powered applications. This approach equips developers, architects, and security professionals with practical and actionable guidelines. Whether building, enhancing, or evaluating the security of these applications, the LLMSVS provides a clear roadmap for all stakeholders involved in the life cycle of LLM-powered systems.

## Assumptions
When utilizing the LLMSVS, it's important to keep in mind the following assumptions:

- The LLMSVS is not a replacement for adhering to secure development best practices, such as secure coding or a Secure Software Development Life Cycle (SSDLC). These practices should be integrally adopted throughout your development efforts, with the LLMSVS serving to augment them specifically for LLM-powered applications.

- The LLMSVS is not intended to substitute for comprehensive risk assessments or in-depth security reviews. Rather, it serves as a guide to address potential security vulnerabilities specific to LLM-powered applications. Employing the LLMSVS should complement, not replace, these crucial security practices to ensure a more thorough evaluation and mitigation of risks.

While the LLMSVS offers a comprehensive framework for enhancing the security of LLM-powered applications, it cannot ensure complete security. It should be viewed as a foundational set of security requirements, with additional protective measures taken as needed to mitigate specific LLM risks and threats.
