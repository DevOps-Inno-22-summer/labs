# DevOps Labs by Ahmed ElBatanony

This repository contains the code for the DevOps course assignments, by Ahmed ElBatanony.

The repository has two projects, a Python project, and a bonus Flutter web project.

For more details on the Python project, visit the [app_python](app_python) folder in the repository.

A markdown linter is used for this repository, which is the VS Code extension [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint).

Dockerfiles are linted by the [Docker VS Code extension](https://code.visualstudio.com/docs/containers/overview).

## Vagrant

To provision the virtual machines, run `vagrant up`.

To destroy the virtual machines, run `vagrant destroy`.

## Terraform

Secret tokens such as the GitHub access token are saved in the `secret.tfvars` file.
This file is ignored by git.

To plan the terraform changes, run `terraform plan -var-file="secret.tfvars"`.

To apply the changes, run `terraform apply -var-file="secret.tfvars"`.

Bonus: the terraform configurations include setting up teams.

## Bonuses

### Lab 5

Used GCP dynamic inventory.

### Lab 6

Playbooks for deploying both apps (Python and Flutter) reuse the same role (via parameters).
