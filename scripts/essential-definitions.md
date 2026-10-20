# Part 0 - Essential Definitions (Start Here)

Read this section **before** the exam outline and service deep-dives. Every term is written for beginners: plain meaning → why the exam cares → a tiny example.

**How to use:** Skim once, then re-read any term you miss in practice tests.

---

## 1. The big picture: AI → ML → Deep Learning → GenAI

| Term | Plain meaning | Exam tip | Tiny example |
| --- | --- | --- | --- |
| **Artificial Intelligence (AI)** | Building systems that do tasks that usually need human intelligence (see, decide, talk, plan). | AI is the **umbrella**. ML is one way to do AI. | A chatbot that answers customer questions. |
| **Machine Learning (ML)** | Teaching computers patterns from **data** instead of writing every rule by hand. | If the answer learns from examples → think ML. | Predict house price from past sales. |
| **Deep Learning (DL)** | ML that uses **many-layer neural networks**; strong on images, speech, and language. | DL needs more data/compute than classic ML. | Detect cats in photos with a CNN. |
| **Generative AI (GenAI)** | AI that **creates** new content (text, image, code, audio), not only labels or numbers. | Contrast with predictive/discriminative ML. | Write a product description from a brief. |
| **Foundation Model (FM)** | Huge pre-trained model that can be adapted to many tasks via prompts or fine-tuning. | Bedrock gives you FMs as a service. | One LLM used for summarize, translate, Q&A. |
| **Large Language Model (LLM)** | Foundation model trained mainly on text to understand and generate language. | Subtype of FM focused on language. | Claude / Llama / Titan Text style models. |
| **Neural network** | Model of connected layers of nodes that transform inputs into outputs. | Building block of deep learning. | Layers learn edges → shapes → objects in images. |
| **Model** | The learned (or configured) system that makes predictions or generations. | “Train a model” vs “call a model API.” | A spam classifier file you deploy. |
| **Algorithm** | The step-by-step learning method (how the model learns). | Algorithm ≠ trained model. | Decision tree algorithm vs your trained tree. |
| **Parameters / weights** | Numbers inside the model that were learned during training. | Not the same as **hyperparameters**. | Millions of weights in a neural net. |
| **Hyperparameters** | Settings **you** choose before/during training (learning rate, epochs, batch size). | Tuned; not learned as weights. | Learning rate = 0.001. |

**Memory hook:** AI ⊃ ML ⊃ Deep Learning; GenAI/LLMs sit on top of deep learning ideas but are used via prompts and APIs.

---

## 2. Learning types (must know)

| Term | What the data looks like | Goal | Example |
| --- | --- | --- | --- |
| **Supervised learning** | **Labeled** inputs (features + correct answer) | Predict labels or numbers | Email → spam / not spam |
| **Unsupervised learning** | **Unlabeled** data | Find structure/groups | Segment customers into clusters |
| **Semi-supervised** | Few labels + many unlabeled | Learn with less labeling cost | Label 1% of images, use the rest |
| **Self-supervised** | Labels created from the data itself | Pre-train language/vision models | Predict the next word in a sentence |
| **Reinforcement learning (RL)** | Agent + environment + **reward/penalty** | Learn actions that maximize reward | Game bot learns winning moves |
| **RLHF** | Humans rank/score model outputs | Align GenAI with human preference | Rank chatbot answers as better/worse |

**Quick pick rule:** Labels given → supervised. No labels, find groups → unsupervised. Learn by reward → RL. Create content → GenAI (often self-supervised pre-training + prompts).

---

## 3. Data vocabulary

