# Deployment Instructions

## Apply manifests
```bash
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
