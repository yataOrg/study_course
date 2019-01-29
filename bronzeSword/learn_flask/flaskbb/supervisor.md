### help
---
```
pip install supervisor
echo_supervisord_conf
echo_supervisord_conf > /etc/supervisord.conf
当前目录 echo_supervisord_conf > supervisord.conf
运行命令
supervisord -c /etc/supervisord.conf

$CWD 指的是当前目录
```
---
```
二、更新新的配置到supervisord

supervisorctl update
1
三、重新启动配置中的所有程序

supervisorctl reload
1
四、启动某个进程(program_name=你配置中写的程序名称)

supervisorctl start program_name
1
五、查看正在守候的进程

supervisorctl
1
六、停止某一进程 (program_name=你配置中写的程序名称)

pervisorctl stop program_name
1
七、重启某一进程 (program_name=你配置中写的程序名称)

supervisorctl restart program_name
1
八、停止全部进程

supervisorctl stop all
```