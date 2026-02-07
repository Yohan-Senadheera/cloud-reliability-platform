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

### Evidence of Recovery

After pod deletion, Kubernetes automatically created a new pod.

![Pod self-healing](docs/images/app/pod_down_auto_up.png)

## Lesson
Pods are disposable. Services provide stability.
