# Solar Feasibility Assistant

AI-powered RAG (Retrieval-Augmented Generation) system that helps rural and semi-urban users in India assess solar energy viability.

## Overview

Users describe their location, rooftop area, monthly electricity bill, and energy needs in plain language. The assistant retrieves relevant chunks from a curated knowledge base of government solar policies (MNRE, PM-KUSUM, BEE) and generates a cited feasibility report — covering system capacity, estimated cost, payback period, and applicable subsidy schemes.

## SDG Alignment

- **SDG 7** (Primary) — Affordable and Clean Energy
- SDG 1 — No Poverty
- SDG 9 — Industry and Innovation
- SDG 13 — Climate Action

## Tech Stack

| Layer | Tool |
|---|---|
| LLM | IBM Granite (`granite4:1b`) via Ollama |
| RAG Framework | LangChain |
| Embeddings | sentence-transformers (`all-MiniLM-L6-v2`) |
| Vector DB | ChromaDB |
| PDF Ingestion | PyMuPDF |
| Frontend | Streamlit |

## Project Structure

```
solar-assistant/
├── docs/              # Knowledge base PDFs (MNRE, PM-KUSUM, BEE guidelines)
├── vectorstore/       # ChromaDB persisted embeddings (auto-generated)
├── ingest.py          # Loads, chunks, and embeds PDFs into ChromaDB
├── rag.py             # RAG chain: retriever + prompt + Granite LLM
├── app.py             # Streamlit user interface
├── .env               # HuggingFace API token (not committed)
└── README.md
```

## Setup

### 1. Clone and install dependencies

```bash
pip install streamlit langchain langchain-community langchain-huggingface langchain-chroma langchain-text-splitters langchain-ollama sentence-transformers chromadb pymupdf python-dotenv huggingface_hub
```

### 2. Install Ollama and pull Granite

Download Ollama from [ollama.com](https://ollama.com), then:

```bash
ollama pull granite4:1b
```

### 3. Add your knowledge base

Place solar policy PDFs (MNRE guidelines, PM-KUSUM scheme document, BEE standards, etc.) into the `docs/` folder.

### 4. Set up environment variables

Create a `.env` file in the project root:

```
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
```

### 5. Build the knowledge base

```bash
python ingest.py
```

This loads all PDFs from `docs/`, splits them into chunks, embeds them, and stores them in `vectorstore/`.

### 6. Run the assistant

```bash
streamlit run app.py
```

Opens automatically at `http://localhost:8501`.

## How It Works

1. User enters location, rooftop area, monthly bill, and appliance needs via the Streamlit form
2. Query is embedded and matched against the ChromaDB knowledge base using cosine similarity
3. Top-5 relevant document chunks are retrieved and assembled into context
4. IBM Granite (running locally via Ollama) generates a grounded feasibility report, citing source documents
5. Report is displayed with capacity estimate, cost range, payback period, and applicable government schemes

## Responsible AI Considerations

- **Fairness** — Knowledge base includes both rural and urban policies with no income-level assumptions
- **Transparency** — Every recommendation cites its source document and chunk
- **Privacy** — No personal data is stored; sessions are stateless
- **Safety** — System prompt instructs the model to flag uncertainty and avoid fabricated figures; every response ends with a disclaimer to consult a certified installer

## Limitations

- Knowledge base is only as accurate and current as the PDFs provided — update `docs/` periodically with the latest scheme guidelines
- `granite4:1b` is a small model optimized for low-resource laptops; responses are good for guidance but not a substitute for professional assessment
- Currently English-only; regional language support is a planned extension

## Author

  Viswanadhula Naga Venkatesh

- Email: viswanadhulavenkatesh94@gmail.com
- GitHub: [25A35A0513](https://github.com/25A35A0513)
- LinkedIn: [viswanadhula-naga-venkatesh](https://linkedin.com/in/viswanadhula-naga-venkatesh)