| Term | Plain meaning | Example |
| --- | --- | --- |
| **Labeled data** | Each example has the “right answer” attached | Photo tagged “dog” |
| **Unlabeled data** | Raw examples with no answer tag | 1M photos with no tags |
| **Structured data** | Rows/columns (tables, CSVs, databases) | Sales spreadsheet |
| **Unstructured data** | No fixed table shape | PDF, email body, image, audio |
| **Semi-structured** | Partial structure (JSON, XML, logs) | API JSON response |
| **Feature** | An input variable the model uses | Age, income, pixel values |
| **Label / target** | The thing you want to predict | Churn = yes/no |
| **Training set** | Data used to teach the model | 70% of historical rows |
| **Validation set** | Data used to tune and compare during development | 15% holdout while tuning |
| **Test / holdout set** | Final unseen data for honest evaluation | Last 15% never used in training |
| **Feature engineering** | Creating/selecting better input columns | Turn “signup date” into “days since signup” |
| **EDA (Exploratory Data Analysis)** | Explore data before modeling (plots, stats, outliers) | Check missing values and class balance |
| **Token** | Small text unit models process (word piece/subword) | “understanding” → a few tokens |
| **Embedding** | Numbers that represent meaning of text/image | Similar sentences → similar vectors |
| **Vector / embedding store** | Database optimized to find similar embeddings | Store handbook chunk vectors for RAG |
| **Corpus** | A collection of documents/text used for training or retrieval | All company policy PDFs |

---

## 4. Classic ML task types

| Task | Output type | Common metrics | Example |
| --- | --- | --- | --- |
| **Classification** | Category / class | Accuracy, precision, recall, F1, confusion matrix | Fraud vs legit |
| **Binary classification** | Two classes | Same as above | Spam / not spam |
| **Multi-class** | Many mutually exclusive classes | Same family | Digits 0–9 |
| **Regression** | Continuous number | MAE, RMSE, R² | Predict sales $ |
| **Clustering** | Groups without preset labels | Silhouette (conceptually) | Customer segments |
| **Recommendation** | Ranked items for a user | Business KPIs / ranking metrics | “Customers also bought” |
| **Forecasting** | Future values over time | Forecast error metrics | Next week’s demand |
| **Anomaly detection** | Unusual vs normal | Precision/recall on rare events | Weird login behavior |
| **Computer vision (CV)** | Understanding images/video | Task-specific (mAP, accuracy) | Detect defects on a line |
| **NLP** | Understanding/generating language | Task-specific (F1, BLEU, ROUGE) | Sentiment of a review |
| **ASR / speech-to-text** | Audio → text | WER (concept) | Call transcription |
| **TTS / text-to-speech** | Text → audio | Naturalness | IVR voice reply |
| **OCR / document AI** | Image/PDF → text/fields | Field accuracy | Extract invoice totals |

---

## 5. Train → evaluate → use

| Term | Plain meaning | Don’t confuse with |
| --- | --- | --- |
| **Training** | Learning patterns from data (update weights) | Inference |
| **Inference / prediction** | Using a trained model on new inputs | Training |
| **Batch inference** | Score many records offline (minutes/hours OK) | Real-time |
| **Real-time inference** | Low-latency online predictions (ms–seconds) | Overnight batch |
| **Asynchronous inference** | Long jobs / big payloads; result when ready | Instant UI score |
| **Epoch** | One full pass through the training data | One batch |
| **Batch size** | How many samples per weight update | Full dataset |
| **Learning rate** | How big each weight update step is | Epoch count |
| **Overfitting** | Great on train, poor on new data (memorized) | Underfitting |
| **Underfitting** | Too simple; weak on train **and** new data | Overfitting |
| **Bias (stats/ML)** | Systematic error; model assumptions too strong | Fairness bias alone |
| **Variance** | Sensitivity to training-set quirks | Bias |
| **Regularization** | Techniques to reduce overfitting | More layers always |
| **Cross-validation** | Rotate train/validate splits for stabler estimates | Single lucky split |
| **Ground truth** | The trusted correct labels/answers | Model output |

### Evaluation metrics (plain English)

| Metric | Asks… | Prefer when… |
| --- | --- | --- |
| **Accuracy** | Overall % correct? | Classes are balanced |
| **Precision** | Of predicted positives, how many were right? | False alarms are costly |
| **Recall (sensitivity)** | Of real positives, how many did we catch? | Misses are costly |
| **F1 score** | Balance of precision and recall | Imbalanced classes |
| **Confusion matrix** | TP / FP / TN / FN counts | Debugging errors |
| **MAE / RMSE** | How far off are numeric predictions? | Regression |
| **BLEU** | Translation quality vs human refs | Machine translation |
| **ROUGE** | Summary overlap vs human refs | Summarization |
| **Perplexity** | How “surprised” an LM is by text (lower often better) | Language modeling |

---

## 6. Generative AI & prompting basics

