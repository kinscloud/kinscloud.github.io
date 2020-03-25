import smtplib
from email.mime.text import MIMEText

mail_host = 'smtp.163.com'
mail_user = 'xxxx@163.com'
# 授权码
mail_pass = 'MIUMSKVSNWXBJYEA'

sender = 'xxxx@163.com'

receivers = ['xxxx@163.com']

# message = MIMEText('这是正文：邮件正文。。。。','plain','utf-8')
message = MIMEText(
    '<html<body><h1>this is a title</h1>\
        <p>content</p>\
            </body></html>', 'html', 'utf-8',
)

message['From'] = sender
message['To'] = ";".join(receivers)
message['Subject'] = '这是主题：smtp邮件测试'

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print('发送成功')
except smtplib.SMTPException as e:
    print(f'发送失败，错误原因：{ e }')
