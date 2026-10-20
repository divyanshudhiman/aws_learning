## Practice Test 9 - Business Scenario Marathon (with answers)

More original scenario items. Same workflow: answer first, then open the result.

---

### Customer experience & contact center

1. A telecom wants real-time agent assist: summarize the live call and suggest next steps from a knowledge base.
    - A. Transcribe streaming + Bedrock/LLM with RAG
    - B. Amazon Glacier retrieval only
    - C. Amazon VPC Flow Logs alone
    - D. AWS Snowcone as the chatbot

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Live speech → text, then an LLM grounded on KB content. Storage/logs/hardware do not implement assist.
    </details>

2. The same company needs a bot that books appointments via dialog slots (date, time, site).
    - A. Amazon Lex
    - B. Amazon Athena
    - C. Amazon CloudWatch Synthetics only
    - D. AWS Certificate Manager only

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Lex is designed for conversational bots with intents and slots.
    </details>

3. After calls, leadership wants topic trends and angry-customer detection from transcripts.
    - A. Amazon Comprehend (topics / sentiment)
    - B. Amazon EC2 Auto Scaling alone
    - C. AWS Transit Gateway
    - D. Amazon S3 Inventory only

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Comprehend analyzes sentiment, entities, and topics in text.
    </details>

4. IVR must speak replies in a natural voice after Lex decides the response text.
    - A. Amazon Polly
    - B. Amazon Textract
    - C. Amazon Macie
    - D. AWS Config

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Polly turns text into speech for IVR/voice UIs.
    </details>

---

### Document intelligence

5. Mortgage applications arrive as multi-page PDFs with handwriting and tables. Extract fields into a loan system.
    - A. Amazon Textract
    - B. Amazon Personalize
    - C. Amazon Forecast
    - D. Amazon GameLift

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Textract extracts text, forms, and tables from documents.
    </details>

6. After extraction, classify each document as “income,” “ID,” or “appraisal” using NLP on the text.
    - A. Amazon Comprehend custom classification (or similar NLP)
    - B. Amazon Route 53
    - C. AWS Direct Connect
    - D. Amazon ElastiCache alone

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Comprehend custom classification labels text into business categories.
    </details>

7. Legal wants searchable Q&A across millions of contracts with NLP ranking, not keyword-only search.
    - A. Amazon Kendra
    - B. Amazon SNS FIFO alone
    - C. Amazon SQS alone
    - D. AWS Budgets

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Kendra provides intelligent enterprise document search.
    </details>

8. Scanned receipts must become line items for expense automation with human review of low confidence.
    - A. Textract + Amazon A2I
    - B. Amazon MQ + Amazon SES only
    - C. AWS WAF + Shield only
    - D. CloudFront + Route 53 only

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Textract extracts; A2I routes uncertain results to people.
    </details>

---

### Vision & media

9. A factory needs to flag cracked products on a conveyor from camera frames.
    - A. Custom vision model on SageMaker (or Rekognition Custom Labels)
    - B. Amazon Translate
    - C. Amazon Polly
    - D. AWS IAM Access Analyzer alone

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Visual defect detection needs computer vision training/custom labels—not translation/TTS.
    </details>

10. A social app must block uploaded images that contain explicit content.
    - A. Amazon Rekognition content moderation
    - B. Amazon Timestream
    - C. Amazon Neptune
    - D. AWS DataSync alone

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Rekognition moderation APIs detect inappropriate visual content.
    </details>

11. Marketing wants product photos turned into short promotional captions.
    - A. Vision captioning / multimodal GenAI (e.g., Bedrock multimodal)
    - B. Amazon VPC Lattice alone
    - C. AWS PrivateLink alone
    - D. Amazon EFS alone

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Image-to-text generation is a multimodal generative task.
    </details>

12. Security cameras need face comparison against an employee watchlist (authorized use, policy approved).
    - A. Amazon Rekognition face comparison / collections
    - B. Amazon Forecast
    - C. Amazon Personalize
    - D. Amazon Athena only

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Rekognition supports face compare/search. Always pair with legal/privacy controls.
    </details>

---

### Forecasting, recommendations, and classical ML

13. A grocery chain forecasts weekly demand per store for perishable goods.
    - A. Amazon Forecast (or SageMaker forecasting)
    - B. Amazon Lex
    - C. Amazon Polly
    - D. Amazon Chime

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Forecast targets time-series demand prediction.
    </details>

