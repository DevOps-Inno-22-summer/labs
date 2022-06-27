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
    token = file("./github_token_secret")
}

resource "github_repository" "iu-devops-labs" {
  name        = "iu-devops-labs"
  description = "Solutions to DevOps labs"
  visibility  = "public"
}

resource "github_branch_default" "default"{
  repository = github_repository.iu-devops-labs.name
  branch     = "master"
}

resource "github_branch_protection" "iu-devops-labs-protection" {
  repository_id = github_repository.iu-devops-labs.name

  pattern          = "master"
  enforce_admins   = true

  required_pull_request_reviews {
    dismiss_stale_reviews  = true
    restrict_dismissals    = true
  }

}