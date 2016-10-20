# /bin/bash

# install ansible
# sudo apt install -y software-properties-common
# sudo apt-add-repository ppa:ansible/ansible
sudo apt update
sudo apt install -y python-simplejson
sudo apt install -y ansible

# provision by ansible
pushd ~/sync/ansible
ansible-playbook -i hosts site.yml --connection=local
popd

echo ''
echo 'Provision Done!'
echo ''