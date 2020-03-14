#!/bin/bash
#********************************************************************
#Author: kin
#QQ： 
#Date： 2020-01-01
#FileName： 
#URL： 
#Description： 
#********************************************************************

export MemcachedIp=$1
export MemcachedPort=$2
export NcCmd="nc $MemcachedIp $MemcachedPort"
export MD5=44be204e373cb7cb6d7c30ed11ab4658

Tips(){
	echo "$0 MemcachedIp MemcachedPort"
	exit 3
}
[ $# -ne 2 ] && Tips
printf "set $MD5 0 0 3\r\nkin\r\n" | $NcCmd > /dev/null 2>&1
if [ $? -eq 0 ];then
	if [ `printf "get $MD5\r\n" | $NcCmd | grep kin | wc -l` -eq 1 ];then
		echo "Memcached status is ok"
		printf "delete $MD5\r\n" | $NcCmd > /dev/null 2>&1
		exit 0
	else
		echo "Memcached status is error."
		exit 2
	fi
else
	echo "Memcached status is error."
	exit 2
fi