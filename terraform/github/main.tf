resource "github_repository" "labs" {
  name          = "labs"
  description   = "DevOps class"
  visibility    = "public"
  has_downloads = true
  has_projects  = true
  has_wiki      = true
}

resource "github_branch_default" "default" {
  repository = github_repository.labs.name
  branch     = "master"
}

resource "github_branch_protection" "labs" {
  pattern                 = "protected"
  repository_id           = github_repository.labs.node_id
  required_linear_history = true
}