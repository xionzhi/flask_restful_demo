"""
@Time    : 18-4-23 下午2:36
@Author  : xionzhi
@Desc    : 任务消息
"""

import time

from datetime import datetime

from service import (celery,
                     logger)


@celery.task
def async_test_log(message: str):
    """
    测试消息队列
    """
    time.sleep(5)

    logger.info(f"async_test_log: {message},{datetime.now()}")


# cat /usr/local/etc/supervisor.d/flask_demo.ini

# [program:flask-demo]
# directory = /Users/xionzhi/xionzDev/python_Dev/my/flask_demo
# command = /usr/local/anaconda3/envs/dev/bin/python /usr/local/anaconda3/envs/dev/bin/gunicorn -b 127.0.0.1:5002 runserver:app

# [program:flask-celery]
# directory = /Users/xionzhi/xionzDev/python_Dev/my/flask_demo
# command = /usr/local/anaconda3/envs/dev/bin/celery -A service.celery worker -l info -c 1
