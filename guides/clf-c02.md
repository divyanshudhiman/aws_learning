# AWS Certified Cloud Practitioner (CLF-C02) Study Guide

Structured personal study notes for the CLF-C02 exam — same study pattern as the AIF-C01 guide: starter definitions, domain Parts, glossary, and scenario practice with answers.

**Edition note:** Original study notes organized as Parts 0–7 for GitHub Pages. Not an official AWS publication. Practice questions are original scenario-style items for learning (not exam dumps).

**Companion guide:** [AI Practitioner (AIF-C01)](../)

---

## How to use this guide

Study Part 0 first, then domains by exam weight, then drill practice tests.

| Part | Focus |
| --- | --- |
| Part 0 - Essential Definitions (Start Here) | Starter glossary |
| Part 1 - Exam Overview | Format & domains |
| Part 2 - Cloud Concepts | Domain 1 (24%) |
| Part 3 - Security and Compliance | Domain 2 (30%) |
| Part 4 - Cloud Technology and Services | Domain 3 (34%) |
| Part 5 - Billing, Pricing, and Support | Domain 4 (12%) |
| Part 6 - Glossary | Full term list |
| Part 7 - Practice Tests | Scenarios with answers |

**Suggested path:** Essential definitions → Exam overview → Technology & services → Security → Cloud concepts → Billing → Practice tests.

---

# Part 0 - Essential Definitions (Start Here)

Read this **before** deep service lists. Plain meaning → exam tip → tiny example.

---

## 1. Cloud vs on-premises

| Term | Plain meaning | Exam tip | Tiny example |
| --- | --- | --- | --- |
| **Cloud computing** | On-demand IT resources over the internet with pay-as-you-go pricing | Contrast with buying/running your own data center | Launch a server in minutes; stop paying when you stop it |
| **On-premises** | You own/operate hardware in your facilities | CapEx heavy; you handle racks, power, cooling | Company basement servers |
| **CapEx** | Upfront capital spend (buy hardware) | Cloud often shifts CapEx → OpEx | Buying a $40k server |
| **OpEx** | Ongoing operating expense | AWS bills are typically OpEx | Monthly EC2 charges |
| **IaaS** | Infrastructure as a Service — you manage OS/apps; provider manages hardware | EC2 is classic IaaS | Virtual machines you patch |
| **PaaS** | Platform as a Service — focus on code; less OS work | Elastic Beanstalk style | Deploy app with less server toil |
| **SaaS** | Software as a Service — complete app you use | Think “login and use” | Browser-based email/productivity |
| **Public cloud** | Shared cloud from a provider (AWS) | Multi-tenant infrastructure | AWS Regions |
| **Private cloud** | Cloud-like resources for one org | Often on-prem or dedicated | Private virtualization stack |
| **Hybrid cloud** | Mix of on-prem + public cloud | Direct Connect / VPN common | Keep DB on-prem, web on AWS |
| **Multi-cloud** | Using more than one public cloud | Strategy/risk tradeoffs | AWS + another provider |

---

## 2. Core cloud benefits (Domain 1 favorites)

| Benefit | Plain meaning | Example |
| --- | --- | --- |
| **Agility** | Experiment and launch faster | Spin up a test env in minutes |
| **Elasticity** | Scale out/in automatically with demand | Add instances for Black Friday |
| **Scalability** | Ability to grow capacity | From 1 to 1,000 servers |
| **High availability** | Keep working through component failures | Multi-AZ database |
| **Fault tolerance** | Continue despite failures | Redundant components |
| **Disaster recovery** | Recover from major outages | Backup Region restore |
| **Global reach** | Deploy near users worldwide | Regions + CloudFront |
| **Economy of scale** | AWS buys at scale → lower unit cost to you | Cheaper than tiny private DC |
| **Trade CapEx for OpEx** | Pay for use instead of big upfront buys | No rack purchase |
| **Stop guessing capacity** | Avoid overbuying servers “just in case” | Autoscale instead of 3-year guess |

---

## 3. Global infrastructure

| Term | Plain meaning | Remember |
| --- | --- | --- |
| **Region** | Geographic area with multiple AZs | Choose for latency, compliance, services |
| **Availability Zone (AZ)** | One or more discrete data centers with redundant power/networking | Isolate failures |
| **Edge location** | Sites that cache content closer to users | CloudFront |
| **Local Zone** | Compute/storage closer to large metro users | Ultra-low latency |
| **Wavelength Zone** | AWS infra at telecom 5G edges | Mobile edge apps |
| **AWS Outposts** | AWS hardware/services in *your* data center | On-prem AWS experience |

---

## 4. Security basics

