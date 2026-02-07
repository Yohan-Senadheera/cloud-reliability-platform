# Incident: API Pod Crash

## Scenario
API pod was manually deleted.

## Detection
- Pod terminated
- New pod created automatically
- Service remained available

## Root Cause
Intentional pod deletion.

## Resolution
Kubernetes recreated the pod automatically.

## Verification
- New pod Running
- API endpoints accessible

## Evidence of Kubernetes Self-Healing

After deleting the API pod, Kubernetes automatically recreated it.

![Pod self-healing](images/pod_down_auto_up.png)

*Figure: API pod terminated and automatically recreated by Kubernetes*


## Lesson
Pods are disposable. Services provide stability.
