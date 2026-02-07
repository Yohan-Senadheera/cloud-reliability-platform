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

## Evidence of Database Dependency Failure

The database was intentionally scaled down and later restored.

![Database scaled down](images/db_replicas_0.png)

*Figure: PostgreSQL scaled to zero replicas*

![Database restored](images/db_replicas_1.png)

*Figure: PostgreSQL restored and available again*


## Lesson
Readiness must reflect dependency health.
