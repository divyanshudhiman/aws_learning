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
