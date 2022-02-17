# README

## Install

Download this python script to install `vagrant` locally ():


And execute it:

```sh
$ chmod a+x install-vagrant.py
$ ./install-vagrant.py
$ rm install-vagrant
```

Test that `vagrand` works:

```sh
$ vagrant
Usage: vagrant [options] <command> [<args>]
```

## Up

Create a ubuntu server virtual machine:

```sh
$ wget https://raw.githubusercontent.com/optersoft/vagrant/Vagrantfile
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