| Term | Plain meaning | Exam tip |
| --- | --- | --- |
| **Shared Responsibility Model** | AWS secures the cloud; you secure *in* the cloud | Shifts by service (EC2 vs RDS vs Lambda) |
| **IAM** | Users, groups, roles, policies controlling access | Least privilege always |
| **Root user** | Account owner identity — protect heavily | MFA; don’t use daily |
| **MFA** | Extra factor beyond password | Enable for root and admins |
| **IAM role** | Assumed identity with temporary credentials | Prefer roles over long-lived keys |
| **IAM policy** | JSON permissions document | Allow/deny actions on resources |
| **Least privilege** | Only permissions needed to do the job | Start narrow |
| **Encryption at rest** | Protect stored data | S3 SSE, EBS encryption, KMS |
| **Encryption in transit** | Protect data moving on the network | TLS/HTTPS |
| **Security group** | Stateful virtual firewall for instances | Allow rules; deny by default |
| **NACL** | Stateless subnet firewall | Optional extra layer |
| **AWS Artifact** | On-demand compliance reports | Auditor asks for SOC/ISO |
| **AWS CloudTrail** | Logs API calls (who did what) | Audit trail |
| **Amazon GuardDuty** | Threat detection | Suspicious findings |
| **AWS WAF** | Web application firewall | Filter malicious HTTP |
| **AWS Shield** | DDoS protection | Standard free; Advanced paid |
| **Amazon Inspector** | Vulnerability assessment | Find exposure/CVEs |
| **AWS Secrets Manager** | Store/rotate secrets | DB passwords, API keys |

---

## 5. Compute one-liners

| Service | Job |
| --- | --- |
| **Amazon EC2** | Virtual servers (instances) you manage |
| **Amazon EC2 Auto Scaling** | Add/remove instances by policy |
| **AWS Lambda** | Run code without managing servers |
| **Amazon ECS / EKS** | Containers / Kubernetes |
| **AWS Fargate** | Serverless compute for containers |
| **AWS Elastic Beanstalk** | Easy app deploy/manage |
| **AWS Batch** | Batch computing jobs |
| **Amazon Lightsail** | Simple VPS-like starting point |

---

## 6. Storage one-liners

| Service | Job |
| --- | --- |
| **Amazon S3** | Object storage; highly durable |
| **S3 Glacier family** | Cheap archival; slower retrieve |
| **Amazon EBS** | Block volumes for EC2 |
| **Amazon EFS** | Shared NFS file storage |
| **AWS Storage Gateway** | Hybrid storage bridge |
| **AWS Backup** | Centralized backup policies |
| **AWS Snow Family** | Physical devices to move huge data |

---

## 7. Database one-liners

| Service | Job |
| --- | --- |
| **Amazon RDS** | Managed relational DB |
| **Amazon Aurora** | Cloud-native MySQL/Postgres-compatible |
| **Amazon DynamoDB** | Managed NoSQL |
| **Amazon Redshift** | Data warehouse |
| **Amazon ElastiCache** | In-memory cache |
| **Amazon DocumentDB** | MongoDB-compatible |
| **Amazon Neptune** | Graph database |

---

## 8. Networking one-liners

| Service | Job |
| --- | --- |
| **Amazon VPC** | Your private virtual network |
| **Subnet** | Slice of VPC in an AZ |
| **Internet Gateway** | VPC ↔ internet |
| **NAT Gateway** | Private subnet outbound internet |
| **AWS Direct Connect** | Dedicated private link |
| **AWS VPN** | Encrypted tunnel over internet |
| **Elastic Load Balancing** | Distribute traffic |
| **Amazon Route 53** | DNS + routing + health checks |
| **Amazon CloudFront** | CDN at edge locations |
| **AWS Global Accelerator** | Improve global performance via AWS network |

---

## 9. Management, billing, support

| Concept | Job |
| --- | --- |
| **AWS CloudFormation** | Infrastructure as code |
| **Amazon CloudWatch** | Metrics, logs, alarms |
| **AWS Config** | Configuration compliance history |
| **AWS Organizations** | Multi-account governance |
| **AWS Trusted Advisor** | Best-practice checks |
| **AWS Cost Explorer** | Analyze spend |
| **AWS Budgets** | Spend/usage alerts |
| **AWS Pricing Calculator** | Estimate before you build |
| **On-Demand** | Pay as you go, no long commitment |
| **Reserved / Savings Plans** | Discount for commitment |
| **Spot Instances** | Cheap spare capacity; can interrupt |
| **Support plans** | Basic → Developer → Business → Enterprise tiers |

---

## 10. Well-Architected pillars

1. Operational Excellence  
2. Security  
3. Reliability  
4. Performance Efficiency  
5. Cost Optimization  
6. Sustainability  

**CAF** guides cloud *adoption*; **Well-Architected** guides *architecture quality*.

---

## 11. Don’t-mix pairs

| A | B | Difference |
| --- | --- | --- |
| Region | AZ | Geography vs isolated site inside Region |
| Security group | NACL | Instance stateful vs subnet stateless |
| IAM user | IAM role | Long-lived vs assumable temporary |
| S3 | EBS | Object store vs EC2 block disk |
| EBS | EFS | Single-instance block vs shared files |
| RDS | DynamoDB | Relational vs NoSQL |
| CloudTrail | CloudWatch | API audit vs monitoring |
| Shield | WAF | DDoS vs Layer-7 filters |
| Direct Connect | VPN | Dedicated private vs internet tunnel |

