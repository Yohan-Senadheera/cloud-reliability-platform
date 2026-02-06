# Architecture

## Overview
This document describes the architecture of the cloud-reliability-platform, a personal project focused on experimenting with cloud-native technologies and understanding system reliability.

## System Components

### Kubernetes Cluster
- Container orchestration platform
- Manages deployment, scaling, and operations of application containers

### WSO2 API Manager
- API gateway and management platform
- Handles API lifecycle, security, and throttling
- Provides API analytics and monitoring

### Observability Stack

#### Prometheus
- Metrics collection and storage
- Time-series database for system and application metrics
- Alert rule evaluation

#### Grafana
- Visualization and dashboarding
- Connects to Prometheus for metric visualization
- Custom dashboards for monitoring system health

## Architecture Diagram
```
┌─────────────────────────────────────────────────────────┐
│                    Kubernetes Cluster                    │
│  ┌──────────────────┐      ┌──────────────────┐        │
│  │  WSO2 API Manager│      │   Applications    │        │
│  │                  │◄─────┤                   │        │
│  └──────────────────┘      └──────────────────┘        │
│           │                          │                   │
│           └──────────┬───────────────┘                   │
│                      ▼                                   │
│            ┌──────────────────┐                         │
│            │   Prometheus     │                         │
│            └──────────────────┘                         │
│                      │                                   │
│                      ▼                                   │
│            ┌──────────────────┐                         │
│            │     Grafana      │                         │
│            └──────────────────┘                         │
└─────────────────────────────────────────────────────────┘
```

## Key Design Principles
- **Observability First**: All components instrumented for metrics and logs
- **Chaos Engineering**: Deliberately introduce failures to test resilience
- **Learning by Breaking**: Understand system behavior through controlled failures
- **Cloud-Native**: Leverage Kubernetes primitives for reliability

## Network Architecture
- Service mesh considerations
- Ingress/egress traffic patterns
- API gateway routing

## Data Flow
1. External requests → API Gateway (WSO2)
2. API Gateway → Backend services in Kubernetes
3. Metrics scraped by Prometheus
4. Grafana queries Prometheus for visualization
5. Alerts triggered based on defined thresholds
