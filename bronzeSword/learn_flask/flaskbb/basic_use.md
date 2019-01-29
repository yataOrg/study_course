### nginx的启动和停止
```
启动、停止nginx
cd /usr/local/nginx/sbin/
./nginx 
./nginx -s stop
./nginx -s quit
./nginx -s reload
```

### requirements.txt
```
Flask==1.0.2
后面可以加
-e .
会调用 pip3 install -e .
走 setup.py
```

### pycharm代码调试
```
Step Over：在单步执行时，在函数内遇到子函数时不会进入子函数内单步执行，而是将子函数整个执行完再停止，也就是把子函数整个作为一步

注意：在不存在子函数的情况下Step Over是和Step Into效果一样的

Step Into：单步执行，遇到子函数就进入并且继续单步执行(即进入子函数）

Step Out：当单步执行到子函数内时，用Step Out就可以执行完子函数余下部分，并返回到上一层函数
```

supervisord -c /etc/supervisord.conf

```
use mysql
mysql://scott:tiger@localhost/mydatabase
dialect+driver://username:password@host:port/database
mysql://root:12345678@localhost:3306/flaskbb
```

### no module named mysqldb
```
pip3 install pymysql
import pymysql
__init__.py
add pymysql.install_as_MySQLdb()
```

### flaskbb 配置和运行
```
python3.
git clone https://github.com/sh4nks/flaskbb.git
git checkout 2.0.0
cd flaskbb
mkdir venv && cd venv
pipenv --three
pipenv shell
cd ../
vim requirements.txt  edit kombu==4.2.2  Pillow==5.3.0
pip install -r requirements-dev.txt
flaskbb makeconfig -d or flaskbb makeconfig –development
make install or flaskbb install
flaskbb --config flaskbb.cfg run

```

### deploying
```
虚拟环境运行app
/Users/yanzhipeng/.local/share/virtualenvs/flask2b/bin/flaskbb --config /usr/local/var/www/my_code/python_web_development/flaskbb/flaskbb.cfg run

/Users/yanzhipeng/.local/share/virtualenvs/flask2b/bin/flaskbb --config /usr/local/var/www/my_code/python_web_development/flaskbb/flaskbb.cfg celery worker -l info

celery multi start w1 -A myproject -l info --logfile = celerylog.log --pidfile = celerypid.pid

```



```
source virtualenvwrapper.sh
lsvirtualenv -b
mkvirtualenv flask2b
workon flask2b
deactivate
mkvirtualenv -p python3.4 env34
rmvirtualenv flask2b
```

