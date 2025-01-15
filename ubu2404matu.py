#!/usr/bin/env python3.12
import os
import sys
import netifaces

if os.getuid() != 0:
    print("Fehlende Root-Rechte!")
    exit(1)

hostname = input("Neuer Hostname: ")

if hostname == "":
    print("Ungültiger Hostname!")
    exit(1)

with open("/etc/hostname","w") as file:
    file.write(hostname)

filename = "/media/felix/STORAGE/" + hostname

with open(filename, "w") as outfile:
    sys.stdout = outfile
    print(hostname)
    print("Mac-Adresse(n):")
    for link in netifaces.interfaces():
        print(link, ":", netifaces.ifaddresses(link)[netifaces.AF_LINK])

with open("/etc/default/grub", "w") as grubconf_alt:
    with open("/tmp/grub", "r") as grubconf_neu:
        grubconf_alt.write(grubconf_neu.read())

os.system("update-grub")
