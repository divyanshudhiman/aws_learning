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
