#!/bin/bash
#********************************************************************
#Author: kin
#QQ： 
#Date： 2020-01-01
#FileName： 
#URL： 
#Description： 
#********************************************************************
yum install -y samba
smbpasswd -a root
mkdir /home/share
mv /etc/samba/smb.conf /etc/samba/smb.conf.bak
cat > /etc/samba/smb.conf <<EOF
[global]
security=user
[phproot]
comment=This is a cloud driver
browseable = yes
path=/var/www/html/
create mask = 0700
directory mask = 0700
valid users = root
force user = root
force group = root
public = yes
available = yes
writable = yes
EOF
systemctl restart smb
systemctl enable smb