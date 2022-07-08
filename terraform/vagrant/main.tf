resource "vagrant_vm" "my_vagrant_vm" {
  vagrantfile_dir = "."
  get_ports       = true
}