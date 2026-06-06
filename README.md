# 🤖 ResearchOS – Multi-Agent AI Research Assistant

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776ab?logo=python&logoColor=white)](https://www.python.org/)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.1%2B-00D084?logo=langchain&logoColor=white)](https://github.com/langchain-ai/langgraph)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-FF6B6B?logo=ai&logoColor=white)](https://ollama.ai)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20DB-FFA500?logo=database&logoColor=white)](https://www.trychroma.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen)](https://github.com/puneethkrishna001-crypto/researchos)

**An autonomous AI research assistant that leverages multi-agent collaboration to conduct comprehensive research, validate information, and generate professional reports—100% offline with local LLMs.**

[✨ Features](#-key-features) • [🏗️ Architecture](#-system-architecture) • [📦 Installation](#-installation-guide) • [🚀 Quick Start](#-running-the-application) • [📝 Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Agent Workflow](#-agent-workflow)
- [Folder Structure](#-folder-structure)
- [Installation Guide](#-installation-guide)
- [Local Setup](#-local-setup)
- [Running the Application](#-running-the-application)
- [Screenshots](#-screenshots)
- [Technical Achievements](#-technical-achievements)
- [Why These Technologies](#-why-these-technologies)
- [Resume-Worthy Highlights](#-resume-worthy-highlights)
- [Deployment Guide](#-deployment-guide)
- [Future Roadmap](#-future-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

## 🎯 Project Overview

ResearchOS is a sophisticated **multi-agent AI research system** designed to autonomously research any topic provided by users. Unlike traditional search engines, ResearchOS combines multiple specialized AI agents working collaboratively to:

- 🔍 **Conduct Deep Research**: Systematically explore topics across multiple sources
- 🧠 **Synthesize Information**: Summarize and connect disparate research findings
- ✅ **Validate Quality**: Critically evaluate information credibility and accuracy
- 📄 **Generate Reports**: Produce professionally formatted PDF research documents
- 💾 **Maintain Memory**: Store research history in vector databases for context awareness

**Key Differentiator**: Built entirely on open-source, locally-run LLMs—no API dependencies, no privacy concerns, fully offline capable.

---

## ✨ Key Features

### 🤖 Multi-Agent Orchestration
| Agent | Responsibility | Purpose |
|-------|-----------------|---------|
| **Researcher** | Web search & scraping | Gathers raw information from diverse sources |
| **Summarizer** | Content synthesis | Condenses information into key insights |
| **Critic** | Quality validation | Evaluates credibility and identifies biases |
| **Writer** | Report generation | Composes professional, structured documents |

### 🎨 Core Capabilities

- ✅ **Autonomous Research Workflows** - Agents coordinate without user intervention
- ✅ **Real-time Web Search** - DuckDuckGo integration for current information
- ✅ **Advanced Web Scraping** - BeautifulSoup for content extraction
- ✅ **AI-Powered Summarization** - Intelligent content condensation
- ✅ **Long-term Memory** - ChromaDB vector storage for semantic search
- ✅ **PDF Report Export** - Professional documents with styling via ReportLab
- ✅ **Dark Futuristic UI** - Sleek Streamlit interface
- ✅ **Research History** - Track and revisit previous investigations
- ✅ **Architecture Dashboard** - Monitor agent coordination in real-time
- ✅ **100% Local Processing** - Ollama + Qwen 2.5 3B—no cloud dependencies
- ✅ **Context Window Optimization** - Efficient memory management for extended research

---

## 🏗️ System Architecture

### High-Level Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         STREAMLIT UI LAYER                       │
│     (Dark Theme • Dashboard • History • Report Viewer)           │
└──────────────────────────┬──────────────────────────────────────┘
                           │
        ┌──────────────────┴──────────────────┐
        │                                     │
┌───────▼──────────────────┐    ┌────────────▼────────────┐
│    LANGGRAPH ORCHESTRATOR │    │  STATE MANAGEMENT       │
│  (Agent Coordination)     │    │  (Research Context)     │
└───────┬──────────────────┘    └────────────┬────────────┘
        │                                    │
    ┌───┴───────────────────────────────────┴───────┐
    │                                               │
┌───▼──────────────┐  ┌──────────────┐  ┌────────┴──────┐  ┌─────────────┐
│ RESEARCHER AGENT │  │SUMMARIZER    │  │ CRITIC AGENT  │  │ WRITER      │
│                  │  │ AGENT        │  │               │  │ AGENT       │
├──────────────────┤  ├──────────────┤  ├───────────────┤  ├─────────────┤
│ • DuckDuckGo     │  │ • LLM        │  │ • Validation  │  │ • PDF Gen   │
│ • BeautifulSoup  │  │   Summarize  │  │ • Credibility │  │ • Formatting│
│ • Content Filter │  │ • Ranking    │  │ • Fact-Check  │  │ • Structure │
└───┬──────────────┘  └──────┬───────┘  └───────┬───────┘  └────┬────────┘
    │                        │                  │               │
    └────────────┬───────────┴──────────────────┴───────────────┘
                 │
    ┌────────────▼─────────────────┐
    │   MEMORY & PERSISTENCE LAYER  │
    ├───────────────────────────────┤
    │ ChromaDB Vector Database      │
    │ • Semantic Search             │
    │ • Research History            │
    │ • Context Retrieval           │
    └───────────────────────────────┘
                 │
    ┌────────────▼─────────────────┐
    │    LOCAL LLM ENGINE           │
    ├───────────────────────────────┤
    │ Ollama + Qwen 2.5 3B          │
    │ • 100% Local Processing       │
    │ • No Cloud Dependencies        │
    │ • Privacy Preserving          │
    └───────────────────────────────┘
```

### Data Flow Architecture

```
User Input (Topic)
       │
       ▼
┌─────────────────┐
│ Initialize      │
│ Research State  │
└────────┬────────┘
         │
    ┌────▼────────────────────────────┐
    │ RESEARCH PHASE                   │
    │ Researcher Agent: Search & Scrape│
    └────┬─────────────────────────────┘
         │
    ┌────▼────────────────────────────┐
    │ SYNTHESIS PHASE                  │
    │ Summarizer: Condense & Extract   │
    └────┬─────────────────────────────┘
         │
    ┌────▼────────────────────────────┐
    │ VALIDATION PHASE                 │
    │ Critic: Evaluate Quality         │
    └────┬─────────────────────────────┘
         │
    ┌────▼────────────────────────────┐
    │ GENERATION PHASE                 │
    │ Writer: Create Report            │
    └────┬─────────────────────────────┘
         │
    ┌────▼────────────────────────────┐
    │ PERSISTENCE PHASE                │
    │ Store to ChromaDB & Generate PDF │
    └────┬─────────────────────────────┘
         │
         ▼
    Research Report Ready
```

---

## 🔄 Agent Workflow

### Detailed Agent Interaction Flow

**1. RESEARCHER AGENT** 🔍
- Receives research topic and context
- Executes parallel web searches via DuckDuckGo
- Scrapes content using BeautifulSoup
- Filters for relevance and quality
- Returns structured research data

**2. SUMMARIZER AGENT** 📝
- Receives raw research data
- Uses Qwen 2.5 3B to synthesize information
- Creates concise summaries maintaining key insights
- Ranks findings by relevance
- Extracts key metrics and statistics

**3. CRITIC AGENT** ✅
- Evaluates information credibility
- Identifies potential biases and errors
- Cross-references findings
- Generates quality scores
- Flags uncertain claims for additional research

**4. WRITER AGENT** 📄
- Receives validated research findings
- Structures information into report sections
- Generates professional narrative
- Creates formatted PDF with charts/tables
- Embeds metadata and citations

### LangGraph State Management

```python
ResearchState = {
    "topic": str,                    # User input
    "search_results": List[Dict],    # Raw web data
    "summaries": List[str],          # Processed information
    "validation_report": Dict,       # Quality metrics
    "final_report": str,             # PDF content
    "research_history_id": str,      # ChromaDB reference
    "iteration_count": int,          # Loop tracking
}
```

---

## 📁 Folder Structure

```
research_agent/
│
├── agents/
│   ├── __init__.py
│   ├── researcher.py              # Web search & scraping agent
│   ├── summarizer.py              # Content synthesis agent
│   ├── critic.py                  # Validation & quality check
│   ├── writer.py                  # Report generation agent
│   └── base_agent.py              # Agent interface
│
├── graph/
│   ├── __init__.py
│   ├── workflow.py                # LangGraph workflow definition
│   ├── state.py                   # State schemas & validation
│   └── nodes.py                   # Workflow nodes/steps
│
├── memory/
│   ├── __init__.py
│   ├── chromadb_manager.py        # Vector database operations
│   ├── cache.py                   # Caching layer
│   └── retrieval.py               # Semantic search utilities
│
├── models/
│   ├── __init__.py
│   ├── llm_manager.py             # Ollama LLM interface
│   ├── embeddings.py              # Embedding models
│   └── response_schemas.py        # Pydantic schemas
│
├── tools/
│   ├── __init__.py
│   ├── search.py                  # DuckDuckGo search wrapper
│   ├── scraper.py                 # BeautifulSoup web scraper
│   ├── parser.py                  # Content parsing utilities
│   └── validators.py              # Data validation functions
│
├── frontend/
│   ├── app.py                     # Main Streamlit application
│   ├── pages/
│   │   ├── dashboard.py
│   │   ├── research.py
│   │   ├── history.py
│   │   └── settings.py
│   ├── components/
│   │   ├── sidebar.py
│   │   ├── report_viewer.py
│   │   └── metrics.py
│   └── styles/
│       └── dark_theme.css
│
├── output/
│   ├── reports/                   # Generated PDF reports
│   ├── research_logs/             # Execution logs
│   └── exports/                   # Export formats
│
├── tests/
│   ├── test_agents.py
│   ├── test_workflow.py
│   ├── test_memory.py
│   └── test_integration.py
│
├── utils/
│   ├── __init__.py
│   ├── config.py                  # Configuration management
│   ├── logger.py                  # Logging setup
│   ├── constants.py               # Global constants
│   └── helpers.py                 # Utility functions
│
├── requirements.txt               # Python dependencies
├── .env.example                   # Environment template
├── config.yaml                    # Application configuration
├── main.py                        # Entry point
├── setup.py                       # Installation script
└── README.md                      # This file
```

---

## 🚀 Installation Guide

### Prerequisites

- **Python 3.8+** (3.10+ recommended)
- **Ollama** installed and running ([Download](https://ollama.ai))
- **Git** for version control
- **4GB+ RAM** minimum (8GB+ recommended)
- **macOS, Linux, or Windows** (WSL2 recommended for Windows)

### Step 1: Clone the Repository

```bash
git clone https://github.com/puneethkrishna001-crypto/researchos.git
cd researchos
```

### Step 2: Create Virtual Environment

```bash
# Using venv (recommended)
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# On Windows (CMD):
venv\Scripts\activate.bat
```

### Step 3: Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt
```

### Step 4: Install and Run Ollama

```bash
# Download Ollama from https://ollama.ai

# Pull Qwen 2.5 3B model (lightweight & efficient)
ollama pull qwen2.5:3b

# Run Ollama server (default: localhost:11434)
ollama serve
```

### Step 5: Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your settings
# OLLAMA_BASE_URL=http://localhost:11434
# OLLAMA_MODEL=qwen2.5:3b
# CHROMADB_PATH=./data/chromadb
# LOG_LEVEL=INFO
```

---

## 🔧 Local Setup

### 1. Verify Ollama Installation

```bash
# Check Ollama server status
curl http://localhost:11434/api/tags

# Expected response includes qwen2.5:3b model
```

### 2. Initialize ChromaDB

```bash
# The application auto-initializes ChromaDB on first run
# Or manually initialize:
python -c "from research_agent.memory.chromadb_manager import ChromaDBManager; ChromaDBManager().initialize()"
```

### 3. Configure LLM Parameters

Edit `config.yaml`:

```yaml
llm:
  base_url: "http://localhost:11434"
  model: "qwen2.5:3b"
  temperature: 0.7
  top_p: 0.9
  context_window: 4096
  max_tokens: 2048

memory:
  db_path: "./data/chromadb"
  embedding_model: "nomic-embed-text"
  chunk_size: 1000
  overlap: 200

tools:
  max_search_results: 10
  scraping_timeout: 30
  retry_attempts: 3

application:
  debug: false
  theme: "dark"
  port: 8501
```

### 4. Test Core Components

```bash
# Test LLM connection
python -c "from research_agent.models.llm_manager import LLMManager; print(LLMManager().test_connection())"

# Test memory system
python -c "from research_agent.memory.chromadb_manager import ChromaDBManager; print(ChromaDBManager().health_check())"

# Test search tools
python -c "from research_agent.tools.search import search_web; print(search_web('artificial intelligence')[:1])"
```

---

## ▶️ Running the Application

### Option 1: Run Full Streamlit Application (Recommended)

```bash
# Ensure Ollama is running in another terminal
streamlit run research_agent/frontend/app.py

# Application launches at: http://localhost:8501
```

### Option 2: Run CLI Interface

```bash
python main.py --topic "Your Research Topic" --output-format pdf
```

### Option 3: Run as Python Module

```python
from research_agent.graph.workflow import create_research_workflow

# Initialize workflow
workflow = create_research_workflow()

# Execute research
result = workflow.invoke({
    "topic": "Quantum Computing Applications",
})

print(result["final_report"])
```

### Option 4: Run Tests

```bash
# Run all tests
pytest tests/ -v

# Run specific test
pytest tests/test_agents.py -v

# With coverage
pytest tests/ --cov=research_agent --cov-report=html
```

---

## 📸 Screenshots

### Main Research Dashboard
```
┌─────────────────────────────────────────────────────┐
│  🤖 ResearchOS Dashboard                            │
├─────────────────────────────────────────────────────┤
│                                                     │
│  📊 Active Research Processes: 1                    │
│  💾 Stored Research Items: 42                       │
│  ⚡ Average Query Time: 2.3s                        │
│                                                     │
├─────────────────────────────────────────────────────┤
│  Recent Research Topics                             │
│  • Machine Learning in Healthcare     [Details]    │
│  • Blockchain Technology              [Details]    │
│  • Neural Network Optimization        [Details]    │
└─────────────────────────────────────────────────────┘
```

### Research Input Interface
```
┌─────────────────────────────────────────────────────┐
│  Enter Research Topic                               │
│  ┌───────────────────────────────────────────────┐  │
│  │ Autonomous Vehicles in Urban Planning        │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  Options:                                           │
│  ☐ Include Historical Context                      │
│  ☑ Validate Information Sources                    │
│  ☐ Generate Comparative Analysis                   │
│                                                     │
│  [🔍 Start Research]  [📊 Advanced Settings]       │
└─────────────────────────────────────────────────────┘
```

### Research Progress Monitor
```
┌─────────────────────────────────────────────────────┐
│  Research Progress                                  │
├─────────────────────────────────────────────────────┤
│  🔍 Research Agent        [████████░░░░] 65%       │
│  📝 Summarizer Agent      [██████░░░░░░] 45%       │
│  ✅ Critic Agent           [░░░░░░░░░░░░] 0%        │
│  📄 Writer Agent           [░░░░░░░░░░░░] 0%        │
│                                                     │
│  Current Task: Scraping and analyzing 12 sources   │
│  Estimated Time Remaining: 2 min 34 sec            │
└─────────────────────────────────────────────────────┘
```

### Generated Report Viewer
```
┌─────────────────────────────────────────────────────┐
│  📄 Research Report Viewer                          │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Title: Autonomous Vehicles in Urban Planning      │
│  Date: 2024-06-06                                  │
│  Status: ✅ Completed                              │
│                                                     │
│  Executive Summary                                  │
│  ─────────────────────────────────────────────────  │
│  This research explores the integration of...      │
│                                                     │
│  [⬇️ Download PDF] [📋 View Full Report]           │
│  [🔄 Regenerate] [💾 Save to History]              │
└─────────────────────────────────────────────────────┘
```

---

## 🏆 Technical Achievements

### 1. **Autonomous Multi-Agent Coordination**
- **Challenge**: Orchestrating 4 independent agents with proper state management
- **Solution**: Implemented LangGraph state machine with conditional routing and feedback loops
- **Impact**: Seamless agent collaboration without manual intervention

### 2. **100% Local LLM Processing**
- **Challenge**: Running sophisticated NLP tasks without cloud APIs
- **Solution**: Optimized Ollama integration with context window management
- **Impact**: Privacy-preserving, cost-free, fully offline operation

### 3. **Semantic Memory & Retrieval**
- **Challenge**: Efficient storage and retrieval of research context across sessions
- **Solution**: ChromaDB with embeddings for semantic similarity search
- **Impact**: Context-aware responses and research continuity

### 4. **Real-time Web Data Integration**
- **Challenge**: Handling varied web content formats and scraping failures
- **Solution**: Robust BeautifulSoup parsing with fallback strategies
- **Impact**: Reliable information gathering from diverse sources

### 5. **Information Quality Validation**
- **Challenge**: Identifying misinformation and bias in research
- **Solution**: Multi-criteria validation framework in Critic agent
- **Impact**: High-quality, credible research outputs

### 6. **Professional Report Generation**
- **Challenge**: Creating formatted, branded PDFs programmatically
- **Solution**: ReportLab with custom templates and styling
- **Impact**: Production-ready deliverables

---

## 💡 Why These Technologies

### 🟢 Python
**Why**: Ecosystem richness for AI/ML, rapid development, extensive libraries
- LangChain/LangGraph integration
- Data science maturity
- Production stability (FastAPI, Gunicorn)

### 🟡 LangGraph
**Why**: Purpose-built for multi-agent workflows
```python
# Enables clean state management
graph.add_node("researcher", researcher_node)
graph.add_node("summarizer", summarizer_node)
graph.add_edge("researcher", "summarizer")  # Clear dependency
```
- Superior to simple chains for complex orchestration
- Built-in cycle support and conditional routing
- State persistence and recovery

### 🔵 LangChain
**Why**: Production-grade abstraction for LLM applications
- Standardized tool interfaces
- Prompt templating and management
- Chain composition and error handling

### 🟣 Ollama
**Why**: Simplest local LLM deployment
- Single binary, multiple model support
- Compatible with LangChain
- No GPU requirements for CPU inference
- Community-maintained model zoo

### 🟠 Qwen 2.5 3B
**Why**: Optimal size-to-performance ratio
| Model | Params | Speed | Quality | RAM |
|-------|--------|-------|---------|-----|
| Qwen 2.5 3B | 3B | ⚡⚡⚡ | ⭐⭐⭐⭐ | 4GB |
| Llama 2 7B | 7B | ⚡⚡ | ⭐⭐⭐⭐⭐ | 8GB |
| Mistral 7B | 7B | ⚡⚡ | ⭐⭐⭐⭐ | 8GB |

### 🔴 ChromaDB
**Why**: Vector database designed for embeddings
- Simple Python API (no infrastructure)
- Built-in embedding support
- Fast semantic search
- Persistent collections
- Alternative to: Pinecone, Weaviate, Milvus (but local-first)

### 🟢 DuckDuckGo
**Why**: Privacy-respecting web search without API keys
- No authentication required
- Respects privacy
- Lightweight library wrapper
- Adequate results for research

### 🟡 BeautifulSoup
**Why**: Robust HTML/XML parsing
- Mature and stable
- Forgiving parser for malformed HTML
- Minimal dependencies
- Easy CSS selector syntax

### 🔵 Streamlit
**Why**: Fastest path to web UI for data apps
- Code-to-UI in minutes
- Hot reloading
- Built-in theming
- Perfect for demos and dashboards
- Alternative: FastAPI + React (overkill for this use case)

### 🟣 ReportLab
**Why**: Programmatic PDF generation with full control
- Python-native (no external binaries)
- Complex layouts and styling
- Charts and tables
- Reliable PDF spec compliance

---

## ⭐ Resume-Worthy Highlights

### 🎓 Architectural Excellence
- ✅ **Multi-Agent System Design**: Orchestrated 4 specialized agents using LangGraph for complex workflows
- ✅ **State Machine Implementation**: Robust state management with conditional routing and error recovery
- ✅ **Memory-Augmented AI**: Semantic memory using vector embeddings for context persistence

### 🔧 Technical Implementation
- ✅ **Full-Stack AI Application**: End-to-end system from web scraping to PDF generation
- ✅ **Local LLM Integration**: Deployed Ollama with Qwen 2.5 3B for 100% offline inference
- ✅ **Production-Grade Code**: Error handling, logging, testing, configuration management
- ✅ **Performance Optimization**: Context window management, embedding caching, parallel processing

### 🎨 User Experience
- ✅ **Interactive Dashboard**: Streamlit UI with dark theme and real-time monitoring
- ✅ **Research History Tracking**: Long-term memory with semantic search capabilities
- ✅ **Professional Outputs**: PDF reports with formatting, citations, and metadata

### 🧪 Quality & Testing
- ✅ **Comprehensive Test Suite**: Unit, integration, and end-to-end tests
- ✅ **CI/CD Ready**: GitHub Actions compatible structure
- ✅ **Logging & Monitoring**: Detailed execution traces for debugging

### 📊 Scalability Considerations
- ✅ **Modular Architecture**: Each agent independently testable and replaceable
- ✅ **Configuration-Driven**: Environment-based settings for different deployments
- ✅ **Extensible Workflow**: Easy to add new agents or tools

### 🌍 Open Source Best Practices
- ✅ **Professional Documentation**: Comprehensive README with badges and examples
- ✅ **Code Quality**: Type hints, docstrings, naming conventions
- ✅ **Community Ready**: Contributing guidelines, issue templates, pull request process

---

## 🌐 Deployment Guide

### Option 1: Docker Deployment

**Dockerfile**:
```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY research_agent/ ./research_agent/
COPY config.yaml .
COPY main.py .

# Expose port
EXPOSE 8501

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1

# Run application
CMD ["streamlit", "run", "research_agent/frontend/app.py", "--server.port=8501", "--server.headless=true"]
```

**Docker Compose** (with Ollama):
```yaml
version: '3.8'

services:
  ollama:
    image: ollama/ollama:latest
    container_name: researchos-ollama
    volumes:
      - ollama_data:/root/.ollama
    ports:
      - "11434:11434"
    command: serve

  researchos:
    build: .
    container_name: researchos-app
    depends_on:
      - ollama
    environment:
      - OLLAMA_BASE_URL=http://ollama:11434
      - OLLAMA_MODEL=qwen2.5:3b
    ports:
      - "8501:8501"
    volumes:
      - ./data:/app/data
      - ./output:/app/output
    restart: unless-stopped
```

**Deploy**:
```bash
docker-compose up -d
# Access at http://localhost:8501
```

### Option 2: Cloud Deployment (AWS EC2)

```bash
# 1. Launch EC2 Instance
# - OS: Ubuntu 22.04 LTS
# - Instance Type: t3.large (2 vCPU, 8GB RAM minimum)
# - Storage: 30GB

# 2. SSH into instance
ssh -i key.pem ubuntu@<instance-ip>

# 3. Install dependencies
sudo apt update
sudo apt install -y python3.10 python3-pip git curl

# 4. Clone and setup
git clone https://github.com/puneethkrishna001-crypto/researchos.git
cd researchos
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 5. Install Ollama
curl https://ollama.ai/install.sh | sh
ollama pull qwen2.5:3b

# 6. Run with systemd
sudo tee /etc/systemd/system/researchos.service > /dev/null <<EOF
[Unit]
Description=ResearchOS Multi-Agent AI
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/researchos
Environment="PATH=/home/ubuntu/researchos/venv/bin"
ExecStart=/home/ubuntu/researchos/venv/bin/streamlit run research_agent/frontend/app.py --server.port=80

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable researchos
sudo systemctl start researchos

# Access at http://<instance-ip>
```

### Option 3: Kubernetes Deployment

**Deploy on Kubernetes cluster**:
```bash
# Build and push image
docker build -t your-registry/researchos:latest .
docker push your-registry/researchos:latest

# Apply Kubernetes manifests
kubectl apply -f k8s/

# Check deployment
kubectl get pods -l app=researchos
kubectl logs -f deployment/researchos
```

---

## 🚀 Future Roadmap

### Phase 1: Core Enhancements (Q3 2024)
- [ ] **Multi-source Integration**: Add arXiv, PubMed, Google Scholar APIs
- [ ] **Advanced Fact-Checking**: Integrate Snopes API for verification
- [ ] **Multimodal Support**: Process images and videos in research
- [ ] **Collaborative Mode**: Multi-user research sessions with shared memory

### Phase 2: Advanced Features (Q4 2024)
- [ ] **Custom Agent Creation**: User-defined agent workflows
- [ ] **Fine-tuned Models**: Task-specific model optimization
- [ ] **Real-time Collaboration**: WebSocket-based live research
- [ ] **Advanced Analytics**: Research quality metrics and insights

### Phase 3: Production Features (Q1 2025)
- [ ] **Enterprise Authentication**: LDAP, OAuth2 integration
- [ ] **Audit Logging**: Compliance and tracking
- [ ] **API Gateway**: RESTful API for external integration
- [ ] **Performance Monitoring**: Prometheus + Grafana integration

### Phase 4: Intelligence Augmentation (Q2 2025)
- [ ] **Reinforcement Learning**: Agent optimization from feedback
- [ ] **Zero-shot Agents**: Agents adaptive to new domains
- [ ] **Graph-based Memory**: Knowledge graph for relationship mapping
- [ ] **Automated Fact Synthesis**: Cross-source consistency validation

---

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

### 1. Fork & Clone
```bash
git clone https://github.com/YOUR_USERNAME/researchos.git
cd researchos
```

### 2. Create Feature Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 3. Make Changes with Tests
```bash
# Write tests for new functionality
# Ensure all tests pass
pytest tests/ -v

# Check code quality
flake8 research_agent/
black --check research_agent/
```

### 4. Commit with Clear Messages
```bash
git commit -m "feat: add new capability"
# or
git commit -m "fix: resolve issue with agent X"
```

### 5. Push & Create Pull Request
```bash
git push origin feature/your-feature-name
# Create PR with detailed description of changes
```

### Contribution Areas
- 🐛 **Bug Fixes**: Report and fix issues
- ✨ **Features**: New agents, tools, or capabilities
- 📚 **Documentation**: Improve README and code comments
- 🧪 **Tests**: Increase code coverage
- 🎨 **UI/UX**: Enhance Streamlit interface
- ⚡ **Performance**: Optimize speed and memory

### Code Style
- Python 3.8+ compatible
- PEP 8 compliant (use `black` for formatting)
- Type hints for all functions
- Docstrings for modules, classes, functions
- 80 character line limit

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

**Summary**: Free to use, modify, and distribute with attribution.

```
MIT License

Copyright (c) 2024 Puneeth Krishna

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 👨‍💻 Author

**Puneeth Krishna**

- 🔗 **GitHub**: [@puneethkrishna001-crypto](https://github.com/puneethkrishna001-crypto)
- 📧 **Email**: [contact@puneethkrishna.dev](mailto:contact@puneethkrishna.dev)
- 💼 **LinkedIn**: [Your LinkedIn Profile](https://linkedin.com/in/puneethkrishna)

### About Me
I'm an AI Engineer passionate about building sophisticated AI systems that solve real-world problems. ResearchOS represents my exploration of multi-agent architectures, local LLMs, and knowledge management systems.

---

## 🙏 Acknowledgments

- **LangChain & LangGraph teams** for excellent orchestration frameworks
- **Ollama community** for making local LLMs accessible
- **ChromaDB** for vector storage and semantic search
- **Streamlit** for rapid UI development
- All contributors and users who've provided feedback

---

## 📞 Support

Need help? Here are your options:

1. **📖 Documentation**: Check [examples/](examples/) directory
2. **🐛 Issues**: [GitHub Issues](https://github.com/puneethkrishna001-crypto/researchos/issues)
3. **💬 Discussions**: [GitHub Discussions](https://github.com/puneethkrishna001-crypto/researchos/discussions)
4. **📧 Email**: contact@puneethkrishna.dev

---

<div align="center">

### If you found this helpful, please consider giving it a ⭐!

**ResearchOS** — *Democratizing AI-Powered Research*

Built with ❤️ by AI enthusiasts for the community

</div>