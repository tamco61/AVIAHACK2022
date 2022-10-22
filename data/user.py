import sqlalchemy as db
from sqlalchemy import orm
import datetime
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class User(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer,  primary_key=True)
    username = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=True)
    privilege = db.Column(db.Integer,  nullable=True)

    driver =  orm.relation('Driver',  back_populates='user')