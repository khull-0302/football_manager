
import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class Coaches(db.Model):
    __tablename__ = "Coaches"

    coach_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    team_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Teams.team_id"), nullable=False)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    years_coaching = db.Column(db.Integer())
    role = db.Column(db.String(), nullable=False)

    team = db.relationship("Teams", back_populates="coaches")

    def __init__(self, team_id, first_name, last_name, role, years_coaching=None):

        self.team_id = team_id
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.years_coaching = years_coaching

    def new_coach_object():
        return Coaches("", "", "", "", None)


class CoachesSchema(ma.Schema):
    class Meta:
        fields = ['coach_id', 'first_name', 'last_name', 'years_coaching', 'role', 'team']

    coach_id = ma.fields.UUID()
    first_name = ma.fields.String(required=True)
    last_name = ma.fields.String(required=True)
    years_coaching = ma.fields.Integer(allow_none=True)
    role = ma.fields.String(required=True)

    team = ma.fields.Nested("TeamsSchema", exclude=['coaches', 'stadium'])


coach_schema = CoachesSchema()
coaches_schema = CoachesSchema(many=True)

