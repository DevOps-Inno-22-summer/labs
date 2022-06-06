# Terraform

## Best practices

- Split the configuration into several files: main, variables, versions, output
- Use `terraform fmt`
- Use `terraform validate`
- Set up a shared remote storage
- Backup state file
- Use `terraform apply` for changing .tfstate

## Screenshot

### With default branch

![githubDefaultBranch](./Images/githubDefaultBranch.png)

### Branch protection rules

![githubBranchProtectionRules](./Images/githubBranchProtectionRules.png)

### Terraform workspace

![terraform](./Images/terraform.png)

### 3 VMs

![3vms](./Images/vagrant.png)
