# Ansible

To run the playbook, run `ansible-playbook playbooks/docker.yaml`

## Resources

Used the [geerlingguy.docker](https://github.com/geerlingguy/ansible-role-docker) role, installed from Ansible Galaxy.

```Shell
ansible-galaxy install geerlingguy.docker
```

Note that for lab 5, no roles file is present since the only role used is from Ansible Galaxy. The downloaded files are not included in the repo.

## Screenshots

![Ansible Install Docker Playbook](../screenshots/lab5/ansible-install-docker.png)

### Running the playbook to deploy Python app (Docker)

![Ansible Deplying Python App](../screenshots/lab6/ansible-run-role-deploy.png)

### Docker container running in Cloud VM after playbook

![Ansible Docker Container running on VM](../screenshots/lab6/app-running-in-vm.png)
