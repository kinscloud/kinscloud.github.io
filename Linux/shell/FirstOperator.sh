#/bin/bash

#设置时区并同步时间
ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
if ! crontab -l | grep ntpdate &>/dev/null ; then
	(echo "* 1 * * * ntpdate time.windows.com > /dev/null 2>&1";crontab -l) | crontab
fi
#禁用selinux
setenforce 0
sed -i '/^SELINUX=/c\SELINUX=disabled' /etc/selinux/config

#清空防火墙默认策略
sys_ver=`cat /etc/redhat-release | awk -F '.' '{print $1}'| awk '{print $4}'`
if [ $sys_ver -eq 6 ];then
	service iptables stop
	/sbin/chkconfig --live 35 iptables off
elif [ $sys_ver -eq 7 ];then
    systemctl stop firewalld
	systemctl disable firewalld
fi

#历史命令显示操作时间
cat >> /etc/bashrc << EOF
export HISTSIZE=3000
export HISTTIMEFORMAT="%F %T `whoami`"
export PROMPT_COMMAND="history -a; $PROMPT_COMMAND"
unset HISTCONTROL
EOF
#SSH超时时间
if ! grep "TMOUT=600" /etc/profile &>/dev/null; then
	echo "export TMOUT=600" >> /etc/profile
fi
#禁止root远程登录
#sed -i 's/#PermitRootLogin yes/PermitRootLogin no/g' /etc/ssh/sshd_config

#禁止定时任务发送邮件
sed -i 's/^MAILTO=root/MAILTO=""/' /etc/crontab

#设置最大打开文件数
cat >> /etc/security/limits.conf <<EOF
* soft nproc 65535
* hard nproc 65535
* soft nofile 65535
* hard nofile 65535
EOF
echo 3865161233 > /proc/sys/fs/file-max
echo "ulimit -SHn 65535" >> /etc/rc.local

#减少Swap使用
echo "0" > /proc/sys/vm/swappiness

#系统内核参数优化
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
#安装系统性能分析工具及其它
yum install gcc make autoconf vim sysstat net-tools iostat iftop iotp lrzsz -y