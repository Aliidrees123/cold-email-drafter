---
title: Cold_Email_Drafter
app_file: app.py
sdk: gradio
sdk_version: 6.9.0
---
# Cold Email Drafter (Multi-Agent AI Demo)

A small portfolio project demonstrating **multi-agent orchestration using the OpenAI Agents SDK**.
The system generates a **cold outreach sales email from a free-text prompt** using several specialized AI agents that collaborate to produce the final result.

This project focuses on **agent architecture and orchestration**, not production email sending.

---

# Overview

The application accepts a description of a product/service and target customer, then generates a cold outreach email.

Instead of using a single model call, the system uses **multiple agents with different responsibilities**:

1. Multiple tone agents generate email drafts.
2. A selector agent evaluates the drafts and chooses the best one.
3. A subject agent generates a subject line for the selected email.
4. A manager agent coordinates the workflow and calls the appropriate tools.

The final result returned to the user is:

* a subject line
* a polished cold outreach email

---

# Example Prompt

```
Write a cold outreach email selling an AI scheduling assistant to small law firms.
```

Example output:

```
Subject: Simplify Scheduling for Your Law Firm

Hi,

I’m reaching out because many small law firms struggle with the time spent coordinating client meetings and court dates.

Our AI scheduling assistant automatically manages availability, reduces back-and-forth emails, and keeps calendars organized.

Firms using our tool typically save several hours per week while avoiding scheduling conflicts.

Would you be open to a quick 10-minute demo to see how it works?

Best,
```

---

# Architecture

The project demonstrates a **simple multi-agent architecture**.

```
User Prompt
     │
     ▼
Manager Agent
     │
     ├── Formal Email Agent
     ├── Friendly Email Agent
     ├── Persuasive Email Agent
     └── Concise Email Agent
            │
            ▼
       Selector Agent
            │
            ▼
        Subject Agent
            │
            ▼
        Final Email
```

Each agent has **one clearly defined responsibility**, allowing the system to remain modular and easy to extend.

---

# Agents

### Tone Agents

Generate email drafts in different styles.

* `formal_agent`
* `friendly_agent`
* `persuasive_agent`
* `concise_agent`

Each receives the same prompt but produces a draft with a different tone.

---

### Selector Agent

Evaluates all generated drafts and selects the most effective cold outreach email based on:

* clarity
* value proposition
* professionalism
* likelihood of response

---

### Subject Agent

Generates a short, relevant subject line for the final selected email.

---

### Manager Agent

Coordinates the entire workflow:

1. validates the prompt
2. calls tone agents
3. selects the best draft
4. generates the subject line

The manager **uses the other agents as tools** via the Agents SDK.

---

# Project Structure

```
COLD-EMAIL-DRAFTER/
│
├── app.py
├── config.py
├── requirements.txt
│
├── my_agents/
│   ├── manager_agent.py
│   ├── formal_agent.py
│   ├── friendly_agent.py
│   ├── persuasive_agent.py
│   ├── concise_agent.py
│   ├── selector_agent.py
│   └── subject_agent.py
│
├── orchestration/
│   └── orchestrator.py
│
├── tools/
│   └── agent_tools.py
│
├── ui/
│   └── gradio_app.py
```

---

# Key Concepts Demonstrated

* Multi-agent architecture
* Agents used as tools
* Manager agent orchestration
* Async execution with the Agents SDK
* Clear separation of responsibilities
* Simple Gradio interface
* Deployable AI application

---

# Tech Stack

* Python
* OpenAI Agents SDK
* Gradio (UI)
* Hugging Face Spaces (deployment)
* python-dotenv

---

# Running the Project Locally

### 1. Clone the repository

```
git clone <repo-url>
cd cold-email-drafter
```

### 2. Create a virtual environment

```
python -m venv .venv
source .venv/Scripts/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Add environment variables

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key
```

### 5. Run the app

```
python app.py
```

The Gradio interface will launch in your browser.

---

# Purpose of This Project

This project was built as a **learning exercise in agentic AI system design**.

The goal was to explore:

* how agents can collaborate through tools
* how orchestration layers manage agent workflows
* how to structure small agent systems cleanly
* how to deploy an agent-based application