```
brew install supervisor
;brew install uwsgi
pip3 install uwsgi

#### 启动：
uwsgi --ini xxx.ini
#### 重启：
uwsgi --reload xxx.pid
#### 停止：
uwsgi --stop xxx.pid

[brew services start uwsgi]

[遇到的各种小坑

; file_name uwsgi.ini
[program:uwsgi]
command=/usr/local/bin/uwsgi --emperor /usr/local/etc/uwsgi
user=yanzhipeng
stopsignal=QUIT
autostart=true
autorestart=true
redirect_stderr=true

; file_name wsgi.py
import os
# from flaskbb import create_app
from flaskbb.app import create_app

from flaskbb.utils.helpers import ReverseProxyPathFix

_basepath = os.path.dirname(os.path.abspath(__file__))

# will throw an error if the config doesn't exist
flaskbb = create_app(config='/usr/local/var/www/my_code/python_web_development/flaskbb/flaskbb.cfg')

#  Uncomment to use the middleware
#flaskbb.wsgi_app = ReverseProxyPathFix(flaskbb.wsgi_app)

if __name__ == "__main__":
    flaskbb.run()


; file_name requirements.txt
alembic==0.9.9
amqp==2.1.4
attrs==17.4.0
Babel==2.5.3
billiard==3.5.0.2
blinker==1.4
celery==4.2.1
certifi==2018.4.16
chardet==3.0.4
click==6.7
click-log==0.2.1
enum34==1.1.6
Flask==1.0.2
Flask-Alembic==2.0.1
flask-allows==0.4.0
Flask-BabelPlus==2.1.1
Flask-Caching==1.4.0
Flask-DebugToolbar==0.10.1
Flask-Limiter==1.0.1
Flask-Login==0.4.1
Flask-Mail==0.9.1
Flask-Redis==0.3.0
Flask-SQLAlchemy==2.3.2
Flask-Themes2==0.1.4
flask-whooshee==0.5.0
Flask-WTF==0.14.2
flaskbb-plugin-conversations==1.0.2
flaskbb-plugin-portal==1.1.1
idna==2.6
itsdangerous==0.24
Jinja2==2.10
kombu==4.2.2
limits==1.3
Mako==1.0.7
MarkupSafe==1.0
mistune==0.8.3
olefile==0.45.1
Pillow==5.3.0
pluggy==0.6.0
Pygments==2.2.0
python-dateutil==2.7.2
python-editor==1.0.3
pytz==2018.4
redis==2.10.6
requests==2.18.4
simplejson==3.14.0
six==1.11.0
speaklater==1.3
SQLAlchemy==1.2.7
SQLAlchemy-Utils==0.33.3
Unidecode==1.0.22
urllib3==1.22
vine==1.1.4
Werkzeug==0.14.1
Whoosh==2.7.4
WTForms==2.1
-e .


; file_name flaskbb.cfg
# This file has been automatically generated on Saturday, 22. December 2018 at 17:31.
# Feel free to adjust it as needed.
import os
import datetime
from flaskbb.configs.default import DefaultConfig


# Flask Settings
# ------------------------------
# There is a whole bunch of more settings available here:
# http://flask.pocoo.org/docs/0.11/config/#builtin-configuration-values
DEBUG = True
TESTING = False
DEBUG_TB_INTERCEPT_REDIRECTS = False

# Server Name - REQUIRED for Celery/Mailing
# The name and port number of the server.
# Required for subdomain support (e.g.: 'myapp.dev:5000') and
# URL generation without a request context but with an application context
# which we need in order to generate URLs (with the celery application)
# Note that localhost does not support subdomains so setting this to
# “localhost” does not help.
# Example for the FlaskBB forums: SERVER_NAME = "forums.flaskbb.org"
SERVER_NAME = "flaskbb.peng"
# SERVER_NAME = "localhost:5000"

# Prefer HTTPS over HTTP
PREFERRED_URL_SCHEME = "http"

# Don't send secure cookies over an unencrypted connection ()
SESSION_COOKIE_SECURE = False
# Don't make cookies available to JS (XSS) - browsers hide httpOnly cookies from JS
SESSION_COOKIE_HTTPONLY = True


# Database
# ------------------------------
# For PostgresSQL:
#SQLALCHEMY_DATABASE_URI = "postgresql://flaskbb@localhost:5432/flaskbb"
# For SQLite:
# SQLALCHEMY_DATABASE_URI = "sqlite:////usr/local/var/www/my_code/python_web_development/flaskbb/flaskbb.sqlite"
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:12345678@localhost:3306/flaskbb"
# This option will be removed as soon as Flask-SQLAlchemy removes it.
# At the moment it is just used to suppress the super annoying warning
SQLALCHEMY_TRACK_MODIFICATIONS = False
# This will print all SQL statements
SQLALCHEMY_ECHO = False


# Security - IMPORTANT
# ------------------------------
# This is the secret key that is used for session signing.
# You can generate a secure key with os.urandom(24)
SECRET_KEY = "f44ee2825fe3c5e7d56b7300377f27e404e0be7cd8654d99"

# You can generate the WTF_CSRF_SECRET_KEY the same way as you have
# generated the SECRET_KEY. If no WTF_CSRF_SECRET_KEY is provided, it will
# use the SECRET_KEY.
WTF_CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = "f2283e796fc14c15547e3cf58a400cfc138ffea7ca43633c"


# Auth
# ------------------------------
LOGIN_VIEW = "auth.login"
REAUTH_VIEW = "auth.reauth"
LOGIN_MESSAGE_CATEGORY = "info"
REFRESH_MESSAGE_CATEGORY = "info"

# The name of the cookie to store the “remember me” information in.
REMEMBER_COOKIE_NAME = "remember_token"
# The amount of time before the cookie expires, as a datetime.timedelta object.
# Default: 365 days (1 non-leap Gregorian year)
REMEMBER_COOKIE_DURATION = datetime.timedelta(days=365)
# If the “Remember Me” cookie should cross domains,
# set the domain value here (i.e. .example.com would allow the cookie
# to be used on all subdomains of example.com).
REMEMBER_COOKIE_DOMAIN = None
# Limits the “Remember Me” cookie to a certain path.
REMEMBER_COOKIE_PATH = "/"
# Restricts the “Remember Me” cookie’s scope to secure channels (typically HTTPS).
REMEMBER_COOKIE_SECURE = False
# Prevents the “Remember Me” cookie from being accessed by client-side scripts.
REMEMBER_COOKIE_HTTPONLY = True


# Full-Text-Search
# ------------------------------
# This will use the "whoosh_index" directory to store the search indexes
WHOOSHEE_DIR = os.path.join(DefaultConfig.basedir, "whoosh_index", DefaultConfig.py_version)
# How long should whooshee try to acquire write lock? (defaults to 2)
WHOOSHEE_WRITER_TIMEOUT = 2
# Minimum number of characters for the search (defaults to 3)
WHOOSHEE_MIN_STRING_LEN = 3


# Redis
# ------------------------------
# If redis is enabled, it can be used for:
#   - Sending non blocking emails via Celery (Task Queue)
#   - Caching
#   - Rate Limiting
REDIS_ENABLED = True
REDIS_URL = "redis://localhost:6379"
REDIS_DATABASE = 0


# Celery
# ------------------------------
# CELERY_BROKER_URL = "redis://localhost:6379"
# CELERY_RESULT_BACKEND = "redis://localhost:6379"


# Rate Limiting
# -------------------------------
# A full list with configuration values is available at the flask-limiter
# docs, but you actually just need those settings below.
# You can disabled the Rate Limiter here as well - it will overwrite
# the setting from the admin panel!
# RATELIMIT_ENABLED = True
# You can choose from:
#   memory:// (default)
#   redis://host:port
#   memcached://host:port
# Using the redis storage requires the installation of the redis package,
# which will be installed if you enable REDIS_ENABLE while memcached
# relies on the pymemcache package.
RATELIMIT_STORAGE_URL = "memory://"


# Caching
# ------------------------------
# For all available caching types, have a look at the Flask-Cache docs
# https://pythonhosted.org/Flask-Caching/#configuring-flask-caching
CACHE_TYPE = "simple"
CACHE_DEFAULT_TIMEOUT = 60


# Mail
# ------------------------------
# Google Mail Example
# https://support.google.com/mail/answer/7126229?hl=en
#MAIL_SERVER = "smtp.gmail.com"
#MAIL_PORT = 587
#MAIL_USE_TLS = True
#MAIL_USE_SSL = True
#MAIL_USERNAME = "your_username@gmail.com"
#MAIL_PASSWORD = "your_password"
#MAIL_DEFAULT_SENDER = ("Your Name", "your_username@gmail.com")

# Local SMTP Server
MAIL_SERVER = "localhost"
MAIL_PORT = 25
MAIL_USE_SSL = False
MAIL_USE_TLS = False
MAIL_USERNAME = ""
MAIL_PASSWORD = ""
MAIL_DEFAULT_SENDER = ("FlaskBB Mailer", "noreply@yourdomain")
# Where to logger should send the emails to
ADMINS = ["admin@yourdomain"]


# Logging Settings
# ------------------------------
# This config section will deal with the logging settings
# for FlaskBB, adjust as needed.

# Logging Config Path
# see https://docs.python.org/library/logging.config.html#logging.config.fileConfig
# for more details. Should either be None or a path to a file
# If this is set to a path, consider setting USE_DEFAULT_LOGGING to False
# otherwise there may be interactions between the log configuration file
# and the default logging setting.
#
# If set to a file path, this should be an absolute file path

LOG_CONF_FILE = None


# Path to store the INFO and ERROR logs
# If None this defaults to flaskbb/logs
#
# If set to a file path, this should be an absolute path
LOG_PATH = os.path.join(DefaultConfig.basedir, 'logs')

# The default logging configuration that will be used when
# USE_DEFAULT_LOGGING is set to True
LOG_DEFAULT_CONF = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'standard': {
            'format': '%(asctime)s %(levelname)-7s %(name)-25s %(message)s'
        },
        'advanced': {
            'format': '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        }
    },

    'handlers': {
        'console': {
            'level': 'NOTSET',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
        'flaskbb': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_PATH, 'flaskbb.log'),
            'mode': 'a',
            'maxBytes': 10485760,  # 10MB
            'backupCount': 5,
        },

        'infolog': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_PATH, 'info.log'),
            'mode': 'a',
            'maxBytes': 10485760,  # 10MB
            'backupCount': 5,
        },
        'errorlog': {
            'level': 'ERROR',
            'formatter': 'standard',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_PATH, 'error.log'),
            'mode': 'a',
            'maxBytes': 10485760,  # 10MB
            'backupCount': 5,
        }
    },

    'loggers': {
        'flask.app': {
            'handlers': ['infolog', 'errorlog'],
            'level': 'INFO',
            'propagate': True
        },
        'flaskbb': {
            'handlers': ['console', 'flaskbb'],
            'level': 'WARNING',
            'propagate': True
        },
    }
}

# When set to True this will enable the default
# FlaskBB logging configuration which uses the settings
# below to determine logging
USE_DEFAULT_LOGGING = True

# If SEND_LOGS is set to True, the admins (see the mail configuration) will
# recieve the error logs per email.
SEND_LOGS = False


# FlaskBB Settings
# ------------------------------ #
# URL Prefixes
FORUM_URL_PREFIX = ""
USER_URL_PREFIX = "/user"
MESSAGE_URL_PREFIX = "/message"
AUTH_URL_PREFIX = "/auth"
ADMIN_URL_PREFIX = "/admin"
# Remove dead plugins - useful if you want to migrate your instance
# somewhere else and forgot to reinstall the plugins.
# If set to `False` it will NOT remove plugins that are NOT installed on
# the filesystem (virtualenv, site-packages).
REMOVE_DEAD_PLUGINS = False


; file_name flaskbb.ini
[uwsgi]
base = /usr/local/var/www/my_code/python_web_development/flaskbb
home = /Users/yanzhipeng/.virtualenvs/flask2b/
pythonpath = /usr/local/var/www/my_code/python_web_development/flaskbb
socket = 127.0.0.1:30002
module = wsgi
wsgi-file = /usr/local/var/www/my_code/python_web_development/flaskbb/wsgi.py
callable = flaskbb
uid = yanzhipeng
gid = staff
logto = /usr/local/var/www/my_code/python_web_development/flaskbb/logs/uwsgi.log
master = true



; file_name flaskbb.peng
server {
    listen 80;
    server_name flaskbb.peng;

    access_log /usr/local/var/www/my_code/python_web_development/flaskbb/logs/access.forums.flaskbb.log;
    error_log /usr/local/var/www/my_code/python_web_development/flaskbb/logs/error.forums.flaskbb.log;

    location / {
        try_files $uri @flaskbb;
    }

    # Static files
    location /static {
       alias /usr/local/var/www/my_code/python_web_development/flaskbb/flaskbb/static;
    }

    location ~ ^/_themes/([^/]+)/(.*)$ {
        alias /usr/local/var/www/my_code/python_web_development/flaskbb/flaskbb/themes/$1/static/$2;
    }

    # robots.txt
    location /robots.txt {
   		alias /usr/local/var/www/my_code/python_web_development/flaskbb/flaskbb/static/robots.txt;
    }

    location @flaskbb {
        uwsgi_pass 127.0.0.1:30002;
        include uwsgi_params;
    }
}

>>> nice








```