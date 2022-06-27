terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

# Configure the GitHub Provider
provider "github" {
  token = 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
}

resource "github_repository" "mainrepo" {
  name        = "waitme"
  description = "My awesome time app"

  visibility = "public"

  template {
    owner      = "github"
    repository = "terraform-module-template"
  }
}