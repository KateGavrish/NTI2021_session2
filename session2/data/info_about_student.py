import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from data.db_session import SqlAlchemyBase


class InfoStudent(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'info_students'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    email = sqlalchemy.Column(sqlalchemy.String)

    year_bd = sqlalchemy.Column(sqlalchemy.Integer)
    month_bd = sqlalchemy.Column(sqlalchemy.Integer)
    day_bd = sqlalchemy.Column(sqlalchemy.Integer)
    place_bd = sqlalchemy.Column(sqlalchemy.String)

    sex = sqlalchemy.Column(sqlalchemy.Integer) #1 man 0 female
    phone = sqlalchemy.Column(sqlalchemy.String)
    flat = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    photo = sqlalchemy.Column(sqlalchemy.String)

    series = sqlalchemy.Column(sqlalchemy.Integer)
    number = sqlalchemy.Column(sqlalchemy.Integer)
    issues_by = sqlalchemy.Column(sqlalchemy.String)
    code = sqlalchemy.Column(sqlalchemy.String)
    date_of_issuance = sqlalchemy.Column(sqlalchemy.String)
    photo_passport = sqlalchemy.Column(sqlalchemy.String)

    index = sqlalchemy.Column(sqlalchemy.Integer)
    street = sqlalchemy.Column(sqlalchemy.String)
    city = sqlalchemy.Column(sqlalchemy.String)
    house = sqlalchemy.Column(sqlalchemy.String)
    number_flat = sqlalchemy.Column(sqlalchemy.Integer)
    isAgreement = sqlalchemy.Column(sqlalchemy.Boolean, default=False)




