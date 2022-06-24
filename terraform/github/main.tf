resource "github_repository" "labs" {
  name             = "labs"
  description      = "Solutions to DevOps labs"
  visibility       = "public"
}

resource "github_branch_default" "default"{
  repository = github_repository.labs.name
  branch     = "master"
}

#Protect the master branch of the labs repository. Only allow a specific user to merge to the branch.
resource "github_branch_protection_v3" "labs" {
  repository     = github_repository.labs.name
  branch         = "master"
  enforce_admins = true

  restrictions {
    users = ["raghadsalameh1"]
  }

  required_status_checks {
    strict   = false
    contexts = ["ci/travis"]
  }

  required_pull_request_reviews {
    dismiss_stale_reviews = true
    dismissal_users       = ["raghadsalameh1"]
    dismissal_teams       = []
  }
}


