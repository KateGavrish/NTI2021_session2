import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_serializer import SerializerMixin

from data.db_session import SqlAlchemyBase


class UserStudent(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    surname = sqlalchemy.Column(sqlalchemy.String)
    middle_name = sqlalchemy.Column(sqlalchemy.String)
    sex = sqlalchemy.Column(sqlalchemy.Integer)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String)

    step1 = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    step2 = sqlalchemy.Column(sqlalchemy.Boolean, default=False)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)