| Term | Plain meaning | Example |
| --- | --- | --- |
| **Prompt** | The text/instructions you send the model | “Summarize this email in 3 bullets” |
| **System prompt** | Standing instructions for behavior/role | “You are a concise support agent…” |
| **Prompt engineering** | Crafting prompts for better, safer outputs | Add format, constraints, examples |
| **Zero-shot** | Task with **no** examples in the prompt | “Classify this ticket: …” |
| **One-shot** | Task with **one** example | Show 1 sample Q→A, then ask new Q |
| **Few-shot** | Task with a few examples | Show 3 samples, then ask |
| **Chain-of-thought** | Ask the model to reason step by step | “Think step by step, then answer” |
| **Temperature** | Randomness knob; **lower** = more deterministic | FAQ bot → low temperature |
| **Top-p / Top-k** | Sampling controls for token choice diversity | Creative copy → higher diversity |
| **Context window** | Max tokens the model can see at once | Long chat may need summarization |
| **Hallucination** | Fluent but **false** invented content | Fake AWS service name |
| **Grounding** | Tie answers to trusted sources | Cite handbook paragraphs |
| **RAG** | Retrieve relevant docs, then generate with them | Policy Q&A over PDFs |
| **Fine-tuning** | Extra training on your data to change behavior/style | Always answer in JSON tickets |
| **Continued pre-training** | More training on domain text (often unlabeled) | Teach medical vocabulary |
| **Transfer learning** | Reuse knowledge from one task on a related task | Vision backbone → defect detector |
| **Agents / tool use** | Model plans and calls tools/APIs | “Get order status” via Lambda |
| **Guardrails** | Filters/policies on inputs/outputs (toxicity, PII, topics) | Block hate speech / strip PII |
| **Prompt injection** | Malicious text tries to override instructions | “Ignore previous rules…” |
| **Jailbreaking** | Attempts to bypass safety limits | Trick model into disallowed content |
| **Multimodal** | Handles more than one data type (text+image…) | Caption a product photo |
| **Tokens in / out** | Billed/processed units of prompt and completion | Longer answers cost more |

**RAG vs fine-tuning (exam favorite):**

- Docs change often / need citations → **RAG**
- Stable style/format / narrow behavior → consider **fine-tuning**
- Always try **prompting** first (cheapest)

---

## 7. Responsible AI vocabulary

| Term | Plain meaning | Why it matters |
| --- | --- | --- |
| **Bias (fairness)** | Unfair systematic outcomes for groups | Hiring/credit risk |
| **Fairness** | Goal of equitable treatment across groups | Measure + mitigate |
| **Transparency** | Being open about how the system works/limits | Trust and audits |
| **Explainability** | Explaining *why* a prediction happened | Regulators, stakeholders |
| **Interpretability** | How understandable the model internals are | Trees > deep nets usually |
| **Model card** | Doc of purpose, data, metrics, limits | “Nutrition label” for models |
| **Human-in-the-loop** | People review/override AI when needed | A2I for low confidence |
| **Toxicity** | Harmful/offensive generated content | Filter + monitor |
| **Privacy** | Protect personal/sensitive data | PII redaction, access control |
| **Accountability** | Clear ownership of AI decisions/risks | Governance process |

---

## 8. Cloud & AWS foundations (needed for AI on AWS)

| Term | Plain meaning | AI angle |
| --- | --- | --- |
| **Region** | Geographic AWS area | Pick for latency/compliance |
| **Availability Zone (AZ)** | Isolated data centers in a Region | Resilience |
| **IAM** | Who can do what on which resource | Least privilege for Bedrock/SageMaker |
| **Shared Responsibility Model** | AWS secures the cloud; you secure *in* the cloud | You own prompts, data, access |
| **Encryption at rest** | Data protected while stored | S3 + KMS for training data |
| **Encryption in transit** | Data protected while moving | TLS to APIs |
| **S3** | Object storage | Datasets, model artifacts, docs for RAG |
| **Lambda** | Serverless functions | Glue agents/tools to APIs |
| **VPC / PrivateLink** | Private network paths | Keep AI traffic off public internet |
| **CloudTrail** | API activity log | Audit who invoked models |
| **AWS Config** | Resource configuration compliance | Encryption/public-access checks |
| **Macie** | Discover sensitive data in S3 | Find PII in training buckets |
| **KMS** | Key management for encryption | Customer-managed keys (CMK) |

