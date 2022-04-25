#!/bin/bash
sudo raspi-config nonint do_boot_behaviour B1
sudo raspi-config nonint do_i2c 0
sudo raspi-config nonint do_change_locale en_US.UTF-8
sudo apt update
sudo apt -y upgrade
sudo apt -y install zsh lv i2c-tools python3-smbus python3-pip
pip3 install -r requirements.txt