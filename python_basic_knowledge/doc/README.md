### python环境搭建
```
1. mac系统通过 brew install python3
2. 源码安装 
	# tar -zxvf Python-3.6.1.tgz
	# cd Python-3.6.1
	# ./configure
	# make && make install
```
> python几个重要的环境变量

1. PYTHONPATH是Python搜索路径，默认我们import的模块都会从PYTHONPATH里面寻找。
2. PYTHONSTARTUP Python启动后，先寻找PYTHONSTARTUP环境变量，然后执行此变量指定的文件中的代码。
3. PYTHONCASEOK 加入PYTHONCASEOK的环境变量, 就会使python导入模块的时候不区分大小写.
4. PYTHONHOME 另一种模块搜索路径。它通常内嵌于的PYTHONSTARTUP或PYTHONPATH目录中，使得两个模块库更容易切换。

```
-c <command>
执行 command 中的 Python 代码。 command 可以为一条或以换行符分隔的多条语句，其中前导空格像在普通模块代码中一样具有作用。

如果给出此选项，sys.argv 的首个元素将为 "-c" 并且当前目录将被加入 sys.path 的开头（以允许该目录中的模块作为最高层级模块被导入）。

-m <module-name>
在 sys.path 中搜索指定名称的模块并将其内容作为 __main__ 模块来执行。

由于该参数为 module 名称，你不应给出文件扩展名 (.py)。 模块名称应为绝对有效的 Python 模块名称，但具体实现可能并不总是强制要求这一点（例如它可能允许你使用包含连字符的名称）。

包名称（包括命名空间包）也允许使用。 当所提供的是包名称而非普通模块名称时，解释器将把 <pkg>.__main__ 作为主模块来执行。 此行为特意被设计为与作为脚本参数传递给解释器的目录和 zip 文件的处理方式类似。
```

```
Cygwin 是一个在 windows 平台上运行的类 UNIX 模拟环境，是 cygnus solutions 公司开发的自由软件（该公司开发的著名工具还有 eCos，不过现已被 Redhat 收购）。它对于学习 UNIX/Linux 操作环境，或者从 UNIX 到 Windows 的应用程序移植，或者进行某些特殊的开发工作，尤其是使用 GNU 工具集在 Windows 上进行嵌入式系统开发，非常有用。
```

import keyword
print(keyword.kwlist)

### 多行注释
```
total = item_one + \
        item_two + \
        item_three
```

```
字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
str = 'hello world'
set[0:-1:2]
```


