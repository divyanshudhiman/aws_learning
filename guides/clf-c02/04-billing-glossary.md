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
