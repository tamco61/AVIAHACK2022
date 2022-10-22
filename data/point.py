import sqlalchemy as db
from sqlalchemy import orm
import datetime
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Point(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'point'
    point_id = db.Column(db.Integer,  nullable=True)
    location_id = db.Column(db.Integer, primary_key=True)

    events = orm.relation('Event', back_populates='point')
