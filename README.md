# Segundo-Deber – Dockerized Flask Systems

This repository contains two fully dockerized systems developed in Python using Flask:

1. 🧩 **Centralized System** – A simple monolithic application
2. 🌐 **Distributed System** – Structured into `frontend/` and `backend/`, but built as a single image

Each system is independent, runs on its own, and has its image published on DockerHub. This allows them to be run locally or from any computer that has Docker installed.

---

## 📂 Project Structure

```
Segundo-Deber/
├── centralized_app/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── templates/
│       └── index.html
├── distributed_system/
│   ├── backend/
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   └── Dockerfile
│   └── frontend/
│       └── index.html
└── README.md
```

---

## ✅ System 1: Centralized Flask App

### 📋 Description

A monolithic Flask web application that renders a static HTML page using Jinja2.

### ▶️ How to Build and Run Locally

```bash
cd centralized_app
docker build -t cristianpilapanta/centralized-app .
docker run -p 5000:5000 cristianpilapanta/centralized-app
```

### 🌐 Access

Open your browser: http://localhost:5000

---

## ✅ System 2: Distributed Flask App

### 📋 Description

This system is structured as:

- `backend/`: A Flask app
- `frontend/`: A static HTML file

Both are served from a single Flask container. No need for nginx or Docker Compose.

### ❌ Why is there no `docker-compose.yml`?

Because the backend serves both the logic and the HTML. Only one container is needed, making `docker-compose` unnecessary.

### ▶️ How to Build and Run Locally

```bash
cd distributed_system/backend
docker build -t cristianpilapanta/distributed-system .
docker run -p 5000:5000 cristianpilapanta/distributed-system
```

### 🌐 Access

Open your browser: http://localhost:5000

---

## 🧪 Running the Images on Any Machine

You can run both systems directly from DockerHub **without cloning the repository**.

### ✅ Minimum Requirements

- Docker Desktop or Docker Engine installed
- Internet connection to pull Docker images
- No need for Python, Flask, or VS Code
- No source code required

---

### ▶️ Run Centralized App via DockerHub

```bash
docker run -p 5000:5000 cristianpilapanta/centralized-app
```

### ▶️ Run Distributed System via DockerHub

```bash
docker run -p 5000:5000 cristianpilapanta/distributed-system
```

### 🌐 Access

Open: http://localhost:5000

---

### ⚠️ Port Note

If port `5000` is already in use, you can remap it:

```bash
docker run -p 8080:5000 cristianpilapanta/distributed-system
```

Then go to: http://localhost:8080

---

### 🔁 Optional: Remove Docker Images After Testing

```bash
docker rmi cristianpilapanta/centralized-app
docker rmi cristianpilapanta/distributed-system
```

---

## 🐳 DockerHub Links

- 🧩 Centralized App:  
  https://hub.docker.com/r/cristianpilapanta/centralized-app

- 🌐 Distributed System:  
  https://hub.docker.com/r/cristianpilapanta/distributed-system

---

## 👨‍🎓 Author

- **Cristian Pilapanta**
