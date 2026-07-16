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

---

# 🐳 Docker

## What is Docker?

Docker is a containerization platform that packages an application along with all its dependencies into a container. This ensures the application runs consistently on any machine without dependency issues.

### Why did I use Docker?

I used Docker to package the Flask application so it can run consistently across different environments without requiring Python or project dependencies to be installed manually.

---

## Docker Workflow

```text
Source Code
     │
     ▼
Dockerfile
     │
docker build
     │
     ▼
Docker Image
     │
docker run
     │
     ▼
Docker Container
```

---

## Dockerfile Explanation

| Instruction | Purpose |
|------------|---------|
| FROM | Uses the official Python base image |
| WORKDIR | Sets the working directory inside the container |
| COPY | Copies project files into the container |
| RUN | Installs required Python packages |
| EXPOSE | Exposes port 5000 |
| CMD | Starts the Flask application |

---

## Commands Used

Build Docker Image

```bash
docker build -t taskflow:v1 .
```

Run Docker Container

```bash
docker run -d -p 5000:5000 --name taskflow-container taskflow:v1
```

View Running Containers

```bash
docker ps
```

View Docker Images

```bash
docker images
```

Stop Container

```bash
docker stop taskflow-container
```

Remove Container

```bash
docker rm taskflow-container
```

---

## Viva Tip

Docker Image → Blueprint of the application.

Docker Container → Running instance of the Docker Image.

---

# 📦 Docker Hub

## What is Docker Hub?

Docker Hub is a cloud-based image registry used to store and share Docker images.

---

## Why did I use Docker Hub?

After building the Docker image locally, I pushed it to Docker Hub so that it could be easily downloaded and deployed on Kubernetes.

---

## Workflow

```text
Docker Image
      │
docker tag
      │
      ▼
Docker Hub Repository
      │
docker push
      │
      ▼
Image Available Online
```

---

## Commands Used

Login

```bash
docker login
```

Tag Image

```bash
docker tag taskflow:v1 jigar1311/taskflow:v1
```

Push Image

```bash
docker push jigar1311/taskflow:v1
```

Pull Image

```bash
docker pull jigar1311/taskflow:v1
```

---

## Viva Tip

Docker Image → Stored Locally

Docker Hub → Stores Images Online

---

# ⚙ GitHub Actions (CI/CD)

## What is GitHub Actions?

GitHub Actions is GitHub's built-in CI/CD service used to automate software development workflows.

---

## Why did I use GitHub Actions?

Whenever I push code to GitHub, the pipeline automatically:

- Checks out the source code
- Builds the Docker image
- Performs a Trivy security scan
- Pushes the Docker image to Docker Hub

This eliminates manual deployment steps.

---

## CI/CD Workflow

```text
Developer Push
       │
       ▼
GitHub Repository
       │
       ▼
GitHub Actions
       │
       ├── Checkout Repository
       ├── Build Docker Image
       ├── Trivy Scan
       └── Push Image to Docker Hub
```

---

## Pipeline File

```text
.github/workflows/ci.yml
```

---

## Viva Tip

CI (Continuous Integration)

Automatically builds and validates code after every push.

CD (Continuous Delivery)

Automatically prepares the application for deployment.

---

# 🔒 Trivy Security Scan

## What is Trivy?

Trivy is an open-source security scanner that scans Docker images for known vulnerabilities and security issues.

---

## Why did I use Trivy?

Before pushing the Docker image to Docker Hub, the pipeline scans the image to detect vulnerabilities. This helps identify security issues early in the development process.

---

## Workflow

```text
Docker Image
      │
      ▼
Trivy Scan
      │
      ▼
Security Report
```

---

## Benefits

- Detects vulnerabilities
- Improves application security
- Integrated into the CI/CD pipeline
- Automated scanning

---

## Viva Tip

Trivy is a DevSecOps tool because it adds security checks into the CI/CD pipeline.

---

# ☸ Kubernetes

## What is Kubernetes?

Kubernetes is a container orchestration platform used to deploy, manage, and scale containerized applications.

---

## Why did I use Kubernetes?

After pushing the Docker image to Docker Hub, Kubernetes pulls the image and runs the application inside Pods.

---

