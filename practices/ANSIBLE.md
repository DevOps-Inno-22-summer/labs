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

# Commands

    ansible-playbook playbooks/
