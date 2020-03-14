#!/bin/bash
#********************************************************************
#Author: kin
#QQ： 
#Date： 2020-01-01
#FileName： 
#URL： 
#Description： 
#********************************************************************
#安装JDK
yum install -y java
#添加Jenkins库到yum库
wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat/jenkins.repo
rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key
yum install -y jenkins
#wget http://pkg.jenkins-ci.org/redhat-stable/jenkins-2.204.2-1.1.noarch.rpm
#rpm -ivh jenkins-2.204.2-1.1.noarch.rpm
#配置jenkis的端口,默认8080，不冲突不改
sed -i '/^JENKINS_PORT/s/8080/8888/g' /etc/sysconfig/jenkins
#访问不了google的修改
sed -i 's/www.google.com/www.baidu.com/g' /var/lib/jenkins/updates/default.json
systemctl restart jenkins 
#systemctl enable jenkins 
chkconfig jenkins on
#查看初始密码
cat /var/lib/jenkins/secrets/initialAdminPassword 
#登录
#http://127.0.0.1:8080
#安装maven
#wget http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo
#yum -y install apache-maven
yum -y install maven
mvn -v