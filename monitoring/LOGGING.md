
### Steps for 7-8 lab
1. add docker-compose.yml
2. add promtail.yml
3. configure ports:
    - app: 5000
    - loki: 3100
    - promtail, grafana: 3000
4. run
```
docker-compose up
``` 
5. go to *localhost:3000* and login with admin-admin
6. add data sourse Loki with http://loki:3100
7. capture logs

### Screenshots

1. List of runing containers
![Containers](https://github.com/AlxGration/devopslabs/blob/master/monitoring/img/containers.jpg)

2. Example of Logs (by 'container_name' and 'job')
![Logs](https://github.com/AlxGration/devopslabs/blob/master/monitoring/img/logs.jpg)

![Job](https://github.com/AlxGration/devopslabs/blob/master/monitoring/img/job.jpg)

### Best practices
- Label values must always be bounded
- Make use of log rotation
- Backup long-term logs in external storage