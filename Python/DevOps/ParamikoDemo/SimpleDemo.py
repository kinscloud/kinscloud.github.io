import paramiko

# pkey = paramiko.RSAKey.from_private_key_file('/home/kin/.ssh.id_rsa')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# ssh.connect(hostname='118.25.83.194',port=22,username='kin',pkey=pkey)
ssh.connect(hostname='118.25.83.194',port=22,username='kin',password='SAMSUNG_TX_Cloud1981')
stdin,stdout,stderr = ssh.exec_command("echo `date` && ls -ltr")
print(stdout.read().decode('utf-8'))
returncode = stdout.channel.recv_exit_status()
print('returncode:',returncode)
ssh.close()