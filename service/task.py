import time

from service import (celery,
                     logger)


@celery.task
def async_test_log(message: str):
    """
    测试消息队列
    """
    time.sleep(60)
    logger.error(f"async_test_log: {message}")


# cat /usr/local/etc/supervisor.d/flask_demo.ini

# [program:flask-demo]
# directory = /Users/xionzhi/xionzDev/python_Dev/my/flask_demo
# command = /usr/local/anaconda3/envs/dev/bin/python /usr/local/anaconda3/envs/dev/bin/gunicorn -b 127.0.0.1:5002 runserver:app

# [program:flask-celery]
# directory = /Users/xionzhi/xionzDev/python_Dev/my/flask_demo
# command = /usr/local/anaconda3/envs/dev/bin/celery -A service.celery worker -l info -c 1