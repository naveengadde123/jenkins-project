# Taskflow DevOps Project

This project is a simple Python Flask application designed to demonstrate a realistic DevOps workflow using Jenkins, Docker, Kubernetes (Kind), and Helm.

## Project goals
- Build a lightweight Python microservice
- Run automated tests in CI
- Build and package the app as a Docker image
- Deploy to a local Kubernetes cluster using Kind
- Manage releases with Helm
- Simulate a production-style delivery pipeline

## Architecture

Code -> Jenkins -> Docker -> Kubernetes (Kind) -> Helm

## Application endpoints
- GET /
- GET /health

## Local development
```bash
cd taskflow
python -m pip install -r requirements.txt
python app.py
```

## Testing
```bash
cd taskflow
python -m pytest -q
```

## Docker build
```bash
docker build -t taskflow:latest .
```

## Kubernetes / Helm deployment
```bash
kubectl apply -f k8s/namespace.yaml
helm upgrade --install taskflow ./helm/taskflow --namespace taskflow --create-namespace
```

## CI/CD flow
1. Developer pushes code
2. Jenkins checks out the source
3. Dependencies are installed
4. Unit tests run
5. Docker image is built
6. Helm validates and deploys to Kind
7. Kubernetes exposes the app through a Service

## Why this project is useful
It connects the most common DevOps tools in a single workflow and is easy to explain in interviews.
