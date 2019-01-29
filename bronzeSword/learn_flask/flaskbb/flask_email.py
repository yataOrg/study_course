#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
# 下面是SMTP服务器配置
app.config['MAIL_SERVER'] = 'smtp.163.com'  # 电子邮件服务器的主机名或IP地址
app.config['MAIL_PORT'] = 25  # 电子邮件服务器的端口
app.config['MAIL_USE_TLS'] = True  # 启用传输层安全
# 注意这里启用的是TLS协议(transport layer security)，而不是SSL协议所以用的是25号端口
app.config['MAIL_USERNAME'] = 'yata818@163.com'  # 你的邮件账户用户名
app.config['MAIL_PASSWORD'] = '5201314qqq'  # 邮件账户的密码,这个密码是指的授权码!授权码!授权码!

mail = Mail(app)


@app.route('/')
def index():
    msg = Message('你好', sender='yata818@163.com', recipients=['yanzhipeng@qutoutiao.net'])
    # 这里的sender是发信人，写上你发信人的名字，比如张三。
    # recipients是收信人，用一个列表去表示。
    msg.body = '你好'
    msg.html = '<b>你好</b> stranger'
    mail.send(msg)
    return '<h1>邮件发送成功</h1>'

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=80)