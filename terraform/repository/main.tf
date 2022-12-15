terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = ">= 4.0"
    }
  }
}

# variable "github_token" {
#   type        = string
#   description = "GitHub Access Token"
# }

provider "github" {
  token = "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"
  owner = "RobertronS"
}

resource "github_repository" "labsDevOpsMasterProgram" {
  name        = "labsDevOpsMasterProgram"
  description = "Terraform Lab 4 solution of DevOps labs"
  visibility  = "public"
}

resource "github_branch_default" "default" {
  repository = github_repository.labsDevOpsMasterProgram.name
  branch     = "master"
}

resource "github_branch_protection_v3" "branch_protection" {
  repository = github_repository.labsDevOpsMasterProgram.name
  branch     = "master"

  required_pull_request_reviews {
    dismiss_stale_reviews = true
    dismissal_users       = ["RobertronS"]
  }
}