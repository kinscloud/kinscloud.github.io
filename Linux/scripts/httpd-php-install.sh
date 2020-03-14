#!/bin/bash
#********************************************************************
#Author: kin
#QQ： 
#Date： 2020-01-01
#FileName： 
#URL： 
#Description： 
#********************************************************************

yum install httpd -y
#修改配置文件，支持多个虚拟主机文件
sed -i '$a#Virtual hosts' /etc/httpd/conf/httpd.conf
sed -i '$aInclude conf/extra/httpd-vhosts.conf' /etc/httpd/conf/httpd.conf
#增加主机配置文件
mkdir -p /etc/httpd/conf/extra/
mkdir -p /var/www/html/testvhost
cat > /etc/httpd/conf/extra/httpd-vhosts.conf << EOF
#多个虚拟主机配置多少VirtualHost节点
<VirtualHost *:80>
DocumentRoot "/var/www/html/testvhost"
ServerName www.testvhost.org
<Directory "/var/www/html/testvhost">
Options FollowSymLinks ExecCGI
AllowOverride All
Order allow,deny
Allow from all
Require all granted
</Directory>
</VirtualHost>
EOF
echo "This is a test vhost page" >> /var/www/html/testvhost/index.html
echo "127.0.0.1 www.testvhost.org" >> /etc/hosts

#安装php与mysql支持
yum -y install php php-devel php-mysql php-fpm
#安装常用PHP模块
yum install -y php-gd php-ldap php-odbc php-pear php-xml php-xmlrpc php-mbstring php-snmp php-soap curl curl-devel php-bcmath gcc
echo -e "<?php\nphpinfo();\n?>" > /var/www/html/testvhost/info.php

systemctl start httpd
systemctl enable httpd


#可选装mysql,推荐装在其它机器上
#sh mysql-install.sh
#可选装Discuz
#wget http://222.187.232.155:8066/soft/1202/Discuz_X3.2_SC_UTF8_veryhuo.com.zip
#将upload文件夹内所有内容存入网站根目录，根目录及子目录
#chown -Rf apache:apache .
#chmod -Rf 755 . 