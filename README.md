# Titanium.ubuntu

Titanium CLI on ubuntu/xenial64.

## Getting Started

1. Install Vagrant to your host OS.

  https://www.vagrantup.com/

2. Install vagrant-vbguest plugin.
  ```
  vagrant plugin install vagrant-vbguest
  ```

3. Install VirtualBox Extension Pack.

  https://www.virtualbox.org/

4. Clone this project.

  ```
  git clone https://github.com/m-imaoka/Titanium.ubuntu.git
  ```

5. Move current directory to ProbizmoStudy.

  ```
  cd [Titanium.ubuntu's path]
  ```
6. add inventory file

  ```
  cp ansible/hosts.sample ansible/hosts
  ```
7. Run Vagrant.

  ```
  vagrant up
  ```
8. Reinstall virtualbox guest additions. (optional)

    Insert VBoxGuestAdditions.iso into CD/DVD storage.

  ```
  vagrant ssh
  sudo mount /dev/cdrom /mnt
  sudo /mnt/VBoxLinuxAdditions.run
  exit
  vagrant reload
  ```
9. Provision virtual machine.

  ```
  vagrant provision
  ```
10. Login virtual machine.

  ```
  vagrant ssh
  ```
