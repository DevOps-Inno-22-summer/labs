terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

# Configure the GitHub Provider
provider "github" {
  token = var.GITHUB_TOKEN
}


resource "github_repository" "test-devops-labs" {
  name        = "test-devops-labs"
  description = "Solutions to DevOps labs"
  visibility  = "public"
}

resource "github_branch_default" "default" {
  repository = github_repository.test-devops-labs.name
  branch     = "master"
}

resource "github_branch_protection" "test-devops-labs" {
  pattern                 = "master"
  repository_id           = github_repository.test-devops-labs.node_id
  required_linear_history = true
}
