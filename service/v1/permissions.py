from functools import wraps

from service import redis_store, logger
from service.common import TokenNotFoundException


def verify_token(request):
    '''
    verify request token
    '''
    def wrapper(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            try:
                token = request.environ.get('HTTP_TOKEN')
                if token is None:
                    raise TokenNotFoundException
                if redis_store.exists(f'token:{token}') == 1:
                    login_user_info = redis_store.hgetall(f'token:{token}')
                    if login_user_info is None:
                        raise ReLoginException
                    setattr(request, 'login_user_info', login_user_info)
                    return func(*args, **kwargs)
                else:
                    raise TokenNotFoundException
            except Exception as e:
                logger.error(e)
                raise e
        return _wrapper
    return wrapper
