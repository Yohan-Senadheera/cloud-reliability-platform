## Decision: Use GitHub Copilot for Initial Project Structure

### Reason
- Accelerates bootstrapping without spending time on manual scaffolding
- Allows early focus on architecture and reliability rather than folder setup

### Outcome
- A clean initial layout that can evolve as the project grows
- Structure separates concerns early (code, docs, infrastructure, runbooks)

### Alternatives Considered
- Manual folder creation (rejected – slower and error-prone)


## Decision: Deploy Application and Database as Separate Kubernetes Workloads

### Reason
- Separating application and database follows microservice principles
- Allows independent scaling, restarts, and failure isolation
- Matches real-world Kubernetes deployment patterns

### Outcome
- API and PostgreSQL run in separate Pods and Deployments
- Kubernetes manages lifecycle and restarts independently
- Readiness checks correctly reflect database availability

### Notes
This setup enables realistic failure testing and recovery scenarios.