---

## 12. 60-second checklist

1. Cloud benefits (agility, elasticity, HA, global, OpEx, stop guessing)  
2. Region vs AZ vs edge  
3. Shared responsibility shifts by service  
4. IAM least privilege + root MFA  
5. EC2 vs Lambda vs containers  
6. S3 vs EBS vs EFS  
7. RDS vs DynamoDB  
8. VPC / SG / Route 53 / CloudFront  
9. On-Demand vs commitment discounts vs Spot  
10. Trusted Advisor, Cost Explorer, Budgets, Artifact, Support  

Continue to **Part 1 - Exam Overview**.

---

# Part 1 - Exam Overview

## Introduction

The AWS Certified Cloud Practitioner (CLF-C02) exam is for people who can demonstrate overall knowledge of the AWS Cloud, independent of a specific job role.

The exam validates that you can:

- Explain the value of the AWS Cloud
- Understand and explain the AWS shared responsibility model
- Understand security best practices
- Understand AWS Cloud costs, economics, and billing practices
- Describe and position core AWS services (compute, network, database, storage)
- Identify AWS services for common use cases

### Target candidate

Up to about **6 months** of exposure to AWS Cloud design, implementation, and/or operations. Suitable for non-IT backgrounds and early cloud careers.

**Out of scope for the candidate (examples):** coding, deep architecture design, troubleshooting, implementation, load/performance testing.

### Exam format (high level)

- About **65** questions total; **50** scored + **15** unscored (unscored not marked)
- Question types: **multiple choice** and **multiple response**
- Scaled score **100–1000**; passing score **700**
- Compensatory scoring: pass the **overall** exam (not each domain separately)
- No penalty for guessing; blanks count as wrong

### Domains and weightings (CLF-C02)

| Domain | Weight |
| --- | --- |
| Domain 1: Cloud Concepts | 24% |
| Domain 2: Security and Compliance | 30% |
| Domain 3: Cloud Technology and Services | 34% |
| Domain 4: Billing, Pricing, and Support | 12% |

**Study bias:** Domain 3 is largest; Domain 2 (security) is close behind — do not under-study IAM/shared responsibility.

---

# Part 2 - Cloud Concepts

## Value of the AWS Cloud

### Why organizations move to AWS

- **Cost savings / economies of scale** — avoid buying and housing hardware for peak “just in case”
- **Global infrastructure** — deploy closer to customers quickly
- **High availability & elasticity** — design for failure and scale with demand
- **Agility** — experiment, fail fast, iterate

##### Scenario example

A retailer used to buy servers every November “for holiday traffic,” then leave them idle. On AWS they keep a small baseline and **Auto Scale** for the season → pay mainly when demand exists.

## Design principles and Well-Architected

Know the **six pillars** and that Well-Architected helps review workloads against best practices (not a product you “buy”).

| Pillar | One-line focus |
| --- | --- |
| Operational Excellence | Run/monitor systems; improve processes |
| Security | Protect data, systems, assets |
| Reliability | Recover from failures; meet demand |
| Performance Efficiency | Use resources efficiently; evolve |
| Cost Optimization | Avoid unnecessary cost |
| Sustainability | Minimize environmental impact |

## Migration and CAF

**AWS Cloud Adoption Framework (CAF)** organizes perspectives for cloud transformation (business + technical). Benefits often cited: reduced business risk, improved ESG, increased revenue, operational efficiency.

**Migration strategies (6 Rs — know the idea):** Rehost, Replatform, Refactor/Re-architect, Repurchase, Retain, Retire.

**Tools that show up in migration talk:**

- **AWS Snowball / Snow Family** — move large datasets physically
- **AWS Database Migration Service (DMS)** — migrate databases
- **AWS Application Discovery Service / Migration Hub** — discover and track (awareness level)

## Cloud economics

| Idea | Meaning |
| --- | --- |
| Fixed vs variable cost | Cloud lets many costs become variable with usage |
| Rightsizing | Match instance/storage size to actual need |
| Managed services | Reduce undifferentiated heavy lifting (patching, HA) |
| Automation | CloudFormation / IaC reduces manual error and time |
| Licensing | BYOL vs license-included options depending on service |

##### Scenario example

Moving a steady database to **Amazon RDS** reduces patching/HA toil versus self-managed EC2 MySQL — economics include *people time*, not only instance price.

---

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

---

# Part 4 - Cloud Technology and Services

Largest domain (34%). Goal: **pick the right service for the scenario**, not deep config.

## Ways to access and operate AWS

| Method | Use |
| --- | --- |
| **AWS Management Console** | Browser GUI |
| **AWS CLI** | Scriptable commands |
| **SDKs** | Call APIs from code |
| **CloudFormation / IaC** | Declarative templates |
| **AWS Tools for PowerShell** | Windows-centric automation |

