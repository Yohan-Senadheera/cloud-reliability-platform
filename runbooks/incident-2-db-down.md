# Incident: Database Unavailable

## Scenario
PostgreSQL scaled to zero replicas.

## Detection
- /healthz returned 200
- /readyz returned 503
- API endpoints failed gracefully

## Root Cause
Database dependency unavailable.

## Resolution
Database replicas restored.

## Verification
- /readyz returned 200
- API requests succeeded

### Evidence of Dependency Failure
Database was intentionally scaled down and later restored.

![Database scaled down](docs/images/app/db_replicas_0.png)
![Database restored](docs/images/app/db_replicas_1.png)

## Lesson
Readiness must reflect dependency health.
