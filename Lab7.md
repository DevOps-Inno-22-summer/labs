# 7

## Monitoring: logging

In this lab you need to get familiar with a logging stack - Promtail, Loki, Grafana. Then prepare a
docker-compose ﬁle and conﬁg ﬁles to setup the stack.

1. Read about the logging stack:

* https://grafana.com/go/webinar/loki-getting-started/
* https://grafana.com/docs/loki/latest/overview/
* https://github.com/grafana/loki

2. Prepare a docker-compose ﬁle with the stack and your app.

* good example of promtail conﬁguration, but be smart - `https://github.com/black-rosary/loki-nginx`

3. Test that it works, prepare a `LOGGING.md` report.
4. Create a monitoring folder, put report, docker-compose.yml and conﬁg ﬁles inside.
5. Provide screenshots of your success in the report.
6. Read about best practices and also put them into the report.

### List of requirements

* Moonitoring folder exists
* `docker-compose.yml` exists and contains the stack and your app
* Mounting of volumes is properly applied in `docker-compose.yml`
* Logging is configured in `docker-compose.yml`, tags are properly set to each container
* promtail.yml exists
    * Logs are taken from correct files
    * Logs are sent to Loki
    * Logs are parsed using regex / json
* `LOGGING.md` exists and contains screenshots with your success
* Best practices in `LOGGING.md`


## Bonus

1. Add your extra app to the `docker-compose.yml`.
2. Conﬁgure stack to get logs from all containers from docker-compose.yml. Provide
screenshots of your success in the report.