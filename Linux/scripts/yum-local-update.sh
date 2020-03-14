#!/bin/bash
#********************************************************************
#Author: kin
#QQ： 
#Date： 2020-01-01
#FileName： 
#URL： 
#Description： 
#********************************************************************

datetime=`date +"%Y-%m-%d"`
exec > /var/log/centosrepo.log
reposync -d -r epel -p /opt/yum/centos/7/os
if [ $? -eq 0 ];then
    createrepo --update  /opt/yum/centos/7/os/epel
    #每次添加新的rpm时,必须更新索引信息
echo "SUCESS: $datetime epel update successful"
else
echo "ERROR: $datetime epel update failed"
fi