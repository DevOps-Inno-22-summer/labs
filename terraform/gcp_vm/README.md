# Deploying project instance on GCP Run

This directory contains a separate configuration for deploying docker container with our app on GCP based vm. The VM will rely on Ansible to get all the services running.

## Applying Terraform

Applying terraform is best from [GCP shell](https://shell.cloud.google.com/) described in Google [docs](https://cloud.google.com/shell/docs/).

```bash
terraform init
terraform plan
terraform apply
```

## Remove all related resources

```bash
terraform destroy
```

## References

* Google terraform vm [tutorial](https://cloud.google.com/docs/terraform/get-started-with-terraform)
* Official terraform [docs about gce](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/getting_started)