**Deployment models:** cloud, on-premises, hybrid (Outposts / VPN / Direct Connect).

---

## Compute

### Amazon EC2

- Virtual machines with choice of instance family/size
- You pick AMI, network, storage, security groups
- Pair with **Auto Scaling** and **Elastic Load Balancing** for HA/scale

**Purchasing options (exam gold):**

| Option | When |
| --- | --- |
| **On-Demand** | Spiky/unknown; no commitment |
| **Savings Plans / Reserved** | Steady usage; want discount |
| **Spot** | Flexible/fault-tolerant batch; can be interrupted |
| **Dedicated Hosts / Instances** | Compliance/licensing needs |

### Containers and serverless

| Need | Prefer |
| --- | --- |
| Run code from events, short jobs, no servers | **Lambda** |
| Containers without managing servers | **Fargate** (with ECS/EKS) |
| Manage container orchestration | **ECS** or **EKS** |
| Simple web app upload-and-run | **Elastic Beanstalk** |
| Tiny/simple VPS experience | **Lightsail** |

##### Scenario examples

- Image resize on upload → **Lambda** (+ S3 event)
- Always-on API with custom OS packages → **EC2** or containers
- Kubernetes shop → **EKS**

---

## Storage

### Amazon S3

- Object storage; objects in buckets
- Extremely durable; access via HTTP APIs
- Features: versioning, lifecycle policies, static website hosting, encryption, Block Public Access
- Classes: Standard, Intelligent-Tiering, IA, Glacier Instant/Flexible/Deep Archive

### Block and file

| Need | Service |
| --- | --- |
| Disk for one EC2 | **EBS** |
| Shared file system for many Linux instances | **EFS** |
| Windows file share (awareness) | **FSx** family |
| Archive rarely accessed objects | **S3 Glacier** |
| Petabyte migrate offline | **Snowball** |

##### Scenario examples

- Photos for a website → **S3** (+ CloudFront)
- Database files for EC2 MySQL you manage → **EBS**
- Shared home directories across fleet → **EFS**

---

## Databases

| Need | Service |
| --- | --- |
| Managed MySQL/Postgres/SQL Server/Oracle | **RDS** |
| High performance MySQL/Postgres-compatible | **Aurora** |
| Serverless key-value / document at scale | **DynamoDB** |
| Analytics warehouse / BI SQL | **Redshift** |
| Cache sessions / hot keys | **ElastiCache** |
| MongoDB-compatible | **DocumentDB** |
| Relationships as a graph | **Neptune** |

**Rule of thumb:** relational joins/transactions → RDS/Aurora; massive simple key lookup → DynamoDB; BI warehouse → Redshift.

---

## Networking and content delivery

### VPC essentials

- VPC → subnets (public/private) across AZs
- Route tables, IGW, NAT, security groups, NACLs
- **VPC peering / Transit Gateway** for connectivity patterns (awareness)

### Traffic and DNS

| Need | Service |
| --- | --- |
| DNS for your domain | **Route 53** |
| Distribute HTTP/TCP load | **ELB** (ALB/NLB/GLB awareness) |
| Cache static content globally | **CloudFront** |
| Private link to AWS/services | **PrivateLink** (awareness) |
| Dedicated connectivity | **Direct Connect** |
| Quick encrypted hybrid | **Site-to-Site VPN** |

##### Scenario examples

- Global static website speed → S3 + **CloudFront**
- App across 2 AZs → ALB + Auto Scaling in private subnets
- Stable low latency to HQ → **Direct Connect**

---

## Application integration & messaging (awareness)

| Service | Job |
| --- | --- |
| **Amazon SQS** | Managed queues |
| **Amazon SNS** | Pub/sub notifications |
| **Amazon EventBridge** | Event bus / routing |
| **AWS Step Functions** | Workflow orchestration |

---

## Analytics & AI/ML (CLF awareness level)

| Service | Job |
| --- | --- |
| **Amazon Athena** | SQL on S3 data |
| **Amazon EMR** | Big data frameworks |
| **AWS Glue** | ETL / data catalog |
| **Amazon Kinesis** | Streaming data |
| **Amazon QuickSight** | BI dashboards |
| **Amazon Rekognition / Comprehend / Transcribe / Polly / Translate / Lex / SageMaker / Bedrock** | AI/ML family (know category, not deep AIF detail) |

---

## Developer / management tools

| Service | Job |
| --- | --- |
| **CloudFormation** | IaC templates |
| **AWS Elastic Beanstalk** | App platform |
| **AWS CodePipeline / CodeBuild / CodeCommit** | CI/CD family (awareness) |
| **Systems Manager** | Patch/run command/ops |
| **CloudWatch** | Observe |
| **AWS Config** | Compliance of configs |
| **Organizations / Control Tower** | Multi-account |

---

## Customer engagement & business apps (light)

Know categories exist: Amazon Connect (contact center), SES (email), Pinpoint (engagement) — enough to match a one-line use case.