14. An e-commerce homepage needs personalized item rankings per user in real time.
    - A. Amazon Personalize
    - B. Amazon Macie
    - C. AWS Artifact
    - D. AWS Control Tower

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Personalize delivers real-time recommendations.
    </details>

15. Fraud scores must return in under 100 ms for card authorization.
    - A. SageMaker real-time endpoint
    - B. SageMaker batch transform overnight
    - C. Manual CSV review next week
    - D. Glacier Deep Archive restore

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Low-latency online scoring needs a real-time endpoint.
    </details>

16. Analysts with no Python skills want to train a churn model from a spreadsheet.
    - A. SageMaker Canvas
    - B. Write custom CUDA kernels
    - C. Configure BGP on a router
    - D. Build a hypervisor from scratch

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Canvas is the no-code/low-code path for business users.
    </details>

---

### Generative AI architecture choices

17. A startup needs an LLM API today without GPUs. Multiple model vendors preferred.
    - A. Amazon Bedrock
    - B. Self-managed racks in a garage only
    - C. Amazon S3 static hosting alone
    - D. AWS Snowmobile alone

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Bedrock is the managed multi-FM API service.
    </details>

18. App must keep proprietary prompts and retrieved chunks private in the AWS account boundary as much as practical.
    - A. Bedrock with private networking patterns + IAM + encryption
    - B. Paste prompts into public Discord channels
    - C. Disable encryption on all buckets
    - D. Share root credentials with contractors

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Combine managed FM access with IAM, encryption, and private connectivity controls.
    </details>

19. Support answers must include citations from the latest product handbook.
    - A. RAG with retrieval + generation citing sources
    - B. Raise temperature to 2.0
    - C. Remove the system prompt
    - D. Fine-tune once and never refresh docs

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: RAG retrieves handbook chunks and can cite them; high temperature worsens reliability.
    </details>

20. The team wants the model to follow a fixed JSON schema for ticket fields.
    - A. Structured prompt / constrained decoding / fine-tune for format
    - B. Random Top-K with no instructions
    - C. Disable validation
    - D. Use emoji-only prompts

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Schema adherence comes from clear prompts, constraints, or specialized fine-tuning—not randomness.
    </details>

21. Agents must call “get_order” and “refund_order” tools safely.
    - A. Bedrock Agents / tool use with least-privilege IAM on backends
    - B. Give the model the production DB password in the prompt
    - C. Allow unrestricted shell on the host
    - D. Skip authentication on refund APIs

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Tool-calling agents plus least privilege protect backends; never put secrets in prompts.
    </details>

22. Creative image ads from text briefs; avoid logos of competitors.
    - A. Image FM with negative prompting + brand guidelines in prompt
    - B. Amazon Forecast
    - C. Amazon Comprehend Medical only
    - D. AWS Backup alone

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Image generation with prompt/negative prompt controls fits ad creative workflows.
    </details>

---

### Responsible AI, risk, and evaluation

23. Before releasing a medical triage chatbot, the team documents intended use, out-of-scope cases, and known failure modes.
    - A. Model card / documentation for responsible release
    - B. Ignoring all limitations
    - C. Maximizing hallucinations for engagement
    - D. Hiding evaluation results

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Transparent documentation (model cards) is a core responsible-AI practice.
    </details>

24. Offline eval shows high BLEU but users hate the translations. Next step?
    - A. Add human evaluation and task-specific metrics
    - B. Trust BLEU alone forever
    - C. Increase temperature without review
    - D. Delete user feedback

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Automatic metrics can miss quality/UX; human eval and domain metrics matter.
    </details>

25. A credit model’s false negatives harm applicants unequally across groups.
    - A. Investigate fairness metrics and mitigate bias
    - B. Ignore disparate impact
    - C. Remove all monitoring
    - D. Publish applicant SSNs

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Fairness analysis and mitigation are required for responsible high-stakes ML.
    </details>

26. Red-team testers try jailbreaks and data-exfiltration prompts before go-live.
    - A. Adversarial testing / misuse evaluation
    - B. Skipping security review
    - C. Shipping with debug mode public
    - D. Hard-coding admin bypasses

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Proactive misuse testing finds jailbreaks and unsafe behaviors early.
    </details>

---

### Security, governance, MLOps

