## Vagrantfile
Created vagrantfile for 3 instances

### Inside virtualbox:
![Virtual box machines](screenshots/all.png "All machines")

### Screenshot of vagrant1 running:
![Screenshot of vagrant1 running](screenshots/vagrant1.png "Vagrant1 machine running")

### Screenshot of vagrant2 running:
![Screenshot of vagrant1 running](screenshots/vagrant2.png "Vagrant2 machine running")

### Screenshot of vagrant3 running:
![Screenshot of vagrant1 running](screenshots/vagrant3.png "Vagrant3 machine running")


## Terraform integration

### Best practices
 - Follow standard module structure with main.tf in every module
 - Adopt naming conventions
 - Declare all variables in variables.tf file
 - Use descriptions for variables
 - Use builtin formatting `terraform fmt`
 - Do not publish sensitive information

### Screenshot of Description change in github repo
![Screenshot of vagrant1 running](screenshots/tf1.jpg)

### Screenshot of branch protection rule applied:
![Screenshot of vagrant1 running](screenshots/tf2.jpg)