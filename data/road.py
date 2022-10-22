import sqlalchemy as db
from sqlalchemy import orm
import datetime
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Road(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'road'
    id = db.Column(db.Integer, primary_key=True)
    source_point_id = db.Column(db.Integer, nullable=True)
    target_point_id = db.Column(db.Integer, nullable=True)
    distance = db.Column(db.Integer, nullable=True)

    driver = orm.relation('Driver',  back_populates='road')