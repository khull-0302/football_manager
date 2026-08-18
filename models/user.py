import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db
from models.user_player_fav_xref import users_players_fav_table

class Users(db.Model):
    __tablename__ = "Users"

    user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_name = db.Column(db.String(), nullable=False, unique=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    role = db.Column(db.String(), nullable=False, default="user")
    active = db.Column(db.Boolean(), default=True)

    
    auth = db.relationship("AuthTokens", back_populates="user", cascade="all, delete-orphan")
    players = db.relationship( "Players", secondary=users_players_fav_table, back_populates="users" )


    def __init__(self, user_name, email, password, role='user', active=True):
        self.user_name = user_name
        self.email = email
        self.password = password
        self.role = role
        self.active = active

    def new_user_obj():
        return Users("", "", "", "user", True)

     
class UsersSchema(ma.Schema):
    class Meta:
        fields = ['user_id', 'user_name', 'email', 'role', 'active', 'players']

    user_id = ma.fields.UUID()
    user_name = ma.fields.String(required=True)
    email = ma.fields.String(required=True)
    role = ma.fields.String(dump_default="user")
    active = ma.fields.Boolean(dump_default=True)

    players = ma.fields.Nested("PlayersSchema", many=True, exclude=['users'] )



user_schema = UsersSchema()
users_schema = UsersSchema(many=True)