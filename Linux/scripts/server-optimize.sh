#!/bin/bash
#********************************************************************
#Author: kin
#QQ： 
#Date： 2020-01-01
#FileName： 
#URL： 
#Description： 
#********************************************************************

## Writes By Tian
## Ver 1.1.0 at 20180705

#关闭 ctrl + alt + del (linux 6.x )
echo "关闭 ctrl + alt + del ......."
sed -i "s/ca::ctrlaltdel:\/sbin\/shutdown -t3 -r now/#ca::ctrlaltdel:\/sbin\/shutdown -t3 -r now/" /etc/inittab
sed -i 's/^id:5:initdefault:/id:3:initdefault:/' /etc/inittab
#linux 7 禁止 ctrl + alt + del
rm -f /usr/lib/systemd/system/ctrl-alt-del.target

#以上根据自己的服务器版本设置服务器

#关闭ipv6
echo "关闭IPv6....."
echo "alias net-pf-10 off" >> /etc/modprobe.conf
echo "alias ipv6 off" >> /etc/modprobe.conf
/sbin/chkconfig --level 35 ip6tables off
echo -e "\033[031m ipv6 is disabled.\033[0m"

#关闭selinux
echo "关闭SElinux......"
sed -i '/^SELINUX=/c\SELINUX=disabled' /etc/selinux/config
#临时关闭
setenforce 0

echo -e "\033[31m The temporary closure of  selinux, if you need,you must reboot.\033[0m"

#关闭防火墙
echo "关闭iptables....."
service iptables stop
/sbin/chkconfig --live 35 iptables off

echo "关闭 firewalld "
systemctl stop firewalld
systemctl disable firewalld

#更新yum源
#yum -y install wget
echo "备份yum源......"
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
#sys_ver=`cat /etc/redhat-release |awk '{print $3}' | awk -F '.' '{print $1}'`
sys_ver=`cat /etc/redhat-release | awk -F '.' '{print $1}'| awk '{print $4}'`
if [ $sys_ver -eq 6 ];then
        wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-6.repo
        yum clean all
        yum makecache
elif [ $sys_ver -eq 7 ];then
        wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo 
        yum clean all
        yum makecache
fi

#安装基础库
echo "安装基础环境和库......"
#yum -y install "Development Tools"
yum -y install lsof lrzsz ntpdate gcc gcc-c++ autoconf libjpeg libjpeg-devel libpng libpng-devel freetype freetype-devel \
                  libxml2 libxml2-devel zlib zlib-devel glibc glibc-devel glib2 glib2-devel bzip2 bzip2-devel ncurses ncurses-devel \
                  curl curl-devel e2fsprogs e2fsprogs-devel krb5-devel libidn libidn-devel  openssl openssl-devel nss_ldap \
                  openldap openldap-devel  openldap-clients openldap-servers libxslt-devel \
                 libevent-devel ntp  libtool-ltdl bison libtool vim-enhanced

## 以下是可选项目

# in `chkconfig --list | awk '{if ($1~/^$/) {exit 0;} else {print $1}}'`; do chkconfig $i off; done
#打开必备启动项目
#for i in {crond,sshd,network,rsyslog};do chkconfig --level 3 $i on;done

#####  设置时区时给出了2个版本的用法，我没有做判断，根据自己的情况注释掉不用的版本 

#设置时区 (linux 6.x)
zone_time(){
#install ntp
yum -y install ntp ntpdate
#time zone
if [ `date +%z` != "+0800" ]; then
     rm -rf /etc/localtime
     ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
cat > /etc/sysconfig/clock << EOF
ZONE="Asia/Shanghai"
UTC=false
ARC=false
EOF
fi
#start ntpd server
/etc/init.d/ntpd start
chkconfig ntpd on
echo "Present time zone:"`date +%z`
echo -e "\033[31m time zone ok \033[0m"
}
#设置时区 (linux 7.x)
zone_7_time(){

# Install ntp
yum -y install ntp ntpdate
# Time zone
if [ `date +%z` != "+0800" ]; then
rm -f /etc/localtime
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
cat > /etc/sysconfig/clock << EOF
ZONE="Asia/Shanghai"
UTC=false
ARC=false
EOF
fi

# Start ntp server
systemctl start ntpd
systemctl enabld ntpd.service
echo "Present time zone:"`date +%z`
echo -e "\033[31m linux 7 time zone ok \033[0m"

}

