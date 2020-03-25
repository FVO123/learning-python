# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = '2'.freeze

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.define 'development', primary: true do |development|
    development.vm.box = 'bento/debian-9.5'

    development.vm.hostname = 'learning-python-vagrant'

    development.vm.provision 'ansible' do |ansible|
      ansible.playbook = 'configuration-management/ansible/playbook.yml'
      ansible.compatibility_mode = '2.0'
      ansible.extra_vars = { ansible_python_interpreter: '/usr/bin/python3' }
    end

    development.cache.scope = :machine if Vagrant.has_plugin?('vagrant-cachier')
  end
end
