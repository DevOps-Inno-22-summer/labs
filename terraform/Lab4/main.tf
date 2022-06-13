terraform {
  cloud {
    organization = "danilag"

    workspaces {
      name = "devops_lab4_git"
    }
  }
}

provider "github" {
  owner = "DanilaG"
  token = var.token
}

resource "github_repository" "devops_labs" {
  name        = "devops_labs"
  description = "Solutions to DevOps labs"
  visibility  = "public"
  auto_init   = false
}

resource "github_branch_default" "default" {
  repository = github_repository.devops_labs.name
  branch     = "master"
}

resource "github_branch_protection" "devops_labs" {
  pattern       = "master"
  repository_id = github_repository.devops_labs.node_id

  required_linear_history = true

  required_status_checks {
    strict   = false
    contexts = ["ci/travis"]
  }
}