####### 以上是时区的设置 有2个版本，根据自己的情况做选择。

## 没必要可以不用，美化提示符

#修改Bash提示符字符串
echo "改Bash提示符字符串......"
echo 'PS1="\[\e[37;40m\][\[\e[32;40m\]\u\[\e[37;40m\]@\h \[\e[36;40m\]\w\[\e[0m\]]\\$ "' >> ~/.bashrc
source .bashrc


#更改字符集(linux 6.x 的字符集)
/bin/cp /etc/sysconfig/i18n /etc/sysconfig/i18n.bak
echo 'LANG="en_US.UTF-8"' >/etc/sysconfig/i18n
#linux 7 的字符集 
Character_install(){
#安装中文支持
yum -y install kde-l10n-Chinese
yum -y reinstall glibc-common

sed -i '/^LANG=/c\LANG="zh_CN.UTF-8"' /etc/locale.conf
source /etc/locale.conf
}

#修改文件打开数
echo "修改文件打开数......"
cat >> /etc/security/limits.conf <<EOF
* soft nproc 65535
* hard nproc 65535
* soft nofile 65535
* hard nofile 65535
EOF
echo 3865161233 > /proc/sys/fs/file-max
echo "ulimit -SHn 65535" >> /etc/rc.local
#优化内核参数
echo "优化内核参数....."
sed -i 's/net.ipv4.tcp_syncookies.*$/net.ipv4.tcp_syncookies = 1/g' /etc/sysctl.conf
cat >> /etc/sysctl.conf << ENDF
net.ipv4.ip_forward = 0
net.ipv4.conf.default.rp_filter = 1
net.ipv4.conf.default.accept_source_route = 0
kernel.sysrq = 0
kernel.core_uses_pid = 1
net.ipv4.tcp_syncookies = 1
kernel.msgmnb = 65536
kernel.msgmax = 65536
kernel.shmmax = 68719476736
kernel.shmall = 4294967296
net.ipv4.tcp_max_tw_buckets = 10000
net.ipv4.tcp_sack = 1
net.ipv4.tcp_window_scaling = 1
net.ipv4.tcp_rmem = 4096 87380 4194304
net.ipv4.tcp_wmem = 4096 16385 4194304
net.core.wmem_default = 8388608
net.core.rmem_default = 8388608
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216
net.core.netdev_max_backlog = 262144
net.core.somaxconn = 262144
net.ipv4.tcp_max_orphans = 3276800
net.ipv4.tcp_max_syn_backlog = 262144
net.ipv4.tcp_timestamps = 0
net.ipv4.tcp_synack_retries = 1
net.ipv4.tcp_syn_retries = 1
net.ipv4.tcp_tw_recycle = 1
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_mem = 94500000 915000000 927000000
net.ipv4.tcp_fin_timeout = 1
net.ipv4.tcp_keepalive_time = 30
net.ipv4.ip_local_port_range = 1024 65535
ENDF
sysctl -p

#优化ssh参数
echo "优化ssh....."
sed -i '/^#UseDNS/s/#UseDNS yes/UseDNS no/g' /etc/ssh/sshd_config
#sed -i 's/#PermitEmptyPasswords no/PermitEmptyPasswords no/g' /etc/ssh/sshd_config
#/etc/init.d/sshd restart
systemctl restart sshd

#使历史命令记录下操作时间
cat >> /etc/bashrc << EOF
export HISTSIZE=3000
export HISTTIMEFORMAT="%F %T "
export PROMPT_COMMAND="history -a; $PROMPT_COMMAND"
unset HISTCONTROL
EOF

