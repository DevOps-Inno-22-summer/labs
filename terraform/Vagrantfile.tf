# -*- mode: ruby -*-
# vi: set ft=ruby :
# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
   # Specifying the box we wish to use
    config.vm.box = "hashicorp/bionic64"
   # Iterating the loop for three times
   (1..3).each do |i|
      # Defining VM properties
      config.vm.define "python_elena#{i}" do |node|
         # Specifying the provider as VirtualBox and naming the VM's
         config.vm.provider "virtualbox" do |vm_node|
         end
      end
   end
  end