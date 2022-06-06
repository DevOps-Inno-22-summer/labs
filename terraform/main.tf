resource "github_repository" "terraform" {
  name        = "DevOpsTerraform"
  description = "Solutions for devops labs"

  
  visibility = "public"
  auto_init = false
  allow_rebase_merge = false
}

resource "github_branch_default" "default"{
  repository = "DevOpsTerraform"
  branch     = "main"
}

resource "github_branch_protection_v3" "git_devops_branch_protect" {
  repository     = "DevOpsTerraform"
  branch         = "main"

  restrictions {
    users = ["AlxGration"]
  }
}