---

# Part 5 - Billing, Pricing, and Support

## Pricing models

| Model | Idea |
| --- | --- |
| **Pay-as-you-go** | Pay for what you use; stop resources to stop most charges |
| **On-Demand** | No upfront commitment for compute |
| **Reserved Instances** | Commit to instance attributes for discount |
| **Savings Plans** | Flexible commitment discount ($/hour for 1–3 years) |
| **Spot** | Deep discount; AWS can reclaim capacity |
| **Free Tier** | Limited free usage for 12 months / always free / trials |

### What usually drives cost

- Compute hours / Lambda requests & duration  
- Storage GB-month + requests  
- Data transfer **out** to internet (ingress often free; watch egress)  
- NAT Gateway, Load Balancer hours, IPs  
- Premium support plan fees  

##### Scenario example

A student leaves a large EC2 + public IPv4 running all month → surprise bill. Fix: stop/terminate unused resources; use budgets/alerts.

## Cost visibility and control

| Tool | Use |
| --- | --- |
| **AWS Pricing Calculator** | Estimate before deploying |
| **AWS Cost Explorer** | Analyze historical spend |
| **AWS Budgets** | Alert on actual/forecast thresholds |
| **Cost anomaly detection** | Spot unusual spend (awareness) |
| **Consolidated billing (Organizations)** | One payer; volume discounts may apply |
| **Trusted Advisor** | Cost-optimization checks (with support tier features) |
| **S3 / EC2 lifecycle & rightsizing** | Practical savings levers |

## Support plans (know the ladder)

| Plan | Typical fit |
| --- | --- |
| **Basic** | Billing/account; Trusted Advisor core checks; no tech support cases for builders |
| **Developer** | Business-hours tech support; general guidance |
| **Business** | 24/7 tech support; full Trusted Advisor checks; production workloads |
| **Enterprise On-Ramp / Enterprise** | Higher severity response, TAM-style engagement (Enterprise) |

**Exam angle:** Production, 24/7, Infrastructure Event Management → think Business/Enterprise — not Developer.

## Billing support vs technical support

- Billing/account questions available even on Basic  
- Architecture/tech troubleshooting needs paid support tiers  

---

# Part 6 - Glossary

### Cloud fundamentals

- **Agility:** Ability to innovate and deploy quickly.
- **Elasticity:** Automatic scaling to match demand.
- **High availability:** System remains accessible despite component failures.
- **Fault tolerance:** Continues operating through failures.
- **Scalability:** Capacity to grow (vertical or horizontal).
- **Horizontal scaling:** Add more instances.
- **Vertical scaling:** Make one instance bigger.
- **Region:** Geographic AWS area with multiple AZs.
- **Availability Zone:** Isolated location within a Region.
- **Edge location:** Site used for CDN/DNS performance near users.

### Security

- **Shared Responsibility Model:** Split of security duties between AWS and customer.
- **IAM:** Identity and Access Management.
- **Least privilege:** Minimal permissions required.
- **MFA:** Multi-factor authentication.
- **Security group:** Stateful instance firewall.
- **NACL:** Stateless subnet firewall.
- **KMS:** Key Management Service for encryption keys.
- **CloudTrail:** API activity logging.
- **GuardDuty:** Intelligent threat detection.
- **Artifact:** Compliance report portal.
- **Shield:** DDoS protection.
- **WAF:** Web Application Firewall.

### Compute & apps

- **EC2:** Virtual servers in the cloud.
- **Lambda:** Serverless functions.
- **Auto Scaling:** Adjust capacity automatically.
- **ELB:** Elastic Load Balancing.
- **Elastic Beanstalk:** Managed application platform.
- **ECS/EKS/Fargate:** Container services.

### Storage & database

- **S3:** Object storage.
- **EBS:** Block storage for EC2.
- **EFS:** Elastic File System (shared).
- **RDS:** Managed relational databases.
- **DynamoDB:** Managed NoSQL.
- **Aurora:** AWS cloud-native relational engine.
- **Redshift:** Data warehouse.
- **Snowball:** Physical data transfer appliance.

### Networking

- **VPC:** Virtual Private Cloud.
- **Subnet:** Network segment in an AZ.
- **Route 53:** DNS service.
- **CloudFront:** Content Delivery Network.
- **Direct Connect:** Dedicated network connection to AWS.
- **VPN:** Encrypted tunnel over the public internet.

### Cost & ops

- **Cost Explorer:** Spend analysis.
- **Budgets:** Threshold alerts.
- **Trusted Advisor:** Best-practice recommendations.
- **CloudWatch:** Monitoring and observability.
- **CloudFormation:** Infrastructure as code.
- **Organizations:** Multi-account management.
- **Well-Architected Framework:** Best-practice pillars for workloads.
- **CAF:** Cloud Adoption Framework for transformation guidance.

---

# Part 7 - Practice Tests

Original scenario-style questions. Answer first, then expand **Answer** for the result.

---

## Practice Test 1 - Mixed CLF scenarios

