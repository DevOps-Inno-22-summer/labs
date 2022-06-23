# k8s

## Manual

### Deployment

```
... % kubectl create deployment app-python --image=danilag/app-python
deployment.apps/app-python created

... % kubectl get deployments
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
app-python   1/1     1            1           7s
```

### Service

```
... % kubectl expose deployment app-python --type=LoadBalancer --port=8080
service/app-python exposed

... % kubectl get services
NAME         TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
app-python   LoadBalancer   10.100.69.17   <pending>     8080:30509/TCP   7s
kubernetes   ClusterIP      10.96.0.1      <none>        443/TCP          12m
```

### pods, svc

```
% kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-574df4cd67-v6dtl   1/1     Running   0          6m53s

NAME                 TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.100.69.17   <pending>     8080:30509/TCP   6m29s
service/kubernetes   ClusterIP      10.96.0.1      <none>        443/TCP          18m
```

### Clean up

```
... % kubectl delete service app-python
service "app-python" deleted

... % kubectl delete deployment app-python
deployment.apps "app-python" deleted
```

## From .yml

### Deployment

```
... % kubectl apply -f deployment.yml    
deployment.apps/app-python-deployment created
```

### Service

```
... % kubectl apply -f service.yml       
service/app-python-service created
```

### pods, svc

```
... % kubectl get pods,svc
NAME                                        READY   STATUS    RESTARTS   AGE
pod/app-python-deployment-dc699bfb9-2h9np   1/1     Running   0          11m
pod/app-python-deployment-dc699bfb9-8rvpd   1/1     Running   0          11m
pod/app-python-deployment-dc699bfb9-mfckj   1/1     Running   0          11m

NAME                         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python-service   NodePort    10.100.233.82   <none>        5000:30024/TCP   11m
service/kubernetes           ClusterIP   10.96.0.1       <none>        443/TCP          11m
```

### All services
```
... % minikube service --all
😿  service default/kubernetes has no node port
|-----------|--------------------|--------------|---------------------------|
| NAMESPACE |        NAME        | TARGET PORT  |            URL            |
|-----------|--------------------|--------------|---------------------------|
| default   | app-python-service |         5000 | http://192.168.64.2:30024 |
| default   | kubernetes         | No node port |
|-----------|--------------------|--------------|---------------------------|
```

### Screenshot

![lab9_1](./Images/lab9_1.png)

![lab9_2](./Images/lab9_2.png)

## Helm

### Install

```
... % helm install app-python app-python
NAME: app-python
LAST DEPLOYED: Thu Jun 23 19:02:33 2022
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services app-python)
  export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
  echo http://$NODE_IP:$NODE_PORT
```

### pods,svc

```
... % kubectl get pods,svc                
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-7c9584c587-5ncvp   1/1     Running   0          2m40s
pod/app-python-7c9584c587-fs7vh   1/1     Running   0          2m40s
pod/app-python-7c9584c587-qs9hv   1/1     Running   0          2m40s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python   NodePort    10.110.56.189   <none>        5000:31769/TCP   2m40s
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP          25h
```

### All services

```
... % minikube service --all
😿  service default/kubernetes has no node port
|-----------|------------|--------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT  |            URL            |
|-----------|------------|--------------|---------------------------|
| default   | app-python | http/5000    | http://192.168.64.2:31769 |
| default   | kubernetes | No node port |
|-----------|------------|--------------|---------------------------|
```

### Workloads page 

```
... % minikube dashboard
🔌  Enabling dashboard ...
    ▪ Используется образ kubernetesui/dashboard:v2.3.1
    ▪ Используется образ kubernetesui/metrics-scraper:v1.0.7
🤔  Verifying dashboard health ...
🚀  Launching proxy ...
🤔  Verifying proxy health ...
🎉  Opening http://127.0.0.1:61647/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/ in your default browser...
```

![workloadsPage](./Images/workloadsPage.png)
