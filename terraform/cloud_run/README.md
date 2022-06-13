# Deploying project instance on GCP Run
This directory contains a separate configuration for deploying docker container with our app into [Google Cloud Run](https://cloud.google.com/run/docs/). A more interesting case would be to describe resources consumed by the instance (secrets, envs, gcs buckets, etc) and build/deploy trigger. 


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
* It turns out you [can't pull Docker Hub](https://stackoverflow.com/questions/66316490/how-to-pull-docker-hub-image-to-google-cloud-run) image directly from GCP. I guess they don't like each other? For popular images from Docker Hub [Google suggests](https://cloud.google.com/container-registry/docs/overview#pull-through_cache) using their cache.
* [Google cloud run doc ref](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_service)
