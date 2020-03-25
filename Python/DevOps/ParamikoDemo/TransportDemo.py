import paramiko

# pkey = paramiko.RSAKey.from_private_key_file('/home/kin/.ssh.id_rsa')
trans = paramiko.Transport('118.25.83.194',22)
# trans.connect(username='kin',pkey=pkey)
trans.connect(username='kin',password='SAMSUNG_TX_Cloud1981')
ssh = paramiko.SSHClient()
ssh._transport = trans

stdin,stdout,stderr = ssh.exec_command("echo `date` && df -hl")
print(stdout.read().decode('utf-8'))

sftp = paramiko.SFTPClient.from_transport(trans)

sftp.put(localpath='./log1.log',remotepath='/tmp/log1.log')
sftp.get(localpath='./log111111111.log',remotepath='/tmp/log1.log')
stdin,stdout,stderr = ssh.exec_command("echo `date` && ls -ltr /tmp")
print(stdout.read().decode('utf-8'))

trans.close()