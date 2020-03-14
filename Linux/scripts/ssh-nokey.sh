#/bin/bash
PASSWORD=000000
IP_ADDR='192.168.1.201'

. /etc/init.d/functions
if ! [ -f ~/.ssh/id_dsa.pub ];then
   ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa >/dev/null 2>&1
   echo -e "\033[32m======Local=========\033[0m"
   action "Generate the key!"  /bin/true
fi

for i in $IP_ADDR;do
	sshpass -p $PASSWORD ssh-copy-id -i ~/.ssh/id_rsa.pub "-o StrictHostKeyChecking=no" ${i}  >/dev/null 2>&1
    #sshpass -p "1qaz@WSX" ssh-copy-id -i .ssh/id_rsa.pub "-o StrictHostKeyChecking=no shadm1@${i}" >/dev/null @>&1     #版本不同的情况下，有时候这块"-o StrictHostKeyChecking=no shadm1@${i}"  不用加双引号
    if [ $? == 0 ];then
        echo -e "\033[32m=========`ssh $i hostname`==========\033[0m"
        action  "send successful" /bin/true
    else
        echo -e "\033[31m======$i=======\033[0m"
        action  "send failed" /bin/false
    fi
done