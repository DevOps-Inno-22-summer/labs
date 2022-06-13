# Lab5 - Ansible Configuration

For the installing docker and configure it in VMs which made by terraform, ansible used. In ansible/inventory/hosts , hosts defined for the VMs.

## References for Roles:

https://github.com/geerlingguy/ansible-role-docker

## References for Playbooks:

https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html
https://docs.ansible.com/ansible/2.5/scenario_guides/guide_docker.html#examples

![Ansible 0](../screenshots/ansible0.png)
![Ansible 1](../screenshots/ansible1.png)

For proving docker installed to server, connection made to a VM server via ssh:

![Ansible 3](../screenshots/ansible3.png)

## Lab6 - Ansible to Cloud

For the deploying app_python to Yandex Cloud, ansible, terraform, and docker hub used. Process is following:

1. Dockerized project put to the docker hub.
2. Terraform configured to deploy the project to Yandex Cloud.
3. Ansible configured to make commands for installing docker and pip to Yandex Cloud.
4. Dockerized project deployed pulled in Yandex Cloud VM and installed by ansible playbook/role.

Ansible Playbook:

![Ansible 4](../screenshots/ansible4.png)

Running Docker container in the VM:

![Ansible 5](../screenshots/ansible5.png)

Running application in the web browser:
http://51.250.6.229:5000
![Ansible 7](../screenshots/ansible7.png)

# Commands

    ansible-playbook playbooks/{file_name}
