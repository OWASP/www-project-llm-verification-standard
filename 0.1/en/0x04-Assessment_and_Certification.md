# Assessment and Certification

## OWASP's Stance on LLMSVS Certifications and Trust Marks

OWASP, as a vendor-neutral not-for-profit organization, does not currently certify any vendors, verifiers or software.

All such assurance assertions, trust marks, or certifications are not officially vetted, registered, or certified by OWASP, so an organization relying upon such a view needs to be cautious of the trust placed in any third party or trust mark claiming (LLM)SVS certification.

This should not inhibit organizations from offering such assurance services, as long as they do not claim official OWASP certification.

## Guidance for Certifying Organizations

For Large Language Model Security Verification Standard (LLMSVS) compliance, an "open book" review is recommend, granting assessors access to essential resources such as system architects, developers, project documentation, source code, and authenticated interfaces, including access to at least one account for each user role.

It is important to note that the LLMSVS only covers the security requirements pertaining to LLM usage and integration. It does not cover general application security controls (e.g web services ) which are not specific to an LLM-powered system. Any additional systems and non-LLM properties should be verified against appropriate standards, such as the [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/).

Certification reports should clearly define the verification scope, particularly noting any exclusions, and summarize findings with details on both passed and failed tests, including guidance for addressing failures. Industry-standard practice requires detailed documentation of the verification process, including work papers, screenshots, scripts for issue replication, and electronic testing records such as proxy logs. Automated tool results alone are insufficient; documentation must provide conclusive evidence of thorough and rigorous testing of all controls. In case of disputes, sufficient evidence should be present to verify that each verified control has indeed been tested.