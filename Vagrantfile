# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/xenial64"

  config.vm.network "private_network", ip: "192.168.56.10"

  config.vm.synced_folder ".", "/home/ubuntu/sync", type: "virtualbox"

  config.vm.provider "virtualbox" do |vb|
    # vb.gui = true # if you use emulator, activate this line.
    vb.cpus = 1
    vb.memory = 4096
    vb.customize ["storageattach", :id, "--storagectl", "IDE", "--port", 0, "--device", 1, "--type", "dvddrive", "--medium", "emptydrive"] # add CDROM device.
    vb.customize ["modifyvm", :id, "--usb", "on"]
    vb.customize ["modifyvm", :id, "--usbehci", "on"] # needs Extension Pack
    vb.customize ['usbfilter', 'add', '0', '--target', :id, '--name', 'Android', '--vendorid', '0x18d1'] # USB filter for Google Inc.
  end
  
  config.vm.provision "shell", privileged: false, path: "provision.sh"
end
