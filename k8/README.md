## kubectl get pods,svc
NAME                                        READY   STATUS    RESTARTS   AGE
pod/devopslab-deployment-7cf9547866-57bjf   1/1     Running   0          43m
pod/devopslab-deployment-7cf9547866-8hjc8   1/1     Running   0          43m
pod/devopslab-deployment-7cf9547866-92zpq   1/1     Running   0          43m

NAME                                   TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/devopslab-deployment-service   LoadBalancer   10.102.109.39   <pending>     7000:32148/TCP   9m20s
service/kubernetes                     ClusterIP      10.96.0.1       <none>        443/TCP          89m

## minikube service --all
|-----------|------------------------------|-------------|-----------------------------|
| NAMESPACE |             NAME             | TARGET PORT |             URL             |
|-----------|------------------------------|-------------|-----------------------------|
| default   | devopslab-deployment-service | http/7000   | http://192.168.59.100:32148 |
|-----------|------------------------------|-------------|-----------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
🎉  Opening service default/devopslab-deployment-service in default browser...
panic: runtime error: index out of range [3] with length 3

goroutine 1 [running]:
k8s.io/minikube/cmd/minikube/cmd.openURLs({0xc001222660?, 0x2, 0x1?})
	/app/cmd/minikube/cmd/service.go:263 +0x4db
k8s.io/minikube/cmd/minikube/cmd.glob..func35(0x372e4e0?, {0xc0003f0340, 0x0, 0x1?})
	/app/cmd/minikube/cmd/service.go:154 +0x655
github.com/spf13/cobra.(*Command).execute(0x372e4e0, {0xc0003f0300, 0x1, 0x1})
	/go/pkg/mod/github.com/spf13/cobra@v1.5.0/command.go:876 +0x67b
github.com/spf13/cobra.(*Command).ExecuteC(0x372dfe0)
	/go/pkg/mod/github.com/spf13/cobra@v1.5.0/command.go:990 +0x3b4
github.com/spf13/cobra.(*Command).Execute(...)
	/go/pkg/mod/github.com/spf13/cobra@v1.5.0/command.go:918
k8s.io/minikube/cmd/minikube/cmd.Execute()
	/app/cmd/minikube/cmd/root.go:170 +0xb46
main.main()
	/app/cmd/minikube/main.go:88 +0x255

