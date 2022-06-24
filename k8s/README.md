# LAB 9

# Prerequisites. MacOS (AppleSilicon)
```
brew install kubectl
brew install minikube
minikube start
```

## Manual setting

### Deployment
```
=> kubectl create deployment app-python --image=alxgration/devopslabs
deployment.apps/app-python created

=> kubectl get deployments 
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
app-python   1/1     1            1           5h23m
```

### Service
```
=> kubectl expose deployment app-python --type=LoadBalancer --port=8080
service/app-python exposed

=> kubectl get services
NAME         TYPE           CLUSTER-IP    EXTERNAL-IP   PORT(S)          AGE
app-python   LoadBalancer   10.98.92.34   <pending>     8080:31279/TCP   27s
kubernetes   ClusterIP      10.96.0.1     <none>        443/TCP          5h29m
```

### pods, svc
```
=> kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS        AGE
pod/app-python-5b788c47bd-4cw4g   1/1     Running   1 (3m56s ago)   5h26m

NAME                 TYPE           CLUSTER-IP    EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.98.92.34   <pending>     8080:31279/TCP   109s
service/kubernetes   ClusterIP      10.96.0.1     <none>        443/TCP          5h31m
```

### Remove deployment
```
=> kubectl delete deployment app-python
deployment.apps "app-python" deleted
```

### Remove service
```
=> kubectl delete service app-python
service "app-python" deleted
```

## .yml setting

### Deployment
```
=> kubectl apply -f deployment.yml 
deployment.apps/app-python-deployment created
```

### Service
```
=> kubectl apply -f service.yml 
service/app-python-service created
```

### pods, svc
```
=> kubectl get pods,svc
NAME                                        READY   STATUS    RESTARTS   AGE
pod/app-python-deployment-fc5fb788c-9s6w2   1/1     Running   0          2m31s
pod/app-python-deployment-fc5fb788c-j6h6p   1/1     Running   0          2m31s
pod/app-python-deployment-fc5fb788c-wzrkg   1/1     Running   0          2m31s

NAME                         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-python-service   NodePort    10.111.123.131   <none>        5000:30975/TCP   34s
service/kubernetes           ClusterIP   10.96.0.1        <none>        443/TCP          6h36m
```

### Run all services
```
=> minikube service --all
|-----------|--------------------|-------------|---------------------------|
| NAMESPACE |        NAME        | TARGET PORT |            URL            |
|-----------|--------------------|-------------|---------------------------|
| default   | app-python-service |        5000 | http://192.168.49.2:30975 |
|-----------|--------------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
🏃  Starting tunnel for service app-python-service.
🏃  Starting tunnel for service kubernetes.
|-----------|--------------------|-------------|------------------------|
| NAMESPACE |        NAME        | TARGET PORT |          URL           |
|-----------|--------------------|-------------|------------------------|
| default   | app-python-service |             | http://127.0.0.1:52432 |
| default   | kubernetes         |             | http://127.0.0.1:52438 |
|-----------|--------------------|-------------|------------------------|
🎉  Opening service default/app-python-service in default browser...
🎉  Opening service default/kubernetes in default browser...
```

### Screen
![RunnedService](https://github.com/AlxGration/devopslabs/blob/master/k8s/runned_project.png)