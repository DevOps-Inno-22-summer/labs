# Configure GCP project
provider "google" {
  project = "codeomatic-org"
}

resource "google_cloud_run_service" "telltime" {
  name     = "telltime"
  location = "us-central1"

  template {
    spec {
      containers {
        image = "gcr.io/codeomatic-org/telltime:v0.0.4"
      }
    }
  }
  traffic {
    percent         = 100
    latest_revision = true
  }
}

data "google_iam_policy" "noauth" {
  binding {
    role = "roles/run.invoker"
    members = [
      "allUsers",
    ]
  }
}

resource "google_cloud_run_service_iam_policy" "noauth" {
  location    = google_cloud_run_service.telltime.location
  project     = google_cloud_run_service.telltime.project
  service     = google_cloud_run_service.telltime.name

  policy_data = data.google_iam_policy.noauth.policy_data
}

# Return service URL
output "url" {
  value = "${google_cloud_run_service.telltime.status[0].url}"
}
