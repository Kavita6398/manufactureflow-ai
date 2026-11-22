# ManufactureFlow AI

**AI-Powered CRM and Manufacturing Operations Management System**

ManufactureFlow AI is an independent portfolio project that aims to combine customer relationship management, manufacturing operations and AI-powered business assistance using the Zoho ecosystem and modern Python technologies.

The project simulates a furniture manufacturing company that manages customers, suppliers, raw materials, production orders, inventory and sales operations.

## Project Overview

ManufactureFlow AI is designed to demonstrate how enterprise business applications can be integrated with an AI assistant to support operational decision-making.

### Business Workflow

1. Manage leads, customers and sales opportunities.
2. Manage suppliers and raw material procurement.
3. Track raw material inventory.
4. Create and manage production orders.
5. Track finished goods inventory.
6. Manage customer sales orders.
7. Query business information through an AI-powered assistant.

## Technology Stack

| Technology | Purpose |
|---|---|
| Zoho CRM | Customer and sales management |
| Zoho Creator | Manufacturing and inventory management |
| Deluge | Business automation |
| Zoho REST APIs | Application integration |
| OAuth 2.0 | Secure authentication |
| Python | Backend development |
| FastAPI | Backend API framework |
| LangGraph | AI agent orchestration |
| Groq / LLM | Language model integration |
| Git and GitHub | Version control |

## System Architecture

The planned architecture consists of three main layers:

**1. Business Application Layer**
- Zoho CRM: Leads, Accounts, Contacts and Deals.
- Zoho Creator: Suppliers, Products, Raw Materials, Purchase Orders, Production Orders, Inventory and Sales Orders.

**2. Backend Integration Layer**
- Python and FastAPI.
- Zoho OAuth 2.0 authentication.
- Zoho CRM and Creator API integration.
- Business logic and data validation.

**3. AI Agent Layer**
- LangGraph-based business assistant.
- Controlled tools for retrieving business information.
- Inventory and production analysis.
- Confirmation-based business operations.

## AI Business Assistant — Planned Capabilities

The assistant is intended to answer questions such as:

- How many office chairs are currently available?
- Which production orders are pending?
- Show the latest deals for Bright Solutions.
- Can we fulfil an order for 20 office chairs?
- Create a sales order for 10 office chairs.

Business calculations and validations will be handled by application code rather than relying solely on the language model.

Write operations will require appropriate authorization, validation and explicit confirmation.

## Current Development Status

This project is being developed incrementally.

### Implemented

- [x] GitHub repository created.
- [x] Python virtual environment configured.
- [x] Initial project structure created.
- [x] FastAPI and backend dependencies installed.
- [x] FastAPI application created.
- [x] Root endpoint (`GET /`) implemented.
- [x] Health endpoint (`GET /health`) implemented.
- [x] Swagger API documentation available.
- [x] Environment configuration using `.env`.
- [x] Centralized configuration module.
- [x] `.env` excluded from Git.

### Planned

- [ ] Zoho CRM module configuration.
- [ ] Zoho Creator manufacturing application.
- [ ] Zoho OAuth 2.0 integration.
- [ ] Zoho CRM API integration.
- [ ] Zoho Creator API integration.
- [ ] Deluge automation.
- [ ] LangGraph AI agent.
- [ ] Read-only business tools.
- [ ] Validated, confirmation-based write operations.
- [ ] Testing, logging and deployment.

## Project Structure

```text
manufactureflow-ai/
│
├── app/
│   ├── agents/
│   ├── api/
│   │   └── routes/
│   ├── core/
│   │   └── config.py
│   ├── integrations/
│   ├── schemas/
│   ├── services/
│   ├── tools/
│   ├── __init__.py
│   └── main.py
│
├── docs/
├── tests/
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## Local Setup

### Prerequisites

- Python 3.13
- Git
- Visual Studio Code

### 1. Clone the repository

```bash
git clone https://github.com/Kavita6398/manufactureflow-ai.git
cd manufactureflow-ai
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can temporarily allow it for the current terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again.

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Configure environment variables

Copy `.env.example` to `.env` and configure the required values.

Do not commit `.env` or expose API credentials in the repository.

### 6. Start the FastAPI server

```bash
python -m uvicorn app.main:app --reload
```

## API Documentation

Once the application is running:

| Endpoint | Description |
|---|---|
| `GET /` | Application information |
| `GET /health` | Application health check |
| `/docs` | Interactive Swagger API documentation |

Local development URL:

```text
http://127.0.0.1:8000
```

## Security Considerations

- Store credentials in environment variables.
- Use OAuth 2.0 for Zoho API authentication.
- Never commit secrets or tokens to GitHub.
- Validate business operations before execution.
- Require authorization and confirmation for sensitive write operations.

## Project Goals

The main goals of ManufactureFlow AI are:

- Demonstrate Zoho CRM and Creator development.
- Implement manufacturing business workflows.
- Integrate enterprise applications through REST APIs.
- Build a tool-using AI agent with LangGraph.
- Apply secure authentication and controlled AI execution.
- Develop an end-to-end business application suitable for real-world scenarios.

## Author

**Kavita Gupta**

GitHub: [Kavita6398](https://github.com/Kavita6398)

---

*ManufactureFlow AI is an independently developed portfolio project. Features described as planned are under development and are not yet implemented.*