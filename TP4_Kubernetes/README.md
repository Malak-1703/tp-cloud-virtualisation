# TP4 : Kubernetes & Kubeflow
## Objectif
Orchestration et MLOps.
## Architecture
- Cluster 3 nœuds (1 Master, 2 Workers).
- Installation de Kubeflow via kustomize.
## Vérification
kubectl get pods -A
kubectl port-forward svc/istio-ingressgateway -n istio-system 8080:80