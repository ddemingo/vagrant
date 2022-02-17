# Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com/) ...

## Create a virtual machine

Create a ubuntu server virtual machine with [Vagrant](vagrant.md), using ubuntu project:

```sh
$ vagrant up
```

Echo the result of `vagrant ssh-config` into your ssh config file, so you just run `ssh ubuntu` from anywhere in your system, where `ubuntu` is the name of the VM.

```sh
$ vagrant ssh-config >> ~/.ssh/config
$ ssh ubuntu
(vagrant) $ 
```

## Remote SSH Extension

You can then use the Visual Studio Code [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) extension to ssh into the Vagrant VM and edit files and do remote development. Simply `CMD-SHIFT-P` then "Remote-SSH: Connect to Host..." and the ssh .config entry you just added is automatically listed - you simply select it and voila, vscode connects to your remote vagrant vm!