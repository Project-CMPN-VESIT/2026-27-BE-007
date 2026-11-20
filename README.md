# AI Legal Assistant Suite (ALAS): Legal Intelligence Platform

[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Next.js](https://img.shields.io/badge/Frontend-Next.js%2016-black?style=flat-square&logo=next.js)](https://nextjs.org/)
[![React](https://img.shields.io/badge/UI-React%2019-61DAFB?style=flat-square&logo=react)](https://react.dev/)
[![LangGraph](https://img.shields.io/badge/Orchestration-LangGraph-FF4F00?style=flat-square)](https://langchain-ai.github.io/langgraph/)
[![Mistral AI](https://img.shields.io/badge/LLM-Mistral%20Large-FF7000?style=flat-square)](https://mistral.ai/)
[![Celery](https://img.shields.io/badge/Tasks-Celery%20%2B%20Redis-37814A?style=flat-square&logo=celery)](https://docs.celeryq.dev/)
[![Tailwind CSS](https://img.shields.io/badge/Styling-Tailwind%20CSS-38B2AC?style=flat-square&logo=tailwind-css)](https://tailwindcss.com/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python)](https://python.org)

**AI Legal Assistant Suite (ALAS): Legal Intelligence Platform** is an institutional-grade, multi-agent legal technology platform engineered for law firm associates, corporate counsels, and litigators. Built with an authoritative, high-density legal aesthetic (inspired by Linear, Harvey, and Ironclad), ALAS pairs deterministic milestone orchestration via **LangGraph** with deep statutory grounding in **Indian Law** and live search integration with **Indian Kanoon**.

---

## Table of Contents

1. [Executive Overview](#executive-overview)
2. [Core Capabilities & Pillars](#core-capabilities--pillars)
   - [Pillar 1: Contract Analysis & Risk Audit](#pillar-1-contract-analysis--risk-audit)
   - [Pillar 2: Autonomous Contract Drafting Studio](#pillar-2-autonomous-contract-drafting-studio)
   - [Pillar 3: Litigation Intelligence & Multi-Doc Case Files](#pillar-3-litigation-intelligence--multi-doc-case-files)
   - [Pillar 4: Pre-Trial Adversarial Debate Simulation](#pillar-4-pre-trial-adversarial-debate-simulation)
   - [Pillar 5: Jurist Legal Assistant & Kanoon RAG](#pillar-5-jurist-legal-assistant--kanoon-rag)
3. [System Architecture](#system-architecture)
4. [Tech Stack](#tech-stack)
5. [Repository Structure](#repository-structure)
6. [Prerequisites](#prerequisites)
7. [Installation & Setup](#installation--setup)
   - [1. Backend Setup](#1-backend-setup)
   - [2. Environment Configuration](#2-environment-configuration)
   - [3. Running Backend Services](#3-running-backend-services)
   - [4. Frontend Setup](#4-frontend-setup)
8. [End-to-End User Guide](#end-to-end-user-guide)
9. [Configuration Reference (`.env`)](#configuration-reference-env)
10. [Evaluation & Benchmarking Suite](#evaluation--benchmarking-suite)
11. [Troubleshooting & FAQ](#troubleshooting--faq)
12. [Design Standards & Architecture](#design-standards--architecture)

---

## Executive Overview

Contract auditing and litigation discovery are traditionally bottlenecked by unstructured parsing, human cognitive fatigue, and unreliable non-deterministic AI agents. ALAS addresses this with:

- **Deterministic Milestones with Structured Autonomy**: Rather than permitting language models to drift into runaway loops, LangGraph state machines enforce linear document coverage and risk calculation, while granting focused autonomy only for statutory legal research.
- **Indian Statutory Grounding**: Direct reasoning against the Indian Contract Act (1872), Specific Relief Act (1963), Arbitration & Conciliation Act (1996), Information Technology Act (2000), Bharatiya Nyaya Sanhita (BNS / IPC), Bharatiya Nagarik Suraksha Sanhita (BNSS / CrPC), and Bharatiya Sakshya Adhiniyam (BSA / Evidence Act).
- **Live Indian Kanoon Research Engine**: Automated scraping and query synthesis referencing Indian judgments, High Courts, and the Supreme Court of India.
- **Institutional Non-AI Aesthetic**: Calm slate palettes, dense tabular layouts, high-contrast typography, and live execution telemetry—no generic multi-colored AI gradients.

---

## Core Capabilities & Pillars

### Pillar 1: Contract Analysis & Risk Audit
- **Comprehensive Document Ingestion**: Supports `.pdf`, `.docx`, and `.txt` agreements (NDAs, MSAs, SaaS, Employment, Commercial Leases).
- **Automated Clause Segmentation & Entity Resolution**: Normalizes contracting entities, effective dates, governing jurisdiction, and obligation hierarchies.
- **Risk Severity Scoring**: Every extracted clause receives a deterministic severity badge (`CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, `INFO`), legal reasoning, confidence score, and applicable statutory sections.
- **Interactive Clause Redline Studio**: Real-time modal allowing attorneys to revise individual clauses with custom bias postures (e.g. *Pro-Company*, *Pro-Vendor*, *Balanced*), review side-by-side diffs, and commit revisions directly back into the contract body.
- **Statutory Cross-Checking**: Cites specific statutory sections (e.g., Section 27 restraint of trade, Section 74 liquidated damages) and relevant Kanoon case laws.

### Pillar 2: Autonomous Contract Drafting Studio
- **6-Stage Milestone LangGraph Pipeline**:
  1. *Intake & Requirements Analysis*: Captures commercial objectives, parties, and deal constraints.
  2. *Skeleton Blueprint Generation*: Constructs an exhaustive institutional table of contents and structural sections.
  3. *Statutory Grounding & Precedents*: Integrates mandatory Indian statutory protections and standard boilerplate clauses.
  4. *Autonomous Clause Generation*: Progressively streams clause prose adhering to the specified style.
  5. *Adversarial Legal Review & Polish*: Audits draft for ambiguities, unconscionable clauses, and missing indemnities.
  6. *Final Validation*: Generates markdown and production-ready PDF deliverables.
- **Real-Time Stage Telemetry**: Live Server-Sent Events (SSE) streaming through the `DraftingStreamConsole`.
- **Posture & Style Controls**: Toggle drafting stance (*Pro-Buyer*, *Pro-Seller*, *Balanced*) and style (*Institutional Legal*, *Plain English*).
- **Version Control & Export**: Full version revision history, live markdown editor, and one-click PDF generation.

### Pillar 3: Litigation Intelligence & Multi-Doc Case Files
- **Multi-Document Litigation Dossiers**: Ingest entire case folders comprising FIRs, Police Charge-Sheets, 161/164 CrPC Witness Statements, Bail Applications, Medical/Forensic Reports, and Pleadings.
- **Chronological Fact Timeline**: Automatically extracts events across all documents with evidentiary page anchors and corroboration cross-links.
- **Witness Contradiction Engine**: Identifies inconsistencies across multiple witness depositions and FIR statements.
- **Statutory Charge Mapping**: Maps alleged factual narratives to specific penal sections (BNS/IPC) and procedural codes (BNSS/CrPC).
- **Procedural Compliance Audits**: Flags violations of statutory procedural mandates (e.g., Section 41A CrPC notice violations, unlawful arrest protocols, chain-of-custody defects in seizure memos).
- **Investigative Gap Detection**: Highlights missing documents, unexamined witnesses, and absent ballistics or forensic reports.

### Pillar 4: Pre-Trial Adversarial Debate Simulation
- **Multi-Agent Courtroom Simulation**:
  - **Prosecution / Plaintiff Agent**: Argues the prima facie case, builds on charges and witness testimony.
  - **Defense Agent**: Formulates statutory objections, cites witness contradictions, procedural lapses, and mitigating factors.
  - **Judicial Bench / Judge Agent**: Synthesizes both arguments, assesses evidentiary admissibility under the Indian Evidence Act / BSA, highlights statutory vulnerabilities, and issues a final decision.
- **Strategic Pre-Trial Brief**: Compiles a comprehensive judicial brief summarizing key contestations, litigation risks, and recommended courtroom tactics.

### Pillar 5: Jurist Legal Assistant & Kanoon RAG
- **Contextual Document Q&A**: Ask detailed legal questions directly against any uploaded contract or case dossier.
- **Statutory & Case Law Grounding**: Returns answers citing relevant case law and sections rather than generic legal advice.

---

## System Architecture

```mermaid
flowchart TD
    subgraph Client["Frontend Layer (Next.js 16 + React 19)"]
        UI["Institutional UI (Shadcn + Tailwind)"]
        LiveSSE["SSE Stream Listeners (Drafting & Debate)"]
        ApiClient["Axios API Client (frontend/services/api.ts)"]
    end

    subgraph API["Backend Gateway (FastAPI)"]
        Router["FastAPI Router (/api/v1)"]
        ContractsRoute["/contracts (Upload, Audit, Redline)"]
        CasesRoute["/cases (Dossier, Timeline, Debate)"]
        TasksRoute["/tasks (Celery Job Inspection)"]
        HealthRoute["/health, /db/health, /celery/health"]
    end

    subgraph Orchestration["Agent & Orchestration Layer (LangGraph)"]
        ContractGraph["Contract Analysis LangGraph<br/>(Deterministic Milestones + Research Loop)"]
        DraftingGraph["Contract Drafting 6-Stage Graph"]
        CaseGraph["Litigation Intelligence Multi-Doc Graph"]
        DebateGraph["Adversarial Trial Debate Graph<br/>(Prosecution vs Defense vs Bench)"]
        JuristRAG["Jurist Kanoon RAG Engine"]
    end

    subgraph Workers["Distributed Task Processing"]
        Redis[("Redis Broker & Result Store<br/>(port 6379)")]
        CeleryWorker["Celery Worker Pool<br/>(Async Heavy Processing)"]
    end

    subgraph Storage["Persistence & Intelligence Tools"]
        DB[("PostgreSQL / SQLite<br/>(SQLAlchemy Async)")]
        Chroma[("ChromaDB<br/>(Vector Store)")]
        KanoonTool["Indian Kanoon Search & Scraper<br/>(DuckDuckGo Index + Direct Doc Fetch)"]
        LLM["Mistral AI API<br/>(mistral-large-latest + mistral-embed)"]
    end

    UI --> ApiClient
    LiveSSE <--> API
    ApiClient --> Router
    Router --> ContractsRoute
    Router --> CasesRoute
    Router --> TasksRoute
    Router --> HealthRoute

    ContractsRoute --> CeleryWorker
    CasesRoute --> CeleryWorker
    CeleryWorker <--> Redis
    CeleryWorker --> Orchestration

    Orchestration --> DB
    Orchestration --> Chroma
    Orchestration --> KanoonTool
    Orchestration --> LLM
```

---

## Tech Stack

| Layer | Technologies |
|---|---|
| **Frontend Framework** | [Next.js 16](https://nextjs.org/) (App Router), [React 19](https://react.dev/), [TypeScript 5](https://www.typescriptlang.org/) |
| **Styling & Components** | [Tailwind CSS 3.4](https://tailwindcss.com/), [Shadcn UI](https://ui.shadcn.com/), [Lucide React](https://lucide.dev/), [Recharts](https://recharts.org/) |
| **Markdown & Export** | [Marked](https://marked.js.org/), [React-Markdown](https://github.com/remarkjs/react-markdown), [html2pdf.js](https://ekoopmans.github.io/html2pdf.js/), [pdfmake](http://pdfmake.org/) |
| **Backend API** | [FastAPI](https://fastapi.tiangolo.com/), [Uvicorn](https://www.uvicorn.org/), [Pydantic v2](https://docs.pydantic.dev/) |
| **Agent Framework** | [LangGraph](https://langchain-ai.github.io/langgraph/), [LangChain](https://python.langchain.com/) |
| **LLMs & Embeddings** | [Mistral AI](https://mistral.ai/) (`mistral-large-latest`, `mistral-embed`) |
| **Task Queue & Cache** | [Celery 5](https://docs.celeryq.dev/), [Redis 7](https://redis.io/) |
| **Databases** | [PostgreSQL](https://www.postgresql.org/) (Production) / [SQLite](https://sqlite.org/) (Local Fallback), [SQLAlchemy 2](https://www.sqlalchemy.org/) |
| **Vector Database** | [ChromaDB](https://www.trychroma.com/) |
| **Legal Search & Research** | Custom Indian Kanoon tools (DDG route-pattern querying + HTML parser) |

---

## Repository Structure

```text
MajorProject/
├── backend/
│   ├── agents/                   # LangGraph workflows and specialist subagents
│   │   ├── case_orchestrator.py               # Case timeline & multi-doc intelligence
│   │   ├── contract_drafting_langgraph.py     # 6-Stage autonomous drafting engine
│   │   ├── contract_langgraph_orchestrator.py # Milestone-based contract audit engine
│   │   ├── trial_debate_langgraph.py          # Adversarial Prosecution vs Defense debate
│   │   └── jurist_rag_langgraph.py            # Kanoon-grounded legal assistant
│   ├── database_migrations/      # Safe schema synchronizers
│   ├── models/                   # SQLAlchemy declarative ORM models
│   │   ├── cases.py              # Case files, documents, facts, contradictions
│   │   ├── contract_analysis.py  # Contract audits, clauses, risks, obligations
│   │   └── contract_draft.py     # Draft versions, blueprints, revision history
│   ├── routes/                   # FastAPI route endpoints
│   │   ├── contracts.py          # Contract upload, audit, redline, draft routes
│   │   ├── cases.py              # Case management, analysis, debate streaming
│   │   └── tasks.py              # Celery task status inspection
│   ├── schemas/                  # Pydantic v2 validation models
│   ├── services/                 # Business logic, document extraction, vector indexing
│   ├── storage/                  # Local uploads, processed outputs, ChromaDB
│   ├── tasks/                    # Celery asynchronous worker tasks
│   ├── tools/                    # Indian Kanoon search & statutory scrapers
│   ├── config.py                 # Pydantic settings loading from .env
│   ├── database.py               # Async/Sync database engine initialization
│   ├── main.py                   # FastAPI application initialization & middleware
│   ├── requirements.txt          # Python dependencies
│   └── worker.py                 # Celery worker process entry point
│
├── frontend/
│   ├── app/                      # Next.js App Router pages
│   │   ├── dashboard/
│   │   │   ├── page.tsx          # Executive Command Center
│   │   │   ├── analysis/         # Pillar 1: Contract Analysis & Deep Audit
│   │   │   │   ├── page.tsx      # Contract repository and filter grid
│   │   │   │   ├── upload/       # Document upload and audit intake
│   │   │   │   └── [id]/         # Deep audit suite, risk table, Kanoon citations
│   │   │   ├── drafting/         # Pillar 2: Contract Drafting Studio
│   │   │   │   ├── page.tsx      # Blueprint intake and configuration
│   │   │   │   └── editor/[id]/  # Live editor, redline studio & PDF export
│   │   │   ├── cases/            # Pillar 3 & 4: Litigation Files & Pre-Trial Debate
│   │   │   │   ├── page.tsx      # Case files repository
│   │   │   │   ├── [id]/         # Multi-doc workspace & upload
│   │   │   │   └── [id]/results/ # Chronological timeline & debate arena
│   │   │   └── settings/         # Profile & configuration preferences
│   ├── components/               # Atomic Shadcn UI components and domain widgets
│   │   ├── ui/                   # Reusable UI primitives (Button, Card, Badge, etc.)
│   │   └── dashboard/            # Domain components (Header, Sidebar, Modals, Streamers)
│   ├── services/api.ts           # Centralized Axios API client
│   └── package.json              # Frontend dependencies and build scripts
│
├── docs/                         # Technical architecture specifications
│   ├── UI_ARCHITECTURE.md        # UI design system & routing specifications
│   └── progress_tracker.md       # LangGraph refactoring & Kanoon integration notes
│
├── evaluation/                   # Evaluation framework (CUAD benchmarks & live tests)
├── start_backend.ps1             # Automated PowerShell backend launcher
├── AGENTS.md                     # Architectural rules for autonomous coding agents
└── README.md                     # This document
```

---

## Prerequisites

Before starting, ensure you have the following installed on your system:

- **Python**: Version `3.10` or `3.11` (Python 3.12 is also supported)
- **Node.js**: Version `18.x` or `20.x` (LTS recommended) and `npm` (or `pnpm`)
- **Redis Server**: Version `6.x` or `7.x`
  - *Option A (Docker - Recommended)*: Have Docker Desktop running; the launcher script can auto-start Redis.
  - *Option B (Native/WSL)*: Redis running locally on `localhost:6379`.
- **Mistral AI API Key**: Obtain a key from the [Mistral AI Console](https://console.mistral.ai/).

---

## Installation & Setup

### 1. Backend Setup

Clone the repository and set up a Python virtual environment:

```bash
# Navigate to the project root
cd MajorProject

# Create a virtual environment
python -m venv venv

# Activate the virtual environment:
# On Windows PowerShell:
.\venv\Scripts\Activate.ps1
# On Windows Command Prompt:
venv\Scripts\activate.bat
# On Linux / macOS:
source venv/bin/activate

# Upgrade pip and install all backend dependencies
python -m pip install --upgrade pip
pip install -r backend/requirements.txt
```

### 2. Environment Configuration

Create a `.env` file in the root of the project (or copy from `backend/.env.example`):

```bash
cp backend/.env.example .env
```

Open `.env` and set your credentials:

```dotenv
# Redis and Celery Task Broker
REDIS_URL=redis://localhost:6379/0
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/1

# File Storage Paths
UPLOAD_DIR=backend/storage/uploads
OUTPUT_DIR=backend/storage/outputs
CHROMA_DIR=backend/storage/chroma

# Mistral AI Credentials
MISTRAL_API_KEY=your_mistral_api_key_here
MISTRAL_MODEL=mistral-large-latest
MISTRAL_EMBEDDING_MODEL=mistral-embed

# Feature Toggles
CONTRACT_ANALYSIS_ENABLED=true
WEB_RESEARCH_ENABLED=true
AUTO_RUN_MIGRATIONS=true

# Optional: PostgreSQL (if omitted, SQLite is used automatically)
# DATABASE_URL=postgresql://user:password@localhost:5432/alas_db
```

> [!NOTE]
> If `DATABASE_URL` is omitted, ALAS will automatically initialize a local SQLite database (`backend/storage/major_project.db`) without requiring any PostgreSQL installation.

### 3. Running Backend Services

#### Automated Method (PowerShell - Windows)

The project includes an intelligent startup script `start_backend.ps1` that checks Docker for Redis, launches the Celery background worker in a separate console, and runs the FastAPI server:

```powershell
.\start_backend.ps1
```

You can also run specific components using switches:
```powershell
.\start_backend.ps1 -ServerOnly   # Starts only the FastAPI server
.\start_backend.ps1 -WorkerOnly   # Starts only the Celery worker
.\start_backend.ps1 -RedisOnly    # Starts only the Redis container
```

#### Manual Method (Cross-Platform)

If you prefer to run services manually across separate terminals:

**Terminal 1 — Redis Server**:
```bash
# Using Docker:
docker run -d --name redis -p 6379:6379 redis:7-alpine

# Or native Redis:
redis-server
```

**Terminal 2 — Celery Background Worker**:
```bash
# Activate your virtual environment first
source venv/bin/activate  # or .\venv\Scripts\Activate.ps1 on Windows

# Start the Celery worker
celery -A backend.worker.celery_app worker --loglevel=info -P solo
```
*(Use `-P solo` or `-P threads` on Windows environments for optimal Celery concurrency).*

**Terminal 3 — FastAPI Web Server**:
```bash
# Activate your virtual environment first
source venv/bin/activate  # or .\venv\Scripts\Activate.ps1 on Windows

# Start Uvicorn
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

Backend services will be live at:
- **API Server**: [http://localhost:8000](http://localhost:8000)
- **Interactive Swagger Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Redoc Documentation**: [http://localhost:8000/redoc](http://localhost:8000/redoc)
- **System Health Endpoint**: [http://localhost:8000/health](http://localhost:8000/health)

---

### 4. Frontend Setup

In a separate terminal, install dependencies and start the Next.js development server:

```bash
# Navigate to the frontend directory
cd frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

The frontend application will be accessible at:
👉 **[http://localhost:3000](http://localhost:3000)**

---

## End-to-End User Guide

### 1. Navigating the Executive Command Center (`/dashboard`)
Upon opening the application, the command center presents:
- High-level KPIs: Active Contracts, Critical Risk Exposures, Open Litigations, and Pending Drafts.
- Quick action buttons to immediately upload a contract, launch a draft, or create a litigation dossier.
- Recent analytical audit activity and risk distribution charts.

### 2. Performing a Deep Contract Audit (`/dashboard/analysis`)
1. Click **"New Analysis"** or navigate to `/dashboard/analysis/upload`.
2. Upload a contract file (`.pdf`, `.docx`, or `.txt`).
3. (Optional) Provide contracting parties (e.g. *Acme Corp* vs *Beta Solutions*), contract category, and specific focus areas.
4. Click **"Start Analysis"**.
5. Once processing completes, inspect the **Contract Analysis Suite** (`/dashboard/analysis/[id]`):
   - **Risk Metric Summary**: Overall risk score (0–100), critical risk counts, and executive summary.
   - **Clauses & Obligations Table**: Filter clauses by severity (`CRITICAL`, `HIGH`, `MEDIUM`, `LOW`).
   - **Statutory Grounds**: View specific sections of the Indian Contract Act or related statutes cited for each violation.
   - **Indian Kanoon Precedents**: Examine live case law links explaining the legal rationale.
   - **Interactive Redlining**: Click **"Redline Clause"** on any risky provision to adjust parameters, generate alternative wording, and save changes to the contract.
   - **Jurist Assistant**: Open the Jurist drawer on the right to interrogate the contract directly.

### 3. Drafting a Contract with Autonomous LangGraph (`/dashboard/drafting`)
1. Navigate to `/dashboard/drafting`.
2. Provide your drafting prompt (e.g., *"Draft a Software-as-a-Service Master Agreement under Indian Law with strict non-solicitation, 30-day payment terms, and reciprocal indemnification"*).
3. Select your drafting parameters:
   - **Governing Law**: Indian Contract Act 1872, Arbitration & Conciliation Act, etc.
   - **Party Bias**: *Balanced*, *Pro-Company*, or *Pro-Vendor*.
   - **Drafting Style**: *Institutional Legal* or *Plain English*.
4. Click **"Generate Blueprint & Draft"**.
5. Watch the **6-Stage Drafting Console** stream events in real time (Intake ➔ Skeleton ➔ Statutory Grounding ➔ Clause Generation ➔ Adversarial Review ➔ Polish).
6. Edit the output in the rich markdown editor and click **"Export as PDF"** for an institutional-grade PDF.

### 4. Litigation Multi-Doc Synthesis & Trial Debate (`/dashboard/cases`)
1. Navigate to `/dashboard/cases` and click **"Create Case"**.
2. Enter the case title, jurisdiction, and initial background narrative.
3. Open the case workspace (`/dashboard/cases/[id]`) and upload litigation documents:
   - First Information Reports (FIRs)
   - Chargesheets & police reports
   - Witness statements (under Section 161/164 CrPC)
   - Medical/Forensic reports
4. Click **"Synthesize Dossier"** and view the **Litigation Intelligence Results** (`/dashboard/cases/[id]/results`):
   - **Chronological Timeline**: Step through each factual event, corroborated across multiple documents.
   - **Contradiction Finder**: Discover where Witness A contradicts Witness B or previous FIR statements.
   - **Charge & Compliance Audit**: Check for statutory non-compliance in arrest or seizure procedures.
5. Launch the **Adversarial Pre-Trial Debate**:
   - Click **"Initiate Trial Simulation"**.
   - Watch the Prosecution AI present the charge-sheet facts and witness corroborations.
   - Observe the Defense AI mount procedural challenges, impeach witness credibility, and cite precedents.
   - Review the Judicial Bench's ruling and download the actionable **Pre-Trial Brief**.

---

## Configuration Reference (`.env`)

| Variable | Type | Default | Description |
|---|---|---|---|
| `REDIS_URL` | String | `redis://localhost:6379/0` | Connection URL for Redis cache and broker |
| `CELERY_BROKER_URL` | String | `redis://localhost:6379/0` | Celery task queue broker URL |
| `CELERY_RESULT_BACKEND`| String | `redis://localhost:6379/1` | Celery task result backend URL |
| `UPLOAD_DIR` | Path | `backend/storage/uploads` | Path for uploaded contracts and case documents |
| `OUTPUT_DIR` | Path | `backend/storage/outputs` | Path for generated PDFs, reports, and diffs |
| `CHROMA_DIR` | Path | `backend/storage/chroma` | Persistence directory for ChromaDB vector embeddings |
| `MISTRAL_API_KEY` | String | *(Required)* | Mistral AI API authorization key |
| `MISTRAL_MODEL` | String | `mistral-large-latest` | LLM model used for multi-agent reasoning |
| `MISTRAL_EMBEDDING_MODEL`| String | `mistral-embed` | Embedding model for semantic search and retrieval |
| `DATABASE_URL` | String | `sqlite:///...` | SQLAlchemy connection string (PostgreSQL or SQLite) |
| `CONTRACT_ANALYSIS_ENABLED`| Boolean | `true` | Enables or disables contract auditing module |
| `WEB_RESEARCH_ENABLED` | Boolean | `true` | Enables live DuckDuckGo / Indian Kanoon web retrieval |
| `AUTO_RUN_MIGRATIONS` | Boolean | `true` | Safely validates and synchronizes DB schema columns on boot |

---

## Evaluation & Benchmarking Suite

ALAS includes an automated evaluation pipeline located in `evaluation/` to benchmark performance against datasets like CUAD (Contract Understanding Atticus Dataset) and live legal targets:

```bash
# Navigate to evaluation directory
cd evaluation

# Run all automated evaluation suites
python run_all_evaluations.py

# Evaluate live target legal contracts
python evaluate_live_targets.py

# Generate academic and publication-ready metric tables
python export_paper_tables.py
```

Results are saved to `evaluation/results/` and summarized in `evaluation/evaluation_results_master.json`.

---

## Troubleshooting & FAQ

### 1. Redis Connection Refused (`Error 10061` or `Connection refused`)
- **Cause**: Redis server is not running on port 6379.
- **Fix**: Run `docker run -d --name redis -p 6379:6379 redis:7-alpine` or execute `.\start_backend.ps1` which starts Redis automatically.

### 2. Celery Worker Hangs or Does Not Execute on Windows
- **Cause**: The default Celery worker pool (`prefork`) is incompatible with Windows process management.
- **Fix**: Launch Celery with the `solo` or `threads` pool flag:
  ```powershell
  celery -A backend.worker.celery_app worker --loglevel=info -P solo
  ```

### 3. Missing or Invalid Mistral API Key
- **Cause**: `MISTRAL_API_KEY` is not defined in `.env` or has expired.
- **Fix**: Verify `.env` exists in the project root and contains `MISTRAL_API_KEY=your_valid_key`.

### 4. Database Schema Mismatch
- **Cause**: Model definitions changed during development.
- **Fix**: The backend automatically runs safe schema migrations on boot (`run_migrations_safely()`). If using SQLite and desiring a completely fresh state, simply delete `backend/storage/major_project.db` and restart the backend.

### 5. Frontend Cannot Connect to Backend (`Network Error` / `ECONNREFUSED`)
- **Cause**: Backend is not running on port 8000 or `NEXT_PUBLIC_API_URL` is set incorrectly.
- **Fix**: Ensure `uvicorn` is active on port 8000. Verify `http://localhost:8000/health` returns `{"status": "healthy"}`.

---

## Design Standards & Architecture

Every UI element in ALAS strictly follows the design standards specified in:
- [`docs/UI_ARCHITECTURE.md`](docs/UI_ARCHITECTURE.md)
- [`AGENTS.md`](AGENTS.md)

### Key Architectural Guidelines
- **Institutional Styling**: Strictly adheres to high-contrast slate neutrals (`#0F172A`, `#F8FAFC`, `#E2E8F0`) and restrained legal blue accents (`#2563EB`).
- **Component Reusability**: All UI elements strictly utilize standardized primitives located in `frontend/components/ui/` combined via `cn(...)`.
- **Strict Routing Rules**: Never resurrect legacy routes (`/dashboard/templates`, `/dashboard/my-contracts`). Follow canonical routes: `/dashboard/analysis`, `/dashboard/drafting`, and `/dashboard/cases`.

---

## License & Authorship

Developed as an advanced academic and production-ready Capstone Legal Intelligence System. 

For inquiries, research citations, or technical support, please refer to the project documentation in the `docs/` folder.
