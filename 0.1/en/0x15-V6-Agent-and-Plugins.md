# V6. Agents and Plugins

## Control Objective
The autonomous nature of agent-based systems presents new risks and can increase the impact of attacks such as prompt injection. These controls aim to reduce the risk associated with autonomous LLM components to an acceptable level.

## V6.1 Agent Access Control

Ensure that access control mechanisms for autonomous agents respect the Principle of Least Privilege.

| # | Requirement | L1 | L2 | L3 |
| - | ---------- | -- | -- | -- |
| 6.1.1 | Ensure that agent based solutions only expose access to the agent tools and plugins required for the current task. When multiple agent supported tasks exist, it should not be possible for a given task to leverage tools or plugins used by another task. | ✓ | ✓ | ✓ |
| 6.1.2 | Ensure that API tokens for third-party services are scoped to the minimum required by the agent or plugin. For example, an agent designed to read messages from a specific Slack channel should not be able to read messages from other channels or post messages. |      | ✓ | ✓ |
| 6.1.3 | Ensure that custom built plugins consider the scope of the currently authenticated principle. Plugins should not be able to access more than what the current principle is authorized to access.  |      | ✓ | ✓ |
| 6.1.4 | Ensure that the host that executes agent tools and plugins is appropriately restricted from making arbitrary egress network requests. Only traffic for required APIs and services should be allowed to help increase the difficulty of data exfiltration from autonomous agents. |      |      | ✓ |
| 6.1.5 | Consider manual approval, sometimes referred to as “human in the loop,” for sensitive operations before autonomous agents can continue execution. |      |      | ✓ |
| 6.1.6 | Ensure that agents are executed in a sand-boxed ephemeral environment to reduce the risk of agent prompts which result in code execution due to software defects. |      |      | ✓ |
| 6.1.7 | Ensure that the host that executes agent tools and plugins is appropriately segregated from other internal components. Certain internal services might need to be queried, but firewall rules should enforce that unrelated services are not reachable. |      |      | ✓ |

## V6.2 Agent Configuration

Ensure that autonomous LLM components are securely configured.

| # | Requirement | L1 | L2 | L3 |
| - | ---------- | -- | -- | -- |
| 6.2.1 | Ensure that custom plugins and agent tools follow existing SSDLC processes. |      | ✓ | ✓ |
| 6.2.2 | Ensure third-party plugins and toolkits are properly vetted according to existing Third-party risk management processes. |      | ✓ | ✓ |
| 6.2.3| Ensure that the parameters for agent tools and plugins are validated prior to execution. Typical checks should include type checks at minimum, in addition to any more specific validation. |      | ✓ | ✓ |
| 6.2.4 | Ensure that credentials for third-party services consumed by agent tools and plugins are securely handled according to section V2.10 “Service Authentication” of the OWASP ASVS. |      | ✓ | ✓ |
| 6.2.5 | Ensure that agent and plugin frameworks contain hooks that allow the raw prompts and completions to be intercepted, enabling LLM guards to operate, and enabling proper monitoring, troubleshooting, and auditing. |      | ✓ | ✓ |
| 6.2.6 | Ensure that the application is protected against indirect plugin calls. The application should at least have a defined constraint over the interaction between the LLM and the web tools to prevent the LLM from executing external instructions returned by the web tools. [\[1\]](#real_world_llm_sec_6) |      | ✓ | ✓ |

## References

<a id="real_world_llm_sec_6">\[1\] https://arxiv.org/pdf/2402.18649</a>