#!/bin/bash
#********************************************************************
#Author: kin
#QQ： 
#Date： 2020-01-01
#FileName： 
#URL： 
#Description： 
#********************************************************************

sed -i '/^#UseDNS/s/#UseDNS yes/UseDNS no/' /etc/ssh/sshd_config
sed -i '/^#GSSAPIAuthentication/s/GSSAPIAuthentication yes/GSSAPIAuthentication no/' /etc/ssh/sshd_config
systemctl restart sshd