Deploy App
=========

A role to deploy a docker image with custome image, container, and ports.

Role Variables
--------------

image: docker image

container_name: name of spawned container

in_port, out_port: ports binding

Example Playbook
----------------

```yaml
- hosts: all

  roles:
    - role: "../roles/deploy_app"
  vars:
    image: 'elbatanony/devops-python:latest'
    container_name: 'devops-python'
    in_port: 5000
    out_port: 5000
```

License
-------

BSD

Author Information
------------------

Ahmed ElBatanony. Innopolis University.
