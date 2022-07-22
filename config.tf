resource "github_repository" "labs" {
  name                 = "labs"
  description          = "DevOps summer classes"
  default_branch       = "master"
  visibility           = "public"
}

resource "github_branch_protection_v3" "labs" {
  repository     = "github_repository.labs"
  branch         = "master"
  enforce_admins = true

  required_pull_request_reviews {
    dismiss_stale_reviews = true
    dismissal_users       = ["safinsaf"]
  }

  restrictions {
    users = ["some-user"]
    apps  = ["labs"]
  }
}