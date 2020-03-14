#安装mariadb数据库 
yum -y install mariadb-server mariadb          
#启动mariadb数据库
systemctl start mariadb                                 
#设置开机自启动
systemctl enable mariadb  
#为数据库root用户设置密码                           
mysqladmin -u root password "1qaz@WSX123" 
mysqlcmd="mysql -uroot -p1qaz@WSX123"
#创建zabbix数据库
$mysqlcmd -e "create database zabbix character set utf8 collate utf8_bin;"
#建立一个名为Zabbix的数据库用户
$mysqlcmd -e "grant all privileges on zabbix.* to zabbix@localhost identified by '1qaz@WSX123';"
$mysqlcmd -e "FLUSH PRIVILEGES;"
# 下载zabbix的rpm仓库包
rpm -Uvh https://repo.zabbix.com/zabbix/4.5/rhel/7/x86_64/zabbix-release-4.5-2.el7.noarch.rpm
#启用可选rpms的存储库
#yum-config-manager --enable rhel-7-server-optional-rpms
#\cp ./zabbix.repo /etc/yum.repos.d/zabbix.repo
#安装Zabbix服务，它会自动安装它所依赖的httpd与PHP。客户端装repo后，只装zabbix-agent
yum -y install zabbix-server-mysql zabbix-web-mysql zabbix-agent zabbix_get
#导入数据库SQL脚本。
zcat /usr/share/doc/zabbix-server-mysql-4.5.2/create.sql.gz | $mysqlcmd zabbix

#修改配置文件
#sed -i '/^DBHost=/c\DBHost=localhost' /etc/zabbix/zabbix_server.conf
#sed -i '/^DBName=/c\DBName=zabbix' /etc/zabbix/zabbix_server.conf
#sed -i '/^DBUser=/c\DBUser=zabbix' /etc/zabbix/zabbix_server.conf
sed -i '/^# DBPassword=/c\DBPassword=1qaz@WSX123' /etc/zabbix/zabbix_server.conf

#修改zabbix-agent客户端agent配置文件，本例装在本机上，其它更改为服务器的ip（127.0.0.1）
#sed -i '/^Server=127.0.0.1/c\Server=127.0.0.1' /etc/zabbix/zabbix_agentd.conf
#sed -i '/^ServerActive=127.0.0.1/c\ServerActive=127.0.0.1' /etc/zabbix/zabbix_agentd.conf
#sed -i '/^Hostname=/c\Hostname=Zabbix Server' /etc/zabbix/zabbix_agentd.conf  #建议修改此行，配置规范的主机名

#编辑http配置文件，设置为上海时区，并该行删除注释符号
sed -i '/php_value date.timezone/c\        php_value date.timezone Asia/Shanghai' /etc/httpd/conf.d/zabbix.conf 

systemctl start httpd              #启动httpd服务
systemctl enable httpd         #设置开机自启动
systemctl start zabbix-server            #启动zabbix服务端
systemctl enable zabbix-server          #设置开机自启动
systemctl start zabbix-agent       #启动agent代理
systemctl enable zabbix-agent          #设置开机自启动
