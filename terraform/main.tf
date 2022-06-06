resource "github_repository" "terraform" {
  name        = "Ilya-Nokhrin-labs"
  description = "Solutions for devops labs"


  visibility = "public"
  auto_init = false
  allow_rebase_merge = false
}

resource "github_branch_default" "default"{
  repository = "Ilya-Nokhrin-labs"
  branch     = "main"
}

resource "github_branch_protection_v3" "git_devops_branch_protect" {
  repository     = "Ilya-Nokhrin-labs"
  branch         = "main"

  restrictions {
    users = ["MrTuxedoCrab"]
  }
}