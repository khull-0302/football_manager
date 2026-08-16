
import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class Divisions(db.Model):
    __tablename__ = "Divisions"

    division_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    division_name = db.Column(db.String(), nullable=False)
    conference = db.Column(db.String(), nullable=False)

    teams = db.relationship("Teams", back_populates="division")

    def __init__(self, division_name, conference):
        self.division_name = division_name
        self.conference = conference

    def new_division_object():
        return Divisions("", "")


class DivisionsSchema(ma.Schema):
    class Meta:
        fields = ['division_id', 'division_name', 'conference', 'teams']

    division_id = ma.fields.UUID()
    division_name = ma.fields.String(required=True)
    conference = ma.fields.String(required=True)

    teams = ma.fields.Nested("TeamsSchema", many=True, exclude=['division'])


division_schema = DivisionsSchema()
divisions_schema = DivisionsSchema(many=True)

