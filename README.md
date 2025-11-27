

---

# 🌍 **ExploreSmart – AI Multi-Agent Travel Discovery System (Mock ADK Repo)**

ExploreSmart is a **multi-agent, intelligent travel discovery system** inspired by the **Google Kaggle AI Agents (Concierge Agents Track)**.
This repository provides a **mock, near-functional starter framework** using Python, with clean extension points for ADK integration.

It includes:

*  **Orchestrator + Multiple Cooperative Agents**
*  **Mock Google Search tool**
*  **Mock Maps tool**
*  **File-based Memory Store (`.mock_memory/`)**
*  **Streamlit UI for user-friendly travel planning**
*  **ADK-ready architecture** for fast extension later

---

#  **Features**

###  Multi-Agent Workflow

The Orchestrator coordinates:

1. **PreferenceAgent** → builds user interest profile
2. **SearchAgent** → fetches places using mock Google Search tool
3. **PlannerAgent** → constructs a smart itinerary
4. **MemoryAgent** → stores user long-term preferences

###  Mock Tools (Works Offline)

* Mock Google Search Tool
* Mock Google Maps Tool
  They generate realistic travel results without API fees.

###  Clean Project Structure

Designed for scalability, readability, and ADK extension.

###  Beautiful Streamlit UI

Interactive and easy for users:

* Enter city
* Enter interests
* Generate itinerary instantly

---

#  **Folder Structure**

```
ExploreSmart-AI/
│
├── agents/
│   ├── orchestrator.py
│   ├── search_agent.py
│   ├── preference_agent.py
│   ├── planner_agent.py
│   ├── memory_agent.py
│   └── tools/
│       ├── google_search_tool.py
│       └── maps_tool.py
│
├── ui/
│   └── app.py
│
├── .mock_memory/
│   └── (auto-created user memory files)
│
├── main.py
├── requirements.txt
└── README.md
```

---

#  **How to Run the Project**

## 1️⃣ Clone the Repo

```bash
git clone https://github.com/yourname/ExploreSmart-AI.git
cd ExploreSmart-AI
```

---

## 2️⃣ Create a Virtual Environment

### Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ (Optional) Add API Keys

To prepare for real ADK / Google Search integration:

Create a **`.env` file**:

```
OPENAI_API_KEY=your_key
GOOGLE_API_KEY=your_key
GOOGLE_CSE_ID=your_custom_search_engine_id
```

> The mock version works fine **without real API keys**.

---

#  **Run Backend from Terminal**

```bash
python main.py
```

Expected output:

```
INFO Orchestrator: start run
INFO SearchAgent: returning 15 places
INFO PlannerAgent: itinerary length=10
```

---

#  **Run the Streamlit UI (Recommended)**

### From project root:

```bash
streamlit run ui/app.py
```

Streamlit starts at:

```
http://localhost:8501
```

---

#  **How the System Works**

### 1. User Input

City + Interests

### 2. PreferenceAgent

Builds a preference profile by merging:

* Current session interests
* Previous memory interests

### 3. SearchAgent

Returns mock (but realistic) travel spots:

* Hidden cafés
* Art places
* Photography spots
* Etc.

### 4. PlannerAgent

Creates a simple morning/evening itinerary with stay duration.

### 5. MemoryAgent

Stores the user’s long-term preferences.

---

#  **Future Enhancements**

These are ideal next steps for the capstone:

* Integrate **real Google Search ADK Tool**
* Integrate **real Google Maps ADK Tool**
* Add **route optimization (travel time-aware)**
* Add **weather-based itinerary planning**
* Add **hotel/dining suggestions**
* Add **image-based trend analysis** (Instagram / YouTube / Shorts)
* Replace mock memory with a vector database

---

#  **Why This Repo Is Useful for Kaggle Capstone**

* Demonstrates full multi-agent architecture
* Works offline (safe for evaluation)
* Clean code structure
* Easy for mentors/judges to understand
* ADK-ready design

---

#  **Author**

**Rapaka Lakshmi Prasanna**
AI & ML Student | Multi-Agent Systems | Web Developer
Balaji Institute of Technology & Science

---

#  **Contributions**

Feel free to open issues or PRs to expand ExploreSmart into a full ADK-integrated travel planner.

---


