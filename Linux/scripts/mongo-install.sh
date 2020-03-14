#!/bin/bash
#********************************************************************
#Author: kin
#QQ： 
#Date： 2020-01-01
#FileName： 
#URL： 
#Description： 
#********************************************************************

cat > /etc/yum.repos.d/MongoDB.repo <<EOF
[mongodb-org-3.6]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/\$releasever/mongodb-org/3.6/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-3.6.asc
EOF

yum makecache
yum -y install mongodb-org

systemctl start mongod.service
systemctl enable mongod.service



#---------------------------------------------
cd /usr/local/src
curl -O https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-3.6.4.tgz

tar -zxvf mongodb-linux-x86_64-3.6.4.tgz

mv mongodb-linux-x86_64-3.6.4 /usr/local/mongodb

export PATH=/usr/local/mongodb/bin:$PATH；

cd /usr/local/mongodb
mkdir data
cd data
mkdir logs
mkdir db

cat > mongodb.conf << EOF
#端口号
port = 27017
#数据目录
dbpath = /usr/local/mongodb/data/db
#日志所在目录
logpath = /usr/local/mongodb/data/logs/mongo.log
#后台运行
fork = true
#日志输出方式
logappend = true
EOF

cd /usr/local/mongodb
mongod -f /usr/local/mongodb/data/mongodb.conf