---

## 9. AWS AI services — one-line map

Use this map when a scenario asks “which service?”

### Language & documents
| Service | One-line job |
| --- | --- |
| **Amazon Comprehend** | NLP: sentiment, entities, key phrases, classification |
| **Amazon Translate** | Machine translation (+ custom terminology) |
| **Amazon Transcribe** | Speech → text |
| **Amazon Polly** | Text → speech |
| **Amazon Textract** | OCR + forms/tables from documents |
| **Amazon Kendra** | Intelligent enterprise search / Q&A over docs |
| **Amazon Lex** | Chatbots / voice bots (intents & slots) |
| **Amazon A2I** | Human review loops for ML predictions |
| **Amazon Mechanical Turk** | On-demand human workforce for tasks/labels |

### Vision & personalization
| Service | One-line job |
| --- | --- |
| **Amazon Rekognition** | Image/video analysis & moderation |
| **Amazon Personalize** | Real-time recommendations |
| **Amazon Forecast** | Time-series forecasting |

### Build / GenAI platforms
| Service | One-line job |
| --- | --- |
| **Amazon Bedrock** | Managed foundation models via API |
| **Bedrock Knowledge Bases** | Managed RAG pattern over your data |
| **Bedrock Guardrails** | Safety/PII/topic controls for GenAI apps |
| **Bedrock Agents** | Orchestrate FM + tools/APIs |
| **Amazon SageMaker** | Build, train, tune, deploy custom ML |
| **SageMaker Canvas** | No-code ML for analysts |
| **SageMaker JumpStart** | Pre-built models / quick start FMs |
| **SageMaker Pipelines** | MLOps workflows (CI/CD for ML) |
| **SageMaker Model Registry** | Catalog/approve model versions |
| **SageMaker Model Monitor** | Detect drift / quality issues in production |
| **SageMaker Clarify** | Bias detection & explainability help |
| **Amazon Q** | AWS’s generative assistant family for work/AWS |

---

## 10. MLOps & lifecycle (short)

Typical supervised flow:

1. **Collect** data  
2. **Prepare** (clean, label, split)  
3. **Train / tune**  
4. **Evaluate** on holdout  
5. **Deploy**  
6. **Monitor** (drift, quality) → retrain when needed  

| Term | Plain meaning |
| --- | --- |
| **MLOps** | People + process + tools to run ML reliably in production |
| **Data drift** | Live inputs no longer look like training data |
| **Model drift / degradation** | Performance drops as the world changes |
| **Model registry** | Versioned catalog of models for promotion |
| **CI/CD for ML** | Automated build/train/test/deploy pipelines |

---

## 11. Instant “don’t mix these up” pairs

| A | B | Difference |
| --- | --- | --- |
| AI | ML | AI = goal/field; ML = learn-from-data approach |
| Training | Inference | Learn vs use |
| Overfitting | Underfitting | Memorized vs too simple |
| Precision | Recall | False alarms vs misses |
| RAG | Fine-tuning | Fetch fresh facts vs change model behavior |
| Batch | Real-time | Offline bulk vs low-latency online |
| Bedrock | SageMaker | Consume FMs vs build/train custom ML (overlap exists, but this is the exam framing) |
| Lex | Polly | Understand dialog vs speak text |
| Transcribe | Translate | Speech→text vs language→language |
| Textract | Comprehend | Extract from documents vs understand text meaning |
| Temperature high | Temperature low | More creative/random vs more stable |

---

## 12. 60-second starter checklist

Before deeper Parts, you should be able to explain in one sentence each:

1. AI vs ML vs DL vs GenAI  
2. Supervised vs unsupervised vs RL  
3. Labeled vs unlabeled; structured vs unstructured  
4. Classification vs regression  
5. Training vs inference; overfitting vs underfitting  
6. Precision vs recall  
7. Prompt, temperature, hallucination, RAG, fine-tuning  
8. Bias, fairness, explainability, guardrails  
9. IAM + shared responsibility for AI apps  
10. Bedrock vs SageMaker vs “which AI service for X”

If any item is fuzzy, re-read that table above, then continue to **Part 1 - Exam Overview**.
