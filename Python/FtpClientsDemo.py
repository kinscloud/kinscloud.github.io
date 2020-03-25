from ftplib import FTP

ftp = FTP(host='localhost',user='root',passwd='000000')
ftp.encoding = 'gbk'

ftp.retrlines('LIST')