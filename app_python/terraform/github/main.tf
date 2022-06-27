terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = ">= 4.0"
    }
  }
}

variable "github_token" {
  type        = string
  description = "GitHub Access Token"
}

provider "github" {
  token = var.github_token
  owner = "elbatanony-devops"
}

resource "github_repository" "devops-terraform" {
  name        = "devops-terraform"
  description = "Solutions to DevOps labs"
  visibility  = "public"
}

resource "github_branch" "master" {
  repository = github_repository.devops-labs.name
  branch     = "master"
}

resource "github_branch_default" "default" {
  repository = github_repository.devops-labs.name
  branch     = "master"
}

resource "github_branch_protection_v3" "branch_protection" {
  repository = github_repository.devops-labs.name
  branch     = "master"

  restrictions {
    users = ["ElBatanony"]
  }
}

resource "github_membership" "membership_for_myself" {
  username = "ElBatanony"
  role     = "admin"
}

resource "github_membership" "membership_for_insaf" {
  username = "safinsaf"
  role     = "admin"
}

resource "github_team" "admins_team" {
  name    = "admins-team"
  privacy = "closed"
}

resource "github_team" "members_team" {
  name    = "members-team"
  privacy = "closed"
}

resource "github_team_members" "admins_team_members" {
  team_id = github_team.admins_team.id

  members {
    username = "ElBatanony"
    role     = "maintainer"
  }

  members {
    username = "safinsaf"
    role     = "maintainer"
  }
}
