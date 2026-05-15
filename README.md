
# Cloud-Native DLP & DevSecOps Platform
![CI](https://github.com/tapanhegde26/DLP-DevSecOps-Platform/actions/workflows/devsecops-pipeline.yml/badge.svg)

A production-grade cloud-native Data Loss Prevention (DLP) and DevSecOps platform built using Kubernetes, FastAPI, Terraform, OpenSearch, and AWS event-driven architecture.

This project demonstrates how modern DevOps and security engineering teams can automatically detect sensitive data exposure across CI/CD pipelines, cloud storage, and containerized environments.

---

# Project Objectives

This platform is designed to:

- Detect sensitive data leakage
- Scan uploaded files for secrets and confidential information
- Generate security incidents automatically
- Store findings in OpenSearch
- Expose operational metrics
- Demonstrate DevSecOps and cloud-native security patterns
- Provide a production-style Kubernetes deployment
- Showcase event-driven security automation

---

# Key Features

## DLP Detection Engine

Detects:

- AWS Access Keys
- Credit Card Numbers
- JWT Tokens
- Private Keys
- Password Patterns

---

## Cloud-Native Architecture

Built using:

- Kubernetes
- Docker
- FastAPI
- OpenSearch
- Prometheus
- Grafana

---

## DevSecOps Features

- CI/CD-ready architecture
- Security-focused microservices
- Metrics exposure
- Containerized workloads
- Infrastructure-as-Code structure
- Kubernetes deployment manifests

---

## Observability

- Prometheus metrics endpoint
- Grafana dashboards
- Incident indexing in OpenSearch

---

# High-Level Architecture

```text
                    +----------------------+
                    |   Developer / User   |
                    +----------+-----------+
                               |
                               v
                     +-------------------+
                     | Upload Sensitive  |
                     | File / Content    |
                     +---------+---------+
                               |
                               v
                   +-----------------------+
                   | FastAPI Scanner API   |
                   +-----------+-----------+
                               |
                +--------------+--------------+
                |                             |
                v                             v
      +-------------------+        +-------------------+
      | DLP Rule Engine   |        | Severity Engine   |
      +-------------------+        +-------------------+
                |
                v
      +---------------------------+
      | Incident JSON Generator   |
      +-------------+-------------+
                    |
                    v
          +----------------------+
          | OpenSearch           |
          | Incident Storage     |
          +----------+-----------+
                     |
                     v
          +----------------------+
          | Grafana Dashboard    |
          +----------------------+
```

---

# Technology Stack

| Category | Technology |
|---|---|
| Container Platform | Kubernetes (Kind) |
| Backend API | FastAPI |
| Search Engine | OpenSearch |
| Monitoring | Prometheus |
| Visualization | Grafana |
| Containerization | Docker |
| IaC | Terraform |
| CI/CD | GitHub Actions |
| Security Scanning | Custom Regex Engine |
| Language | Python 3.11 |

---

# Repository Structure

```text
cloud-native-dlp-platform/
│
├── infrastructure/
│   └── terraform/
│       ├── modules/
│       └── environments/
│
├── services/
│   ├── scanner-service/
│   │   ├── app/
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   │
│   └── api-service/
│
├── kubernetes/
│   ├── base/
│   ├── monitoring/
│   └── security/
│
├── docs/
│   ├── architecture/
│   └── screenshots/
│
├── test-data/
│
└── .github/
    └── workflows/
```

---

# Local Development Setup

# Prerequisites

Install the following tools:

| Tool | Purpose |
|---|---|
| Docker Desktop | Containers |
| kubectl | Kubernetes CLI |
| Kind | Local Kubernetes |
| Helm | Kubernetes package manager |
| Terraform | Infrastructure as Code |
| Python 3.11 | Backend development |

---

# Verify Installation

```bash
docker --version
kubectl version --client
kind version
terraform version
helm version
python3 --version
```

---

# Step 1 — Clone Repository

```bash
git clone https://github.com/<your-username>/cloud-native-dlp-platform.git

cd cloud-native-dlp-platform
```

---

# Step 2 — Create Kubernetes Cluster

```bash
kind create cluster \
  --name dlp-platform \
  --config kubernetes/kind-config.yaml
```

Verify:

```bash
kubectl get nodes
```

---

# Step 3 — Start OpenSearch

```bash
docker compose up -d
```

Verify:

```bash
curl http://localhost:9200
```

---

# Step 4 — Install Monitoring Stack

## Install Grafana

```bash
helm install grafana grafana/grafana \
  --namespace monitoring \
  --create-namespace
```

---

## Install Prometheus

```bash
helm install prometheus \
prometheus-community/kube-prometheus-stack \
--namespace monitoring \
--create-namespace
```

---

# Step 5 — Build Scanner Service

```bash
docker build -t scanner-service:2.0 \
services/scanner-service
```

---

# Step 6 — Load Image Into Kind

```bash
kind load docker-image scanner-service:2.0 \
--name dlp-platform
```

---

# Step 7 — Deploy Scanner Service

```bash
kubectl apply -f kubernetes/base/
```

---

# Step 8 — Verify Deployment

```bash
kubectl get pods
kubectl get svc
```

---

# API Endpoints

# Health Check

```http
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

---

# File Scan API

```http
POST /scan/file
```

Upload file:

```bash
curl -X POST \
  -F "file=@test-data/aws-secret.txt" \
  http://localhost:8080/scan/file
```

---

# Example Detection Result

```json
{
  "incident": {
    "filename": "aws-secret.txt",
    "timestamp": "2026-05-15T10:00:00Z",
    "findings": [
      {
        "type": "aws_access_key",
        "severity": "HIGH",
        "matches_found": 1,
        "sample": "AKIAIOSFODNN7EXAMPLE"
      }
    ],
    "overall_severity": "HIGH"
  }
}
```

---

# Supported Detection Rules

| Detection Type | Severity |
|---|---|
| AWS Access Key | HIGH |
| Credit Card Number | HIGH |
| JWT Token | MEDIUM |
| Password Pattern | MEDIUM |
| Private Key | CRITICAL |

---

# OpenSearch Verification

Check indices:

```bash
curl localhost:9200/_cat/indices?v
```

Query incidents:

```bash
curl localhost:9200/dlp-incidents/_search
```

---

# Metrics Endpoint

Prometheus metrics exposed at:

```text
http://localhost:8080/metrics
```

---

# Security Features

## Current Features

- Sensitive data detection
- Incident generation
- Kubernetes deployment
- Containerized microservice
- Metrics instrumentation
- OpenSearch indexing

---

## Planned Features

- GitHub Actions DevSecOps pipeline
- Gitleaks integration
- Trivy container scanning
- SBOM generation
- OPA/Gatekeeper policies
- AWS event-driven DLP pipeline
- Slack alerts
- Kubernetes RBAC hardening
- Secrets management
- AI-powered contextual DLP

---

# Sample Test Data

# AWS Key Test

```text
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
```

---

# Credit Card Test

```text
4111 1111 1111 1111
```

---

# Development Workflow

```text
Developer
   |
Git Push
   |
CI/CD Pipeline
   |
Security Scanning
   |
Docker Build
   |
Kubernetes Deployment
```

---

# Kubernetes Components

| Resource | Purpose |
|---|---|
| Deployment | Scanner service |
| Service | Internal networking |
| Ingress | External routing |
| Prometheus | Metrics |
| Grafana | Visualization |

---

# Monitoring Stack

| Tool | Purpose |
|---|---|
| Prometheus | Metrics collection |
| Grafana | Dashboards |
| OpenSearch | Incident search |
| FastAPI Metrics | Application telemetry |

---

# Future Enhancements

## AWS Event-Driven Pipeline

Planned architecture:

```text
S3 Upload
   |
EventBridge
   |
SQS
   |
Lambda
   |
DLP Scan
   |
OpenSearch
```

---

## AI-Powered DLP

Future capabilities:

- Context-aware detection
- LLM-based classification
- False-positive reduction
- Document sensitivity scoring

---

# Screenshots

Add screenshots to:

```text
docs/screenshots/
```

Recommended screenshots:

- Grafana dashboard
- Kubernetes pods
- OpenSearch incidents
- CI/CD pipeline
- Scanner API response

---

# Architecture Diagrams

Store diagrams in:

```text
docs/architecture/
```

Recommended tools:

- draw.io
- Excalidraw
- Lucidchart

---

# Production Considerations

This project intentionally uses:

- Kind instead of EKS
- Local OpenSearch instead of managed service
- Local Kubernetes for cost optimization

This allows:

- Zero/low-cost operation
- Easy local demos
- Portfolio-friendly deployment

---

# Learning Outcomes

This project demonstrates skills in:

- DevOps Engineering
- DevSecOps
- Kubernetes
- Cloud Security
- DLP Engineering
- Security Automation
- Infrastructure as Code
- Event-driven systems
- Observability
- Python backend engineering

---

# Author

Developed by <your-name>

---

# License

MIT License
