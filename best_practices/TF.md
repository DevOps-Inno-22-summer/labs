## Best practices for Terraform

- Dont't change terraform state file (.tfstate) manually, do this using "apply" command
- Set up a shared remote storage
- Backup state file
- Use 1 state file per Environment (test/dev/prod)
- Use CI for terraform code

## Screenshots

### Lab 4

1. 3 VMs from VirtualBox

[VMs](../images/vms.png)

2. Workspace with GitHub repo in Terraform Cloud

[Workspace](../images/terraform.png)

3. Snippet from Vagrant console output

[Snippet](../images/vagrant-console.png)

### Lab 5

![Terraform build completed](../images/terraform_complete.png)
![Cloud - network list](../images/cloud_networks.png)
![Cloud - network details](../images/cloud_network_overview.png)
![Ansible install playbook part 1](../images/ansible_install_part1.png)
![Ansible install playbook part 2](../images/ansible_install_part2.png)