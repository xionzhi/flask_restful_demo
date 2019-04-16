"""
@Time    : 18-4-23 下午2:36
@Author  : xionzhi
@Desc    : 异常信息
"""

from flask import jsonify
from service import app


class _BaseExc(Exception):
    message = None
    status_code = 500

    def __init__(self, msg=None):
        self.message = msg or self.message

    def __str__(self):
        return self.message


class AccountNotFoundException(_BaseExc):
    message = '用户不存在'
    status_code = 400


class AccountPasswdErrorException(_BaseExc):
    message = '账号或密码错误'
    status_code = 400


class AccountRepeatException(_BaseExc):
    message = '账号已注册'
    status_code = 400


class AccountPasswdShortException(_BaseExc):
    message = '密码长度过短'
    status_code = 400


class RequestParameterException(_BaseExc):
    message = '请求参数错误'
    status_code = 401


class TokenNotFoundException(_BaseExc):
    message = '登陆已过期'
    status_code = 400


@app.errorhandler(Exception)
def coupon_not_exists_exception(error):
    if isinstance(error, _BaseExc):
        return jsonify({'code': error.status_code, 'message': error.message}), error.status_code
    return jsonify({'message': '你成功触发了一个异常'}), 500
