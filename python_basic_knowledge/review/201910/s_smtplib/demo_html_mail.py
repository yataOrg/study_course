#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yanzhipeng
# @Date:   2019-10-09 17:30:18
# @Last Modified by:   yanzhipeng
# @Last Modified time: 2019-10-09 21:48:48


import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = 'smtp.qq.com'
mail_user = '1366525100@qq.com'
mail_pass = 'njqankhqkahbfihd'

sender = '1366525100@qq.com'
receivers = ['yata818@163.com']

mail_msg = '''
<pre>阿朱小明叫哆哆</pre>
<p>2019-10-09 17:35</p>
'''

message = MIMEText(mail_msg, 'html', 'utf-8')
message['From'] = Header('雅塔test1', 'utf-8')
message['To'] = Header('哆哆', 'utf-8')
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
	smtpObj = smtplib.SMTP()
	smtpObj.connect(mail_host, 25)
	smtpObj.login(mail_user, mail_pass)
	smtpObj.sendmail(sender, receivers, message.as_string())
	print("邮件发送成功 html")
	smtpObj.quit()
except smtplib.SMTPException:
	print("Error: 无法发送邮件")
