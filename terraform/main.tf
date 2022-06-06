resource "github_repository" "devops-labs" {
    name    = "devops-labs"
    description = "Solutions to DevOps labs"
    visibility = "public"
}

resource "github_branch_default" "default" {
  repository = github_repository.devops_labs.name
  branch     = "master"
}