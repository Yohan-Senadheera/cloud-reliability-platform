# Cloud Reliability Platform

A production-style reliability engineering project that demonstrates
how a containerized API behaves under failures and how observability
is used to detect, understand, and validate recovery.

This project was built to simulate cloud-native reliability behavior locally
using Kubernetes, without relying on a specific cloud provider.

---

## High-Level Architecture

Client  
→ Kubernetes Service  
→ API Pod (Uvicorn + FastAPI)  
→ PostgreSQL Pod  

The system exposes health, readiness, and metrics endpoints and is
fully observable using Prometheus, Grafana, and Alertmanager.

---
## Architecture Overview

A high-level view of the Cloud Reliability Platform, showing request flow, core components, and the observability stack.

![Architecture Diagram](docs/images/Architecture.png)

*Figure: Kubernetes-based architecture with API and PostgreSQL services, monitored using Prometheus and Grafana.*

For a detailed breakdown of each component, see [docs/architecture.md](docs/architecture.md).

---
## What This Project Demonstrates

- Containerized FastAPI service
- Kubernetes Deployments and Services
- Dependency-aware readiness checks
- Prometheus metrics instrumentation
- Prometheus Operator (ServiceMonitor, PrometheusRule)
- Custom Grafana dashboard using SRE Golden Signals
- Real incident simulations and recovery
- Runbooks and engineering documentation

---

## Observability & Monitoring

The project includes a **custom Grafana dashboard** focused on
**service-level Golden Signals (Traffic, Errors, Latency)** and was
used during real incident simulations.

👉 See: [Observability & Monitoring – Deep Dive](docs/observability.md)

---

## Incident Runbooks

Real failure scenarios were simulated and documented:

- API pod crash and self-healing
- Database unavailability and readiness gating
- Kubernetes readiness failure handling

👉 See: [Runbooks](/runbooks/)

---

## Engineering Approach

This project was built incrementally:
1. Application → Container → Kubernetes
2. Failures introduced intentionally
3. Observability used to explain behavior
4. Documentation written alongside development

The goal was to **operate a service**, not just deploy one.

## How to Navigate This Repository

- `docs/architecture.md` – system design and runtime behavior
- `docs/observability.md` – metrics, dashboards, and alerting deep dive
- `docs/runbooks/` – real incident simulations and recovery steps

