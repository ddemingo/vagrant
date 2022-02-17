# README

## Install

Download this python script to install `vagrant` locally ():

> [install-vagrant.py](https://raw.githubusercontent.com/optersoft/vagrant/main/install-vagrant.py)



And execute it:

```sh
$ chmod a+x install-vagrant.py
$ ./install-vagrant.py
```

Test that `vagrand` works:

```sh
$ vagrant
Usage: vagrant [options] <command> [<args>]
```

## Up

Create a ubuntu server virtual machine:

```sh
$ curl https://raw.githubusercontent.com/optersoft/vagrant/main/Vagrantfile -o Vagrantfile
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