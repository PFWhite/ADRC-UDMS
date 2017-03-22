# REDCap VM for the ADRC UDMS

## Overview

This directory contains a Vagrant VM used to testing and development work on the ADRC UDMS. It is based on the VM defined in CTS-IT's redcap_deployment repo.

## Requirements

This VM requires that Vagrant, VirtualBox, vagrant-hostsupdater plugin, vagrant-env and vagrant-triggers plugin be installed on the host system.

See [Creating the Test VM With Vagrant](docs/creating_the_test_vm_with_vagrant.rst) for details on how to meet those requirements.

## Using the Development Environment

With the above requirements and configuration completed, start the VM with the command

    vagrant up

After about two minutes, the VM should be accessible at [http://udmsrc.dev/redcap/](http://udmsrc.dev/redcap/) and at [https://udmsrc.dev/redcap/](https://udmsrc.dev/redcap/) (or whatever URL _URL\_OF\_DEPLOYED\_APP_ is set to in _.env_)

