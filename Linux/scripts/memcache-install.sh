#!/bin/bash
#********************************************************************
#Author: kin
#QQ： 
#Date： 2020-01-01
#FileName： 
#URL： 
#Description： 
#********************************************************************

yum install memcached -y
#使用默认值启动
systemctl start memcached
#自定义启动多个实例 -m 缓存最大内存 -p 端口号 -d 后台运行 -c 最大并发连接数
memcached -m 16m -p 11211 -d -u root -c 8192
memcached -m 16m -p 11212 -d -u root -c 8192