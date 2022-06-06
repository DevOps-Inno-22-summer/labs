# Configure the GitHub Provider
provider "github" {
    token = "${var.token}"
}

resource "github_repository" "labs" {
  name             = "labs"
  description      = "Solutions to DevOps labs"
  visibility       = "public"
}

resource "github_branch_default" "default"{
  repository = github_repository.labs.name
  branch     = "master"
}

