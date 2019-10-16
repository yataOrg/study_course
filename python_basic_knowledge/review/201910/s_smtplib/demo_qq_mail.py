#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yanzhipeng
# @Date:   2019-10-09 16:56:04
# @Last Modified by:   yanzhipeng
# @Last Modified time: 2019-10-09 21:49:05

import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = 'smtp.qq.com'
mail_user = '1366525100@qq.com'
mail_pass = 'njqankhqkahbfihd'

sender = '1366525100@qq.com'
receivers = ['yata818@163.com']

message = MIMEText('Python smtplib 邮件发送测试', 'plain', 'utf-8')
message['From'] = Header('雅塔测试', 'utf-8')
message['To'] = Header('测试', 'utf-8')

subject = "Python SMTP 邮件测试"

message['Subject'] = Header(subject, 'utf-8')


try:
	smtpObj = smtplib.SMTP()
	smtpObj.connect(mail_host, 25)
	smtpObj.login(mail_user, mail_pass)
	smtpObj.sendmail(sender, receivers, message.as_string())
	print("邮件发送成功")
	smtpObj.quit()
except smtplib.SMTPException:
	print("Error: 无法发送邮件")