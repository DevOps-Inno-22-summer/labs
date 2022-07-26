# -*- mode: ruby -*-
# vi: set ft=ruby :

servers=[
  {
    :hostname => "DevOps1",
    :ip => "192.168.56.10",
    :box => "ubuntu/trusty64",
    :ram => 2048,
    :cpu => 2
  },
  {
    :hostname => "DevOps2",
    :ip => "192.168.56.11",
    :box => "ubuntu/trusty64",
    :ram => 2048,
    :cpu => 2
  },
  {
    :hostname => "DevOps3",
    :ip => "192.168.56.12",
    :box => "ubuntu/trusty64",
    :ram => 2048,
    :cpu => 2
  }
]

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|

  servers.each do |machine|
    config.vm.define machine[:hostname] do |node|
      node.vm.box = machine[:box]
      node.vm.hostname = machine[:hostname]
      node.vm.network "private_network", ip: machine[:ip]
      node.vm.provider "virtualbox" do |vb|
        vb.customize ["modifyvm", :id, "--memory", machine[:ram]]
      end
    end
  end

#   config.vm.box = "ubuntu20"
#
#    config.vm.provider "virtualbox" do |vb|
#        vb.memory = "4096"
#   end
#
#   config.vm.network "forwarded_port", guest: 8000, host: 8080
#   # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
#   # config.vm.network "private_network", ip: "192.168.56.100"
#   # config.vm.network "public_network"
#   config.vm.synced_folder "./data", "/vagrant_data", :nfs => { :mount_options => ["dmode=777", "fmode=666"] }
#
#   # Enable provisioning with a shell script. Additional provisioners such as
#   # Ansible, Chef, Docker, Puppet and Salt are also available. Please see the
#   # documentation for more information about their specific syntax and use.
#   config.vm.provision "docker" do |d|
#     d.pull_images "nyahonk/devops_course:latest"
#     d.run "nyahonk/devops_course:latest"
#   end
end
