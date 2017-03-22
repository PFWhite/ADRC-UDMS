Creating the Test VM With Vagrant
=================================

Purpose
-------

The "vagrant" folder was created with the goal of making testing `REDCap <http
://project-redcap.org/>`__ and REDCap extensions as easy as possible.  The
root folder contains the `Vagrantfile <Vagrantfile>`__ which
allows you to start a virtual machine capable of running the `REDCap software
<http://http://www.project-redcap.org>`__.  This virtual machine will install
Apache and MySQL software without any user intervention.  If provided with a
the REDCap binaries in the form of a redcap*.zip file Vagrant will install and
configure REDCap as well.

There are a few important things to note before proceeding with running
RED-I to import data into a sample REDCap project:

-  You have to obtain the REDCap software from http://project-redcap.org/ if there isn't already a redcap*.zip in your repo.
-  You have to install the **Vagrant** software
-  You have to install the **Virtual Box** software or another virtual machine provider.  For this discussion we will assume Virtual Box is the virtual machine provider for Vagrant.
-  You have to install the vagrant-hostsupdater plugin
-  You have to install the vagrant-env plugin
-  You have to install the vagrant-triggers plugin

Steps
-----

1. Install Vagrant and Virtual Box
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On a Linux machine run:

::

  sudo apt-get install vagrant
  sudo apt-get install virtualbox

On a Mac OSX machine:

-  Download and install vagrant from
   https://www.vagrantup.com/downloads.html
-  Download and install the latest virtual box from
   http://download.virtualbox.org/virtualbox/

On Mac OSX users using brew can install these packages using brew cask:

::

  brew cask install virtualbox
  brew cask install vagrant


2. Install Vagrant plugins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vagrant will need a few plugins for this VM.  On any platform:

::

  vagrant plugin install vagrant-hostsupdater
  vagrant plugin install vagrant-env
  vagrant plugin install vagrant-triggers

For more details about Vagrant software you can go to
`why-vagrant <https://docs.vagrantup.com/v2/why-vagrant/>`__ page.


3. Get your REDCap zip file
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If it's not already provided in this repo, you must obtain a copy of the REDCap
software from http ://project-redcap.org/.  Save the file with its default
name to the root of this repository.  This ensures that the provisioning
script `bootstrap.sh <bootstrap.sh>`__ script can extract the files to the
virtual machine path "**/var/www/redcap**\ ".

If you put multiple redcap*.zip files in the vagrant folder, the provisioning
script will use the one with the highest version number.

4. Start the VM
~~~~~~~~~~~~~~~

Follow this procedure to start the REDCap VM:

::

   # must be in the root directory of this repository
   vagrant up

Vagrant will instantiate and provision the new VM. The initial download of the
box file is slow, but this need happen only occur once.  Vagrant will cache
the box file indefinitely.  With the box file downloaded, the REDCap VM can be
built from scratch in 2-3 minutes.  If it completes successfully you should a
message like this at the end of the log:

::

    ==> default: Checking if redcap application is running...
    ==> default:      <b>Welcome to REDCap!</b>
    ==> default: Please try to login to REDCap as user 'admin' and password: 'password'

The REDCap web application should be accessible in the browser at http://hcvtargetrc.dev/redcap/

The REDCap instance will be setup with the sample projects that shipped with
that REDCap zip file.


5. Verify the VM is running via the console
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also verify the virtual machine is working properly by accessing it
at the console using:

::

   vagrant ssh

This will connect you to a shell on the virtual machine.

You can check the REDCap server from the console with the command ``check_redcap``.  You will see output like this if it is running correctly:

::

      vagrant@redcap:~$ check_redcap
            <b>Welcome to REDCap!</b>

The REDCap VM you connect to when you do ``vagrant ssh` is a Debian Linux 8.2 VM.
You will connect as user ``vagrant``.  You can sudo to root without a password.
The root of the git repository is mounted within the VM at ``/vagrant``.
Any changes you make to the /vagrant folder from the VM will be immediately
reflected in the host in the root of ther repo and vice versa.

As with any ssh session, type ``exit`` when you are done at the shell.
