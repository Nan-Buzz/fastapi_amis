from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from database import Base
from sqlalchemy import Boolean, Column, Integer, String, VARCHAR, BIGINT, ForeignKey
import uuid


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}



def gen_id():
    return uuid.uuid4().hex


# class AdminUser(Base):
#     """
#     管理员用户表
#     """
#     __tablename__ = "admin_user"
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(String(32), default=gen_id, comment="用户id")
#     email = Column(String(128), unique=True, index=True, nullable=False, comment="邮箱")
#     phone = Column(VARCHAR(16), unique=True, index=True, nullable=True, comment="手机号")
#     nickname = Column(String(128), comment="用户昵称")
#     avatar = Column(String(256), comment="用户头像")
#     hashed_password = Column(String(128), nullable=False, comment="密码")
#     is_active = Column(Boolean(), default=False, comment="邮箱是否激活")
#     role_id = Column(Integer, comment="角色表")

# @as_declarative
# class AdminRole(Base):
#     """
#     简单的用户角色表设计
#     """
#     role_id = Column(Integer, primary_key=True, index=True, comment="角色Id")
#     role_name = Column(String(64), comment="角色名字")
#     permission_id = Column(BIGINT, comment="权限ID")
#     re_mark = Column(String(128), comment="备注信息")

#     @declared_attr 
#     def __tablename__(cls) -> str:
#         import re 
#         # 如果没有指定__tablename__ 则默认使用model类名转换表名字 
#         name_list = re.findall(r"[A-Z][a-z\d]*", cls.__name__) 
#         # 表明格式替换成_格式 如 MallUser 替换成 mall_user 
#         return "_".join(name_list).lower()



