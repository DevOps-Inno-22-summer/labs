## Result

- Link to Docker-Image (https://hub.docker.com/repository/docker/alxgration/devops-docker)

- Playbook "install_docker" console log
![PlaybookDocker](https://github.com/AlxGration/devopslabs/blob/master/ansible/playbook_screen.jpg)

- Playbook "docker_image_deploy" console log
![PlaybookDeploy](https://github.com/AlxGration/devopslabs/blob/master/ansible/deploy_screen.jpg)

## Install Ansible using python-pip
```
pip install ansible
```

## Install docker-role
```
ansible-galaxy role install geerlingguy.docker  
```

Configure docker-role

## Run Ansible playbook 
```
ansible-playbook playbooks/install_docker.yml  
```
