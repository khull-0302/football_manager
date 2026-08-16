
import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class Stadiums(db.Model):
    __tablename__ = "Stadiums"

    stadium_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    stadium_name = db.Column(db.String(), nullable=False)
    state = db.Column(db.String(), nullable=False)
    capacity = db.Column(db.Integer())
    debut_year = db.Column(db.Integer())
    team_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Teams.team_id"), nullable=False)


    team = db.relationship("Teams", back_populates="stadium")

    def __init__(self, team_id, stadium_name, state, capacity=None, debut_year=None):

        self.team_id = team_id
        self.stadium_name = stadium_name
        self.state = state
        self.capacity = capacity
        self.debut_year = debut_year

    def new_stadium_object():
        return Stadiums("", "", "", None, None)


class StadiumsSchema(ma.Schema):
    class Meta:
        fields = ['stadium_id', 'team_id', 'stadium_name', 'state', 'capacity', 'debut_year', 'team']

    stadium_id = ma.fields.UUID()
    team_id = ma.fields.UUID()
    stadium_name = ma.fields.String(required=True)
    state = ma.fields.String(required=True)
    capacity = ma.fields.Integer(allow_none=True)
    debut_year = ma.fields.Integer(allow_none=True)

    team = ma.fields.Nested("TeamsSchema", exclude=['stadium', "players"])


stadium_schema = StadiumsSchema()
stadiums_schema = StadiumsSchema(many=True)
