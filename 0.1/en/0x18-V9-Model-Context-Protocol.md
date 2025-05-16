# V.9 Model Context Protocol (MCP) Security

## Control Objective
Ensure every MCP server, client and tool operates with strong authentication, least-privilege access, integrity assurance and continuous monitoring so that LLM integrations cannot be hijacked, abused or silently altered.

| #    | Requirement | L1 | L2 | L3 |
| ---- | ----------- | -- | -- | -- |
| 9.1  | Require mutual-TLS or signed access-tokens for every MCP client server connection to authenticate both sides. | ✓ | ✓ | ✓ |
| 9.2  | Store OAuth / API credentials for MCP tools in a dedicated secrets-manager; never in plaintext configs or model context. | ✓ | ✓ | ✓ |
| 9.3  | Enforce fine-grained, least-privilege permission scopes for each tool (e.g., read-only, no delete). | ✓ | ✓ | ✓ |
| 9.4  | Maintain an allow-list of approved MCP servers with integrity-pinned hashes; block unknown or modified servers. |    | ✓ | ✓ |
| 9.5  | Validate & hash-pin tool descriptions; alert on any post-approval mutation (“tool-poisoning”). |    |    | ✓ |
| 9.6  | Schema and type-validate every tool invocation and every argument before execution. | ✓ | ✓ | ✓ |
| 9.7  | Scan tool descriptions, inputs and outputs for prompt-injection patterns and hidden directives before passing them to the model. | ✓ | ✓ | ✓ |
| 9.8  | Apply rate-limits and resource quotas on each tool to mitigate DoS and runaway cost-spikes. | ✓ | ✓ | ✓ |
| 9.9  | Require explicit human-in-the-loop approval for high-risk operations (financial transfers, file writes, privileged admin APIs). |    |    | ✓ |
| 9.10 | Log every MCP call (caller, tool, parameters, result) and stream to SIEM; retain logs per data-retention policy. | ✓ | ✓ | ✓ |
| 9.11 | Baseline normal tool-call patterns and raise alerts on anomalies (e.g., new tools, unusual volume, unusual time-of-day). |    |    | ✓ |
| 9.12 | Run each MCP server in a sandboxed, network-segmented environment; block outbound traffic except whitelisted APIs. |    |    | ✓ |
| 9.13 | Produce and maintain an SBOM for every MCP server, connector and library; remediate known CVEs within policy SLAs. |    | ✓ | ✓ |
| 9.14 | Conduct automated drift-detection and re-validation of MCP tool hashes, server manifests and OAuth permission scopes whenever a change is observed or at least every 30 days. |    |    | ✓ |
| 9.15 | Adopt signed-update / notarisation mechanisms for MCP server binaries or containers to prevent supply-chain attacks. |    |    | ✓ |
| 9.16 | Provide user-facing transparency UI showing which tools are exposed, when invoked and with which parameters. | ✓ | ✓ | ✓ |
| 9.17 | Scan MCP server code with SAST tools (or equivalent) to detect and fix “classical” vulnerabilities (e.g., OS command injection) that could be triggered via prompt injection. | ✓ | ✓ | ✓ |
