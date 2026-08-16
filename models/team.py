import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db

class Teams(db.Model):
    __tablename__ = "Teams"

    team_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    team_name = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(), nullable=False, unique=True)
    net_worth = db.Column(db.Integer())
    division_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Divisions.division_id"), nullable=False)


    players = db.relationship("Players", back_populates="team", cascade="all, delete-orphan")
    coaches = db.relationship("Coaches", back_populates="team", cascade="all, delete-orphan")
    stadium = db.relationship("Stadiums", back_populates="team", uselist=False, cascade="all, delete-orphan")
    division = db.relationship("Divisions", back_populates="teams")

    def __init__(self, team_name, city, division_id, net_worth=None):
        self.team_name = team_name
        self.city = city
        self.division_id = division_id
        self.net_worth = net_worth

    def new_team_object():
        return Teams("", "", "", None)

class TeamsSchema(ma.Schema):
    class Meta:
        fields = ["team_id", "team_name", "city", "net_worth", "players", "coaches", "stadium", "division"]

    team_id = ma.fields.UUID()
    team_name = ma.fields.String(required=True)
    city = ma.fields.String(required=True)
    net_worth = ma.fields.Integer(allow_none=True)
    


    division = ma.fields.Nested("DivisionsSchema", exclude=['teams'])
    coaches = ma.fields.Nested("CoachesSchema", many=True, exclude=['team'])
    stadium = ma.fields.Nested("StadiumsSchema", exclude=['team'])
    players = ma.fields.Nested('PlayersSchema', many=True, exclude=['team', 'users'])
    
team_schema = TeamsSchema()
teams_schema = TeamsSchema(many=True)