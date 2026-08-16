from flask import jsonify, request

from db import db
from util.reflection import populate_object
from lib.authenticate import authenticate_return_auth, authenticate
from models.team import Teams, team_schema, teams_schema
from models.player import Players, player_schema, players_schema
from models.stadium import Stadiums, stadium_schema, stadiums_schema



@authenticate_return_auth
def add_stadium(auth_info):
    post_data = request.form if request.form else request.json

    team_id = post_data.get("team_id")

    if auth_info.user.role != 'super-admin':
        return jsonify({"message": "unauthorized"}), 401
    
    team_query = db.session.query(Teams).filter(Teams.team_id == team_id).first()

    if not team_query:
        return jsonify({"message": "team does not exist"}), 404

    new_stadium = Stadiums.new_stadium_object()

    populate_object(new_stadium, post_data)

    try:
        db.session.add(new_stadium)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create record"}), 400
    
    return jsonify({"message": "stadium created", "result": stadium_schema.dump(new_stadium)}), 201


@authenticate
def get_all_stadiums():
    stadiums_query = db.session.query(Stadiums).all()
    
    return jsonify({"message": "stadiums found", "results": stadiums_schema.dump(stadiums_query)}), 200