from email.mime.text import MIMEText
msg = MIMEText('hello,send by Python...','plain','utf-8')

#输入Emai地址和口令：
from_addr = input('From:')
password = input('Password:')
#输入收件人的地址：
to_addr = input('To:')
#输入SMTP服务地址：
smtp_server = input('SMTP server:')


import smtplib
server = smtplib.SMTP(smtp_server,465)  #SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()