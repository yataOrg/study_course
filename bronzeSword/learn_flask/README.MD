## 青铜剑级别
### 入门教程
---

```
export FLASK_APP=demo0.py 
export FLASK_ENV=development 
export FLASK_DEBUG=1
pip3 install Flask
flask run
flask run --host=0.0.0.0
flask run --port 5001
```
---
```
* command 中 python3 -c "import os;print(os.urandom(16))"
* python3 虚拟环境 python3 -m venv venv

```

# 活在当下
> 如果想要在正式发行之前使用最新的 Flask 开发版本，可以使用如下命令从主分支 安装或者更新代码：
* pip install -U https://github.com/pallets/flask/archive/master.tar.gz
* pip3 install -U https://github.com/pallets/flask/archive/master.tar.gz

> 在开始工作前，先要激活相应的虚拟环境：
* . venv/bin/activate

* (pip3 install -e .) (pip3 install -e /path/a) Install a project in editable mode (i.e. setuptools “develop mode”) from a local project path or a VCS url.
* abc


### 导入配置
```
==========方式一：============
 app.config['SESSION_COOKIE_NAME'] = 'session_lvning'  #这种方式要把所有的配置都放在一个文件夹里面，看起来会比较乱，所以选择下面的方式
==========方式二：==============
app.config.from_pyfile('settings.py')  #找到配置文件路径，创建一个模块，打开文件，并获取所有的内容，再将配置文件中的所有值，都封装到上一步创建的配置文件模板中

print(app.config.get("CCC"))
=========方式三：对象的方式============
 import os 
 os.environ['FLAKS-SETTINGS'] = 'settings.py'
 app.config.from_envvar('FLAKS-SETTINGS') 

===============方式四（推荐）：字符串的方式，方便操作，不用去改配置，直接改变字符串就行了 ==============
app.config.from_object('settings.DevConfig')

----------settings.DevConfig----------
from app import app
class BaseConfig(object):
    NNN = 123  #注意是大写
    SESSION_COOKIE_NAME = "session_sss"

class TestConfig(BaseConfig):
    DB = "127.0.0.1"

class DevConfig(BaseConfig):
    DB = "52.5.7.5"

class ProConfig(BaseConfig):
    DB = "55.4.22.4"
```


### detect_types=sqlite3.PARSE_DECLTYPES
```
g.db = sqlite3.connect(
    current_app.config['DATABASE'],
    detect_types=sqlite3.PARSE_DECLTYPES
)
```

```
11.13.1. Module functions and constants模板函数及常量
l sqlite3.PARSE_DECLTYPES
这个常量被connect函数作为detect_types参数进行使用。

通过设置它可以让sqlite3模块对返回的每列的声明类型进行分析。它将会分析出声明类型的第一个单词，举例说，例如“integer primary key”，将会分析出“integer”，再或者如“number(10)”则会分析出“number”。然后对于此列，它将会查找转换字典，并使用针对此类型的转换函数。

l sqlite3.PARSE_COLNAMES
这个常量被connect函数作为detect_types参数进行使用。

通过设置它可以让SQLite接口分析返回的每个列名。它将会查找格式为[mytype]的字符串，然后决定”mytype”是否是此列的类型。它还会尝试在转换字典中查找是否存在“mytype”条目，如果找到就使用转换函数来返回列的值。被查找的列表只是在cursor.description中列名的第一个单词，例如，你在SQL语句中使用'as "x[datetime]"'，则列名将会是”x”。
```

### flask 命令行 自定义命令
```
使用Click可以实现flask命令。查看这个项目的文档来获取关于编写命令的所有知识。

        这个例子添加了带有参数name的命令create_user：


import click
from flask import Flask
 
 
app = Flask(__name__)
 
 
@app.cli.command()
@click.argument('name')
def create_user(name):
    ...



flask create_user admin
        这个示例添加了同样的命令，但是命令为user create，表示一个命令在一个命令组内。如果你想组织多种相关的命令，这是很有用的：




import click
from flask import Flask
from flask.cli import AppGroup
 
 
app = Flask(__name__)
user_cli = AppGroup('user')
 
 
@user_cli.command('create')
@click.argument('name')
def create_user(name):
    ...
 
 
app.cli.add_command(user_cli)



flask user create demo

```

### click command 两种方式
---
```
#@click.group 装饰器把方法装饰为可以拥有多个子命令的group对象，并采用group.add_command()方法把command对象关联到group对象
#1.通过方法add_command

@click.group()
def cli():
    pass

@click.command()
def initdb():
    click.echo('Initialized the database')
    
@click.command()
def dropdb():
    click.echo('Dropped the database')
cli.add_command(initdb)
cli.add_command(dropdb)
#直接进行装饰
@click.group()
def cli():
    pass

@cli.command()
def initdb():
    click.echo('Initialized the database')
    
@cli.command()
def dropdb():
    click.echo('Dropped the database')

```

