# 🚀 TaskFlow

### A Dockerized Flask-Based Task Management Application with GitHub Actions CI/CD, Trivy Security Scan, and Kubernetes Deployment

---

## 📌 Project Overview

TaskFlow is a simple Task Management web application developed using **Flask** and **SQLite**. Users can create, update, delete, search, and manage their daily tasks through a clean and user-friendly interface.

The main goal of this project is **not only to build a Flask application but also to implement a complete DevOps workflow**. The application is containerized using Docker, automated with GitHub Actions CI/CD, scanned using Trivy for security, and deployed on a Kubernetes (Kind) cluster.

---

## 🎯 Project Objective

The objective of this project is to learn and implement the core concepts of DevOps by deploying a simple Flask application through an automated software delivery pipeline.

The project demonstrates:

- Application Development using Flask
- Version Control using Git & GitHub
- Containerization using Docker
- Image Storage using Docker Hub
- Continuous Integration using GitHub Actions
- Security Scanning using Trivy
- Container Orchestration using Kubernetes (Kind)

---

## ❓ Problem Statement

Deploying applications manually on different systems often leads to dependency issues, inconsistent environments, and time-consuming deployments.

This project solves these challenges by packaging the application into a Docker container, automating the build and deployment process using GitHub Actions, scanning the application for vulnerabilities using Trivy, and deploying it consistently on Kubernetes.

---

# ✨ Features

### Application Features

- Create Task
- Edit Task
- Delete Task
- Search Tasks
- Filter Tasks
- Mark Task Complete
- Mark Task Pending
- Set Priority
- Set Due Date
- Responsive User Interface

---

# 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Framework | Flask |
| Database | SQLite |
| Frontend | HTML, CSS, JavaScript |
| Version Control | Git & GitHub |
| Containerization | Docker |
| Image Registry | Docker Hub |
| CI/CD | GitHub Actions |
| Security | Trivy |
| Container Orchestration | Kubernetes (Kind) |

---

# 🏗 Project Architecture

```text
                Developer
                    │
                    ▼
              GitHub Repository
                    │
                    ▼
           GitHub Actions (CI/CD)
                    │
      ┌─────────────┼─────────────┐
      ▼             ▼             ▼
 Build Image   Trivy Scan   Push Image
      │                           │
      └─────────────┬─────────────┘
                    ▼
              Docker Hub
                    │
                    ▼
           Kubernetes (Kind)
                    │
                    ▼
          Running TaskFlow App
```

---

# 📁 Project Structure

```text
TaskFlow/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── kubernetes/
│   ├── namespace.yaml
│   ├── deployment.yaml
│   └── service.yaml
│
├── taskflow/
│   ├── static/
│   ├── templates/
│   ├── models.py
│   ├── routes.py
│   └── __init__.py
│
├── app.py
├── config.py
├── Dockerfile
├── .dockerignore
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 📌 Application Workflow

```text
User
   │
   ▼
Browser
   │
   ▼
Flask Application
   │
   ▼
Routes
   │
   ▼
SQLite Database
   │
   ▼
HTML Templates
   │
   ▼
Browser Response
```

---

# ⚙ DevOps Workflow

```text
Code Push
    │
    ▼
GitHub
    │
    ▼
GitHub Actions
    │
    ├── Checkout Code
    ├── Build Docker Image
    ├── Trivy Scan
    └── Push Image to Docker Hub
            │
            ▼
      Docker Hub
            │
            ▼
 Kubernetes (Kind)
            │
            ▼
 Running Application
```