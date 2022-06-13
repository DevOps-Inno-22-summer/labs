# Deploying project instance on GCP Run
This directory contains a separate configuration for deploying docker container with our app on GCP based vm. The VM will rely on Ansible to get all the services running.


# Applying Terraform
Applying terraform is best from [GCP shell](https://shell.cloud.google.com/) described in Google [docs](https://cloud.google.com/shell/docs/).


```
terraform init
terraform plan
terraform apply
```


# Remove all related resources
```
terraform destroy
```


# References
