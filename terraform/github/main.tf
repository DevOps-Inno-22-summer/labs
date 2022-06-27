terraform {
  required_providers {
    github = {
      source = "integrations/github"
      version = ">= 4.0"
    }
  }
}

provider "github" {
    owner = "Heivory"
    token = var.token
}

resource "github_repository" "devops" {
    name = "DevOps-Labs-terraform"
    description = "Solutions to DevOps labs"

    visibility = "public"

    auto_init = true
}

resource "github_branch_default" "default"{
    repository = github_repository.devops.name
    branch = "main"
}

resource "github_branch_protection" "devops_labs" {
   pattern       = "main"
   repository_id = github_repository.devops.node_id

   required_linear_history = true

   required_status_checks {
     strict   = false
     contexts = ["ci/travis"]
   }
 }
