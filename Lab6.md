# 6

## Ansible 2

In this lab you need to use ansible to prepare CD process for your application.

1. Create an ansible role for your application's docker image deployment.
2. Update a playbook.
3. Deploy the role.
4. Provide screenshots of ansible run in ANSIBLE.md

### List of requirements

* New role is present in `ansible/roles`
* Playbook uses new role
* Screenshots are present in `ANSIBLE.md`

## Bonus

CD improvement:

1. Create an extra playbook for your bonus app, reuse your existing role and overide the image var only.

Application improvements:

1. Implement any metrics to your app.
2. Implement a healthcheck.
3. Improve logging.
4. Add any extra logic, but don't forget to cover it with unit tests.

> Monitoring - https://devops.com/metrics-logs-and-traces-the-golden-triangle-of-observability-in-
monitoring/