import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db
from models.user_player_fav_xref import users_players_fav_table

class Players(db.Model):
    __tablename__ = "Players"

    player_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    position = db.Column(db.String(), nullable=False)
    height = db.Column(db.String())
    weight = db.Column(db.Integer())
    jersey_number = db.Column(db.Integer(), nullable=False)
    team_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Teams.team_id"), nullable=False)


    team = db.relationship("Teams", back_populates="players")
    users = db.relationship( "Users", secondary=users_players_fav_table, back_populates="players" )

    def __init__(self, first_name, last_name, position, jersey_number, team_id, height=None, weight=None):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.jersey_number = jersey_number
        self.team_id = team_id
        self.height = height
        self.weight = weight

    def new_player_object():
        return Players("", "", "", 0, "", None, None)

     

class PlayersSchema(ma.Schema):
    class Meta:
        fields = ['player_id', 'first_name', 'last_name', 'position', 'height', 'weight', 'jersey_number', 'team', 'users']

    player_id = ma.fields.UUID()
    first_name = ma.fields.String(required=True) 
    last_name = ma.fields.String(required=True) 
    position = ma.fields.String(required=True) 
    height = ma.fields.String(allow_none=True) 
    weight = ma.fields.Float(allow_none=True) 
    jersey_number = ma.fields.Integer(required=True)

    team = ma.fields.Nested("TeamsSchema", exclude=['players']) 
    users = ma.fields.Nested( "UsersSchema", many=True, exclude=['players', 'email', 'user_name'] )


player_schema = PlayersSchema()
players_schema = PlayersSchema(many=True)