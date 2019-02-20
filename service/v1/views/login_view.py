from uuid import uuid1
from flask import request
from sqlalchemy import func, and_, or_
from flask_bcrypt import check_password_hash
from flask_restful import Resource

from service import (db, logger, redis_store)
from service.v1.permissions import verify_token
from service.common import (AccountNotFoundException,
                            AccountPasswdErrorException)
from service.models import (DIDUserModel,
                            DIDGroupModel)
from service.models import (DICUserStatusModel,
                            DICGroupTypeModel,
                            DICGroupStatusModel)


class LoginView(Resource):
    def post(self):
        _passwd = request.json.get('passWord')
        _phone = request.json.get('phoneNumber')

        try:
            if None in (_passwd, _phone):
                raise RequestParameterException

            user_query = db.session.query(DIDUserModel.id,
                                          DIDUserModel.uname,
                                          DIDUserModel.passwd,
                                          DIDUserModel.phone,
                                          DIDUserModel.email). \
                filter(DIDUserModel.phone == _phone).first()
            if user_query is None:
                raise AccountNotFoundException
            
            if check_password_hash(user_query.passwd, _passwd) is False:
                raise AccountPasswdErrorException

            token = uuid1().hex
            login_user_info = {
                'id': user_query.id,
                'uname': user_query.uname,
                'phone': user_query.phone,
                'email': user_query.email
            }
            redis_store.hmset(f'token:{token}', login_user_info)
            redis_store.expire(f'token:{token}', 60 * 5)

            return {'code': 200, 'token': token, 'login_user_info': login_user_info}
        except Exception as e:
            logger.error(e)
            db.session.rollback()
            raise e
        