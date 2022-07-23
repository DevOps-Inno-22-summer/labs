# Before applying deployment:

### kubectl get pods output
```
NAME                          READY   STATUS    RESTARTS   AGE
python-app-5fcdcc8c6b-9bjck   1/1     Running   0          10m
```

### kubectl get svc output
```
NAME         TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
kubernetes   ClusterIP      10.96.0.1      <none>        443/TCP          35h
python-app   LoadBalancer   10.107.9.202   <pending>     8000:32074/TCP   6m31s
```

# After applying deployment:

### kubectl get pods output
```
NAME                                     READY   STATUS    RESTARTS   AGE
python-app-deployment-54b99bfc96-92zqw   1/1     Running   0          9m18s
python-app-deployment-54b99bfc96-fdv8q   1/1     Running   0          9m18s
python-app-deployment-54b99bfc96-znq5l   1/1     Running   0          9m18s
```

### kubectl get svc output
```
NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
kubernetes           ClusterIP   10.96.0.1       <none>        443/TCP          37h
python-app-service   NodePort    10.99.239.250   <none>        8000:31422/TCP   85m
```

### minikube service output

![MinukubeOutputLab9](../screenshots/MinukubeOutputLab9.png)

### Web ip proof

![WebProofLab9](../screenshots/WebProofLab9.png)