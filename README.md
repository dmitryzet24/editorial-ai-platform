# Intelligence: AI-Driven Content Discovery Platform

> **Enterprise-grade Editorial Intelligence for Niche Content Strategy.** > *Transforming social signals from Reddit/Web into a data-backed content plan for Blog.*

---

### 👔 Executive Summary
Managing a niche blog requires constant trend-spotting. This platform automates the "Discovery" phase by scanning social platforms for high-potential trends. It filters out irrelevant content (e.g., copyrighted characters), analyzes emotional appeal ("Cuteness Factor"), and presents the blog owner with a curated list of article ideas, reducing content research time by ~80%.

---

### 💻 Technical Architecture
This project demonstrates an **Event-Driven, Local-First Infrastructure** designed for production-level reliability.

- **Event Streaming:** Kafka-compatible **Redpanda** for decoupling ingestion from processing.
- **AI Orchestration:** Multi-stage **OpenAI (GPT-4o/mini)** pipeline with structured JSON outputs.
- **Semantic Memory:** **ChromaDB** (Vector Store) for automated content deduplication.
- **Data Engineering:** **dbt** for transforming raw event logs into actionable business metrics.
- **Infrastructure:** **Terraform** managed Docker environment.

---

### 🧠 Intelligence Logic:
To maintain brand integrity, the system applies specific AI-driven evaluation criteria:
1. **Technique Validation:** Automatic filtering to ensure content is specifically *knitted* (not crochet/amigurumi).
2. **Emotional Scoring:** LLM-based assessment of "Wholesome" and "Cozy" visual potential.
3. **Market Gaps:** Comparison of incoming trends against existing blog posts via semantic embeddings.
4. **Brand Safety:** Filtering out copyrighted intellectual property (e.g., Disney/Pokemon characters).
