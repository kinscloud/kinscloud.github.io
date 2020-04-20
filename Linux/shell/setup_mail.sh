#/bin/bash

#发送告警邮件脚本
yum install -y mailx

echo "set from=xxx@163.com smtp=smtp.163.com" >> /etc/mail.rc
echo "set smtp-auth-user=xxx@163.com smtp-auth-password=xxx" >> /etc/mail.rc
echo "set smtp-auth=login" >> /etc/mail.rc