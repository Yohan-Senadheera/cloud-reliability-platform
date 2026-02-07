## Incident: Service Not Ready in Kubernetes

### Symptoms
- Readiness probe returns HTTP 503
- Kubernetes Service does not route traffic to the Pod

### Detection
- curl to /readyz returns status "not ready"
- Pod remains Running but not Ready

### Root Cause
- Database dependency not available or not reachable

### Impact
- Traffic blocked by Kubernetes until dependencies are healthy

### Resolution
- Restore database service
- Verify readiness probe transitions to Ready

### Verification
- kubectl get pods shows Ready state
- API requests succeed
