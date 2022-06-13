# Best practices for TF.md

1. Split the configuration into several files: main, variables, versions, output.
2. Keep your modules and your environment implementation code separate.

## What can you see here?

1. Screenshot with 3 VMs from Virtual box
![Virtualbox](https://github.com/NastyRu/DevOps_labs/blob/lab4/terraform/virtualbox.png)

2. Screenshot the workspace with GitHub repository
![Terraform](https://github.com/NastyRu/DevOps_labs/blob/lab4/terraform/terraform.png)

References:
1. https://medium.com/clarusway/running-flask-web-server-on-virtualbox-using-ansible-and-vagrant-d2b92c6d4075
2. https://hashicorp-terraform.awsworkshop.io/040_terraform_cloud_setup/3-cloud-workspace-create.html
3. https://enlear.academy/automate-infrastructure-as-code-with-terraform-cloud-github-7651f345466a

## Yandex Cloud VM

1. Screenshot of success run
```sh
ansible-playbook playbook/main.yml
```
![console](https://github.com/NastyRu/DevOps_labs/blob/master/terraform/console.png)

2. Screenshot of VM in Yandex cloud
![yandex](https://github.com/NastyRu/DevOps_labs/blob/master/terraform/yandex.png)
