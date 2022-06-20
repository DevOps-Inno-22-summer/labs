# 8

## Monitoring: metrics

In this lab you need to get familiar with Prometheus. Then you need to set up it and conﬁgure apps to obtain metrics.

1. Read about Prometheus
* https://prometheus.io/docs/introduction/overview/
* https://prometheus.io/docs/practices/naming/

2. Add Prometheus to the docker-compose.yml
3. Conﬁgure Prometheus to obtain metrics from Loki and Prometheus containers.
4. Check `http://localhost:9090/targets`.
* Provide screenshots of your success in `METRICS.md` in monitoring folder.
5. Set up dashboards in Grafana for Loki and Prometeheus.
* https://grafana.com/grafana/dashboards/13407
* https://grafana.com/grafana/dashboards/3662
* Provide screenshots of your success in `METRICS.md`
6. Update conﬁg of all services in `docker-compose.yml`.
* Add log rotation.
* Add mem limits.

### List of requirements

* Prometheus service exists
* mem_limit in all services
* logging and log rotation in all services
* prometheus.yml exists and and scrapes metrics from Loki and Prometheus
* `METRICS.md` exists and contains following screenshots:
    * dashboard for loki
    * dashboard for prometheus
    * prometheus/targets 

## Bonus
1. Add any metrics to your apps. Python examples:
* https://dzone.com/articles/monitoring-your-synchronous-python-web-application
* https://opensource.com/article/18/4/metrics-monitoring-and-python

2. Obtain metrics from your apps.
3. Set up a simple Grafana dashboard.
4. Update the `METRICS.md` with screenshots.
5. Update conﬁg of all services in `docker-compose.yml`.
* Add healthchecks.