27. Only CI roles may register production model packages.
    - A. IAM least privilege on SageMaker Model Registry actions
    - B. Anonymous internet write access
    - C. Shared local admin passwords
    - D. Disabled MFA for all

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Restrict registry/deploy permissions with IAM.
    </details>

28. Prove to auditors that nobody publicly exposed the training bucket last quarter.
    - A. CloudTrail + Config + S3 access/public-block evidence
    - B. Verbal assurance only
    - C. Delete all logs
    - D. Turn off encryption

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Audit trails and config history provide evidence for compliance reviews.
    </details>

29. Detect sensitive PII sitting in data-science S3 buckets.
    - A. Amazon Macie
    - B. Amazon Polly
    - C. Amazon Pinpoint
    - D. Amazon WorkSpaces only

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Macie discovers sensitive data in S3.
    </details>

30. Automate train → evaluate → conditional register → deploy.
    - A. SageMaker Pipelines
    - B. Manual USB stick handoff
    - C. Email model binaries
    - D. Untracked laptop scripts only

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Pipelines encode repeatable, governed MLOps workflows.
    </details>

31. After launch, feature distributions shift vs training. Alert the team.
    - A. SageMaker Model Monitor (data drift)
    - B. Disable alarms
    - C. Ignore production metrics
    - D. Delete the endpoint silently

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Model Monitor detects data/model quality drift.
    </details>

32. Encrypt model artifacts and datasets with customer-managed keys.
    - A. AWS KMS CMKs with SSE-KMS
    - B. Plaintext on public disks
    - C. Shared Google Docs for weights
    - D. Unencrypted EBS by default preference

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: KMS CMKs give controlled encryption for sensitive ML assets.
    </details>

---

### Prompt & FM parameter scenarios

33. A coding assistant invents APIs. Product wants stricter, more factual answers.
    - A. Lower temperature + RAG over official docs + system constraints
    - B. Max temperature and no grounding
    - C. Remove citations
    - D. Allow unrestricted tool shell

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Lower randomness plus grounding reduces hallucinations for factual tasks.
    </details>

34. Marketing wants more diverse slogan ideas from the same brief.
    - A. Increase temperature (moderately)
    - B. Set temperature to 0 and ban creativity
    - C. Shrink context to empty
    - D. Disable the model

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Higher temperature increases diversity/creativity (with quality tradeoffs).
    </details>

35. The prompt includes three worked ticket examples before the new ticket. This is:
    - A. Few-shot prompting
    - B. Batch inference
    - C. Sharding
    - D. Blue/green DNS

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Multiple in-prompt examples = few-shot.
    </details>

36. “Do not mention competitors; refuse medical dosage advice.” These are:
    - A. Guardrail / policy instructions in the system prompt (or Guardrails service)
    - B. VPC route tables
    - C. EBS volume types
    - D. Placement groups

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Behavioral constraints belong in system prompts and/or Bedrock Guardrails.
    </details>

---

### Select-TWO and tradeoff scenarios

37. A bank builds GenAI over internal policies. Which TWO are essential? (Select TWO.)
    - A. Access control with IAM
    - B. Grounding via RAG on approved policies
    - C. Publishing all policies to an anonymous website
    - D. Hard-coding database passwords in prompts
    - E. Disabling encryption

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answers: A and B

      Explanation: Secure access plus grounded retrieval are foundational; C–E create severe risk.
    </details>

38. Choose TWO appropriate uses of Amazon Comprehend. (Select TWO.)
    - A. Sentiment analysis on reviews
    - B. Entity extraction from support tickets
    - C. Training ResNet from raw pixels end-to-end as a vision API
    - D. Managing Route 53 hosted zones
    - E. Issuing X.509 certificates

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answers: A and B

      Explanation: Comprehend is NLP (sentiment, entities, etc.), not vision networking or PKI.
    </details>

39. Choose TWO reasons to prefer RAG over fine-tuning for a changing knowledge base. (Select TWO.)
    - A. Documents update frequently
    - B. Need to cite current sources
    - C. You want permanent knowledge freeze forever
    - D. You refuse to retrieve any context
    - E. You only care about GPU vanity metrics

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answers: A and B

      Explanation: RAG shines when content changes and citations matter.
    </details>

