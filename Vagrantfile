Vagrant.configure("2") do |config|

    config.vm.define :ubuntu do |ubuntu|
      ubuntu.vm.box = "peru/ubuntu-20.04-server-amd64"
  
      ubuntu.vm.provider "virtualbox" do |vm|
        vm.name = "ubuntu"
        vm.memory = "4096"
        vm.cpus = 2
      end
  
    end
  
end
  