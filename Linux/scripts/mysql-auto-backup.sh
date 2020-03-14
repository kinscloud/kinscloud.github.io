#!/bin/bash
#********************************************************************
#Author: kin
#QQ： 
#Date： 2020-01-01
#FileName： 
#URL： 
#Description： 
#********************************************************************
BAK_DIR="/data/backup/mysql/`date +%Y-%m-%d`"
MYSQLDB="test"
MYSQLUSER="root"
MYSQLPW="1QAZ@wsx123"

if [ $UID -ne 0 ]; then
	echo "This script must use the root user!!!"
	sleep 2
	exit 0
fi
if [ ! -d $BAK_DIR ]; then
	mkdir -p $BAK_DIR
fi

/usr/bin/mysqldump -u$MYSQLUSER -p$MYSQLPW -d $MYSQLDB > $BAK_DIR/test_db.sql
echo "The mysql backup successfully"