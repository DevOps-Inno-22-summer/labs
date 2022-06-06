resource "github_repository" "devops_labs" {
    name    = "devops_labs"
    description = "DevOps lab 4"
    visibility = "public"
}

resource "github_branch_default" "default" {
  repository = github_repository.devops_labs.name
  branch     = "master"
}

resource "github_branch_protection" "devops_labs" {
  pattern       = "master"
  repository_id = github_repository.devops_labs.node_id
}
