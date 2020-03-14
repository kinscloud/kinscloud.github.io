#!/bin/bash
#********************************************************************
#Author: kin
#QQ： 
#Date： 2020-01-01
#FileName： 
#URL： 
#Description： 
#********************************************************************
#设置阿里云镜像为本地yum源
#清空防火墙配置,关闭selinux
sed -i '/^SELINUX=/c\SELINUX=disabled' /etc/selinux/config
#临时关闭
setenforce 0
iptables -F
sh yum-ali.sh
#安装epel
yum install epel-release -y
#安装基础软件
yum install -y make cmake gcc gcc-c++
#安装制作yum源需要的一些软件
yum install -y pcre-devel zlib-devel  openssl openssl-devel createrepo yum-utils
#安装nginx
yum install nginx -y
#修改nginx配置文件
sed -i '42c \\troot\t\t/opt/yum/centos/7/os/epel/;' /etc/nginx/nginx.conf
sed -i '48i \\t\tautoindex on;\n\t\tautoindex_exact_size off;\n\t\tautoindex_localtime on;\n\t\tindex index.html;' /etc/nginx/nginx.conf
expand /etc/nginx/nginx.conf > /tmp/nginx.conf
mv -f /tmp/nginx.conf /etc/nginx/nginx.conf
#root /opt/yum/centos/7/os/epel/;
#location / {
#	autoindex on;
#	autoindex_exact_size off;
#	autoindex_localtime on;
#	index index.html;
#}
systemctl start nginx
systemctl enabled nginx

#创建索引
mkdir -p /opt/yum/centos/7/os/epel/
createrepo /opt/yum/centos/7/os/epel/
#将epel源同步到本地/opt/yum/centos/7/os/中
reposync -r epel -p /opt/yum/centos/7/os/
#设置定时任务运行本地源更新yum_update.sh
echo '0 2 * * 3 /bin/sh /root/yum-local-update.sh'>> /var/spool/cron/root
#更新索引
createrepo --update /opt/yum/centos/7/os/epel/
#在测试服务器上编写repo文件
cat > /etc/yum.repos.d/local-7.repo <<EOF
[local]
name=centos-local
baseurl=http://192.168.1.89/
enabled=1
gpgcheck=0
EOF
#清理缓存数据
yum clean all && yum makecache


