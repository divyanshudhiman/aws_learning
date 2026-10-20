# AWS Certified AI Practitioner (AIF-C01) Study Guide

Personal study notes for the AIF-C01 exam.

**Source material:** Adapted from [jwalsh/aif-c01](https://github.com/jwalsh/aif-c01) by Jason Walsh, licensed under the [MIT License](https://github.com/jwalsh/aif-c01/blob/main/LICENSE). Copyright (c) Jason Walsh.

---

<!-- source: doc/aif-c01-notes.org -->

# AWS Certified AI Practitioner (AIF-C01) Exam Notes

## Course Overview

### Introduction

- Course expectations
- AI definition and importance
- AWS Cloud overview

### Course Structure

- Theoretical concepts
- Hands-on practice
- Quizzes and assessments

### AWS Account Setup

- Creating an AWS account
- Setting up budgets
- Troubleshooting activation

## Domain 1: Fundamentals of AI and ML

### Key Concepts

- Artificial Intelligence
- Machine Learning
- Deep Learning
- Neural Networks

### ML Types

- Supervised Learning
- Unsupervised Learning
- Reinforcement Learning

### Data Types and Handling

- Labeled and Unlabeled data
- Structured and Unstructured data
- Time-series, Image, Text data
- Training data characteristics

### ML Project Lifecycle

- Data collection and preparation
- Model selection and training
- Evaluation and deployment
- Monitoring and maintenance

## Domain 2: Fundamentals of Generative AI

### Key Concepts

- Tokens and Embeddings
- Prompt Engineering
- Transformer Architecture
- Foundation Models

### Amazon Bedrock

- Overview and capabilities
- Foundation Model (FM) selection
- FM Evaluation techniques
- RAG & Knowledge Base implementation

### Use Cases

- Image and Text Generation
- Summarization and Translation
- Chatbots and Customer Service

### Advanced Concepts

- Fine-tuning models
- Agents in Bedrock
- GuardRails implementation

## Domain 3: Applications of Foundation Models

### Selection Criteria

- Cost considerations
- Modality requirements
- Latency expectations
- Model Size and Complexity

### Techniques

- Retrieval Augmented Generation (RAG)
- Prompt Engineering best practices
- Fine-tuning methods and use cases

### Evaluation Metrics

- ROUGE for summarization
- BLEU for translation
- BERTScore for semantic similarity

### Integration with AWS Services

- SageMaker integration
- Lambda function deployment
- API Gateway setup

## Domain 4: Guidelines for Responsible AI

### Key Features

- Bias detection and mitigation
- Fairness in AI systems
- Inclusivity considerations
- Robustness and Safety measures

### Ethical Considerations

- Transparency in AI decision-making
- Accountability frameworks
- Privacy protection strategies

### Legal and Compliance

- Legal risks and mitigation
- Dataset characteristics and implications
- Bias effects and monitoring techniques

### MLOps Best Practices

- Continuous integration for ML
- Deployment strategies
- Monitoring and logging

## Domain 5: Security, Compliance, and Governance

### AWS Security Services

- Identity and Access Management (IAM)
- Key Management Service (KMS)
- Amazon Macie for data discovery
- CloudTrail for auditing

### Shared Responsibility Model

- AWS responsibilities
- Customer responsibilities
- Security best practices

### Compliance Frameworks

- ISO certifications
- SOC compliance
- GDPR considerations
- Algorithm accountability

### Data Governance

- Data lifecycle management
- Logging and monitoring strategies
- Access control and encryption

## AWS Managed AI Services

### Amazon Comprehend

- Natural Language Processing capabilities
- Use cases and limitations

### Amazon Translate

- Machine translation features
- Integration with other services

### Amazon Transcribe

- Speech-to-text capabilities
- Customization options

### Amazon Polly

- Text-to-speech service
- Voice selection and SSML

### Amazon Rekognition

- Image and video analysis
- Face detection and comparison

### Amazon Forecast

- Time-series forecasting
- Dataset types and model selection

### Amazon Personalize

- Recommendation systems
- Integration and deployment

### Amazon Textract

- Document analysis and data extraction
- Forms and tables processing

### Amazon Kendra

- Enterprise search service
- Natural language querying

### Amazon SageMaker

- End-to-end ML platform
- Built-in algorithms and custom models
- Deployment and monitoring

## Exam Preparation

### Study Strategies

- Review key concepts regularly
- Practice with hands-on labs
- Utilize AWS documentation

### Practice Exams

- Take multiple practice tests
- Analyze and learn from mistakes
- Time management strategies

### Exam Tips

- Read questions carefully
- Eliminate obviously wrong answers
- Manage time effectively during the exam

## Tasks [0/5]

- [ ] Complete all course videos and hands-on labs
- [ ] Review AWS documentation for all mentioned services
- [ ] Take and review practice exams
- [ ] Create flashcards for key concepts and services
- [ ] Schedule and take the certification exam

## Resources

- [[https://aws.amazon.com/certification/certified-ai-ml-specialty/][AWS Certified AI Practitioner Certification]]
- [[https:/*docs.aws.amazon.com*][AWS Documentation]]
- [[https://aws.amazon.com/whitepapers/][AWS Whitepapers]]
- Course materials and practice tests

```emacs-lisp
  (setq org-todo-keywords
        '((sequence "TODO" "IN-PROGRESS" "REVIEW" "|" "DONE" "ARCHIVED")))
```

---

<!-- source: doc/aws-ai-practitioner-course-outline.org -->

# AWS Certified AI Practitioner (AIF-C01) Course Outline

## Artificial Intelligence & Course Introduction

### What to expect from this course

### Private Course Feedback Link

### Important: Course Structure

### Important Message: Udemy

### What is Artificial Intelligence (AI)?

### About your Instructor

## Code & Slides Download

### Code & Slides Download

## Introduction to AWS & Cloud Computing

### Section Introduction

### Traditional IT - Overview

### What is Cloud Computing?

### The Different Types of Cloud Computing

### AWS Cloud Overview

### Creating an AWS Account

### AWS Account Activation Troubleshooting

### Tour of the Console & Services in AWS

### Shared Responsibility Model & AWS Acceptable Policy

### Quiz: Introduction to AWS & Cloud Computing

## Course Cost & AWS Budget Setup

### Course Cost

### AWS Budget Setup

## Amazon Bedrock and Generative AI (GenAI)

### Section Introduction

### What is Generative AI (GenAI)?

### Amazon Bedrock - Overview

### Amazon Bedrock - Hands On

### Amazon Bedrock - Foundation Model (FM)

### Amazon Bedrock - Foundation Model (FM) - Hands On

### Amazon Bedrock - Fine-Tuning a Model

### Amazon Bedrock - FM Evaluation

### Amazon Bedrock - FM Evaluation - Hands On

### Amazon Bedrock - RAG & Knowledge Base

### Amazon Bedrock - RAG & Knowledge Base - Hands On

### Amazon Bedrock - RAG & Knowledge Base - Complete Setup - Hands On

### More GenAI Concepts

### Amazon Bedrock - GuardRails

### Amazon Bedrock - GuardRails - Hands On

### Amazon Bedrock - Agents

### Amazon Bedrock - Pricing & Other Features

### Amazon Bedrock - AI Stylist - Hands On

### Quiz: Amazon Bedrock and Generative AI (GenAI)

## Prompt Engineering

### Section Introduction

### What is Prompt Engineering?

### Prompt Engineering - Hands On

### Prompt Performance Optimization

### Prompt Performance Optimization - Hands On

### Prompt Engineering Techniques

### Prompt Templates

### Quiz: Prompt Engineering

## Amazon Q - Deep Dive

### Section Introduction

### Amazon Q Business

### Amazon Q Business - Hands On

### Amazon Q Apps

### Amazon Q Apps - Hands On

### Amazon Q Business - Hands On - Cleanup

### Amazon Q Developer

### Amazon Q Developer - Hands On

### PartyRock

### Quiz: Amazon Q

## Artificial Intelligence (AI) & Machine Learning (ML)

### Section Introduction

### AI, ML, Deep Learning, and GenAI

### Training Data

### Supervised Learning

### Unsupervised Learning

### Reinforcement Learning

### RLHF - Reinforcement Learning from Human Feedback

### Model Fit, Bias, and Variance

### Model Evaluation Metrics

### Machine Learning - Inferencing

### Phases of a Machine Learning Project

### Quiz: Artificial Intelligence (AI) & Machine Learning (ML)

## AWS Managed AI Services

### Section Introduction

### Why AWS Managed Services?

### Amazon Comprehend

### Amazon Comprehend - Hands On

### Amazon Translate

### Amazon Translate - Hands On

### Amazon Transcribe

### Amazon Polly

### Amazon Polly - Hands On

### Amazon Rekognition

### Amazon Forecast

### Amazon Lex

### Amazon Lex - Hands On

### Amazon Personalize

### Amazon Textract

### Amazon Textract - Hands On

### Amazon Kendra

### Amazon Mechanical Turk

### Amazon Augmented AI

### Amazon Augmented AI - Hands On

### AWS DeepRacer

### AWS DeepRacer - Hands On

### Amazon Comprehend Medical & Transcribe Medical

### Amazon Comprehend Medical & Transcribe Medical - Hands On

### Amazon's Hardware for AI

### Amazon's Hardware for AI - Hands On

### Quiz: AWS Managed AI Services

## Amazon SageMaker - Deep Dive

### Section Introduction

### Amazon SageMaker

### Amazon SageMaker - Hands On

### Amazon SageMaker - Data Tools

### Amazon SageMaker - Models and Humans

### Amazon SageMaker - Governance

### Amazon SageMaker - Consoles

### Amazon SageMaker - Summary

### Quiz: Amazon SageMaker

## AI Challenges and Responsibilities

### Section Introduction

### AI Challenges and Responsibilities - Overview

### Responsible AI

### GenAI Challenges

### Compliance for AI

### Governance for AI

### Security and Privacy for AI

### GenAI Security Scoping Matrix

### MLOps

### Quiz: AI Challenges and Responsibilities

## AWS Security Services

### Section Introduction

### IAM Introduction: Users, Groups, Policies

### IAM Users & Groups - Hands On

### IAM Policies

### IAM Policies - Hands On

### IAM Roles

### IAM Roles - Hands On

### Amazon EC2

### Create an EC2 Instance with EC2 User Data to have a Website - Hands On

### AWS Lambda

### AWS Lambda - Hands On

### Amazon Macie

### AWS Config

### Amazon Inspector

### AWS CloudTrail

### AWS CloudTrail - Hands On

### AWS Artifact

### AWS Trusted Advisor

### AWS Network Security

### AWS Security Services - Summary

### Quiz: AWS Security Services

## Preparing for the Exam + Practice Exam - AWS Certified AI Practitioner

### State of Learning Checkpoint

### Example Sample Exam Questions Walkthrough

### Exam Walkthrough and Signup

### Save 50% on your AWS Exam Cost!

### Get an Extra 30 Minutes on your AWS Exam - Non Native English Speakers only

### Practice Exam - AWS Certified AI Practitioner

### AWS Certification Paths

## Congratulations

### Congratulations

### Bonus Lecture

## Tasks [0/5]

- [ ] Complete all course videos and hands-on labs
- [ ] Review AWS documentation for all mentioned services
- [ ] Take and review practice exams
- [ ] Schedule the certification exam
- [ ] Review weak areas identified in practice exams

## Resources

- [[https://aws.amazon.com/certification/certified-ai-ml-specialty/][AWS Certified AI Practitioner Certification]]
- [[https:/*docs.aws.amazon.com*][AWS Documentation]]
- Course materials and practice tests

```emacs-lisp
  (setq org-todo-keywords
        '((sequence "TODO" "IN-PROGRESS" "REVIEW" "|" "DONE" "ARCHIVED")))
```

---

<!-- source: aws-services-overview.org -->

# AWS Services Overview

## AWS Services Overview

### EC2

#### List Instances

```shell
  aws ec2 describe-instances | jq -r '.Reservations[].Instances[].InstanceId'
```

| i-09a85540250dd5f7f |
| i-0b6b20ba6db18df32 |
| i-09ce4c8ebcfcff4cf |

#### List Volumes

```shell
  aws ec2 describe-volumes | jq -r '.Volumes[].VolumeId'
```

| vol-0e042966ec7cfd553 |
| vol-010145d8448cad2a4 |
| vol-0e1e871141f867720 |

#### List VPCs

```shell
  aws ec2 describe-vpcs | jq -r '.Vpcs[].VpcId'
```

| vpc-0217a5e9b879a8c13 |
| vpc-f0fc4e8a          |

### S3

#### List Buckets

```shell
  aws s3 ls | grep aif
```

| 2024-09-04 | 08:56:23 | aif-c01            |
| 2024-09-17 | 12:39:43 | aif-c01-input      |
| 2024-09-04 | 19:20:17 | aif-c01-jasonwalsh |
| 2024-09-04 | 19:18:18 | aif-c01-jwalsh     |
| 2024-09-17 | 12:39:44 | aif-c01-output     |

#### List Buckets (API)

```shell
  aws s3api list-buckets | jq -r '.Buckets[].Name | select(startswith("aif") or startswith("mla"))'
```

| aif-c01            |
| aif-c01-input      |
| aif-c01-jasonwalsh |
| aif-c01-jwalsh     |
| aif-c01-output     |

### IAM

#### List Users

```shell
  aws iam list-users | jq -r '.Users[].UserName'
```

| dev    |
| jwalsh |
| prod   |
| qat    |

#### List Roles

```shell
aws iam list-roles | jq -r '.Roles[].RoleName | select(
    startswith("aif-c01") or
    startswith("mla-") or
    contains("SageMaker") or
    contains("Bedrock") or
    contains("Comprehend") or
    contains("Translate") or
    contains("DeepLens") or
    contains("RoboMaker") or
    contains("MLWorkflow") or
    contains("MLOps")
)'
```

| A2ISageMaker-ExecutionRole-20240911T190545                       |
| aif-c01-batch-role                                               |
| aif-c01-bedrock-cloudwatch                                       |
| AmazonBedrockExecutionRoleForAgentFlowEval                       |
| AmazonBedrockExecutionRoleForAgents_6TYTN6S0PBE                  |
| AmazonBedrockExecutionRoleForAgents_9RZ7WT2H7L9                  |
| AmazonBedrockExecutionRoleForAgents_B2K8YVKZT9O                  |
| AmazonBedrockExecutionRoleForAgents_G43OC4197X                   |
| AmazonBedrockExecutionRoleForAgents_GJS4XAN7EQK                  |
| AmazonBedrockExecutionRoleForAgents_IQYJI0VJ819                  |
| AmazonBedrockExecutionRoleForAgents_JH1R5YCMQ                    |
| AmazonBedrockExecutionRoleForAgents_JPXMYT1RME                   |
| AmazonBedrockExecutionRoleForAgents_OENM3J46LQF                  |
| AmazonBedrockExecutionRoleForAgents_OYF0TFY67C9                  |
| AmazonBedrockExecutionRoleForAgents_ROL4TVUQ6ZK                  |
| AmazonBedrockExecutionRoleForAgents_RQG76BFYU0Q                  |
| AmazonBedrockExecutionRoleForAgents_YE04U6EGG7E                  |
| AmazonBedrockExecutionRoleForFlows_81RENNE1Y5                    |
| AmazonBedrockExecutionRoleForFlows_BIZVT5E45B                    |
| AmazonBedrockExecutionRoleForKnowledgeBase_0odwt                 |
| AmazonBedrockExecutionRoleForKnowledgeBase_4uy41                 |
| AmazonBedrockExecutionRoleForKnowledgeBase_ci1wt                 |
| AmazonBedrockExecutionRoleForKnowledgeBase_fatg9                 |
| AmazonComprehendServiceRole-aif-cio                              |
| AmazonComprehendServiceRole-aif-cio-outputer                     |
| AmazonComprehendServiceRole-aif-cio-outputerj                    |
| AmazonComprehendServiceRole-asdfasdf                             |
| AmazonComprehendServiceRole-categories                           |
| AmazonComprehendServiceRole-ClassifyProjects                     |
| AmazonSageMaker-ExecutionRole-20190123T172234                    |
| AmazonSageMaker-ExecutionRole-20240918T171879                    |
| AmazonSagemakerCanvasBedrockRole-20240918T171879                 |
| AmazonSageMakerCanvasEMRSExecutionAccess-20240918T171879         |
| AmazonSageMakerServiceCatalogProductsApiGatewayRole              |
| AmazonSageMakerServiceCatalogProductsCloudformationRole          |
| AmazonSageMakerServiceCatalogProductsCodeBuildRole               |
| AmazonSageMakerServiceCatalogProductsCodePipelineRole            |
| AmazonSageMakerServiceCatalogProductsEventsRole                  |
| AmazonSageMakerServiceCatalogProductsExecutionRole               |
| AmazonSageMakerServiceCatalogProductsFirehoseRole                |
| AmazonSageMakerServiceCatalogProductsGlueRole                    |
| AmazonSageMakerServiceCatalogProductsLambdaRole                  |
| AmazonSageMakerServiceCatalogProductsLaunchRole                  |
| AmazonSageMakerServiceCatalogProductsUseRole                     |
| AmazonTranslateServiceRole-localization                          |
| AmazonTranslateServiceRole-localizationasfasdf                   |
| AWSDeepLensGreengrassGroupRole                                   |
| AWSDeepLensGreengrassRole                                        |
| AWSDeepLensLambdaRole                                            |
| AWSDeepLensServiceRole                                           |
| AWSRoboMakerDeepRacer-15518159-LambdaExecutionRole-1U972HGKRIR1I |
| AWSRoboMakerDeepRacer-1551815998-SimulationJobRole-11N5TFQ2YCT73 |
| AWSServiceRoleForAmazonSageMakerNotebooks                        |
| AWSServiceRoleForRoboMaker                                       |
| ExecuteRoleMLWorkflow                                            |
| mla-sagemaker-role                                               |
| SageMaker-MLOpsEngineer                                          |

#### List Groups

```shell
  aws iam list-groups | jq -r '.Groups[].GroupName'
```

| MachineLearning |
| Serverless      |

### Lambda

#### List Functions

```shell
  aws lambda list-functions | jq -r '.Functions[].FunctionName | select(startswith("mla-c01") or startswith("aif-c01"))'
```

### CloudFormation

#### List Stacks

```shell
  aws cloudformation list-stacks | jq -r '.StackSummaries[].StackName | select(
      contains("mla-c01") or
      contains("aif-c01") or
      contains("mla-") or
      contains("aif-") or
      contains("ml-") or
      contains("ai-") or
      contains("sagemaker") or
      contains("bedrock") or
      contains("comprehend") or
      contains("rekognition")
  )'
```

### RDS

#### List DB Instances

```shell
  aws rds describe-db-instances | jq -r '.DBInstances[].DBInstanceIdentifier'
```

: database-1

### DynamoDB

#### List Tables

```shell
  aws dynamodb list-tables | jq -r '.TableNames[]'
```

### CloudWatch

#### List Metrics

```shell
  aws cloudwatch list-metrics | jq -r '.Metrics[].MetricName' | sort | uniq | grep -E 'AI|ML|Predict|Inference|SageMaker|Comprehend|Rekognition|Bedrock|Polly|Textract|Transcribe|Translate'
```

: PredictCount

### SQS

#### List Queues

```shell
  aws sqs list-queues | jq -r '.QueueUrls[] | select(
      contains("aif-c01") or
      contains("ml-") or
      contains("ai-") or
      contains("sagemaker") or
      contains("comprehend") or
      contains("rekognition") or
      contains("textract") or
      contains("polly") or
      contains("transcribe") or
      contains("translate") or
      contains("bedrock") or
      contains("inference") or
      contains("prediction")
  )'
```

### SNS

#### List Topics

```shell
  aws sns list-topics | jq -r '.Topics[].TopicArn | select(
      contains("aif-c01") or
      contains("mla-c01") or
      contains("ml-") or
      contains("ai-") or
      contains("sagemaker") or
      contains("comprehend") or
      contains("rekognition") or
      contains("textract") or
      contains("polly") or
      contains("transcribe") or
      contains("translate") or
      contains("bedrock") or
      contains("inference") or
      contains("prediction")
  )'
```

### ECS (Elastic Container Service)

#### List Clusters

```shell
  aws ecs list-clusters | jq -r '.clusterArns[]'
```

#### List Services

```shell
  aws ecs list-services --cluster default | jq -r '.serviceArns[]'
```

#### List Task Definitions

```shell
  aws ecs list-task-definitions | jq -r '.taskDefinitionArns[]'
```

### EKS (Elastic Kubernetes Service)

#### List Clusters

```shell
  aws eks list-clusters | jq -r '.clusters[]'
```

### ECR (Elastic Container Registry)

#### List Repositories

```shell
  aws ecr describe-repositories | jq -r '.repositories[].repositoryName'
```

### Route 53

#### List Hosted Zones

```shell
  aws route53 list-hosted-zones | jq -r '.HostedZones[].Name'
```

: watermid.com.

#### List Health Checks

```shell
aws route53 list-health-checks | jq -r '.HealthChecks[].Id'
```

### CloudFront

#### List Distributions

```shell
  aws cloudfront list-distributions | jq -r '.DistributionList.Items[].Id'
```

### Elastic Beanstalk

#### List Applications

```shell
  aws elasticbeanstalk describe-applications | jq -r '.Applications[].ApplicationName'
```

#### List Environments

```shell
  aws elasticbeanstalk describe-environments | jq -r '.Environments[].EnvironmentName'
```

### API Gateway

#### List APIs

```shell
  aws apigateway get-rest-apis | jq -r '.items[].name'
```

### Step Functions

#### List State Machines

```shell
  aws stepfunctions list-state-machines | jq -r '.stateMachines[].name'
```

: jwalsh-ml-states

### Kinesis

#### List Streams

```shell
  aws kinesis list-streams | jq -r '.StreamNames[]'
```

### Elasticsearch Service

#### List Domains

```shell
  aws es list-domain-names | jq -r '.DomainNames[].DomainName'
```

### ElastiCache

#### List Cache Clusters

```shell
  aws elasticache describe-cache-clusters | jq -r '.CacheClusters[].CacheClusterId'
```

### Redshift

#### List Clusters

```shell
  aws redshift describe-clusters | jq -r '.Clusters[].ClusterIdentifier'
```

### Athena

#### List Work Groups

```shell
  aws athena list-work-groups | jq -r '.WorkGroups[].Name'
```

: primary

#### List Named Queries

```shell
  aws athena list-named-queries | jq -r '.NamedQueries'
```

: null

### Glue

#### List Databases

```shell
  aws glue get-databases | jq -r '.DatabaseList[].Name'
```

#### List Tables

```shell
  aws glue get-tables --database-name default | jq -r '.TableList[].Name'
```

#### List Jobs

```shell
  aws glue get-jobs | jq -r '.Jobs[].Name'
```

: mla-job

### EMR (Elastic MapReduce)

#### List Clusters

```shell
  aws emr list-clusters | jq -r '.Clusters[].Id'
```

### Systems Manager

#### List Parameters

```shell
  aws ssm describe-parameters | jq -r '.Parameters[].Name | select(
      startswith("/aif-c01/") or
      startswith("/mla-c01/") or
      contains("ml-") or
      contains("ai-") or
      contains("sagemaker") or
      contains("comprehend") or
      contains("rekognition") or
      contains("textract") or
      contains("polly") or
      contains("transcribe") or
      contains("translate") or
      contains("bedrock") or
      contains("inference") or
      contains("prediction")
  )'
```

#### List Documents

```shell
  aws ssm list-documents | jq -r '.DocumentIdentifiers[].Name | select(
      contains("AI") or
      contains("ML") or
      contains("SageMaker") or
      contains("Comprehend") or
      contains("Rekognition") or
      contains("Textract") or
      contains("Polly") or
      contains("Transcribe") or
      contains("Translate") or
      contains("Bedrock") or
      contains("Inference") or
      contains("Prediction") or
      contains("MachineLearning")
  )'
```

| AWS-DisableSageMakerNotebookRootAccess                 |
| AWSConformancePacks-OperationalBestPracticesforAIandML |

### Secrets Manager

#### List Secrets

```shell
  aws secretsmanager list-secrets | jq -r '.SecretList[].Name'
```

### KMS (Key Management Service)

#### List Keys

```shell
  aws kms list-keys | jq -r '.Keys[].KeyId' | wc -l
```

: 7

#### List Aliases

```shell
  aws kms list-aliases | jq -r '.Aliases[].AliasName' | wc -l 
```

: 15

### CloudTrail

#### List Trails

```shell
  aws cloudtrail describe-trails | jq -r '.trailList[].Name'
```

### Config

#### List Config Rules

```shell
  aws configservice describe-config-rules | jq -r '.ConfigRules[].ConfigRuleName'
```

### WAF (Web Application Firewall)

#### List Web ACLs

```shell
aws waf list-web-acls | jq -r '.WebACLs[].Name'
```

### Cognito

#### List User Pools

```shell
aws cognito-idp list-user-pools --max-results 60 | jq -r '.UserPools[].Name'
```

### SageMaker

#### List Notebook Instances

```shell
aws sagemaker list-notebook-instances | jq -r '.NotebookInstances[].NotebookInstanceName'
```

#### List Training Jobs

```shell
aws sagemaker list-training-jobs | jq -r '.TrainingJobSummaries[].TrainingJobName'
```

#### List Models

```shell
aws sagemaker list-models | jq -r '.Models[].ModelName'
```

### Comprehend

#### List Document Classification Jobs

```shell
aws comprehend list-document-classification-jobs | jq -r '.DocumentClassificationJobPropertiesList[].JobName'
```

#### List Entity Recognizers

```shell
aws comprehend list-entity-recognizers | jq -r '.EntityRecognizerPropertiesList[].EntityRecognizerArn'
```

### Rekognition

#### List Collections

```shell
aws rekognition list-collections | jq -r '.CollectionIds[]'
```

### Translate

#### List Translation Jobs

```shell
aws translate list-text-translation-jobs | jq -r '.TextTranslationJobPropertiesList[].JobName'
```

### Polly

#### List Voices

```shell
aws polly describe-voices | jq -r '.Voices[].Id'
```

### Lex

#### List Bots

```shell
aws lex-models get-bots | jq -r '.bots[].name'
```

### Forecast

#### List Datasets

```shell
aws forecast list-datasets | jq -r '.Datasets[].DatasetArn'
```

#### List Predictors

```shell
aws forecast list-predictors | jq -r '.Predictors[].PredictorArn'
```

### IoT Core

#### List Things

```shell
aws iot list-things | jq -r '.things[].thingName'
```

#### List Policies

```shell
aws iot list-policies | jq -r '.policies[].policyName'
```

### AppSync

#### List GraphQL APIs

```shell
aws appsync list-graphql-apis | jq -r '.graphqlApis[].name'
```

### Neptune

#### List DB Clusters

```shell
aws neptune describe-db-clusters | jq -r '.DBClusters[].DBClusterIdentifier'
```

### DocumentDB

#### List DB Clusters

```shell
aws docdb describe-db-clusters | jq -r '.DBClusters[].DBClusterIdentifier'
```

### Elastic Beanstalk

#### List Applications

```shell
aws elasticbeanstalk list-applications | jq -r '.Applications[].ApplicationName'
```

#### List Environments

```shell
aws elasticbeanstalk list-environments | jq -r '.Environments[].EnvironmentName'
```

### AWS Batch

#### List Job Definitions

```shell
aws batch list-job-definitions | jq -r '.jobDefinitions[].jobDefinitionName'
```

#### List Job Queues

```shell
aws batch list-job-queues | jq -r '.jobQueues[].jobQueueName'
```

#### List Compute Environments

```shell
aws batch list-compute-environments | jq -r '.computeEnvironments[]'
```

### AWS Transfer Family

#### List Servers

```shell
aws transfer list-servers | jq -r '.Servers[].ServerId'
```

### AWS Backup

#### List Backup Vaults

```shell
aws backup list-backup-vaults | jq -r '.BackupVaultList[].BackupVaultName'
```

#### List Backup Plans

```shell
aws backup list-backup-plans | jq -r '.BackupPlansList[].BackupPlanName'
```

### AWS DataSync

#### List Tasks

```shell
aws datasync list-tasks | jq -r '.Tasks[].TaskArn'
```

#### List Locations

```shell
aws datasync list-locations | jq -r '.Locations[].LocationArn'
```

### AWS Direct Connect

#### List Connections

```shell
aws directconnect describe-connections | jq -r '.connections[].connectionName'
```

#### List Virtual Interfaces

```shell
aws directconnect describe-virtual-interfaces | jq -r '.virtualInterfaces[].virtualInterfaceName'
```

### AWS Global Accelerator

#### List Accelerators

```shell
aws globalaccelerator list-accelerators | jq -r '.Accelerators[].Name'
```

### AWS App Mesh

#### List Meshes

```shell
aws appmesh list-meshes | jq -r '.meshes[].meshName'
```

### AWS Cloud Map

#### List Namespaces

```shell
aws servicediscovery list-namespaces | jq -r '.Namespaces[].Name'
```

### AWS CodeBuild

#### List Projects

```shell
aws codebuild list-projects | jq -r '.projects[]'
```

### AWS CodeCommit

#### List Repositories

```shell
aws codecommit list-repositories | jq -r '.repositories[].repositoryName'
```

### AWS CodeDeploy

#### List Applications

```shell
aws deploy list-applications | jq -r '.applications[]'
```

### AWS CodePipeline

#### List Pipelines

```shell
aws codepipeline list-pipelines | jq -r '.pipelines[].name'
```

### AWS X-Ray

#### List Groups

```shell
aws xray get-groups | jq -r '.Groups[].GroupName'
```

### AWS Certificate Manager (ACM)

#### List Certificates

```shell
aws acm list-certificates | jq -r '.CertificateSummaryList[].DomainName'
```

### AWS CloudHSM

#### List Clusters

```shell
aws cloudhsm describe-clusters | jq -r '.Clusters[].ClusterId'
```

### AWS Fargate

#### List Task Definitions

```shell
aws ecs list-task-definitions | jq -r '.taskDefinitionArns[]'
```

### AWS Amplify

#### List Apps

```shell
aws amplify list-apps | jq -r '.apps[].name'
```

### Amazon MQ

#### List Brokers

```shell
aws mq list-brokers | jq -r '.BrokerSummaries[].BrokerName'
```

### Amazon Managed Streaming for Apache Kafka (MSK)

#### List Clusters

```shell
aws kafka list-clusters | jq -r '.ClusterInfoList[].ClusterName'
```

### Amazon Managed Workflows for Apache Airflow (MWAA)

#### List Environments

```shell
aws mwaa list-environments | jq -r '.Environments[]'
```

### AWS Lake Formation

#### List Data Lake Settings

```shell
aws lakeformation list-data-lake-settings | jq -r '.DataLakeSettings.DataLakeAdmins[].DataLakePrincipalIdentifier'
```

### Amazon Managed Blockchain

#### List Networks

```shell
aws managedblockchain list-networks | jq -r '.Networks[].Name'
```

### AWS Elemental MediaLive

#### List Channels

```shell
aws medialive list-channels | jq -r '.Channels[].Name'
```

### AWS Elemental MediaConvert

#### List Queues

```shell
aws mediaconvert list-queues | jq -r '.Queues[].Name'
```

### AWS Elemental MediaPackage

#### List Channels

```shell
aws mediapackage list-channels | jq -r '.Channels[].Id'
```

### AWS Elemental MediaStore

#### List Containers

```shell
aws mediastore list-containers | jq -r '.Containers[].Name'
```

### Amazon Timestream

#### List Databases

```shell
aws timestream-write list-databases | jq -r '.Databases[].DatabaseName'
```

### AWS IoT Analytics

#### List Datasets

```shell
aws iotanalytics list-datasets | jq -r '.datasetSummaries[].datasetName'
```

### AWS IoT Events

#### List Detector Models

```shell
aws iotevents list-detector-models | jq -r '.detectorModelSummaries[].detectorModelName'
```

### AWS IoT SiteWise

#### List Assets

```shell
aws iotsitewise list-assets | jq -r '.assetSummaries[].name'
```

### Amazon Kendra

#### List Indices

```shell
aws kendra list-indices | jq -r '.IndexConfigurationSummaryItems[].Name'
```

### Amazon Managed Grafana

#### List Workspaces

```shell
aws grafana list-workspaces | jq -r '.workspaces[].name'
```

### Amazon Managed Service for Prometheus

#### List Workspaces

```shell
aws amp list-workspaces | jq -r '.workspaces[].alias'
```
### AWS Outposts

#### List Outposts

```shell
aws outposts list-outposts | jq -r '.Outposts[].OutpostId'
```

### AWS Wavelength

#### List Wavelength Zones

```shell
aws ec2 describe-availability-zones --filters Name=opt-in-status,Values=opted-in --query 'AvailabilityZones[?GroupName==`Wavelength`].ZoneName' | jq -r '.[]'
```

### AWS Local Zones

#### List Local Zones

```shell
aws ec2 describe-availability-zones --filters Name=opt-in-status,Values=opted-in --query 'AvailabilityZones[?GroupName==`Local Zones`].ZoneName' | jq -r '.[]'
```

### AWS Snowball

#### List Jobs

```shell
aws snowball list-jobs | jq -r '.JobListEntries[].JobId'
```

### AWS Storage Gateway

#### List Gateways

```shell
aws storagegateway list-gateways | jq -r '.Gateways[].GatewayARN'
```

### AWS DataSync

#### List Tasks

```shell
aws datasync list-tasks | jq -r '.Tasks[].TaskArn'
```

### AWS Elastic Disaster Recovery (DRS)

#### List Recovery Instances

```shell
aws drs describe-recovery-instances | jq -r '.items[].recoveryInstanceID'
```

### Amazon Managed Blockchain

#### List Networks

```shell
aws managedblockchain list-networks | jq -r '.Networks[].Id'
```

### AWS Amplify

#### List Apps

```shell
aws amplify list-apps | jq -r '.apps[].name'
```

### AWS App Runner

#### List Services

```shell
aws apprunner list-services | jq -r '.ServiceSummaryList[].ServiceName'
```

### AWS AppConfig

#### List Applications

```shell
aws appconfig list-applications | jq -r '.Items[].Id'
```

### AWS AppFlow

#### List Flows

```shell
aws appflow list-flows | jq -r '.flows[].flowName'
```

### AWS Application Discovery Service

#### List Configurations

```shell
aws discovery list-configurations --configuration-type SERVER | jq -r '.configurations[].configurationId'
```

### AWS CodeArtifact

#### List Domains

```shell
aws codeartifact list-domains | jq -r '.domains[].name'
```

### AWS CodeStar

#### List Projects

```shell
aws codestar list-projects | jq -r '.projects[].projectId'
```

### AWS Compute Optimizer

#### List Recommendations

```shell
aws compute-optimizer get-ec2-instance-recommendations | jq -r '.instanceRecommendations[].instanceName'
```

### AWS Data Exchange

#### List Data Sets

```shell
aws dataexchange list-data-sets | jq -r '.DataSets[].Name'
```

### AWS Data Pipeline

#### List Pipelines

```shell
aws datapipeline list-pipelines | jq -r '.pipelineIdList[].name'
```

### AWS DataBrew

#### List Jobs

```shell
aws databrew list-jobs | jq -r '.Jobs[].Name'
```

### AWS DeepComposer

#### List Compositions

```shell
aws deepcomposer list-compositions | jq -r '.compositions[].compositionName'
```

### AWS DeepLens

#### List Projects

```shell
aws deeplens list-projects | jq -r '.Projects[].Name'
```

### AWS DeepRacer

#### List Models

```shell
aws deepracer list-models | jq -r '.Models[].ModelName'
```

### AWS Device Farm

#### List Projects

```shell
aws devicefarm list-projects | jq -r '.projects[].name'
```

### AWS Direct Connect

#### List Connections

```shell
aws directconnect describe-connections | jq -r '.connections[].connectionName'
```

### AWS Fault Injection Simulator

#### List Experiments

```shell
aws fis list-experiments | jq -r '.experiments[].id'
```

### AWS Global Accelerator

#### List Accelerators

```shell
aws globalaccelerator list-accelerators | jq -r '.Accelerators[].Name'
```

### AWS Glue DataBrew

#### List Datasets

```shell
aws databrew list-datasets | jq -r '.Datasets[].Name'
```

### AWS Ground Station

#### List Satellites

```shell
aws groundstation list-satellites | jq -r '.satellites[].satelliteId'
```

### AWS Health

#### List Events

```shell
aws health describe-events | jq -r '.events[].eventTypeCode'
```

### AWS IoT 1-Click

#### List Devices

```shell
aws iot1click-devices list-devices | jq -r '.Devices[].DeviceId'
```

### AWS IoT Analytics

#### List Channels

```shell
aws iotanalytics list-channels | jq -r '.channelSummaries[].channelName'
```

### AWS IoT Core Device Advisor

#### List Suite Definitions

```shell
aws iotdeviceadvisor list-suite-definitions | jq -r '.suiteDefinitionInformationList[].suiteDefinitionId'
```

### AWS IoT Events

#### List Inputs

```shell
aws iotevents list-inputs | jq -r '.inputs[].inputName'
```

### AWS IoT FleetWise

#### List Campaigns

```shell
aws iotfleetwise list-campaigns | jq -r '.campaigns[].name'
```

### AWS IoT Greengrass V2

#### List Core Devices

```shell
aws greengrassv2 list-core-devices | jq -r '.coreDevices[].coreDeviceThingName'
```

### AWS IoT RoboRunner

#### List Destinations

```shell
aws iotroborunner list-destinations | jq -r '.destinations[].id'
```

### AWS IoT SiteWise

#### List Asset Models

```shell
aws iotsitewise list-asset-models | jq -r '.assetModelSummaries[].id'
```

### AWS IoT TwinMaker

#### List Workspaces

```shell
aws iottwinmaker list-workspaces | jq -r '.workspaceSummaries[].workspaceId'
```
### AWS Proton

#### List Environments

```shell
aws proton list-environments | jq -r '.environments[].name'
```

#### List Services

```shell
aws proton list-services | jq -r '.services[].name'
```

### AWS App Mesh

#### List Meshes

```shell
aws appmesh list-meshes | jq -r '.meshes[].meshName'
```

#### List Virtual Services

```shell
aws appmesh list-virtual-services --mesh-name your-mesh-name | jq -r '.virtualServices[].virtualServiceName'
```

### AWS Cloud Map

#### List Namespaces

```shell
aws servicediscovery list-namespaces | jq -r '.Namespaces[].Name'
```

#### List Services

```shell
aws servicediscovery list-services | jq -r '.Services[].Name'
```

### AWS Cloud9

#### List Environments

```shell
aws cloud9 list-environments | jq -r '.environmentIds[]'
```

### AWS CloudShell

#### List Environments

```shell
aws cloudshell get-environment | jq -r '.environment.environmentId'
```

### AWS CodeGuru Reviewer

#### List Repository Associations

```shell
aws codeguru-reviewer list-repository-associations | jq -r '.RepositoryAssociationSummaries[].Name'
```

### AWS CodeGuru Profiler

#### List Profiling Groups

```shell
aws codeguruprofiler list-profiling-groups | jq -r '.profilingGroups[].name'
```

### AWS Compute Optimizer

#### List Enrollment Statuses

```shell
aws compute-optimizer get-enrollment-statuses | jq -r '.statuses[].status'
```

### AWS Control Tower

#### List Enabled Controls

```shell
aws controltower list-enabled-controls | jq -r '.enabledControls[].controlIdentifier'
```

### AWS Data Exchange

#### List Data Sets

```shell
aws dataexchange list-data-sets | jq -r '.DataSets[].Name'
```

### AWS DataSync

#### List Locations

```shell
aws datasync list-locations | jq -r '.Locations[].LocationArn'
```

### AWS DeepRacer

#### List Models

```shell
aws deepracer list-models | jq -r '.Models[].ModelName'
```

### AWS Elemental MediaTailor

#### List Configurations

```shell
aws mediatailor list-playback-configurations | jq -r '.Items[].Name'
```

### AWS Fault Injection Simulator

#### List Experiment Templates

```shell
aws fis list-experiment-templates | jq -r '.experimentTemplates[].id'
```

### AWS Glue DataBrew

#### List Projects

```shell
aws databrew list-projects | jq -r '.Projects[].Name'
```

### AWS Ground Station

#### List Missions

```shell
aws groundstation list-missions | jq -r '.missionList[].missionId'
```

### AWS Health

#### List Event Types

```shell
aws health describe-event-types | jq -r '.eventTypes[].eventTypeCode'
```

### AWS IAM Identity Center (successor to AWS Single Sign-On)

#### List Instances

```shell
aws sso-admin list-instances | jq -r '.Instances[].InstanceArn'
```

### AWS IoT Core Device Advisor

#### List Suite Runs

```shell
aws iotdeviceadvisor list-suite-runs | jq -r '.suiteRunsList[].suiteRunId'
```

### AWS IoT FleetWise

#### List Signal Catalogs

```shell
aws iotfleetwise list-signal-catalogs | jq -r '.signalCatalogSummaries[].name'
```

### AWS IoT RoboRunner

#### List Sites

```shell
aws iotroborunner list-sites | jq -r '.sites[].id'
```

### AWS IoT TwinMaker

#### List Entities

```shell
aws iottwinmaker list-entities --workspace-id your-workspace-id | jq -r '.entitySummaries[].entityName'
```

### AWS Lake Formation

#### List Resources

```shell
aws lakeformation list-resources | jq -r '.ResourceInfoList[].ResourceArn'
```

### AWS License Manager

#### List License Configurations

```shell
aws license-manager list-license-configurations | jq -r '.LicenseConfigurations[].LicenseConfigurationId'
```

### AWS Mainframe Modernization

#### List Applications

```shell
aws m2 list-applications | jq -r '.applications[].applicationId'
```

### AWS Managed Services

#### List AWS Managed Services Operations

```shell
aws managedservices list-operations | jq -r '.operationList[].id'
```

### AWS Network Firewall

#### List Firewalls

```shell
aws network-firewall list-firewalls | jq -r '.Firewalls[].FirewallName'
```

### AWS Network Manager

#### List Global Networks

```shell
aws networkmanager list-global-networks | jq -r '.GlobalNetworks[].GlobalNetworkId'
```

### AWS Private 5G

#### List Network Resources

```shell
aws private-networks list-network-resources | jq -r '.networkResources[].name'
```

### AWS Resilience Hub

#### List Apps

```shell
aws resiliencehub list-apps | jq -r '.appSummaries[].name'
```

### AWS Resource Access Manager (RAM)

#### List Resources

```shell
aws ram list-resources | jq -r '.resources[].arn'
```

### AWS RoboMaker

#### List Robot Applications

```shell
aws robomaker list-robot-applications | jq -r '.robotApplicationSummaries[].name'
```

### AWS Amplify UI Builder

#### List Components

```shell
aws amplifyuibuilder list-components --app-id YOUR_APP_ID --environment-name YOUR_ENV_NAME | jq -r '.entities[].name'
```

### AWS AppConfig

#### List Environments

```shell
aws appconfig list-environments --application-id YOUR_APP_ID | jq -r '.Items[].Name'
```

### AWS Application Cost Profiler

#### List Report Definitions

```shell
aws application-cost-profiler list-report-definitions | jq -r '.reportDefinitions[].reportName'
```

### AWS Audit Manager

#### List Assessments

```shell
aws auditmanager list-assessments | jq -r '.assessmentMetadata[].name'
```

### AWS Backup Gateway

#### List Gateways

```shell
aws backup-gateway list-gateways | jq -r '.Gateways[].GatewayArn'
```

### AWS Billing Conductor

#### List Billing Groups

```shell
aws billingconductor list-billing-groups | jq -r '.BillingGroups[].Name'
```

### AWS Chatbot

#### List Slack Channel Configurations

```shell
aws chatbot list-slack-channel-configurations | jq -r '.slackChannelConfigurations[].configurationName'
```

### AWS Clean Rooms

#### List Collaborations

```shell
aws cleanrooms list-collaborations | jq -r '.collaborations[].name'
```

### AWS Cloud Control API

#### List Resources

```shell
aws cloudcontrol list-resources --type-name AWS::EC2::Instance | jq -r '.ResourceDescriptions[].Identifier'
```

### AWS Cloud WAN

#### List Global Networks

```shell
aws networkmanager list-global-networks | jq -r '.GlobalNetworks[].GlobalNetworkId'
```

### AWS CodeCatalyst

#### List Projects

```shell
aws codecatalyst list-projects --space-name YOUR_SPACE_NAME | jq -r '.projects[].name'
```

### AWS Compute Optimizer

#### List Auto Scaling Group Recommendations

```shell
aws compute-optimizer get-auto-scaling-group-recommendations | jq -r '.autoScalingGroupRecommendations[].autoScalingGroupArn'
```

### AWS Connect

#### List Phone Numbers

```shell
aws connect list-phone-numbers --instance-id YOUR_INSTANCE_ID | jq -r '.PhoneNumberSummaryList[].PhoneNumber'
```

### AWS Control Tower

#### List Enabled Controls

```shell
aws controltower list-enabled-controls | jq -r '.enabledControls[].controlIdentifier'
```

### AWS Data Exchange

#### List Data Sets

```shell
aws dataexchange list-data-sets | jq -r '.DataSets[].Name'
```

### AWS DataZone

#### List Domains

```shell
aws datazone list-domains | jq -r '.domains[].name'
```

### AWS DevOps Guru

#### List Insights

```shell
aws devops-guru list-insights | jq -r '.proactiveInsights[].Id'
```

### AWS Directory Service

#### List Directories

```shell
aws ds list-directories | jq -r '.DirectoryDescriptions[].DirectoryId'
```

### AWS Elastic Disaster Recovery

#### List Source Servers

```shell
aws drs describe-source-servers | jq -r '.items[].sourceServerID'
```

### AWS Elemental Appliances and Software

#### List Activations

```shell
aws elemental-appliances-software list-activations | jq -r '.activations[].id'
```

### AWS Elemental MediaConnect

#### List Flows

```shell
aws mediaconnect list-flows | jq -r '.Flows[].Name'
```

### AWS Fault Injection Simulator

#### List Experiment Templates

```shell
aws fis list-experiment-templates | jq -r '.experimentTemplates[].id'
```

### AWS FinSpace

#### List Environments

```shell
aws finspace list-environments | jq -r '.environments[].name'
```

### AWS Global Accelerator

#### List Accelerators

```shell
aws globalaccelerator list-accelerators | jq -r '.Accelerators[].Name'
```

### AWS Glue

#### List Workflows

```shell
aws glue list-workflows | jq -r '.Workflows[]'
```

### AWS Ground Station

#### List Ground Stations

```shell
aws groundstation list-ground-stations | jq -r '.groundStationList[].groundStationId'
```

### AWS Health

#### List Events

```shell
aws health describe-events | jq -r '.events[].arn'
```

### AWS IoT 1-Click

#### List Devices

```shell
aws iot1click-devices list-devices | jq -r '.Devices[].DeviceId'
```

### AWS IoT Analytics

#### List Datasets

```shell
aws iotanalytics list-datasets | jq -r '.datasetSummaries[].datasetName'
```

### AWS IoT Events

#### List Detector Models

```shell
aws iotevents list-detector-models | jq -r '.detectorModelSummaries[].detectorModelName'
```

### AWS IoT Fleet Hub

#### List Applications

```shell
aws iotfleethub list-applications | jq -r '.applicationSummaries[].applicationName'
```

### AWS IoT Greengrass V2

#### List Core Devices

```shell
aws greengrassv2 list-core-devices | jq -r '.coreDevices[].coreDeviceThingName'
```

### AWS IoT TwinMaker

#### List Workspaces

```shell
aws iottwinmaker list-workspaces | jq -r '.workspaceSummaries[].workspaceId'
```

### AWS IoT Wireless

#### List Wireless Devices

```shell
aws iotwireless list-wireless-devices | jq -r '.WirelessDeviceList[].Id'
```

### AWS Kendra

#### List Data Sources

```shell
aws kendra list-data-sources --index-id YOUR_INDEX_ID | jq -r '.SummaryItems[].Name'
```

### AWS Key Management Service (KMS)

#### List Keys

```shell
aws kms list-keys | jq -r '.Keys[].KeyId'
```

### AWS Lambda

#### List Layers

```shell
aws lambda list-layers | jq -r '.Layers[].LayerName'
```

### AWS License Manager

#### List License Configurations

```shell
aws license-manager list-license-configurations | jq -r '.LicenseConfigurations[].LicenseConfigurationArn'
```

### AWS Managed Blockchain

#### List Networks

```shell
aws managedblockchain list-networks | jq -r '.Networks[].Name'
```

### AWS Marketplace Catalog

#### List Entities

```shell
aws marketplace-catalog list-entities --entity-type AWSMarketplace::CloudFormation | jq -r '.EntitySummaryList[].Name'
```

### AWS Migration Hub

#### List Application States

```shell
aws mgh list-application-states | jq -r '.ApplicationStateList[].ApplicationId'
```

### AWS Network Firewall

#### List Firewall Policies

```shell
aws network-firewall list-firewall-policies | jq -r '.FirewallPolicies[].Name'
```

### AWS OpsWorks CM

#### List Servers

```shell
aws opsworks-cm list-servers | jq -r '.Servers[].ServerName'
```

### AWS Organizations

#### List Accounts

```shell
aws organizations list-accounts | jq -r '.Accounts[].Name'
```

### AWS Outposts

#### List Sites

```shell
aws outposts list-sites | jq -r '.Sites[].SiteId'
```

### AWS Panorama

#### List Devices

```shell
aws panorama list-devices | jq -r '.Devices[].DeviceId'
```

### AWS Private Certificate Authority

#### List Certificate Authorities

```shell
aws acm-pca list-certificate-authorities | jq -r '.CertificateAuthorities[].Arn'
```

### AWS Proton

#### List Environments

```shell
aws proton list-environments | jq -r '.environments[].name'
```

### AWS Purchase Orders Console

#### List Purchase Orders

```shell
aws purchase-orders list-purchase-orders | jq -r '.PurchaseOrders[].PurchaseOrderId'
```

### AWS Resource Access Manager (RAM)

#### List Resources

```shell
aws ram list-resources | jq -r '.resources[].resourceShareArn'
```

### AWS Resource Groups

#### List Groups

```shell
aws resource-groups list-groups | jq -r '.GroupIdentifiers[].GroupName'
```

### AWS RoboMaker

#### List Robot Applications

```shell
aws robomaker list-robot-applications | jq -r '.robotApplicationSummaries[].name'
```

### AWS Secrets Manager

#### List Secrets

```shell
aws secretsmanager list-secrets | jq -r '.SecretList[].Name'
```

### AWS Security Hub

#### List Findings

```shell
aws securityhub get-findings | jq -r '.Findings[].Title'
```

### AWS Service Catalog

#### List Portfolios

```shell
aws servicecatalog list-portfolios | jq -r '.PortfolioDetails[].DisplayName'
```

### AWS Service Quotas

#### List Services

```shell
aws service-quotas list-services | jq -r '.Services[].ServiceName'
```

### AWS Shield

#### List Protections

```shell
aws shield list-protections | jq -r '.Protections[].Name'
```

### AWS Signer

#### List Signing Profiles

```shell
aws signer list-signing-profiles | jq -r '.profiles[].profileName'
```

### AWS Step Functions

#### List State Machines

```shell
aws stepfunctions list-state-machines | jq -r '.stateMachines[].name'
```

### AWS Storage Gateway

#### List Gateways

```shell
aws storagegateway list-gateways | jq -r '.Gateways[].GatewayARN'
```

### AWS Systems Manager

#### List Documents

```shell
aws ssm list-documents | jq -r '.DocumentIdentifiers[].Name'
```

### AWS Transfer Family

#### List Servers

```shell
aws transfer list-servers | jq -r '.Servers[].ServerId'
```

### AWS Trusted Advisor

#### List Checks

```shell
aws trustedadvisor describe-trusted-advisor-checks --language en | jq -r '.checks[].name'
```

### AWS VPC Lattice

#### List Service Networks

```shell
aws vpc-lattice list-service-networks | jq -r '.items[].name'
```

### AWS WAF

#### List Web ACLs

```shell
aws waf list-web-acls | jq -r '.WebACLs[].Name'
```

### AWS Well-Architected Tool

#### List Workloads

```shell
aws wellarchitected list-workloads | jq -r '.WorkloadSummaries[].WorkloadName'
```

### AWS X-Ray

#### List Groups

```shell
aws xray get-groups | jq -r '.Groups[].GroupName'
```

## Execute All Commands

To execute all the commands at once, you can use:

```emacs-lisp
(org-babel-execute-buffer)
```

Note: Ensure you have the necessary AWS CLI permissions and configurations set up before running these commands.
Some commands may take a while to execute depending on the number of resources in your AWS account.
Some commands require specific parameters (like YOUR_INDEX_ID) which you need to replace with actual values from your AWS environment.

---

<!-- source: practice-tests/aif-c01-practice-01.org -->

# AWS Certified AI Practitioner (AIF-C01): Practice Exam 1 - Fundamentals of AI and ML

## Domain 1: Fundamentals of AI and ML

### Question 1: What is the primary difference between AI and Machine Learning?

**Answer:** Machine Learning is a subset of AI that focuses on systems that can learn from data
**Explanation:** AI is a broader concept of machines being able to carry out tasks in a way that we would consider "smart". Machine Learning is a specific subset of AI that trains a machine how to learn, focusing on the development of computer programs that can access data and use it to learn for themselves.

   - [ ] AI is data-driven while Machine Learning is rule-based
   - [X] Machine Learning is a subset of AI that focuses on systems that can learn from data
   - [ ] AI requires supervised learning while Machine Learning can be unsupervised
   - [ ] There is no significant difference between AI and Machine Learning

### Question 2: Which of the following is an example of unsupervised learning?

**Answer:** Clustering customer data to identify market segments
**Explanation:** Unsupervised learning involves finding patterns or structures in data without pre-existing labels. Clustering is a common unsupervised learning technique used to group similar data points together, such as identifying market segments from customer data.

   - [ ] Predicting house prices based on historical sales data
   - [ ] Classifying emails as spam or not spam
   - [X] Clustering customer data to identify market segments
   - [ ] Recognizing handwritten digits in images

### Question 3: Which AWS service is most appropriate for natural language processing tasks?

**Answer:** Amazon Comprehend
**Explanation:** Amazon Comprehend is a natural language processing (NLP) service that uses machine learning to find insights and relationships in text. It's specifically designed for tasks such as sentiment analysis, entity recognition, and key phrase extraction.

   - [ ] Amazon Rekognition
   - [X] Amazon Comprehend
   - [ ] Amazon SageMaker
   - [ ] Amazon Polly

### Question 4: What is the primary purpose of feature engineering in the ML development lifecycle?

**Answer:** To create new input features that better represent the underlying problem to predictive models
**Explanation:** Feature engineering is the process of using domain knowledge to extract features from raw data. This process helps to create new input features that can better represent the underlying problem to predictive models, potentially improving their performance and interpretability.

   - [ ] To reduce the number of features in the dataset
   - [X] To create new input features that better represent the underlying problem to predictive models
   - [ ] To normalize all features to the same scale
   - [ ] To remove outliers from the dataset

### Question 5: Which of the following is a key component of MLOps?

**Answer:** Continuous integration and continuous delivery (CI/CD) for ML models
**Explanation:** MLOps (Machine Learning Operations) aims to streamline the process of taking machine learning models to production and maintaining them. Continuous integration and continuous delivery (CI/CD) for ML models is a key component of MLOps, ensuring that models can be reliably and efficiently updated and deployed.

   - [ ] Manual data cleansing
   - [ ] One-time model deployment
   - [X] Continuous integration and continuous delivery (CI/CD) for ML models
   - [ ] Ad-hoc model retraining

---

<!-- source: practice-tests/aif-c01-practice-02.org -->

# AWS Certified AI Practitioner (AIF-C01): Practice Exam 2 - Fundamentals of Generative AI

## Domain 2: Fundamentals of Generative AI

### Question 1: What is a key characteristic of foundation models in generative AI?

**Answer:** They are trained on large, diverse datasets and can be adapted to a wide range of tasks
**Explanation:** Foundation models are large AI models trained on vast amounts of unlabeled data. They can be adapted to a wide range of downstream tasks through fine-tuning or prompt engineering, making them versatile tools for various AI applications.

   - [ ] They are small, task-specific models
   - [ ] They require minimal computational resources
   - [ ] They are trained on large, diverse datasets and can be adapted to a wide range of tasks
   - [ ] They can only be used for text generation tasks

### Question 2: What is prompt engineering in the context of generative AI?

**Answer:** The practice of designing and refining input prompts to get desired outputs from AI models
**Explanation:** Prompt engineering is the process of crafting and refining input prompts to elicit specific, desired responses from large language models or other AI systems. It's a crucial skill in effectively using and interacting with generative AI models.

   - [ ] A technique for training AI models
   - [ ] The practice of designing and refining input prompts to get desired outputs from AI models
   - [ ] A method for compressing AI models
   - [ ] A way to visualize AI model outputs

### Question 3: Which AWS service provides a fully managed environment for building generative AI applications?

**Answer:** Amazon Bedrock
**Explanation:** Amazon Bedrock is a fully managed service that provides access to foundation models from leading AI companies through a single API. It offers tools and capabilities to build, scale, and deploy generative AI applications securely.

   - [ ] Amazon SageMaker
   - [ ] Amazon Comprehend
   - [ ] Amazon Bedrock
   - [ ] AWS Lambda

### Question 4: What is a potential limitation of generative AI models?

**Answer:** They may produce hallucinations or false information
**Explanation:** Generative AI models, especially large language models, can sometimes produce "hallucinations" - plausible-sounding but factually incorrect or nonsensical information. This is a known limitation that users and developers need to be aware of when working with these models.

   - [ ] They can only process text data
   - [ ] They require small datasets to function
   - [ ] They may produce hallucinations or false information
   - [ ] They are always 100% accurate

### Question 5: What is the primary advantage of using AWS generative AI services for building applications?

**Answer:** They provide accessibility and lower barriers to entry for AI development
**Explanation:** AWS generative AI services, like Amazon Bedrock, provide accessibility and lower barriers to entry for AI development. They offer pre-trained models and managed infrastructure, allowing developers to build AI applications without the need for extensive ML expertise or large computational resources.

   - [ ] They are always free to use
   - [ ] They provide accessibility and lower barriers to entry for AI development
   - [ ] They guarantee 100% accuracy in all outputs
   - [ ] They eliminate the need for any programming knowledge

---

<!-- source: practice-tests/aif-c01-practice-03.org -->

# AWS Certified AI Practitioner (AIF-C01): Practice Exam 3 - Applications of Foundation Models

## Domain 3: Applications of Foundation Models

### Question 1: What is Retrieval Augmented Generation (RAG) in the context of foundation models?

**Answer:** A technique that combines information retrieval with text generation to produce more accurate and contextually relevant responses
**Explanation:** Retrieval Augmented Generation (RAG) is a technique that enhances language models by retrieving relevant information from an external knowledge base before generating a response. This allows the model to access up-to-date or domain-specific information, improving the accuracy and relevance of its outputs.

   - [ ] A method for compressing large language models
   - [ ] A technique that combines information retrieval with text generation to produce more accurate and contextually relevant responses
   - [ ] A type of generative adversarial network
   - [ ] A way to visualize the internal workings of a neural network

### Question 2: Which AWS service is suitable for storing embeddings within a vector database for use with foundation models?

**Answer:** Amazon OpenSearch Service
**Explanation:** Amazon OpenSearch Service supports vector search capabilities, making it suitable for storing and querying embeddings. This can be particularly useful in applications using foundation models, such as implementing efficient similarity search or enhancing retrieval for RAG systems.

   - [ ] Amazon DynamoDB
   - [ ] Amazon S3
   - [ ] Amazon OpenSearch Service
   - [ ] Amazon RDS for MySQL

### Question 3: What is the purpose of the 'temperature' parameter in text generation with foundation models?

**Answer:** To control the randomness and creativity of the generated text
**Explanation:** The 'temperature' parameter in text generation controls the randomness of the model's output. A higher temperature results in more diverse and creative outputs, while a lower temperature makes the output more focused and deterministic. This allows users to balance between creativity and consistency in generated text.

   - [ ] To set the maximum length of the generated text
   - [ ] To control the processing speed of the model
   - [ ] To control the randomness and creativity of the generated text
   - [ ] To adjust the model's learning rate

### Question 4: What is 'few-shot learning' in the context of prompt engineering?

**Answer:** A technique where a small number of examples are provided in the prompt to guide the model's response
**Explanation:** Few-shot learning in prompt engineering involves providing a small number of examples (typically 2-5) within the prompt to demonstrate the desired task or output format. This technique helps guide the model's understanding and can improve performance on specific tasks without fine-tuning the model.

   - [ ] A method for training models on very small datasets
   - [X] A technique where a small number of examples are provided in the prompt to guide the model's response
   - [ ] A way to reduce the size of the model
   - [ ] A process for rapidly fine-tuning a model

### Question 5: What is a key consideration when fine-tuning a foundation model for a specific task?

**Answer:** The quality and relevance of the fine-tuning dataset
**Explanation:** When fine-tuning a foundation model, the quality and relevance of the fine-tuning dataset is crucial. The dataset should be representative of the target task, free from biases, and of high quality. Poor quality or irrelevant data can lead to degraded performance or unintended behaviors in the fine-tuned model.

   - [ ] The size of the original pre-training dataset
   - [X] The quality and relevance of the fine-tuning dataset
   - [ ] The number of parameters in the model
   - [ ] The hardware used for training

---

<!-- source: practice-tests/aif-c01-practice-04.org -->

# AWS Certified AI Practitioner (AIF-C01): Practice Exam 4 - Responsible AI and Security

## Domain 4: Guidelines for Responsible AI

## Domain 5: Security, Compliance, and Governance for AI Solutions

### Question 1: What is a key principle of responsible AI development?

**Answer:** Fairness and non-discrimination in AI system outputs
**Explanation:** Fairness and non-discrimination are crucial principles in responsible AI development. This involves ensuring that AI systems do not perpetuate or amplify biases based on characteristics such as race, gender, age, or other protected attributes. It's important to assess and mitigate biases in training data and model outputs.

   - [ ] Maximizing model complexity
   - [ ] Prioritizing speed over accuracy
   - [ ] Fairness and non-discrimination in AI system outputs
   - [ ] Keeping AI development processes secret

### Question 2: Which AWS service can help detect and monitor bias in machine learning models?

**Answer:** Amazon SageMaker Clarify
**Explanation:** Amazon SageMaker Clarify provides tools for detecting bias in machine learning models. It can help identify potential biases in training data and model predictions, and provide explanations for model decisions, supporting the development of fair and transparent AI systems.

   - [ ] Amazon Rekognition
   - [ ] Amazon SageMaker Clarify
   - [ ] Amazon Comprehend
   - [ ] AWS CloudTrail

### Question 3: What is a key benefit of using explainable AI models?

**Answer:** They provide transparency in decision-making processes, building trust with users and stakeholders
**Explanation:** Explainable AI models provide insights into how they arrive at their decisions or predictions. This transparency helps build trust with users and stakeholders, allows for better auditing and validation of model behavior, and can be crucial in regulated industries where decision rationales must be provided.

   - [ ] They always produce more accurate results than black-box models
   - [ ] They require less computational resources
   - [ ] They provide transparency in decision-making processes, building trust with users and stakeholders
   - [ ] They eliminate the need for human oversight

### Question 4: Which AWS service can help with maintaining regulatory compliance for AI systems?

**Answer:** AWS Audit Manager
**Explanation:** AWS Audit Manager helps continuously audit AWS usage to simplify how you assess risk and compliance with regulations and industry standards. It can be particularly useful for AI systems, helping to ensure they meet various regulatory requirements and governance standards.

   - [ ] Amazon SageMaker
   - [ ] Amazon Rekognition
   - [ ] AWS Audit Manager
   - [ ] Amazon Comprehend

### Question 5: What is a key aspect of data governance in AI systems?

**Answer:** Ensuring data quality, privacy, and appropriate usage throughout its lifecycle
**Explanation:** Data governance in AI systems involves managing the availability, usability, integrity, and security of data. This includes ensuring data quality, protecting privacy, maintaining appropriate access controls, and ensuring that data is used in compliance with relevant regulations and ethical standards throughout its lifecycle.

   - [ ] Collecting as much data as possible without restrictions
   - [ ] Ensuring data quality, privacy, and appropriate usage throughout its lifecycle
   - [ ] Keeping all data indefinitely
   - [ ] Sharing all data publicly to promote transparency

---

<!-- source: practice-tests/aif-c01-practice-05.org -->

# AWS Certified AI Practitioner (AIF-C01): Practice Exam 5 - Comprehensive Review

## Comprehensive Review: All Domains

### Question 1: What is the primary purpose of Amazon SageMaker?

**Answer:** To build, train, and deploy machine learning models at scale
**Explanation:** Amazon SageMaker is a fully managed machine learning platform that enables developers and data scientists to quickly and easily build, train, and deploy machine learning models at any scale. It provides all the components used for machine learning in a single toolset, so models get to production faster with much less effort and at lower cost.

   - [ ] To provide database services
   - [ ] To build, train, and deploy machine learning models at scale
   - [ ] To manage EC2 instances
   - [ ] To provide content delivery services

### Question 2: In the context of generative AI, what is a 'token'?

**Answer:** A unit of text that the model processes, which can be a word, part of a word, or a character
**Explanation:** In generative AI, particularly with large language models, a 'token' is the basic unit of text that the model processes. Depending on the model and tokenization method, a token can represent a word, part of a word, or even a single character. Understanding tokens is important for tasks like prompt engineering and managing model inputs and outputs.

   - [ ] A security credential
   - [ ] A unit of computational power
   - [ ] A unit of text that the model processes, which can be a word, part of a word, or a character
   - [ ] A type of neural network layer

### Question 3: What is the purpose of 'fine-tuning' a foundation model?

**Answer:** To adapt the model to perform well on a specific task or domain
**Explanation:** Fine-tuning is the process of further training a pre-trained foundation model on a specific dataset or for a specific task. This allows the model to adapt its general knowledge to perform well on a particular domain or application, improving its performance and relevance for specific use cases.

   - [ ] To reduce the model's size
   - [ ] To increase the model's general knowledge
   - [ ] To adapt the model to perform well on a specific task or domain
   - [ ] To make the model forget its previous training

### Question 4: Which of the following is a key principle of responsible AI?

**Answer:** Fairness and non-discrimination
**Explanation:** Fairness and non-discrimination are crucial principles in responsible AI development. This involves ensuring that AI systems do not perpetuate or amplify biases based on characteristics such as race, gender, age, or other protected attributes. It's important to assess and mitigate biases in training data and model outputs to create AI systems that are equitable and just.

   - [ ] Maximizing profit
   - [ ] Fairness and non-discrimination
   - [ ] Rapid development at any cost
   - [ ] Keeping AI development processes secret

### Question 5: What AWS service would you use to detect and redact sensitive information in documents?

**Answer:** Amazon Macie
**Explanation:** Amazon Macie is a data security and data privacy service that uses machine learning and pattern matching to discover and protect sensitive data in AWS. It can automatically detect sensitive data such as personally identifiable information (PII) or intellectual property, and provide alerts or automated remediation.

   - [ ] Amazon Rekognition
   - [ ] Amazon Comprehend
   - [ ] Amazon Macie
   - [ ] Amazon Textract

### Question 6: What is the primary function of Amazon Bedrock?

**Answer:** A fully managed service that provides foundation models via API
**Explanation:** Amazon Bedrock is a fully managed service that makes foundation models from AWS and third-party providers accessible via an API. It allows developers to easily experiment with and evaluate different foundation models, privately customize them, and build generative AI applications.

   - [ ] A database service for AI applications
   - [ ] A fully managed service that provides foundation models via API
   - [ ] A tool for creating custom neural network architectures
   - [ ] A service for managing AI model versioning

### Question 7: In machine learning, what does the term 'overfitting' refer to?

**Answer:** When a model learns the training data too well, including its noise and peculiarities
**Explanation:** Overfitting occurs when a machine learning model learns the training data too well, including the noise and random fluctuations in the training set. As a result, the model performs very well on the training data but poorly on new, unseen data. This reduces the model's ability to generalize and make accurate predictions on new data.

   - [ ] When a model is too simple to capture the underlying patterns in the data
   - [ ] When a model learns the training data too well, including its noise and peculiarities
   - [ ] When a model takes too long to train
   - [ ] When a model requires too much computational power

### Question 8: What is the purpose of the 'top-p' (or nucleus) sampling parameter in text generation?

**Answer:** To control the diversity of generated text by limiting the cumulative probability of considered tokens
**Explanation:** Top-p (nucleus) sampling is a text generation strategy that dynamically selects the smallest set of words whose cumulative probability exceeds the probability p. This method helps balance between diversity and quality in generated text. By adjusting the 'top-p' parameter, you can control how focused or creative the model's outputs are.

   - [ ] To set the maximum length of generated text
   - [ ] To control the diversity of generated text by limiting the cumulative probability of considered tokens
   - [ ] To determine the processing speed of the model
   - [ ] To set the minimum probability threshold for each word

### Question 9: Which AWS service would you use to build a conversational AI chatbot?

**Answer:** Amazon Lex
**Explanation:** Amazon Lex is a service for building conversational interfaces into any application using voice and text. It provides the advanced deep learning functionalities of automatic speech recognition (ASR) for converting speech to text, and natural language understanding (NLU) to recognize the intent of the text, enabling you to build applications with highly engaging user experiences and lifelike conversational interactions.

   - [ ] Amazon Polly
   - [ ] Amazon Lex
   - [ ] Amazon Transcribe
   - [ ] Amazon Comprehend

### Question 10: What is Retrieval Augmented Generation (RAG) in the context of generative AI?

**Answer:** A technique that combines information retrieval with text generation to produce more accurate and contextually relevant responses
**Explanation:** Retrieval Augmented Generation (RAG) is a technique that enhances language models by retrieving relevant information from an external knowledge base before generating a response. This allows the model to access up-to-date or domain-specific information, improving the accuracy and relevance of its outputs. RAG is particularly useful for applications requiring current or specialized knowledge.

    - [ ] A method for compressing large language models
    - [ ] A technique that combines information retrieval with text generation to produce more accurate and contextually relevant responses
    - [ ] A type of generative adversarial network
    - [ ] A way to visualize the internal workings of a neural network

### Question 11: Which of the following is NOT a typical stage in the machine learning development lifecycle?

**Answer:** Hardware optimization
**Explanation:** While hardware considerations are important in machine learning, "hardware optimization" is not typically considered a distinct stage in the ML development lifecycle. The typical stages include data collection, data preparation, feature engineering, model selection, training, evaluation, deployment, and monitoring. Hardware optimization might be a consideration throughout these stages but is not usually treated as a separate phase.

    - [ ] Feature engineering
    - [ ] Model training
    - [ ] Hardware optimization
    - [ ] Model deployment

### Question 12: What is the main advantage of using pre-trained foundation models?

**Answer:** They reduce the time and resources needed to develop AI applications for specific tasks
**Explanation:** Pre-trained foundation models offer significant advantages in AI development. They have already learned general patterns and features from vast amounts of data, which can be leveraged for various downstream tasks. This reduces the time, data, and computational resources needed to develop AI applications for specific tasks, as developers can fine-tune these models rather than training from scratch.

    - [ ] They always provide perfect accuracy for any task
    - [ ] They reduce the need for any task-specific data
    - [ ] They reduce the time and resources needed to develop AI applications for specific tasks
    - [ ] They eliminate the need for any further training or fine-tuning

### Question 13: In the context of AI security, what is 'prompt injection'?

**Answer:** A technique where malicious inputs are crafted to manipulate an AI model's behavior
**Explanation:** Prompt injection is a security concern in AI systems, particularly with large language models. It involves crafting inputs (prompts) in a way that can manipulate the model's behavior, potentially causing it to ignore previous instructions, reveal sensitive information, or produce harmful outputs. Understanding and mitigating prompt injection risks is crucial for developing secure AI applications.

    - [ ] A method for optimizing model training
    - [ ] A technique where malicious inputs are crafted to manipulate an AI model's behavior
    - [ ] A way to inject new knowledge into a model without retraining
    - [ ] A process for rapidly fine-tuning a model

### Question 14: Which AWS service would you use to monitor the performance of a deployed machine learning model?

**Answer:** Amazon SageMaker Model Monitor
**Explanation:** Amazon SageMaker Model Monitor is a capability of Amazon SageMaker that continuously monitors the quality of machine learning models in production. It detects deviations in model quality, such as data drift and model drift, and provides alerts so that you can take corrective action. This helps ensure that the models maintain their prediction quality over time.

    - [ ] AWS CloudWatch
    - [ ] Amazon SageMaker Model Monitor
    - [ ] AWS Config
    - [ ] Amazon Inspector

### Question 15: What is the purpose of the 'few-shot learning' technique in prompt engineering?

**Answer:** To guide the model's response by providing a small number of examples in the prompt
**Explanation:** Few-shot learning in prompt engineering involves providing a small number of examples (typically 2-5) within the prompt to demonstrate the desired task or output format. This technique helps guide the model's understanding and can improve performance on specific tasks without fine-tuning the model. It's particularly useful when you want the model to follow a specific pattern or style in its responses.

    - [ ] To train a model on very small datasets
    - [ ] To guide the model's response by providing a small number of examples in the prompt
    - [ ] To reduce the model's memory usage
    - [ ] To increase the model's processing speed

### Question 16: Which of the following is a key consideration for responsible AI development?

**Answer:** Ensuring AI systems are transparent and explainable
**Explanation:** Transparency and explainability are crucial aspects of responsible AI development. They involve making AI systems understandable to users, stakeholders, and regulators. This includes being able to explain how the AI makes decisions, what data it uses, and what its limitations are. Transparent and explainable AI helps build trust, enables better auditing and validation, and is often necessary for regulatory compliance in many industries.

    - [ ] Maximizing model complexity
    - [ ] Keeping AI development processes secret
    - [ ] Ensuring AI systems are transparent and explainable
    - [ ] Prioritizing speed over accuracy in all cases

### Question 17: What is the primary purpose of Amazon Comprehend?

**Answer:** Natural Language Processing (NLP) tasks such as sentiment analysis and entity recognition
**Explanation:** Amazon Comprehend is a natural language processing (NLP) service that uses machine learning to find insights and relationships in text. It can be used for various NLP tasks including sentiment analysis, entity recognition, key phrase extraction, and topic modeling. This makes it useful for analyzing customer feedback, processing documents, and deriving insights from large volumes of text data.

    - [ ] Image and video analysis
    - [ ] Natural Language Processing (NLP) tasks such as sentiment analysis and entity recognition
    - [ ] Text-to-speech conversion
    - [ ] Database management

### Question 18: In the context of AI governance, what is the purpose of a model card?

**Answer:** To provide transparent documentation about a model's development, use, and limitations
**Explanation:** A model card is a documentation framework for transparent reporting of AI model information. It typically includes details about a model's development, intended use cases, performance characteristics, limitations, and ethical considerations. Model cards help improve transparency and accountability in AI development, enabling better understanding and appropriate use of AI models by developers, users, and stakeholders.

    - [ ] To create a physical representation of a neural network
    - [ ] To provide transparent documentation about a model's development, use, and limitations
    - [ ] To encrypt model parameters for security
    - [ ] To optimize model performance

### Question 19: Which AWS service would you use to convert speech to text?

**Answer:** Amazon Transcribe
**Explanation:** Amazon Transcribe is an automatic speech recognition (ASR) service that makes it easy for developers to add speech-to-text capability to their applications. It uses machine learning models to accurately convert speech to text and can handle various audio formats, multiple speakers, and even provide features like speaker identification and custom vocabulary.

    - [ ] Amazon Polly
    - [ ] Amazon Transcribe
    - [ ] Amazon Translate
    - [ ] Amazon Comprehend

### Question 20: What is a potential risk of using generative AI models in content creation?

**Answer:** The model may generate content that infringes on copyrights or contains biased information
**Explanation:** While generative AI models are powerful tools for content creation, they come with certain risks. One significant risk is that these models, trained on vast amounts of data from the internet, may inadvertently reproduce copyrighted material or reflect biases present in their training data. This could lead to legal issues with copyright infringement or the propagation of harmful biases. It's crucial to implement appropriate safeguards and review processes when using generative AI for content creation.

    - [ ] The model may generate content too slowly
    - [X] The model may generate content that infringes on copyrights or contains biased information
    - [ ] The model may consume too much storage space
    - [ ] The model may only generate content in a single language

---

# Additional materials from upstream README

# AWS Certified AI Practitioner (AIF-C01) Exam Preparation

## Introduction

This project provides comprehensive study materials, code examples, and a robust development environment for preparing for the AWS Certified AI Practitioner (AIF-C01) exam, announced in [[https://aws.amazon.com/blogs/training-and-certification/august-2024-new-offerings/][August 2024]]. While the primary focus is on the AIF-C01 exam, the project also lays groundwork for the AWS Certified Machine Learning Engineer – Associate (MLA-C01) certification.

Key features of this project:
- Structured learning paths covering all AIF-C01 exam domains
- Secondary information supporting MLA-C01 / ME1-C01 
- Hands-on code examples using AWS AI/ML services
- Local development environment with LocalStack for AWS service simulation
- Integration of Python and Clojure for a comprehensive learning experience
- Emphasis on best practices in AI/ML development and responsible AI

Whether you're an executive looking to understand AI/ML capabilities in AWS or a practitioner aiming for certification, this project provides the resources you need to succeed.

## Example Usage for Each Domain

### Domain 0: Environment Setup and Connection Checks

```clojure
(require '[aif-c01.d0-setup.environment :as d0])
(d0/check-aws-credentials)
```

### Domain 1: Fundamentals of AI and ML

```clojure
(require '[aif-c01.d1-fundamentals.basics :as d1])
(d1/explain-ai-term :ml)
(d1/list-ml-types)
```

### Domain 2: Fundamentals of Generative AI

```clojure
(require '[aif-c01.d2-generative-ai.concepts :as d2])
(d2/explain-gen-ai-concept :prompt-engineering)
(d2/list-gen-ai-use-cases)
```

### Domain 3: Applications of Foundation Models

```clojure
(require '[aif-c01.d3-foundation-models.applications :as d3])
(d3/describe-rag)
(d3/list-model-selection-criteria)
```

### Domain 4: Guidelines for Responsible AI

```clojure
(require '[aif-c01.d4-responsible-ai.practices :as d4])
(d4/list-responsible-ai-features)
(d4/describe-bias-effects)
```

### Domain 5: Security, Compliance, and Governance for AI Solutions

```clojure
(require '[aif-c01.d5-security-compliance.governance :as d5])
(d5/list-aws-security-services)
(d5/describe-data-governance-strategies)
```

## Responsible AI

A key focus of this project is on responsible AI practices. We cover:

- Ethical considerations in AI/ML development
- Bias detection and mitigation strategies
- Fairness and inclusivity in AI systems
- Robustness and safety measures
- Compliance and governance in AI projects

## Study Resources

In addition to code examples, this project includes:

- Curated lists of AWS documentation and whitepapers
- Links to relevant AWS training materials
- Practice questions for each exam domain
- Glossary of key AI/ML terms in the context of AWS

## Disclaimer

This project is not affiliated with or endorsed by Amazon Web Services. All AWS service names and trademarks are property of Amazon.com, Inc. or its affiliates.