40. Choose TWO SageMaker inference options that match their use case. (Select TWO.)
    - A. Real-time endpoint → low-latency online predictions
    - B. Batch transform → large offline scoring jobs
    - C. Real-time endpoint → month-long offline warehouse scoring only
    - D. Batch transform → 5 ms interactive UI calls
    - E. Glacier → online fraud scoring

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answers: A and B

      Explanation: Real-time for online latency; batch for bulk offline. C–E mismatch latency/storage.
    </details>

---

### End-to-end “pick the architecture” scenarios

41. Global retailer: multilingual product Q&A grounded on catalogs + order API tools + content filters.
    - A. Bedrock (LLM) + Knowledge Bases/RAG + Agents/tools + Guardrails (+ Translate if needed)
    - B. Single unmonitored EC2 with open SSH and no IAM
    - C. Public S3 website with secrets in query strings
    - D. Only CloudWatch Logs Insights with no model

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Production GenAI needs grounding, tools, and safety controls—not exposed unmanaged hosts.
    </details>

42. Media company: auto-caption videos, translate captions, voice-over in a second language.
    - A. Transcribe → Translate → Polly
    - B. Rekognition → Macie → Config
    - C. Personalize → Forecast → Lex
    - D. Athena → Redshift → DMS only

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Speech-to-text, then MT, then TTS is the classic media localization chain.
    </details>

43. Insurer: extract claim forms, detect claim text sentiment/risk phrases, human review exceptions.
    - A. Textract + Comprehend + A2I
    - B. GameLift + CloudFront + Route 53 only
    - C. WorkSpaces + WorkDocs only
    - D. Snowball + Snowmobile only

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Document AI + NLP + human review matches claims workflows.
    </details>

44. Startup MVP: chat with PDFs in one week, minimal ops.
    - A. Bedrock Knowledge Bases (managed RAG) pattern
    - B. Build a custom GPU cluster OS
    - C. Train a foundation model from scratch
    - D. Design a new silicon accelerator first

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Managed RAG gets an MVP live without training a foundation model.
    </details>

45. Enterprise: governed model promotion across accounts with approval gates.
    - A. SageMaker Model Registry + Pipelines + IAM/SCP governance
    - B. Emailing .pkl files with no review
    - C. Deploying from laptops with admin rights
    - D. Skipping evaluation always

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Registry + pipelines + org policies enable governed promotion.
    </details>

---

### Final mixed check

46. Which statement about hallucinations is most accurate?
    - A. Models can produce fluent but false content; ground and verify
    - B. Hallucinations never happen on AWS
    - C. Higher temperature always removes hallucinations
    - D. Logging causes hallucinations

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Hallucinations are a known GenAI risk; mitigate with grounding, constraints, and verification.
    </details>

47. Shared Responsibility: patching the Bedrock control-plane hosts is primarily:
    - A. AWS’s responsibility for the managed service
    - B. Every customer’s weekly on-site task
    - C. The marketing team’s job
    - D. Handled by disabling IAM

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: For managed services, AWS handles underlying infrastructure; customers handle data, identity, and app config.
    </details>

48. Best first step when a GenAI app leaks PII in outputs?
    - A. Enable Guardrails/PII filters, review prompts/logs, restrict data access
    - B. Publicly post the leak for virality
    - C. Increase temperature
    - D. Remove all authentication

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Contain with filters and access controls; investigate prompts and data paths.
    </details>

49. A practitioner compares fine-tuning vs prompt engineering for a small style change. Prefer first:
    - A. Prompt engineering (cheaper/faster to iterate)
    - B. Immediate full fine-tune of a huge model
    - C. Training a new FM from scratch
    - D. Buying dedicated fiber to every user

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Start with prompts; fine-tune when prompts cannot meet stable requirements.
    </details>

50. Success metric for a RAG support bot should emphasize:
    - A. Answer groundedness / citation correctness and user task success
    - B. Only token count vanity
    - C. Only how long the prompt looks
    - D. Only number of GPUs purchased

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: RAG quality is about grounded, useful answers—not infra vanity metrics.
    </details>

---

### Quick self-score (Test 9)

| Score | Result |
| --- | --- |
| 45–50 | Exam-ready on these patterns |
| 35–44 | Solid — revisit misses by service family |
| 25–34 | Re-study Domains 2–5 scenarios |
| Below 25 | Return to Parts 3–7 lessons, then retry Tests 8–9 |
