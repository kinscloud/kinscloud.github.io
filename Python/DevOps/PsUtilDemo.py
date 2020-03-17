import psutil
#查看逻辑cpu的个数
psutil.cpu_count()
#查看物理cpu的个数
psutil.cpu_count(logical=False)
psutil.cpu_times_percent() #cpu的总使用情况
psutil.cpu_times_percent(percpu=True) #每个cpu的使用情况
psutil.cpu_percent() #cpu的使用率
#要查看cpu的负载呢，我们还是使用其他的命令吧
# import os
# os.getloadavg()

#查看系统缓存的信息
psutil.swap_memory()
psutil.swap_memory().total  #单位是字节
psutil.swap_memory().total/1024 #swap总大小，以kb单位表示
psutil.swap_memory().free/1024  #空闲swap大小，以kb单位表示

#统计内存使用情况
##############总内存 ,使用的,空闲  ,使用百分比,buffers ，cached  单位是字节
# for i in ['total','used','free','percent','buffers','cached']:
#     ret=getattr(psutil.virtual_memory(),i)
    # print(ret)
    
#获取磁盘信息
psutil.disk_partitions()
#获取挂载点的分区信息，通过device去的话显示有问题
psutil.disk_usage("/boot")
psutil.disk_usage("/boot").percent

#获取网卡ens33的IP地址
psutil.net_if_addrs()['ens33'][0].address
#子网掩码
psutil.net_if_addrs()['ens33'][0].netmask
#查看网卡是否开启
psutil.net_if_stats()['ens33'].isup
#查看网卡的速率，命令有ifconfig，ethtool
psutil.net_if_stats()['ens33'].speed

#psutil.net_connections 查看网络的连接情况
for i in psutil.net_connections():
    if i.raddr:  #判断外部地址情况不为空的情况，避免raddr=()产生错误
        print(i.laddr.ip,i.laddr.port,i.raddr.ip,i.raddr.port,i.status,i.pid)
        
#进程的情况
p=psutil.Process(1094) #1094是nginx的master进程
p.num_threads()  #打开的线程数，由于nginx是一个主进程和多个工作进程，因此都为1
p.cwd()          #进程的工作目录路径
p.cmdline()      #nginx的命令进程信息
p.exe()           #执行的命令
p.is_running()    #是否存活
p.name()           #进程名称
p.nice()           #进程的nice值
p.status()         #状态
p.threads()        #它的线程情况
p.ppid()          #它的父进程
p.username()      #它的执行用户
p.memory_percent() #内存利用率
p.cpu_percent()    #cpu利用率
psutil.pid_exists(1111) #查看进程是否存在
psutil.pid_exists(1094)