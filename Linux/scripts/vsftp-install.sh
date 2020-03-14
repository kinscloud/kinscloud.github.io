#!/bin/bash
#********************************************************************
#Author: kin
#QQ： 
#Date： 2020-01-01
#FileName： 
#URL： 
#Description： 
#********************************************************************

cat <<EOF
选择VSFTP的安装模式：
1.匿名模式
2.本地用户模式
3.虚拟用户模式
EOF
read -p "请选择（1，2，3）:" n
expr $n + 1 &> /dev/null
if [ $? -ne 0 ] ; then
    echo "只能输入数字进行选择"
    exit 1
fi
anonymous(){
	#匿名模式
	#修改配置文件
    sed -i '$a\anon_umask=022\nanon_upload_enable=YES\nanon_mkdir_write_enable=YES\nanon_other_write_enable=YES' /etc/vsftpd/vsftpd.conf
	chown -Rf ftp /var/ftp/pub
	systemctl start vsftpd
}
local(){
	#本地用户模式
	#修改配置文件
	sed -i '/^anonymous_enable=/c\anonymous_enable=NO' /etc/vsftpd/vsftpd.conf
	#允许root用户登录
	sed -i '/^root/d' /etc/vsftpd/user_list 
	sed -i '/^root/d' /etc/vsftpd/ftpusers
	
	systemctl start vsftpd
	
}
vuser(){
	#虚拟用户模式
	#增加ftp用户
	cd /etc/vsftpd/
	echo -e "kin\n000000" > vuser.list
	db_load -T -t hash -f vuser.list vuser.db
	chmod 600 vuser.db
	rm -f vuser.list
	#增加映射用户ftpuser
	useradd -d /var/ftproot -s /sbin/nologin ftpuser
	chmod -Rf 700 /var/ftproot/
	#新建一个用于虚拟用户认证的PAM文件vsftpd.vu
	echo "auth       required     pam_userdb.so db=/etc/vsftpd/vuser" > /etc/pam.d/vsftpd.vu
	echo "account    required     pam_userdb.so db=/etc/vsftpd/vuser" >> /etc/pam.d/vsftpd.vu
	#修改配置文件
	sed -i '/^anonymous_enable=/c\anonymous_enable=NO' /etc/vsftpd/vsftpd.conf
	sed -i '/^pam_service_name=/c\pam_service_name=vsftpd.vu' /etc/vsftpd/vsftpd.conf
	sed -i '$a\guest_enable=YES\nguest_username=ftpuser\nallow_writeable_chroot=YES'  /etc/vsftpd/vsftpd.conf
	#多用户不用权限在配置文件中，目录里是以用户名为名称的配置文件
	mkdir /etc/vsftpd/vusers_dir/
	echo -e "write_enable=YES\nanon_world_readable_only=YES\nanon_upload_enable=YES\nanon_mkdir_write_enable=YES\nanon_other_write_enable=YES\nvirtual_use_local_privs=YES" > /etc/vsftpd/vusers_dir/kin
	sed -i '$a\user_config_dir=/etc/vsftpd/vusers_dir'  /etc/vsftpd/vsftpd.conf
	
	systemctl start vsftpd
}
yum install vsftpd -y
iptables -F
systemctl enable vsftpd
case $n in
    1)
        anonymous
        ;;
    2)
        local
        ;;
    3)
        vuser
        ;;
    *)
        echo "只能选择1，2，3操作"
        exit 1
        ;;
esac

