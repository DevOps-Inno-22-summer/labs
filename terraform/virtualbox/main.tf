resource "github_repository" "terraform" {
  name        = "DevOpsTerraform"
  description = "Solutions for devops labs"

  private = false
  teams = {}
  webhooks = {}
  default_branch = "main"

  branch_protection = {
    main = {}
  }
}
