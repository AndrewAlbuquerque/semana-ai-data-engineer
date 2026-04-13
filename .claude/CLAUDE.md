# ShopAgent — Semana AI Data Engineer 2026

## Project Overview

Multi-agent e-commerce AI system built across 4 live nights (April 13-16, 2026) + 1 podcast.
Participants go from zero to a working ShopAgent: autonomous agents that query structured data (SQL)
and semantic data (vectors), with a conversational interface and professional frontend.

**Central Question:** *O que eu consigo fazer agora que nao conseguia antes?*

**Docker-First:** Days 1-3 run 100% local. Day 4 migrates to cloud — same architecture, different endpoint.

## Architecture: The Ledger + The Memory

```
+------------------+     +------------------+     +------------------+
|  DATA GENERATION |     |   AI / LLM       |     |   INTERFACE      |
|  ShadowTraffic   |     |   Claude         |     |   Chainlit       |
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

**The Ledger (Supabase/Postgres):** Exact data — revenue, counts, averages, JOINs
**The Memory (Qdrant):** Meaning — complaints, sentiment, review themes via RAG

## 3-Agent Crew (Day 4)

| Agent | Role | Tool | Store |
|-------|------|------|-------|
| AnalystAgent | SQL data analyst | supabase_execute_sql | The Ledger |
| ResearchAgent | Customer experience researcher | qdrant_semantic_search | The Memory |
| ReporterAgent | Executive report writer | (synthesis only) | Both via context |

## Stack by Day

| Day | Theme | New Stack |
|-----|-------|-----------|
| 1 Mon | INGERIR | ShadowTraffic, Pydantic, Claude Code, Docker |
| 2 Tue | CONTEXTUALIZAR | LlamaIndex, Qdrant, Postgres, MCP |
| 3 Wed | AGENTE | LangChain, Chainlit, AgentSpec |
| 4 Thu | MULTI-AGENT | CrewAI, DeepEval, LangFuse, Cloud |

## Directory Structure

```
gen/                          # Data generation (ShadowTraffic + Docker)
  docker-compose.yml          # Postgres + Qdrant + ShadowTraffic
  shadowtraffic.json          # E-commerce data generators
  init.sql                    # Postgres schema (customers, products, orders)
  .env.example                # Environment template
docs/                         # Event documentation
  AGENDA.md                   # 900-line detailed agenda with code examples
  semana-ai-data-engineer-shop-agent.md  # Full curriculum spec
presentation/                 # HTML slide decks (Days 1-4)
.claude/
  kb/                         # 18 Knowledge Base domains
  agents/                     # 10 SubAgents (ai-ml/, communication/, exploration/, domain/)
  commands/                   # Custom Claude Code commands
```

## Knowledge Base Domains (18)

| Domain | Path | Purpose | Day |
|--------|------|---------|-----|
| shadowtraffic | kb/shadowtraffic/ | Synthetic data generation | 1 |
| pydantic | kb/pydantic/ | Data validation + structured outputs | 1 |
| python | kb/python/ | Clean code patterns | 1-4 |
| llamaindex | kb/llamaindex/ | RAG ingestion + query | 2 |
| qdrant | kb/qdrant/ | Vector DB (The Memory) | 2-4 |
| supabase | kb/supabase/ | Postgres (The Ledger) | 2-4 |
| prompt-engineering | kb/prompt-engineering/ | Prompting techniques | 2 |
| langchain | kb/langchain/ | Agent framework + tool routing | 3 |
| chainlit | kb/chainlit/ | Chat interface + streaming | 3-4 |
| genai | kb/genai/ | GenAI architecture patterns | 3-4 |
| crewai | kb/crewai/ | Multi-agent orchestration | 4 |
| deepeval | kb/deepeval/ | LLM evaluation + testing | 4 |
| langfuse | kb/langfuse/ | LLMOps observability | 4 |
| testing | kb/testing/ | pytest patterns | 3-4 |
| architecture | kb/architecture/ | System design | 1-4 |
| exploration | kb/exploration/ | Codebase analysis | 1-4 |
| communication | kb/communication/ | Stakeholder communication | 1-4 |

## SubAgents

| Agent | Category | Domain |
|-------|----------|--------|
| shopagent-builder | domain/ | ShopAgent components by day (green, opus) |
| genai-architect | ai-ml/ | Multi-agent architecture design (purple, opus) |
| ai-data-engineer | ai-ml/ | Pipeline + cloud optimization (blue) |
| ai-prompt-specialist | ai-ml/ | Prompt engineering (blue) |
| llm-specialist | ai-ml/ | LLM selection + optimization |
| codebase-explorer | exploration/ | Code analysis + discovery |
| kb-architect | exploration/ | Knowledge base design |
| the-planner | communication/ | Project planning |
| meeting-analyst | communication/ | Meeting notes extraction |

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
# Edit .env with your SHADOWTRAFFIC_LICENSE and ANTHROPIC_API_KEY
docker compose up
```

## Conventions

- Python 3.11+ with type hints
- KB files: concepts < 150 lines, patterns < 200 lines
- File naming: kebab-case
- MCP validation required before KB updates
- All code production-ready (real imports, error handling)
- Environment-based URLs (localhost for local, cloud URLs via env vars)
