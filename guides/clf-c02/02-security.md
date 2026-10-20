# Part 3 - Security and Compliance

## Shared Responsibility Model

**AWS:** Security *of* the cloud — facilities, hardware, global network, hypervisor, managed service infrastructure.

**Customer:** Security *in* the cloud — guest OS (when you manage it), apps, data, identity, network configs (security groups), encryption choices, patching where you control the OS.

### How responsibility shifts

| Service style | Customer still owns | AWS takes more of |
| --- | --- | --- |
| **EC2 (IaaS)** | Guest OS, patches, apps, SG rules, data | Hardware, hypervisor, facilities |
| **RDS (managed DB)** | Data, access, network placement, some config | DB engine patching/HA plumbing (service-managed) |
| **Lambda / many SaaS-like** | Code, IAM to invoke, data sensitivity | Runtime hosts, scaling infrastructure |

##### Scenario example

On EC2 you must patch Linux. On RDS you don’t SSH in to patch MySQL the same way — but you still control who can query the data and whether storage is encrypted.

## Identity and access

### Protect the root user

- Enable **MFA**
- Do **not** use root for daily work
- Don’t create access keys for root unless absolutely required (prefer not)
- Root-only tasks exist (e.g., account-level changes) — know root is special

### IAM building blocks

| Building block | Role |
| --- | --- |
| **User** | Long-lived identity for a person (or rarely an app) |
| **Group** | Collection of users sharing policies |
| **Role** | Assumable identity; temporary credentials |
| **Policy** | Permissions document (AWS managed or customer managed) |
| **Identity Center** | Workforce single sign-on / centralized access |

**Best practices:** least privilege; prefer **roles** for EC2/Lambda/apps; rotate credentials; use MFA; use groups for people permissions.

### Federation

External identity provider → temporary AWS access (corporate SSO patterns). CLF level: know federation exists and Identity Center helps workforce access.

## Encryption and data protection

- **At rest:** S3 encryption, EBS encryption, RDS encryption, **AWS KMS** keys
- **In transit:** TLS, HTTPS listeners, VPN / Direct Connect patterns
- **Secrets Manager / Systems Manager Parameter Store:** don’t hard-code secrets

## Governance, logging, compliance

| Need | Service |
| --- | --- |
| Compliance reports / agreements | **AWS Artifact** |
| API activity audit | **AWS CloudTrail** |
| Metrics/logs/alarms | **Amazon CloudWatch** |
| Config history & rules | **AWS Config** |
| Continuous audit help | **AWS Audit Manager** |
| Threat detection | **Amazon GuardDuty** |
| Vulnerability findings | **Amazon Inspector** |
| Central security findings | **AWS Security Hub** |
| Account best-practice checks | **AWS Trusted Advisor** |

##### Scenario example

Auditor asks for SOC reports → **Artifact**. Security asks who deleted a bucket yesterday → **CloudTrail**. Ops wants CPU alarm → **CloudWatch**.

## Network security components

| Control | What it does |
| --- | --- |
| **Security groups** | Stateful allow-list at instance/ENI |
| **Network ACLs** | Stateless rules at subnet |
| **AWS WAF** | Layer-7 web filters |
| **AWS Shield** | DDoS protection |
| **AWS Firewall Manager** | Central policy across accounts (awareness) |
| **Private subnets + NAT** | No inbound from internet; controlled outbound |

## Marketplace security

Third-party security products are available in **AWS Marketplace** — CLF often tests that you know this option exists.
