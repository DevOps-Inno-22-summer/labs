# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/focal64"

   config.vm.provider "virtualbox" do |vb|
       vb.memory = "1024"
  end

#   config.vm.network "forwarded_port", guest: 80, host: 8080
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
  config.vm.network "private_network", ip: "192.168.56.100"
  # config.vm.network "public_network"
  config.vm.synced_folder "./data", "/vagrant_data", :nfs => { :mount_options => ["dmode=777", "fmode=666"] }

  # Enable provisioning with a shell script. Additional provisioners such as
  # Ansible, Chef, Docker, Puppet and Salt are also available. Please see the
  # documentation for more information about their specific syntax and use.
  config.vm.provision "docker" do |d|
    d.pull_images "nyahonk/devops_course:latest"
    d.run "nyahonk/devops_course:latest"
  end
end