### setup setuptools 发包
```
5. 准备好上面的步骤，一个包就基本完整了，剩下的就是打包了(cd到包的根目录)：
可以使用下面命令打包一个源代码的包:

python setup.py sdist build
这样在当前目录的dist文件夹下，就会多出一个以tar.gz结尾的包了：

也可以打包一个wheels格式的包，使用下面的命令搞定：

python setup.py bdist_wheel --universal
这样会在dist文件夹下生成一个whl文件，

6. 上传生成的包，可以使用setuptools,或者twine上传,推荐使用twine上次，因为使用setuptools上传时，你的用户名和密码是明文或者未加密传输，安全起见还是使用twine吧
# 上传source 包
python setup.py sdist upload
# 上传pre-compiled包
python setup.py bdist_wheel upload
使用twine上传,先安装twine

sudo pip install twine

twine upload dist/*
上传前都会提示你前面注册的用户名和密码。一切搞定，你的包现在可以通过pip在任何地方安装了。
```

### setup.py  打包 发包

> 在需要打包的包目录下创建 setup.py 文件 和 MANIFEST.in（无静态文件可以不用创建） 文件

### setup.py 里输入

### 引入构建包信息的模块
* from distutils.core import setup

### 定义发布的包文件的信息
```
setup(
    name="plane_01",  # 发布的包的名称
    version="1.00.001",  # 发布包的版本序号
    description="打飞机小游戏",  # 发布包的描述信息
    author="桔子",  # 发布包的作者信息
    author_email="1847562860@qq.com",  # 作者的联系邮箱
    py_modules=['__init__', 'ariplane']  # 发布包中的模块文件列表
)
MANIFEST.in 文件里输入要打包的 静态文件/文件夹

recursive-include font *
recursive-include Images *
recursive-include sounds *
打开当前目录命令行：

输入

python setup.py sdist
打包成功，在目录下生成 dist文件夹 

包的网络发布：

首先，进入 https://pypi.org 网站上，注册一个账号;

然后打开cmd命令行输入以下命令 安装 twine 第三方模块

pip install twine
装好后，进入打包目录的命令行输入以下命名 上传网络

twine upload dist/*


setup函数各参数详解：
>>python setup.py --help
  --name              包名称
  --version (-V)      包版本
  --author            程序的作者
  --author_email      程序的作者的邮箱地址
  --maintainer        维护者
  --maintainer_email  维护者的邮箱地址
  --url               程序的官网地址
  --license           程序的授权信息
  --description       程序的简单描述
  --long_description  程序的详细描述
  --platforms         程序适用的软件平台列表
  --classifiers       程序的所属分类列表
  --keywords          程序的关键字列表
  --packages  需要打包的目录列表
  --py_modules  需要打包的python文件列表
  --download_url  程序的下载地址
  --cmdclass  
  --data_files  打包时需要打包的数据文件，如图片，配置文件等
  --scripts  安装时需要执行的脚步列表

setup.py打包命令各参数详解：
>>python setup.py --help-commands
  --python setup.py build     # 仅编译不安装
  --python setup.py install    #安装到python安装目录的lib下
  --python setup.py sdist      #生成压缩包(zip/tar.gz)
  --python setup.py bdist_wininst  #生成NT平台安装包(.exe)
  --python setup.py bdist_rpm #生成rpm包  

```

### 从本地文件夹安装
```
pip install -e /path/to/your/setup.py
```

### 修饰符
```
@修饰符 
　　‘@’符号用作函数修饰符是python2.4新增加的功能，修饰符必须出现在函数定义前一行，不允许和函数定义在同一行。也就是说＠A def f(): 是非法的。 只可以在模块或类定义层内对函数进行修饰，不允许修修饰一个类。一个修饰符就是一个函数，它将被修饰的函数做为参数，并返回修饰后的同名函数或其它可调用的东西。

　　本质上讲，装饰符@类似于回调函数，把其它的函数（暂且称为目的参数）作为自己的入参，在目的函数执行前，执行一些自己的操作，比如：计数、打印一些提示信息等，然后返回目的函数。下面列举一个简单的例子。

import time

def time(func):
    print(time.ctime())
    return func()

@time  # 从这里可以看出@time 等价于 time(xxx()),但是这种写法你得考虑python代码的执行顺序
def xxx():
    print('Hello world!')


运行结果：
Wed Jul 26 23:01:21 2017
Hello world!
--------------------- 
```


