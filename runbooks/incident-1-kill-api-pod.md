# Incident 1 – API Pod Crash

## Scenario
API pod was deleted manually to simulate a crash.

## Detection
- Pod disappeared from `kubectl get pods`
- Service endpoint temporarily unavailable

## Response
- Kubernetes automatically created a new pod

## Verification
- New pod reached `Running`
- `/healthz` returned 200 OK

## Learning
Kubernetes self-healing ensures service recovery without manual intervention.