1. A startup wants to try AWS with almost no upfront hardware cost and the ability to shut resources off when idle. Which cloud benefit is primary?
    - A. CapEx maximization
    - B. Trade CapEx for OpEx / pay-as-you-go
    - C. Mandatory 3-year hardware contracts
    - D. Owning the data-center building

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: Cloud lets you avoid large upfront CapEx and pay for what you use (OpEx style).
    </details>

2. Which AWS global infrastructure component provides isolated failure domains inside a Region?
    - A. Edge location only
    - B. Availability Zone
    - C. Single rack switch
    - D. AWS Marketplace

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: AZs isolate failures within a Region. Edge locations mainly help CDN/DNS proximity.
    </details>

3. Who is responsible for guest OS patching on Amazon EC2?
    - A. AWS only
    - B. The customer
    - C. ICANN
    - D. The domain registrar

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: Shared responsibility: on EC2, the customer manages the guest OS.
    </details>

4. An auditor needs SOC reports for AWS. Where should the customer look first?
    - A. Amazon Polly
    - B. AWS Artifact
    - C. Amazon Lightsail
    - D. AWS Snowmobile only

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: Artifact provides on-demand compliance reports and agreements.
    </details>

5. Best practice for the AWS account root user?
    - A. Use it for daily EC2 work
    - B. Enable MFA and avoid daily use
    - C. Share the password in Slack
    - D. Disable all logging

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: Protect root with MFA and use IAM users/roles for everyday tasks.
    </details>

6. Grant temporary permissions to an EC2 application to read an S3 bucket. Prefer:
    - A. Embed root access keys in code
    - B. Attach an IAM role to the instance
    - C. Publish keys on a website
    - D. Disable IAM entirely

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: Instance profiles/roles provide temporary credentials without hard-coding keys.
    </details>

7. Stateful firewall attached to an EC2 instance’s network interface:
    - A. Network ACL only
    - B. Security group
    - C. AWS Budgets
    - D. Amazon Athena

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: Security groups are stateful instance-level firewalls. NACLs are subnet-level and stateless.
    </details>

8. Store product images for a global website with high durability and HTTP access:
    - A. Amazon S3
    - B. Amazon RDS
    - C. Amazon VPC Peering alone
    - D. AWS Config alone

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: S3 is object storage ideal for images/static assets (often with CloudFront).
    </details>

9. Disk volume for a single EC2 database you manage yourself:
    - A. Amazon EBS
    - B. Amazon CloudFront
    - C. Amazon SNS
    - D. AWS WAF

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: EBS provides block storage volumes for EC2 instances.
    </details>

10. Shared file system mounted by many Linux EC2 instances:
    - A. Amazon EFS
    - B. Amazon SQS
    - C. Amazon Glacier Deep Archive only
    - D. AWS Shield

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: EFS is a shared NFS-style file system for multiple instances.
    </details>

11. Managed MySQL with automated backups and Multi-AZ options:
    - A. Amazon RDS
    - B. Amazon S3 Glacier
    - C. Amazon CloudFront
    - D. AWS Snowcone only

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: RDS manages relational engines like MySQL.
    </details>

12. Serverless key-value store for millions of simple lookups per second:
    - A. Amazon DynamoDB
    - B. Amazon Redshift only for this tiny key lookup
    - C. AWS Artifact
    - D. Amazon WorkSpaces only

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: DynamoDB is managed NoSQL designed for scalable key-value access.
    </details>

13. Run code when an object lands in S3 without managing servers:
    - A. AWS Lambda
    - B. Dedicated Hosts only
    - C. AWS Snowball Edge as the only option
    - D. Amazon Redshift Spectrum alone

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Lambda is event-driven serverless compute.
    </details>

14. Distribute HTTP traffic across EC2 instances in multiple AZs:
    - A. Elastic Load Balancing
    - B. Amazon Macie alone
    - C. AWS Budgets
    - D. Amazon Comprehend

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: ELB distributes traffic and supports multi-AZ architectures.
    </details>

15. DNS for example.com with health checks:
    - A. Amazon Route 53
    - B. Amazon EBS
    - C. Amazon ECR only
    - D. AWS IAM Access Analyzer only

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Route 53 is AWS DNS with routing policies and health checks.
    </details>

16. Cache static assets at locations near users worldwide:
    - A. Amazon CloudFront
    - B. AWS CloudTrail
    - C. AWS Config
    - D. Amazon Inspector

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: CloudFront is the CDN using edge locations.
    </details>

17. Private dedicated network from on-premises to AWS (not over the public internet):
    - A. AWS Direct Connect
    - B. Public Wi-Fi hotspot
    - C. Amazon Polly
    - D. Amazon Lightsail DNS only

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Direct Connect provides dedicated connectivity. VPN uses the encrypted public internet.
    </details>

18. Record who called which AWS API yesterday:
    - A. AWS CloudTrail
    - B. Amazon Forecast
    - C. Amazon Personalize
    - D. Amazon Textract

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: CloudTrail is the API audit log service.
    </details>

