#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yanzhipeng
# @Date:   2019-10-09 20:58:51
# @Last Modified by:   yanzhipeng
# @Last Modified time: 2019-10-09 21:47:46

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

mail_host = 'smtp.qq.com'
mail_user = '1366525100@qq.com'
mail_pass = 'njqankhqkahbfihd'

sender = '1366525100@qq.com'
receivers = ['yata818@163.com']

msgRoot = MIMEMultipart('related')
msgRoot['From'] = Header('测试测试from', 'utf-8')
msgRoot['To'] = Header("测试to", 'utf-8')
subject = 'this is test of subject'
msgRoot['Subject'] = Header(subject, 'utf-8')

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">菜鸟教程链接</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
"""

msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

# 指定图片为当前目录
fp = open('../../data/mail_test.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)



try:
	smtpObj = smtplib.SMTP()
	smtpObj.connect(mail_host, 25)
	smtpObj.login(mail_user, mail_pass)
	smtpObj.sendmail(sender, receivers, msgRoot.as_string())
	print("邮件发送成功 html-image")
	smtpObj.quit()
except smtplib.SMTPException:
	print("Error: 无法发送邮件")