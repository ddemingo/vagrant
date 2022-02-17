Vagrant.configure("2") do |config|

    config.vm.define :ubuntu do |ubuntu|
      ubuntu.vm.box = "peru/ubuntu-20.04-server-amd64"
      ubuntu.vm.network :forwarded_port, guest: 80, host: 8080
      ubuntu.vm.network "private_network", ip: "192.168.50.4"
  
      ubuntu.vm.provider "virtualbox" do |vm|
        vm.name = "ubuntu"
        vm.memory = "4096"
        vm.cpus = Etc.nprocessors
      end

      ubuntu.vm.provider :libvirt do |vm|
        vm.memory = "4096"
        vm.cpus = Etc.nprocessors
        vm.qemu_use_session = false
        # vm.cpu_mode = "host-passthrough"
      end
  
    end
  
end
  