# Setting Up a Project Using `uv` and FastAPI

## 1. Install `uv`

First, install `uv` using the following command:
uv is a fast Python package and project manager used to create Python projects, manage dependencies, and run applications.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify the installation:

```bash
uv version
```

## 2. Set Up the Project

Initialize a new project using the following command:

```bash
uv init [project-name] --bare
```

Example:

```bash
uv init devcloud --bare
```

- `uv init`: Creates a new Python project.
- `devcloud`: Specifies the project or folder name.
- `--bare`: Creates only the `pyproject.toml` file without generating `main.py` and `README.md`.

## 3. Install FastAPI

Follow the official FastAPI installation guide:

https://fastapi.tiangolo.com/tutorial/#install-fastapi

Install FastAPI using the following command:

```bash
uv add "fastapi[standard]"
```

The `uv add` command creates a virtual environment (`.venv`), downloads FastAPI and its dependencies, and adds the dependency to `pyproject.toml`.

Alternatively, we can create a virtual environment manually and use `pip` to install FastAPI.

## 4. Create the First FastAPI Application

Follow the official FastAPI First Steps tutorial:

https://fastapi.tiangolo.com/tutorial/first-steps/

## 5. Run FastAPI in Development Mode

Run the application using the following command:

```bash
uv run fastapi dev
```

This runs the FastAPI application in development mode. By default, the application is accessible through the loopback IP address (`127.0.0.1:8000`) and does not accept requests from other machines through its network IP address.

Example:

```bash
~/proj$ curl 127.0.0.1:8000
{"msg":"Hello World"}
```

When we try to access the application using the machine's IP address:

```bash
~/proj$ curl 172.24.119.82:8000
curl: (7) Failed to connect to 172.24.119.82 port 8000 after 0 ms: Could not connect to server
```

The request fails because the application is listening only on the loopback interface.

## 6. Run FastAPI in Production Mode

Run the application using the following command:

```bash
uv run fastapi run
```

This runs the FastAPI application in production mode. By default, the application listens on `0.0.0.0:8000`, allowing it to accept requests through all available IPv4/IPv6 network interfaces.

For example, when we send a request using the machine's IP address, we receive the response:

```bash
~/proj$ curl 172.24.120.82:8000
{"msg":"Hello World"}
```

We can also access the application using the loopback IP address:

```bash
~/proj$ curl 127.0.0.1:8000
{"msg":"Hello World"}
```