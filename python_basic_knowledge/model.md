## python models
> this is some models

### configparser
> config.ini
```
[db]
db_port = 3306
db_user = root
db_host = 127.0.0.1
```

```
import configparser

Config = configparser.ConfigParser()
Config.read("config.ini")
data = Config.sections()
print(data)
db_host = Config.get("db", "db_host")
print(db_host)
```

> demo.ini
```
[Section1]
foo=%(bar)s is %(baz)s!
baz=fun
bar=Python
```

> demo.py
```
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import ConfigParser
import string, os
cf = ConfigParser.ConfigParser()
cf.read("test.conf")
res = cf.get('Section1', 'foo')
print "默认情况下, raw=False, 此时输出 %s" % res
res = cf.get('Section1', 'foo', raw=False)
print "raw=False, 无参数vars 此时等同于默认输出:%s" % res
res = cf.get('Section1', 'foo', raw=True)
print "raw=True, 无参数vars 此时等输出未被匹配原字符:%s" % res
res = cf.get('Section1', 'foo', raw=False, vars={'bar': 'Documentation','baz': 'evil'})
print "raw=False, vars存在 此时使用vars中的值进行匹配:%s" % res
res = cf.get('Section1', 'foo', raw=True, vars={'bar': 'Documentation', 'baz':'sdsd'})
print "raw=True, vars存在 此时vars不生效,输出未被匹配原字符:%s" % res
res = cf.get('Section1', 'foo', raw=False, vars={'bar': 'Documentation'})
print "raw=True, vars存在，但只包含一个值, 此时另一个值取默认匹配值,输出未:%s" % res
```

### yaml
> 第二种config文件是config.yaml,用到的是YAML语言,它是专门用来写配置文件的语言，非常简洁和强大，远比 JSON 格式方便。

* config.yaml
```
mysql.confg
  conn:
    host: 'localhost'
    port: 3306
    db: 'test'
    user: 'root'
    passwd: '123456'
    charset: 'utf-8'

redis.config
  conn:
    host: 'localhost'
    port: '6379'
```



```
import os
import yaml
config_file = os.path.dirname(os.path.realpath(__file__)) + '/config.yaml'
configs = yaml.load(open(config_file,'r'))
conns = configs.get('mysql.config')['conn']
for k,v in conns.items():
    print(k,'====:',v)

```

> 下面是封装的代码
```
import os
import yaml

class ConfigParser(object):

    config_file = os.path.dirname(os.path.realpath(__file__)) + '/config.yaml'
    configs = yaml.load(open(config_file,'r'))
    @classmethod
    def get(cls, server='mysql.config',key=None):
        if not cls.configs:
            cls.configs = yaml.load(open(cls.config_file, 'r'))
        section = cls.configs.get(server, None)
        if section is None:
            raise NotImplementedError
        value = section.get(key, None)
        if value is None:
                raise NotImplementedError
        return value

if __name__ == '__main__':
    configs = ConfigParser()
    mysql_conn = configs.get(key='conn')
    print(mysql_conn)
```









