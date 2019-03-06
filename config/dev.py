import os
import logging.handlers

from datetime import timedelta


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

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# log conf
log_file = base_dir + '/log/' + 'service.log'
handler = logging.handlers.TimedRotatingFileHandler(log_file, 'D', 1, 7)
fmt = '%(levelname)s %(asctime)s %(pathname)s [line:%(lineno)d] %(message)s'
formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(handler)
LOGGER.setLevel(logging.INFO)