## Kubernetes Files

| File | Purpose |
|------|---------|
| namespace.yaml | Creates a separate namespace |
| deployment.yaml | Creates and manages Pods |
| service.yaml | Exposes the application |

---

## Kubernetes Workflow

```text
Docker Hub
      │
      ▼
Deployment
      │
      ▼
Pods
      │
      ▼
Service
      │
      ▼
Application Access
```

---

## Commands Used

Create Resources

```bash
kubectl apply -f kubernetes/
```

View Pods

```bash
kubectl get pods -n taskflow
```

View Services

```bash
kubectl get svc -n taskflow
```

View Deployments

```bash
kubectl get deployments -n taskflow
```

Delete Resources

```bash
kubectl delete -f kubernetes/
```

---

## Viva Tip

Pod → Smallest deployable unit in Kubernetes.

Deployment → Manages Pods.

Service → Exposes Pods to users.

Namespace → Separates project resources.

Kind → Local Kubernetes cluster running inside Docker.


# 📋 Commands Reference

## Run Application

```bash
python app.py
```

---

## Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

## Docker Commands

Build Docker Image

```bash
docker build -t taskflow:v1 .
```

Run Docker Container

```bash
docker run -d -p 5000:5000 --name taskflow-container taskflow:v1
```

View Running Containers

```bash
docker ps
```

View Docker Images

```bash
docker images
```

Stop Container

```bash
docker stop taskflow-container
```

Remove Container

```bash
docker rm taskflow-container
```

Run Docker Container

```bash
docker run -d -p 5000:5000 --name taskflow-container taskflow:v1
```

Port Mapping

```bash
docker run -p 5000:5000 taskflow:v1
```

Explanation

```
Host Port (5000)  →  Container Port (5000)
```

---

## Docker Hub Commands

Login

```bash
docker login
```

Tag Image

```bash
docker tag taskflow:v1 jigar1311/taskflow:v1
```

Push Image

```bash
docker push jigar1311/taskflow:v1
```

Pull Image

```bash
docker pull jigar1311/taskflow:v1
```

---

## Kubernetes Commands

Create Resources

```bash
kubectl apply -f kubernetes/
```

View Pods

```bash
kubectl get pods -n taskflow
```

View Services

```bash
kubectl get svc -n taskflow
```

View Deployments

```bash
kubectl get deployments -n taskflow
```

Delete Resources

```bash
kubectl delete -f kubernetes/
```

Port Forward Service

```bash
kubectl port-forward service/taskflow-service 5000:80 -n taskflow
```

OR (Port Forward Pod)

```bash
kubectl port-forward pod/<pod-name> 5000:5000 -n taskflow
```

Access Application

```
http://localhost:5000
```

---

## Git Commands

Add Files

```bash
git add .
```

Commit Changes

```bash
git commit -m "Your commit message"
```

Push to GitHub

```bash
git push origin main
```

Pull Latest Changes

```bash
git pull origin main
```

---

## Project Status

✅ Flask Application Developed

✅ Dockerized Application

✅ Docker Image Published to Docker Hub

✅ GitHub Actions CI/CD Pipeline

✅ Trivy Security Scan

✅ Kubernetes Deployment using Kind

---

## ✅ Project Completion Status

| Component | Status |
|-----------|--------|
| Flask Application | ✅ |
| Docker | ✅ |
| Docker Hub | ✅ |
| GitHub Actions | ✅ |
| Trivy | ✅ |
| Kubernetes | ✅ |

---

**TaskFlow** successfully demonstrates an end-to-end DevOps workflow, including application development, containerization, automated CI/CD, security scanning, and Kubernetes deployment.

---

![Python](https://img.shields.io/badge/Python-3.13-blue)

![Flask](https://img.shields.io/badge/Flask-3.x-black)

![Docker](https://img.shields.io/badge/Docker-Container-blue)

![GitHub Actions](https://img.shields.io/badge/CI/CD-GitHub%20Actions-green)

![Kubernetes](https://img.shields.io/badge/Kubernetes-Kind-326CE5)

## 🔗 Repository

https://github.com/yourusername/TaskFlow

## 📦 Docker Hub

https://hub.docker.com/r/jigar1311/taskflow

