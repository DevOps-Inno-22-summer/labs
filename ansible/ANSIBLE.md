## Result

- Playbook "install_docker" console log
![PlaybookDocker](https://github.com/AlxGration/devopslabs/blob/master/ansible/playbook_screen.jpg)

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
