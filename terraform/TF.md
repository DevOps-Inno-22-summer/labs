# Terraform

## Terraform Best practices

* Best [practices](https://cloud.google.com/docs/terraform/best-practices-for-terraform) from Google Cloud docs.
* Module [structure](https://www.terraform.io/language/modules/develop)
* Use `terraform import` to pull the current state of the resource before applying.
* Don't publish sensitive information

## References

* Manage github repo through [terraform config](https://learn.hashicorp.com/tutorials/terraform/github-user-teams)
* [Gitlab repo provider](https://registry.terraform.io/providers/gitlabhq/gitlab/latest/docs) (just in case)
* Terraform [variables](https://www.terraform.io/language/values/variables)

## GCP VM

After applying terraform VM was created:
![running vm](gcp_vm/screenshots/telltime-vm-running.png)

Related resources were added as well:
![related resources](gcp_vm/screenshots/attached-resources.png)

## Vagrant

3 running VMs:
![vagrant VMs](../vagrant/screenshots/3vms-running.png)

## Github repo synchronized

Main repo page:
![main repo page](github/screenshots/repo-main-page.png)

Protected branch:
![protected branch](github/screenshots/protected-branch.png)
