"""
@Time    : 18-4-23 下午2:36
@Author  : xionzhi
@Desc    : 路由
"""

from service import api
from service.v1.views.login_view import (LoginView)
from service.v1.views.user_view import (UserView)


api.add_resource(LoginView, '/v1/login')
api.add_resource(UserView, '/v1/user')
