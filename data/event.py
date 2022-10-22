import sqlalchemy as db
from sqlalchemy import orm
import datetime
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Event(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'Event'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flights = db.Column(db.Integer, nullable=True)
    date = db.Column(db.DateTime, default=datetime.datetime.now)
    point_id = db.Column(db.Integer, db.ForeignKey('point.location_id'))
    gate_id = db.Column(db.Integer, db.ForeignKey('point.location_id'))
    number_passengers = db.Column(db.Integer, nullable=True)

    point = orm.relation('Point')