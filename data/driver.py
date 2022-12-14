import sqlalchemy as db
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Driver(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'driver'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    location = db.Column(db.Integer, db.ForeignKey('road.source_point_id'))
    status = db.Column(db.Integer, nullable=True)
    bus = db.Column(db.Integer, nullable=True)

    point = orm.relation('Road')
    id_user = orm.relation('User')
