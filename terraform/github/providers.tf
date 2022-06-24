# Configure the GitHub Provider
provider "github" {
    token = "${var.token}"
    owner = "devops-lab-org"
}