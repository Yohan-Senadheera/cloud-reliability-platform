# Architectural & Engineering Decisions

This document records **why** decisions were made, not just what was built.

---

## Decision: Use Kubernetes Instead of Local Containers

**Reason**
- Kubernetes enables failure simulation and self-healing
- Matches real production environments
- Supports readiness-based traffic control

**Outcome**
- Pods are disposable
- Services remain stable
- Recovery is automatic

---

## Decision: Separate API and Database Workloads

**Reason**
- Failure isolation
- Independent lifecycle management
- Realistic microservice architecture

**Outcome**
- Readiness reflects database availability
- Failures are observable and controlled

---

## Decision: Separate Health and Readiness Endpoints

**Reason**
- Liveness ≠ readiness
- Prevents traffic during partial failures

**Outcome**
- App stays alive during DB failures
- Traffic blocked until dependencies recover

---

## Decision: Use Prometheus Operator

**Reason**
- Declarative monitoring
- Kubernetes-native observability
- Industry-standard tooling

**Outcome**
- Metrics scraped via ServiceMonitor
- Alerts defined via PrometheusRule
