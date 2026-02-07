## Architecture Status

The project is currently in the initialization phase.

At this stage:
- Repository structure is in place
- No application or infrastructure components have been deployed yet

Next steps will introduce:
- API service
- Kubernetes deployment
- API gateway
- Observability stack

## High-Level Architecture (Kubernetes)

The application is deployed inside a Kubernetes cluster using standard primitives.

Components:
- FastAPI application deployed as a Kubernetes Deployment
- PostgreSQL deployed as a separate Deployment
- Services expose both components internally
- kubectl port-forward used for local access during development

Runtime flow:
Client
 → kubectl port-forward
 → Kubernetes Service (API)
 → API Pod
 → PostgreSQL Service
 → PostgreSQL Pod

Health, readiness, and metrics endpoints are exposed from the API pod.
