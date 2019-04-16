"""
@Time    : 18-4-23 下午2:36
@Author  : xionzhi
@Desc    : 入口
"""

import socket

from flask import Flask
from flask_restful import Api
from pymongo import MongoClient
from celery import Celery, platforms
from flask_bcrypt import Bcrypt
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

platforms.C_FORCE_ROOT = True

__all__ = [
    'app',
    'celery',
    'redis_store',
    'mongodb_client',
    'db',
    'ma',
    'api',
    'bcrypt',
    'logger'
]

app = Flask(__name__, static_folder='../static')

hostname = socket.gethostname()

if hostname == 'ProServiceName':
    app.config.from_object('config.pro')
else:
    app.config.from_object('config.dev')

app.debug = app.config['APP_DEBUG']
app.config['JSON_AS_ASCII'] = False

celery = Celery(__name__, broker=f'amqp://{app.config["BROKER_USER"]}:{app.config["BROKER_PWD"]}@'
                                 f'{app.config["BROKER_HOST"]}:{app.config["BROKER_PORT"]}/'
                                 f'{app.config["BROKER_VHOST"]}')
celery.conf.update(app.config)

app.config.setdefault('SQLALCHEMY_DATABASE_URI',
                      f'mysql+pymysql://{app.config["DATABASE_USER"]}:{app.config["DATABASE_PASSWORD"]}@'
                      f'{app.config["DATABASE_HOST"]}:{app.config["DATABASE_PORT"]}/{app.config["DATABASE_NAME"]}')
app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)
app.config.setdefault('SQLALCHEMY_ECHO', app.config['SQL_DEBUG'])
app.config.setdefault('SQLALCHEMY_POOL_RECYCLE', 3333)
app.config.setdefault('SQLALCHEMY_POOL_SIZE', 50)
app.config.setdefault('SQLALCHEMY_MAX_OVERFLOW', 50)

redis_store = FlaskRedis(app, decode_responses=True)
mongodb_client = MongoClient(host=app.config['MONGODB_HOST'], port=app.config['MONGODB_PORT'])
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)
bcrypt = Bcrypt(app)
logger = app.config['LOGGER']

app.config['UPLOADED_PHOTO_ALLOW'] = ('jpg', 'jpeg', 'png', 'gif')


def _route_init():
    from service.v1.urls import api as v1_api
    v1_api.init_app(app)


_route_init()
