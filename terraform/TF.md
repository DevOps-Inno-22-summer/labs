# Terraform
`cloud_run` folder contains a separate configuration for deploying docker container with our app into Google Cloud Run. A more interesting case would be to describe resources consumed by the instance (secrets, envs, gcs buckets, etc) and build/deploy trigger.

# Best practices
* Best [practices](https://cloud.google.com/docs/terraform/best-practices-for-terraform) from Google Cloud docs.
* Module [structure](https://www.terraform.io/language/modules/develop)

# References
* Manage github repo through [terraform config](https://learn.hashicorp.com/tutorials/terraform/github-user-teams)
* [Gitlab repo provider](https://registry.terraform.io/providers/gitlabhq/gitlab/latest/docs) (just in case)
* It turns out you [can't pull Docker Hub](https://stackoverflow.com/questions/66316490/how-to-pull-docker-hub-image-to-google-cloud-run) image directly from GCP. I guess they don't like each other? For popular images from Docker Hub [Google suggests](https://cloud.google.com/container-registry/docs/overview#pull-through_cache) to use their cache.
* [Google cloud run doc ref](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_service)