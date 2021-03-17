import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_serializer import SerializerMixin

from data.db_session import SqlAlchemyBase


class Direction(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'direction'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    facult = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String, unique=True)
    budget_places = sqlalchemy.Column(sqlalchemy.Integer)
    is_budget = sqlalchemy.Column(sqlalchemy.Boolean)
    is_fiz = sqlalchemy.Column(sqlalchemy.Boolean)
    is_inf = sqlalchemy.Column(sqlalchemy.Boolean)

    subjects = sqlalchemy.Column(sqlalchemy.String)