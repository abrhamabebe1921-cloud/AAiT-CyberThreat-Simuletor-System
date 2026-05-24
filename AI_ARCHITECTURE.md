# ThreatMapper AI Architecture
*Full breakdown of the Machine Learning, LLM, and RAG components powering the backend.*

## 1. LLM System (`Database/llm_agent_core.py`)
Acts as the central router and brain:
- **SQL_QUERY**: Converts natural language into PostgreSQL queries automatically.
- **RAG_QUERY**: Searches the internal security knowledge base.
- **MULTI_STEP**: Handles complex reasoning engine requests.

## 2. Multi-Provider Interface (`Database/llm_client_adapter.py`)
Modular AI adapters allowing switching between:
- Mock AI (for offline testing)
- LM Studio (fully local models)
- HuggingFace
- OpenAI

## 3. RAG System (`Database/ingest_rag.py`)
- Retrieves context to inject security policies into the AI.
- Uses `SentenceTransformer('all-MiniLM-L6-v2')` for powerful semantic searches.

## 4. Machine Learning Detectors (`AI/models/`)
Utilizes `scikit-learn` and `xgboost` inside `ml_pipeline.py`:
- `anomaly_detector.joblib` *(IsolationForest)*: Unsupervised anomaly detection for abnormal tracking and attacks.
- `fp_classifier.joblib` *(XGBClassifier)*: False-positive detection. Drops fake alerts from noisy IDS sensors.
- `preprocessor.joblib` *(StandardScaler/LabelEncoder)*: Normalizes data attributes seamlessly.

## 5. Security Log Telemetry
AI models actively learn from incoming streams:
- **Suricata IDS**: `eve.json`, `fast.log`, `stats.log`
- **Zeek Logging**: `conn.log`, `dns.log`, `http.log`, `files.log`

---
*This architecture is injected directly into the ThreatMapper AI Chat Context so it fully understands its own underlying operational footprint.*
