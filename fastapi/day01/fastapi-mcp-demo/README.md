# FastAPI and FastMCP Project Setup

## 1. Create a Project

```bash
uv init fastapi-mcp-demo --bare
```

This creates only the `pyproject.toml` file and the `.venv` virtual environment.

## 2. Install Packages

Navigate to the project directory:

```bash
cd fastapi-mcp-demo
```

Install the required packages:

```bash
uv add "fastapi[standard]" fastmcp
```

## 3. Create `main.py`

Create a `main.py` file in the project directory.

## 4. Run the Application

**Option 1: Using the FastAPI CLI**
Fast API cli internally uses uvicorn only
```bash
uv run fastapi dev
```

**Option 2: Using Uvicorn directly**

Uvicorn is an ASGI (Asynchronous Server Gateway Interface) server.

```bash
uv run uvicorn main:app --reload
```

**Option 3: Activate the virtual environment and run Uvicorn**

```bash
source .venv/bin/activate
uvicorn main:app --reload
```