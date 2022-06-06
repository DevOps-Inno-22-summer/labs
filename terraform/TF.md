## Best practices for Terraform

- Dont't change terraform state file (.tfstate) manually, do this using "apply" command
- Set up a shared remote storage
- Backup state file
- Use 1 state file per Environment (test, dev, prod)
- Use CI for terraform code


## Screenshots

1. 3 VMs from VirtualBox
![Virtualbox](https://github.com/AlxGration/devopslabs/blob/master/terraform/screen_machines.PNG)

2. Workspace with GitHub repo in Terraform Cloud
![Terraform](https://github.com/AlxGration/devopslabs/blob/master/terraform/repository.PNG)

## Commands to run terraform

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