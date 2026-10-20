# AWS Certified Cloud Practitioner (CLF-C02) Study Guide

Structured personal study notes for the CLF-C02 exam — same study pattern as the AIF-C01 guide: starter definitions, domain Parts, glossary, and scenario practice with answers.

**Edition note:** Original study notes organized as Parts 0–7 for GitHub Pages. Not an official AWS publication. Practice questions are original scenario-style items for learning (not exam dumps).

**Companion guide:** [AI Practitioner (AIF-C01)](../index.html)

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
