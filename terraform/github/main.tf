resource "github_repository" "labs" {
  name        = "labs"
  description = "DevOps class"
  visibility  = "public"
}

resource "github_branch_default" "default" {
  repository = github_repository.labs.name
  branch     = "master"
}

resource "github_branch_protection" "labs" {
  pattern                 = "master"
  repository_id           = github_repository.labs.node_id
  required_linear_history = true
}