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
