import time

from service import db, bcrypt
from datetime import datetime

from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.dialects.mysql import DATETIME, VARCHAR, INTEGER, TINYINT, TEXT


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(INTEGER, primary_key=True)
    ctime = db.Column(DATETIME, nullable=False, default=datetime.now)
    mtime = db.Column(DATETIME, nullable=False, default=datetime.now, onupdate=datetime.now)
    create_time_unix = db.Column(INTEGER, nullable=False, default=time.time)
    modify_time_unix = db.Column(INTEGER, nullable=False, default=time.time, onupdate=time.time)


class DIDUserModel(BaseModel):
    __tablename__ = 'did_user'
    '''
    CREATE TABLE `did_user` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `uname` varchar(50) DEFAULT NULL COMMENT '用户名称',
      `passwd` varchar(100) DEFAULT NULL COMMENT '密码',
      `phone` varchar(15) DEFAULT NULL COMMENT '电话号码',
      `email` varchar(50) DEFAULT NULL COMMENT '邮件地址',
      `photo` varchar(50) DEFAULT NULL COMMENT '头像照片',
      `group_id` int(11) NOT NULL COMMENT '所属组 ID',
      `status` tinyint(4) NOT NULL COMMENT '用户状态',
      `ctime` datetime DEFAULT NULL COMMENT '创建时间',
      `mtime` datetime DEFAULT NULL COMMENT '修改时间',
      `create_time_unix` int(11) DEFAULT NULL COMMENT '创建时间 UNIX',
      `modify_time_unix` int(11) DEFAULT NULL COMMENT '修改时间 UNIX',
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户信息表'
    '''
    uname = db.Column(VARCHAR(50), comment='用户名称')
    passwd = db.Column(VARCHAR(100), comment='密码')
    phone = db.Column(VARCHAR(15), comment='电话号码')
    email = db.Column(VARCHAR(50), comment='邮件地址')
    photo = db.Column(VARCHAR(50), comment='头像照片')
    group_id = db.Column(INTEGER, comment='所属组id')
    status = db.Column(TINYINT(4), nullable=False, default=1, comment='用户状态')

    @hybrid_property
    def _password(self):
        return self.passwd

    @_password.setter
    def _password(self, pwd):
        self.passwd = bcrypt.generate_password_hash(pwd)


class DIDGroupModel(BaseModel):
    __tablename__ = 'did_group'
    '''
    CREATE TABLE `did_group` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `gname` varchar(50) DEFAULT NULL COMMENT '组织名称',
      `group_type` tinyint(4) NOT NULL DEFAULT '2' COMMENT '组织类型',
      `status` tinyint(4) NOT NULL DEFAULT '1' COMMENT '组织状态',
      `ctime` datetime DEFAULT NULL COMMENT '创建时间',
      `mtime` datetime DEFAULT NULL COMMENT '修改时间',
      `create_time_unix` int(11) DEFAULT NULL COMMENT '创建时间 UNIX',
      `modify_time_unix` int(11) DEFAULT NULL COMMENT '修改时间 UNIX',
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='组织信息表'
    '''
    gname = db.Column(VARCHAR(50), comment='组织名称')
    group_type = db.Column(TINYINT(4), nullable=False, default=2, comment='组织类型')
    status = db.Column(TINYINT(4), nullable=False, default=1, comment='组织状态')


#######################################################################
class DICUserStatusModel(BaseModel):
    __tablename__ = 'dic_user_status'

    status_id = db.Column(TINYINT(4))
    status_name = db.Column(VARCHAR(20))


class DICGroupTypeModel(BaseModel):
    __tablename__ = 'dic_group_type'

    type_id = db.Column(TINYINT(4))
    type_name = db.Column(VARCHAR(20))


class DICGroupStatusModel(BaseModel):
    __tablename__ = 'dic_group_status'

    status_id = db.Column(TINYINT(4))
    status_name = db.Column(VARCHAR(20))
