#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yanzhipeng
# @Date:   2019-10-09 18:09:51
# @Last Modified by:   yanzhipeng
# @Last Modified time: 2019-10-09 21:48:20

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

mail_host = 'smtp.qq.com'
mail_user = '1366525100@qq.com'
mail_pass = 'njqankhqkahbfihd'

sender = '1366525100@qq.com'
receivers = ['yata818@163.com']

message = MIMEMultipart()

message['From'] = Header('雅塔测试', 'utf-8')
message['To'] = Header('测试', 'utf-8')

subject = "Python SMTP 邮件测试"
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文
message.attach(MIMEText('测试测试，我是邮件正文...', 'plain', 'utf-8'))

# 构造附件1
att1 = MIMEText(open("../../data/test.md", "rb").read(), 'base64', 'utf-8')
att1['Content-Type'] = "application/octet-stream"
att1['Content-Disposition'] = 'attachment; filename="azhu1.txt"'

# 构造附件2
att2 = MIMEText(open("../../data/azhu1.md", "rb").read(), 'base64', 'utf-8')
att2['Content-Type'] = "application/octet-stream"
att2['Content-Disposition'] = 'attachment; filename="azhu2.txt"'

message.attach(att1)
message.attach(att2)



try:
	smtpObj = smtplib.SMTP()
	smtpObj.connect(mail_host, 25)
	smtpObj.login(mail_user, mail_pass)
	smtpObj.sendmail(sender, receivers, message.as_string())
	print("邮件发送成功 file")
	smtpObj.quit()
except smtplib.SMTPException:
	print("Error: 无法发送邮件")

