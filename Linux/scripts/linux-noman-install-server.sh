#!/bin/bash
#********************************************************************
#Author: kin
#QQ： 
#Date： 2020-01-01
#FileName： 
#URL： 
#Description： 
#********************************************************************

#主机IP：192.168.1.88，以实际为准，虚拟机安装报错可调大内存，不然空间不足
#清空防火墙配置,关闭selinux
sed -i '/^SELINUX=/c\SELINUX=disabled' /etc/selinux/config
#临时关闭
setenforce 0
iptables -F
#首先挂载好光盘镜像，
mkdir -p /media/cdrom
mount /dev/cdrom /media/cdrom
#配置DHCP，为客户端主机分配可用的IP地址
yum install dhcp -y
rm -f /etc/dhcp/dhcpd.conf
cat > /etc/dhcp/dhcpd.conf <<EOF
allow booting;
allow bootp;
ddns-update-style interim;
ignore client-updates;
subnet 192.168.1.0 netmask 255.255.255.0 {
        option subnet-mask      255.255.255.0;
        option domain-name-servers  192.168.1.88;
        range dynamic-bootp 192.168.1.100 192.168.1.200;
        default-lease-time      21600;
        max-lease-time          43200;
        next-server             192.168.1.88;
        filename                "pxelinux.0";
}
EOF
systemctl restart dhcpd
systemctl enable dhcpd
#配置tftp-server，为客户端主机提供引导及驱动文件
yum install xinetd tftp-server -y
sed -i '/disable/{s/yes/no/}' /etc/xinetd.d/tftp 
systemctl restart xinetd
systemctl enable xinetd
#配置SYSLinux服务程序，复制/usr/share/syslinux目录中的引导文件
yum install syslinux -y
cd /var/lib/tftpboot
cp /usr/share/syslinux/pxelinux.0 .
cp /media/cdrom/images/pxeboot/{vmlinuz,initrd.img} .
cp /media/cdrom/isolinux/{vesamenu.c32,boot.msg} .
mkdir pxelinux.cfg
cp /media/cdrom/isolinux/isolinux.cfg pxelinux.cfg/default
#修改配置文件两行参考如下
sed -i '1c default linux' pxelinux.cfg/default
sed -i '64c append initrd=initrd.img inst.stage2=ftp://192.168.1.88 ks=ftp://192.168.1.88/pub/ks.cfg quiet' pxelinux.cfg/default
#配置VSFtpd服务程序，确保将光盘镜像顺利传输给客户端主机
yum install vsftpd -y
systemctl restart vsftpd
systemctl enable vsftpd
cp -r /media/cdrom/* /var/ftp
#创建KickStart应答文件,可按自己需求修改
cp ~/anaconda-ks.cfg /var/ftp/pub/ks.cfg
chmod +r /var/ftp/pub/ks.cfg
sed -i '5c url --url=ftp://192.168.1.88' /var/ftp/pub/ks.cfg 
#sed -i '25c timezone Asia/Shanghai --isUtc' /var/ftp/pub/ks.cfg 
sed -i '30c clearpart --all --initlabel' /var/ftp/pub/ks.cfg 