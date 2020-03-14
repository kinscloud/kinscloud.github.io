#!/bin/bash
#********************************************************************
#Author: kin
#QQ： 
#Date： 2020-01-01
#FileName： 
#URL： 
#Description： 
#********************************************************************

#下载mysql源安装包
wget http://dev.mysql.com/get/mysql57-community-release-el7-10.noarch.rpm
#安装mysql源
yum localinstall -y mysql57-community-release-el7-10.noarch.rpm

yum install -y mysql-community-server    
systemctl start mysqld                
systemctl enable mysqld     

#启动成功后可以查看初始化密码随机生成的
password=`cat /var/log/mysqld.log | grep "temporary password"  | awk -F':' '{print $NF}' | sed 's/ //'`
mysqlcmd="mysql -uroot -p$password"
#登录MySQL修改mysql用户密码
$mysqlcmd  --connect-expired-password  -e "ALTER USER 'root'@'localhost' IDENTIFIED BY '1qaz@WSX123'";
#远程设置
mysqlcmd="mysql -uroot -p1qaz@WSX123"
$mysqlcmd -e "use mysql; update user set host='%' where user='root';"
#授权用户名的权限，赋予任何主机访问数据的权限
$mysqlcmd -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'%'WITH GRANT OPTION;"
$mysqlcmd -e "FLUSH PRIVILEGES;"
