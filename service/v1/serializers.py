from marshmallow import fields

from service import ma, redis_store
from service.models import (DIDUserModel,
                            DIDGroupModel,)
from service.models import (DICUserStatusModel,
                            DICGroupTypeModel,
                            DICGroupStatusModel)


class BaseSchema(ma.Schema):
    id = fields.Integer()
    ctime = fields.DateTime(format='%Y-%m-%d %H:%M:%S')
    mtime = fields.DateTime(format='%Y-%m-%d %H:%M:%S')
    create_time_unix = fields.Integer()
    modify_time_unix = fields.Integer()


class DIDUserSchema(BaseSchema):
    uname = fields.String()
    phone = fields.String()
    email = fields.String()
    photo = fields.String()
    group_id = fields.Integer()
    status = fields.Integer()

    class Meta:
        model = DIDUserModel
        fields = ('id', 'ctime', 'mtime', 'create_time_unix', 'modify_time_unix',
                  'uname', 'phone', 'email', 'photo', 'group_id', 'status')


class DIDGroupSchema(BaseSchema):
    gname = fields.String()
    group_type = fields.Integer()
    status = fields.Integer()

    class Meta:
        model = DIDGroupModel
        fields = ('id', 'ctime', 'mtime', 'create_time_unix', 'modify_time_unix',
                  'gname', 'group_type', 'status')


############################################################
class DICUserStatusSchema(BaseSchema):
    class Meta:
        model = DICUserStatusModel


class DICGroupTypeSchema(BaseSchema):
    class Meta:
        model = DICGroupTypeModel


class DICGroupStatusSchema(BaseSchema):
    class Meta:
        model = DICGroupStatusModel
