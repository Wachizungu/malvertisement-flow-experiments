AdFisher
=========

AdFisher is a tool for running Automated Experiments on Personalized Ad Settings. 

Requirements
-----------
Installation instructions:
```pipenv install```
pipenv shell
import nltk
nltk.download()
exit()
deactivate


After installing the requirements, please visit **/examples** to view how to run sample scripts. 


Architecture
-----------

AdFisher has two parts - an **examples** folder and a **core** folder. **examples** contains some example scripts to run experiments in addition to some test logs generated from our past experiments. The **core** comprises of several modules which setup the experiments and perform the analyses on the collected data. 

Quick Start
-----------
This repository can be used with [Vagrant](https://www.vagrantup.com/) to quickly get a virtual machine with all the necessary dependencies described above installed.  This can be useful for development and testing experiments.

1. git clone https://github.com/tadatitam/info-flow-experiments
2. vagrant up

This defaults to an Ubuntu Server 14.04 LTS (Trusty Tahr) build and will have the AdFisher source directory synced to /vagrant on the virtual machine. You can SSH into this machine with `vagrant ssh`.

Troubleshooting
-----------
1. If you see an error saying the browser failed to start, try switching *headless* from False to True (check README at AdFisher/examples for more details).
2. With headless set to True, the virtual display buffer tool (Xvfb) sometimes throws an error 
```RuntimeError: Xvfb did not start```
However, this occurs rarely. We get around this problem by collecting data from many many instances, so that these rare failures can be treated as noise.







