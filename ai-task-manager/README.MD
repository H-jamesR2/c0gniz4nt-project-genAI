# AI-Powered Task Management System

## 📌 Overview
The AI-Powered Task Management System is a **full-stack** application designed to help users efficiently manage, prioritize, and analyze their tasks. The system seamlessly integrates **multiple LLM providers** (OpenAI, Claude, Grok (API keys not easily accessible currently - Feb 2025), and Gemini) for AI-powered task assistance while ensuring **secure authentication** with users’ own credentials. The **React + Vite + TypeScript frontend** provides an intuitive user experience, while the **FastAPI backend** handles authentication, task management, and AI integration.

## 🚀 Features
- **Task Management & Scheduling**  
  - Create, edit, and delete tasks with priority and deadline sorting.
  - Multi-select tasks for bulk actions like deletion or AI analysis.
  - Seamless UI with smooth animations and responsive design.
- **AI Integration**  
  - Secure authentication with OpenAI, Claude, and Gemini.
  - LLM-powered task suggestions and enhancements.
  - Rate-limiting and Redis caching for optimized performance.
- **Data Persistence & Performance**  
  - **FastAPI + SQLite** for lightweight storage.
  - **Redis caching** for session management and response optimization.
  - Authentication with OAuth/API keys per LLM provider.

## 🏗 Tech Stack
- **Frontend**: React.js (Vite, TypeScript, TailwindCSS)
- **Backend**: FastAPI (Python), SQLite, Redis
- **LLM Providers**: OpenAI, Claude, Gemini
- **Authentication**: OAuth / API key-based authentication per provider
- **Containerization**: Docker (Planned for deployment optimization)

---

## 📖 User Stories
### 🎯 As a User, I want to:
1. **Create, edit, and delete tasks** with deadlines and priorities.
2. **Authenticate securely** with my preferred LLM provider.
3. **Set a default LLM provider** for AI-generated task insights.
4. **Analyze my tasks** using AI to optimize my workflow.
5. **View task analytics** based on historical performance.

---

## 🔧 Setup & Installation

### 1️⃣ Backend Setup (FastAPI + SQLite + Redis)
```bash
# Clone the repository
git clone "web link for ai-task-manager"
cd ai-task-manager
```

```bash
# Create virtual environment & install dependencies
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r backend/requirements.txt
```

```bash
# Start Redis server (Ensure Redis is installed)
redis-server &

# Run FastAPI server
uvicorn backend.main:app --reload
```

### 2️⃣ Frontend Setup (React + Vite + TypeScript)
```bash
cd frontend
npm install
npm run dev
```

### 3️⃣ Environment Variables Setup
Create a `.env` file in the `backend/` directory and set your API keys:
```
OPENAI_API_KEY=your_openai_key
GROK_API_KEY=your_grok_key
CLAUDE_API_KEY=your_claude_key
GEMINI_API_KEY=your_gemini_key
DATABASE_URL=sqlite:///./task_manager.db
REDIS_URL=redis://localhost:6379
```

---

## 🛠️ Future Improvements
1. **Docker containerization** for seamless deployment.
2. **PostgreSQL integration** for scalable data storage.
3. **Enhanced AI features**, including auto-prioritization of tasks.
4. **Mobile-friendly design** for improved usability.
5. **User settings page** to configure LLM preferences dynamically.

---