19. Alarm when EC2 CPU is high for 5 minutes:
    - A. Amazon CloudWatch
    - B. AWS Artifact
    - C. Amazon QuickSight only
    - D. AWS FreeRTOS only

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: CloudWatch metrics and alarms monitor resources.
    </details>

20. Detect potentially unauthorized or anomalous account activity from AWS logs:
    - A. Amazon GuardDuty
    - B. Amazon S3 Glacier Instant Retrieval alone
    - C. Amazon Route 53 Registrar alone
    - D. AWS License Manager alone

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: GuardDuty provides intelligent threat detection.
    </details>

21. Fault-tolerant batch jobs that can tolerate interruption for lowest compute cost:
    - A. Spot Instances
    - B. Always use the largest Dedicated Host
    - C. Root user interactive sessions only
    - D. AWS Artifact

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Spot offers discounts but can be reclaimed — good for flexible workloads.
    </details>

22. Steady 24/7 production EC2 usage for one year; want a discount without rewriting apps:
    - A. Savings Plans or Reserved Instances
    - B. Delete the VPC
    - C. Disable encryption
    - D. Use only Spot for the database primary

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Commitment discounts fit steady-state production. Spot is risky for primary DBs.
    </details>

23. Get notified if monthly charges exceed $200:
    - A. AWS Budgets
    - B. Amazon Lex only
    - C. Amazon Rekognition only
    - D. AWS Snowball

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Budgets alert on cost/usage thresholds.
    </details>

24. Estimate the monthly cost of 3 EC2 instances and an ALB before building:
    - A. AWS Pricing Calculator
    - B. Amazon Macie only
    - C. AWS WAF only
    - D. Amazon Neptune only

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Pricing Calculator estimates costs pre-deployment.
    </details>

25. Production workload needs 24/7 technical support and full Trusted Advisor checks:
    - A. Business Support (or higher)
    - B. Basic Support only
    - C. No support plan exists for production
    - D. Only email Amazon retail support

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Business (and Enterprise tiers) unlock 24/7 tech support and broader Trusted Advisor checks.
    </details>

---

## Practice Test 2 - More scenarios

1. Which Well-Architected pillar focuses on protecting data and systems?
    - A. Security
    - B. Cost Optimization only
    - C. Sustainability only
    - D. Color scheme design

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Security is a Well-Architected pillar.
    </details>

2. Moving a large archive to AWS without enough internet bandwidth — best fit?
    - A. AWS Snowball
    - B. Email ZIP files
    - C. USB left on a park bench
    - D. Amazon SNS alone

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Snow Family devices physically transfer large datasets.
    </details>

3. Multi-account company wants centralized billing:
    - A. AWS Organizations consolidated billing
    - B. Separate credit cards with no linkage only
    - C. Disable Cost Explorer
    - D. Delete CloudTrail

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Organizations enables consolidated billing across accounts.
    </details>

4. Which service helps define infrastructure as code templates?
    - A. AWS CloudFormation
    - B. Amazon Polly
    - C. Amazon Transcribe
    - D. Amazon Translate

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: CloudFormation provisions resources from templates.
    </details>

5. Private subnet instances need outbound internet for patches but no inbound from internet:
    - A. NAT Gateway (+ proper routes/SGs)
    - B. Assign public IPs to all and open 0.0.0.0/0 inbound SSH
    - C. Remove the route table
    - D. Use only Amazon Glacier

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: NAT allows outbound from private subnets without inbound internet exposure.
    </details>

6. DDoS protection included at no extra cost for all customers:
    - A. AWS Shield Standard
    - B. Amazon Redshift RA3 only
    - C. Amazon Braket
    - D. AWS Ground Station

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Shield Standard is automatic/no additional charge; Advanced is paid.
    </details>

7. Filter SQL injection attempts against a public web app:
    - A. AWS WAF
    - B. Amazon Aurora Serverless alone
    - C. Amazon EFS alone
    - D. AWS Backup alone

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: WAF filters web exploits at Layer 7.
    </details>

8. Analytics team wants a data warehouse for complex BI SQL:
    - A. Amazon Redshift
    - B. Amazon SQS
    - C. AWS Certificate Manager alone
    - D. Amazon VPC Lattice alone

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Redshift is the managed data warehouse.
    </details>

9. Run containers without managing EC2 instances:
    - A. AWS Fargate
    - B. Only bare-metal without orchestration
    - C. Amazon S3 static hosting as containers
    - D. AWS Artifact

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Fargate provides serverless compute for containers.
    </details>

10. Developer wants the simplest path to upload a web app and let AWS handle capacity provisioning details:
    - A. AWS Elastic Beanstalk
    - B. Manually rack servers
    - C. AWS Snowmobile for every deploy
    - D. Amazon Macie for deploys

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Elastic Beanstalk simplifies application deployment and management.
    </details>

