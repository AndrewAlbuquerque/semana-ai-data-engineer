# ShopAgent — Semana AI Data Engineer 2026 (Gemini CLI Edition)

## Project Overview

Multi-agent e-commerce AI system built across 4 live nights (April 13-16, 2026).
Participants build **ShopAgent**: autonomous agents that query structured data (SQL) and semantic data (vectors).

**Core Mandate:** This project is optimized for **Gemini CLI**. Use its toolset (`grep_search`, `read_file`, `replace`, `run_shell_command`) to explore and build the system.

**Docker-First:** Days 1-3 run 100% local. Day 4 migrates to cloud.

## Architecture: The Ledger + The Memory

```
+------------------+     +------------------+     +------------------+
|  DATA GENERATION |     |   AI / LLM       |     |   INTERFACE      |
|  ShadowTraffic   |     |   Gemini 1.5 Pro |     |   Chainlit       |
+--------+---------+     |   LlamaIndex     |     +--------+---------+
         |               |   LangChain      |              |
         v               |   CrewAI         |              v
+------------------+     +--------+---------+     +------------------+
|  STORAGE         |              |               |   QUALITY        |
|  Postgres        |              v               |   DeepEval       |
|  (The Ledger)    |     +------------------+     |   LangFuse       |
|  Qdrant          |<--->|   MCP Protocol   |     +------------------+
|  (The Memory)    |     +------------------+
+------------------+
```

**The Ledger (Postgres):** Exact data — revenue, counts, averages, JOINs.
**The Memory (Qdrant):** Meaning — complaints, sentiment, themes via RAG.

## Gemini CLI Workflows

- **Research:** Use `grep_search` to find symbols and `read_file` to understand logic.
- **Strategy:** Formulate plans before making changes.
- **Execution:** Use `replace` for surgical edits. Always add tests to verify changes.
- **Validation:** Run `pytest` or `docker compose` commands to verify the system state.

## Data Model (4 Entities)

| Entity | Store | Fields |
|--------|-------|--------|
| customers | Postgres | customer_id, name, email, city, state, segment |
| products | Postgres | product_id, name, category, price, brand |
| orders | Postgres | order_id, customer_id (FK), product_id (FK), qty, total, status, payment, created_at |
| reviews | JSONL→Qdrant | review_id, order_id (FK), rating, comment, sentiment |

## Local Dev Quickstart

```bash
cd gen
cp .env.example .env
cp license.env.example license.env
# Edit .env with your GOOGLE_API_KEY
docker compose up -d
```

## Conventions

- Python 3.11+ with type hints.
- Use `ChatGoogleGenerativeAI` from `langchain-google-genai` for LLM tasks.
- Environment-based URLs (localhost for local, cloud URLs via env vars).
- Rigorous validation: Always check Postgres data and Qdrant collections after ingestion.
