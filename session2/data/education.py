import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from data.db_session import SqlAlchemyBase


class EducationStudent(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'education_students'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    certificate_number = sqlalchemy.Column(sqlalchemy.Integer)
    is_scan = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    form_of_education = sqlalchemy.Column(sqlalchemy.Integer, default=0) # 1-platnoe 0-besplatnoe
    math = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    russian = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    informat = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    fizika = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    direct = sqlalchemy.Column(sqlalchemy.String)
    is_id = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    is_id_scan = sqlalchemy.Column(sqlalchemy.Boolean, default=False)

    is_original = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    is_sogl_to_zach = sqlalchemy.Column(sqlalchemy.Boolean, default=False)


