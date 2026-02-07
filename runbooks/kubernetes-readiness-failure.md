# Incident: Kubernetes Readiness Failure

## Symptoms
- Pod Running but Not Ready
- Traffic blocked by Service

## Detection
- Readiness probe failing
- Metrics showed 503 responses

## Resolution
- Restored database
- Pod transitioned to Ready

## Verification
- Service routed traffic again

## Lesson
Readiness is a traffic gate, not a health check.
