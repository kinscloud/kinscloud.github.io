yum install -y expect
ssh-keygen -t rsa -P "" -f /root/.ssh/id_rsa
for i in 192.168.1.212 192.168.1.213;do
expect -c "
spawn ssh-copy-id -i /root/.ssh/id_rsa.pub root@$i
        expect {
                \"*yes/no*\" {send \"yes\r\"; exp_continue}
                \"*password*\" {send \"000000\r\"; exp_continue}
                \"*Password*\" {send \"000000\r\";}
        } "
done 