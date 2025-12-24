# LLM Chatbot with RAG & RLHF

A full-stack AI chatbot application that combines **Retrieval-Augmented Generation (RAG)** for real-time knowledge access and a complete **Reinforcement Learning from Human Feedback (RLHF)** pipeline for continuous model improvement.

## 🚀 Features

### 1. Interactive Chat & RAG

- **Chat Interface**: React-based UI for interacting with the LLM.
- **Knowledge Ingestion**: Users can upload/ingest text snippets directly from the UI into a Vector Database (ChromaDB).
- **Context Retrieval**: The backend retrieves relevant context for every query to ground the LLM's responses.

### 2. Data Collection & Feedback

- **Conversation History**: All user queries and model responses are stored in PostgreSQL.
- **User Feedback**: Users can rate responses (👍 / 👎), creating a labeled dataset for training.

### 3. Training Pipeline (RLHF)

The application includes three standalone scripts to fine-tune the model based on collected data:

- **Supervised Fine-Tuning (SFT)**: Fine-tunes the base model on conversations with positive ratings.
- **Reward Modeling**: Trains a classifier (The "Judge") to predict human preferences based on feedback history.
- **PPO (Proximal Policy Optimization)**: Uses Reinforcement Learning to align the model's policy using the trained Reward Model.

---

## 📂 Project Structure

```text
llm-chatbot/
├── backend/
│   ├── app/
│   │   ├── config.py           # Configuration (LLM paths, DB URLs)
│   │   ├── db.py               # Database session management
│   │   ├── judge.py            # Reward Model (Judge) logic
│   │   ├── llm.py              # LLM generation logic
│   │   ├── main.py             # FastAPI app entrypoint
│   │   ├── models.py           # SQLAlchemy models (Conversation, Feedback)
│   │   ├── rag.py              # ChromaDB vector store & retrieval logic
│   │   ├── routes_chat.py      # FastAPI routes for chat & ingestion
│   │   ├── routes_feedback.py  # FastAPI routes for feedback collection
│   │   ├── schemas.py          # Pydantic models
│   │   ├── train_reward.py     # Script: Train Reward Model
│   │   ├── train_rl.py         # Script: Train PPO (RL)
│   │   └── train_sft.py        # Script: Train SFT
│   |
│   ├── db/                     # ChromaDB persistent storage
│   │   └── chroma/             # ChromaDB database files
|   |       └── chroma.sqlite3  # ChromaDB database file
|   |
|   └── requirements.txt        # Python dependencies
│
├── frontend/
│   ├── node_modules/           # Node.js dependencies
│   ├── src/
│   │   ├── components/             # React components
│   │   │   ├── Feedback/           # Feedback component
│   │   │   │   ├── Feedback.tsx    # Feedback component
│   │   │   │   └── Feedback.module.css       # Feedback component styles
│   │   │   └── MessageInput/                 # Message input component
│   │   │   │    └── MessageInput.tsx         # Message input component
│   │   │   │    └── MessageInput.module.css  # Message input component styles
│   │   │   └── ReadmeRenderer.tsx            # Renders this README.md file
│   │   │   
│   │   ├── api.ts              # Axios API client
│   │   ├── App.tsx             # Main App Component
│   │   ├── Chat.tsx            # Main Chat Component
│   │   ├── global.d.ts         # TypeScript global declarations
│   │   └── main.tsx            # Main entrypoint
│   │   
│   ├── static/
│   │   └── index.css           # Global stylesheet
│   |
│   ├── .env                    # Environment variables (Vite)
│   ├── .env.example            # Example environment variables file
│   ├── index.html              # HTML entrypoint
│   ├── node_modules/           # Node.js dependencies
│   ├── package.json            # Node.js package config
│   ├── tsconfig.json           # TypeScript config
│   ├── package-lock.json       # Node.js package lock file
│   ├── tsconfig.node.json      # TypeScript config for Node.js
│   └── vite.config.ts          # Vite.js config
|
├── .env                        # Environment variables (LLM paths, DB URLs)
├── .env.example                # Example environment variables file
├── .gitignore                  # Git ignore file
├── python-version              # Python version file
├── LICENSE                     # License file
├── PostgreSQL.md               # Database setup commands
├── pyproject.toml              # Python project configuration
├── README.md                   # Project documentation
└── uv.lock                     # uv lock file
```

---

## 🛠️ Setup & Installation

### 1. Database Setup

Ensure PostgreSQL is running. Create the database and user using the commands found in `PostgreSQL.md`:

```sql
CREATE DATABASE llm_chatbot_db;
-- See PostgreSQL.md for full permissions setup
```

### 2. Backend

Navigate to the backend directory and install dependencies (assuming `requirements.txt` exists):

```bash
cd backend
uv pip install fastapi uvicorn sqlalchemy psycopg2-binary transformers trl torch langchain-chroma langchain-huggingface

# Run the server
uvicorn app.main:app --reload
```

### 3. Frontend

Navigate to the frontend directory:

```bash
cd frontend
npm install
npm run dev # for development
npm start # for production
```

---

## 🔄 Workflows

### A. The RAG Workflow (Runtime)

1. **Ingest**: User pastes text into the UI and clicks **"Ingest (RAG)"**. The text is embedded and stored in ChromaDB.
2. **Chat**: User asks a question.
3. **Retrieve**: Backend searches ChromaDB for relevant context.
4. **Generate**: LLM answers the question using the retrieved context.

### B. The RLHF Training Workflow (Offline)

Once enough data is collected in the database, run the training scripts in order:

**1. Supervised Fine-Tuning (SFT)**
Teaches the model "how" to speak by mimicking good conversations.

```bash
python -m app.train_sft
```

**2. Reward Model Training**
Creates a digital judge that learns to distinguish between good (👍) and bad (👎) responses.

```bash
python -m app.train_reward
```

**3. Reinforcement Learning (PPO)**
Optimizes the policy model to maximize rewards generated by the Reward Model.

```bash
python -m app.train_rl
```

---
