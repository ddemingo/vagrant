# README

## Install

Download this python script to install `vagrant` locally (Save Link as ...):

> [install-vagrant.py](https://raw.githubusercontent.com/ddemingo/vagrant/main/install-vagrant.py)



And execute it:

```sh
$ chmod a+x install-vagrant.py
$ ./install-vagrant.py
```

Close the terminal and open again.

Test that `vagrand` works:

```sh
$ vagrant
Usage: vagrant [options] <command> [<args>]
```

## Up

Create a ubuntu server virtual machine:

```sh
$ curl https://raw.githubusercontent.com/ddemingo/vagrant/main/Vagrantfile -o Vagrantfile
$ vagrant up
```

Vagrant will create a directory called `.vagrant` in the same path where the `Vagrantfile` is located, where it stores information and boxes states. 

```sh
$ ls -la
drwxrwxr-x ... .vagrant
```

Log into the virtual machine:

```sh
$ vagrant ssh
```

To halt vm:

```sh
$ vagrant halt
```