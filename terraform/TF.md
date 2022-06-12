# LAB 5-6

## Best practices for Terraform-YandexCloud

- Store access tokens and secrets as environment variables
- Create user and add ssh key
- Output variable to know the IP address

## Screenshots

1. Create YaCloud VM console log
![YaCloudLog](https://github.com/AlxGration/devopslabs/blob/master/terraform/ya_cloud/ya_cloud_console.jpg)

1. YaCloud VM
![YaCloudVm](https://github.com/AlxGration/devopslabs/blob/master/terraform/ya_cloud/ya_cloud_vm.jpg)

## Guides used to do lab 5-6

- https://cloud.yandex.ru/docs/tutorials/infrastructure-management/terraform-quickstart
- https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html
- https://www.digitalocean.com/community/tutorials/how-to-use-ansible-to-install-and-set-up-docker-on-ubuntu-18-04#playbook-yml
- https://docs.ansible.com/ansible/2.5/modules/docker_container_module.html#examples

# LAB 3-4

## Best practices for Terraform-Github

- Dont't change terraform state file (.tfstate) manually, do this using "apply" command
- Set up a shared remote storage
- Backup state file
- Use 1 state file per Environment (test, dev, prod)
- Use CI for terraform code

## Screenshots

1. 3 VMs from VirtualBox
![Virtualbox](https://github.com/AlxGration/devopslabs/blob/master/terraform/virtualbox/screen_machines.PNG)

2. Workspace with GitHub repo in Terraform Cloud
![Terraform](https://github.com/AlxGration/devopslabs/blob/master/terraform/virtualbox/repository.PNG)

## Commands to run terraform (lab4)

```
terraform init
terraform import github_repository.terraform devopslabs #Import repository to terraform
terraform plan # check what is changed
terraform apply # apply changes
```

## Guides used to do lab 4

- https://medium.com/clarusway/running-flask-web-server-on-virtualbox-using-ansible-and-vagrant-d2b92c6d4075
- https://learn.hashicorp.com/tutorials/terraform/install-cli
- https://registry.terraform.io/providers/integrations/github/latest/docs/resources/repository
- https://registry.terraform.io/providers/integrations/github/latest/docs/resources/branch_protection_v3
- https://registry.terraform.io/providers/integrations/github/latest/docs/resources/branch_defaults
- https://www.youtube.com/watch?v=aHve0Ji13IY
- https://www.youtube.com/watch?v=gxPykhPxRW0
- https://enlear.academy/automate-infrastructure-as-code-with-terraform-cloud-github-7651f345466a