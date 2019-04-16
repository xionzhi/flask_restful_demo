"""
@Time    : 18-4-23 下午2:36
@Author  : xionzhi
@Desc    : 开发模式配置文件
"""

import os
import logging.handlers


APP_DEBUG = True

# mysql conf
SQL_DEBUG = True
DATABASE_HOST = '127.0.0.1'
DATABASE_PASSWORD = '123456'
DATABASE_USER = 'root'
DATABASE_NAME = 'dbtmp'
DATABASE_PORT = 3306

# redis conf
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 10
REDIS_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'

# mongo conf
MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017

# broker conf
BROKER_USER = 'guest'
BROKER_PWD = 'guest'
BROKER_VHOST = '/'
BROKER_HOST = '127.0.0.1'
BROKER_PORT = 5672
TASK_SERIALIZER = 'pickle'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ACCEPT_CONTENT = ['json', 'msgpack']
CELERY_TASK_SERIALIZER = 'msgpack'
CELERY_EVENT_SERIALIZER = 'msgpack'
CELERY_RESULT_SERIALIZER = 'json'
BROKER_POOL_LIMIT = 10
CELERY_MAX_TASKS_PER_CHILD = 100
CELERY_IMPORTS = (
    'service.task',
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# log conf
LOG_FILE = BASE_DIR + '/log/' + 'service.log'
HANDLER = logging.handlers.TimedRotatingFileHandler(LOG_FILE, 'D', 1, 7)
LOG_FMT = '%(levelname)s %(asctime)s %(pathname)s [line:%(lineno)d] %(message)s'
LOG_FORMATTER = logging.Formatter(LOG_FMT)
HANDLER.setFormatter(LOG_FORMATTER)

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(HANDLER)
LOGGER.setLevel(logging.INFO)