11. Which statement about elasticity is best?
    - A. Capacity grows and shrinks with demand automatically
    - B. You must buy peak capacity for 5 years always
    - C. Elasticity means the Ethernet cable stretches
    - D. It only applies to printers

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Elasticity is dynamic matching of resources to demand.
    </details>

12. Where do edge locations help most directly?
    - A. Content delivery / DNS performance near users
    - B. Replacing IAM
    - C. Replacing KMS
    - D. Billing Support plan selection only

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Edge locations support CloudFront and related edge services.
    </details>

13. Customer responsibility for S3 typically includes:
    - A. Configuring access policies and encryption choices for their data
    - B. Physically replacing AWS disk drives in the Region
    - C. Cooling the AWS facility
    - D. Rack power distribution

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Customers control data access configuration; AWS handles the underlying storage infrastructure.
    </details>

14. Visualize last month’s spend by service:
    - A. AWS Cost Explorer
    - B. Amazon Lex
    - C. Amazon Polly
    - D. AWS Snowball Edge Compute only

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Cost Explorer analyzes historical costs and usage.
    </details>

15. Which pair correctly matches service → use case? (Select TWO)
    - A. Amazon SNS → push notifications/pub-sub
    - B. Amazon SQS → decouple with queues
    - C. Amazon SNS → block storage volumes
    - D. Amazon SQS → DNS hosting
    - E. Amazon SNS → physical data truck

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answers: A and B

      Explanation: SNS is pub/sub messaging; SQS is queuing. Neither is block storage, DNS, or Snow devices.
    </details>

16. Least privilege means:
    - A. Grant only required permissions
    - B. Give AdministratorAccess to everyone
    - C. Share root credentials
    - D. Disable MFA for convenience

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Least privilege minimizes permissions to what the job needs.
    </details>

17. Hybrid connectivity for a quick encrypted tunnel over the internet:
    - A. AWS Site-to-Site VPN
    - B. Amazon S3 Transfer Acceleration only as the VPN
    - C. Amazon CloudFront invalidation
    - D. AWS Budgets

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Site-to-Site VPN encrypts traffic over the public internet to your VPC.
    </details>

18. Which service is primarily for configuration compliance history of AWS resources?
    - A. AWS Config
    - B. Amazon Kinesis Video Streams only
    - C. Amazon GameLift only
    - D. AWS Device Farm only

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Config tracks configurations and evaluates rules over time.
    </details>

19. A company must keep objects cheap for 7-year archive, restore rarely OK in hours:
    - A. S3 Glacier Flexible Retrieval or Deep Archive (as appropriate)
    - B. EC2 instance store as long-term archive
    - C. Security group rules as storage
    - D. CloudWatch Alarms as storage

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Glacier storage classes are designed for low-cost archival with longer retrieval times.
    </details>

20. Select TWO cloud value propositions. (Select TWO)
    - A. Stop guessing capacity
    - B. Go global in minutes
    - C. Mandatory CapEx for every experiment
    - D. Impossible elasticity
    - E. No shared responsibility ever

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answers: A and B

      Explanation: Classic AWS cloud benefits include stopping capacity guessing and global reach. CapEx-heavy experiments and “no shared responsibility” are wrong.
    </details>

21. Best first place for personalized best-practice recommendations on cost and security?
    - A. AWS Trusted Advisor
    - B. Amazon OpenSearch Service as the only tool
    - C. Amazon EMR alone
    - D. AWS Ground Station alone

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Trusted Advisor surfaces checks across cost, security, performance, fault tolerance, and service limits (feature depth depends on support plan).
    </details>

22. Which describes IaaS best?
    - A. You manage OS and apps; provider manages hardware/virtualization
    - B. Provider manages the complete business SaaS app only
    - C. There is no customer responsibility
    - D. It only means “email as a service”

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: EC2-style IaaS leaves OS/app responsibility with the customer.
    </details>

23. Amazon VPC is:
    - A. Your logically isolated virtual network in AWS
    - B. A physical truck
    - C. A support plan name
    - D. An S3 storage class

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: VPC is the foundational virtual network construct.
    </details>

24. Sustainability pillar encourages:
    - A. Reducing environmental impact of workloads
    - B. Maximizing idle always-on overprovisioning
    - C. Turning off all encryption
    - D. Ignoring rightsizing

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Sustainability focuses on minimizing environmental impact of cloud workloads.
    </details>

25. Passing score model for CLF-C02 is best described as:
    - A. Scaled score with 700 minimum; compensatory overall pass
    - B. Must score 100% in every domain
    - C. Pass if you answer 1 question
    - D. No scaled scoring exists

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: AWS uses scaled scoring (pass at 700) with compensatory scoring across domains.
    </details>

---

### Quick self-score

| Combined score ( /50 ) | Result |
| --- | --- |
| 45–50 | Strong — review only weak service families |
| 35–44 | Good — drill Security + Technology misses |
| 25–34 | Re-read Parts 0, 3, and 4 |
| Below 25 | Restart Part 0 definitions, then retry |
