# 🚀 Telegram AI Agent

**Telegram AI Agent** is a modular AI agent built with **Python**, using **LLM (Groq / OpenAI-compatible models)** for response generation and supporting short-term and long-term user memory.  
This project demonstrates an agent architecture that works with Telegram, NLP, databases, and external tools.

---

## 🛠 Libraries Used

- **groq** — connects to LLM for generating responses.  
- **psycopg2** — PostgreSQL integration for storing chat history and user memory.  
- **spacy** — NLP for intent recognition and text processing.  
- **dotenv** — loading environment variables from `.env`.  
- **aiogram** — Telegram integration, command and message handling.  

---

## 🧠 Key Features

- **Personalized User Memory**  
  - Short-term chat history storage.  
  - Long-term facts storage (name, preferences, work, study, family, location).  

- **Intent Recognition**  
  - NLP (spacy) for understanding user intents.  
  - Automatic tool selection based on user request (weather, currency, news).  

- **External Tool Integration**  
  - **Weather Tool** — real-time weather API integration.  
  - **Currency Tool** — currency conversion (in progress).  
  - **News Tool** — news retrieval (in progress).  

- **RAG (Retrieval-Augmented Generation)**  
  - Embedding vectors for relevant context search.  
  - Improves response accuracy and personalization.  

---

## 🏗 Architecture

```

Telegram
↓
Bot Handler (aiogram)
↓
Agent Controller
├── Memory Manager       # Short-term and long-term memory
├── RAG / Embeddings     # Contextual search
├── Intent Router        # User intent recognition
├── Tool Dispatcher      # External tool calls
↓
LLM (Groq / OpenAI-compatible)
↓
Formatted Response
↓
Telegram

```id="rbldyb-en"

### Architectural Principles

- Layered architecture  
- Prompt-driven orchestration  
- Explicit tool execution  
- Extensible design  
- Database abstraction  

---

## 📂 Project Structure

```

.
├── README.md          # Documentation and project description
├── agent/             # Core agent logic (memory, orchestration, NLP)
│   ├── core/          # Agent logic and memory
│   │   ├── agent.py       # Main agent controller (LLM orchestration)
│   │   ├── memory.py      # Long-term structured memory
│   │   └── message.py     # Short-term chat history management
│   ├── nlp/           # NLP parsing and routing
│       ├── intents.py     # Intent definitions
│       ├── parser.py      # User text parsing logic
│       ├── router.py      # Routing intents to tools
│       └── tools.py       # Intent-to-tool mapping
├── bot/               # Telegram integration
│   ├── commands.py        # Command handlers (/start, /delete)
│   └── telegram.py        # Bot initialization and dispatcher
├── config/            # Configuration and logging
│   ├── logging.py
│   └── settings.py
├── db/                # Database layer
│   ├── init_db.py
│   ├── models.py
│   └── session.py
├── prompts/           # LLM prompt templates
│   ├── system_prompts/
│   └── tool_prompts/
├── services/          # API integrations & utilities
│   ├── api/           # weather.py, currency.py, news.py
│   └── utils/         # geo_utils.py
├── main.py            # Application entry point
└── f.txt              # Temporary / test file

```id="bdjob9-en"

---

## ⚙️ Tech Stack

- Python 3.10+  
- **LLM:** Groq / OpenAI-compatible models  
- **Telegram Bot:** aiogram  
- **Database:** PostgreSQL / SQLite (via psycopg2 + SQLAlchemy)  
- NLP: spacy  
- Env management: dotenv  
- Async support: asyncio  

---

## 🔐 Environment Variables

Create a `.env` file:

```

TELEGRAM_TOKEN=
LLM_API_KEY=
DATABASE_URL=
WEATHER_API_KEY=
NEWS_API_KEY=
CURRENCY_API_KEY=

````id="srb7ed-en"

---

## ▶️ Running the Project

```bash
git clone <repository>
cd project
pip install -r requirements.txt
python main.py

---

## 🎯 Project Goals

* Demonstrate AI agent architecture
* Conversational memory handling
* RAG workflow integration
* Tool execution logic
* Telegram-based interaction
* Modular backend design

---

## 📌 Future Improvements

* Docker containerization
* CI/CD pipeline
* Improved intent classification
* Advanced memory ranking
* Multi-tool parallel execution
* Rate limiting & security hardening

```
