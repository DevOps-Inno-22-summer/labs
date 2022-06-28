# Kubernetes

## kubectl get pods,svc

![Outpout of get pods and svc after manual](../screenshots/lab9/kubectl-get-pods-svc-1.png)
![Outpout of get pods and svc after apply](../screenshots/lab9/kubectl-get-pods-svc-2.png)

## minikube service --all

![Outpout of Service All Console](../screenshots/lab9/service-all-console.png)
![Outpout of Service All Browser](../screenshots/lab9/service-all-browser.png)

## helm

![helm cmd get pods and svc](../screenshots/lab10/helm-cmd-get-pds-svc.png)
![helm k8s dashboard](../screenshots/lab10/helm-k8s-dashboard.png)

## Lab 9 Bonus

Created `flutter_deployment.yml` and `flutter_service.yml` for Flutter bonus project.

Definitions:

- Ingress: incoming data to the cluster
- Ingress controller: a required component for ingress to function. Not started automatically with a cluster
- StatefulSet: gives an unchangeable unique id to each pod. Useful for persistant data (using storage volumes)
- DaemonSet: makes sure that some or all nodes run a specific pod
- PersistentVolumes: k8s api for handling storage as a resource in a cluster
