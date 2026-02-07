#!/usr/bin/env bash
set -euo pipefail

kubectl apply -f k8s/00-namespace.yaml
kubectl apply -f k8s/10-postgres.yaml

# build image + load into kind
docker build -t cloud-rel-api:0.1 ./app
kind load docker-image cloud-rel-api:0.1 --name cloud-rel

kubectl apply -f k8s/20-api.yaml

echo "Done. Run: kubectl -n cloud-rel port-forward svc/api 8000:8000"