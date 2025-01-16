#!/bin/bash
if [ $(whoami) = "root" ]
then
    apt update
    apt full-upgrade -y
    apt autoremove -y
    apt install -y htop tree vlc zsh python3-netifaces
    wget https://raw.githubusercontent.com/desinfectuser/autoinstall/main/ubu2404matu.py -q -O /tmp/ubu2404matu.py
    wget https://raw.githubusercontent.com/desinfectuser/autoinstall/main/grub -q -O /tmp/grub
    python3.12 /tmp/ubu2404matu.py
else
  pkexec "$0" "$@"
fi
