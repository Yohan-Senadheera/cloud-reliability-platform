## Progress Log

### Day 0 – Repository Initialization
- Created a new GitHub repository
- Used GitHub Copilot to automatically generate the initial folder structure
- Goal: establish a clean, scalable layout before adding application or infrastructure code

### Day 4 – Application Deployed on Kubernetes
- Deployed FastAPI application to a Kubernetes cluster
- Deployed PostgreSQL as a separate workload
- Verified Pods, Services, and Deployments are running correctly
- Accessed the application using kubectl port-forward
- Validated health, readiness, API endpoints, and metrics from inside the cluster

Current stack:
Client → Kubernetes Service → Pod → Uvicorn → FastAPI → PostgreSQL
