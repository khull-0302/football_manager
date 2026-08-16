from flask import jsonify, request

from db import db
from models.team import Teams, team_schema, teams_schema
from util.reflection import populate_object
from lib.authenticate import authenticate_return_auth, authenticate


@authenticate_return_auth
def add_team(auth_info):
    if auth_info.user.role != 'super-admin':
        return jsonify({"message": "unauthorized"}), 401
    
    post_data = request.form if request.form else request.get_json()

    new_team = Teams.new_team_object()

    populate_object(new_team, post_data)

    try:
        db.session.add(new_team)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print("ERROR:", e)
        return jsonify({"message": "unable to create record"}), 400

    return jsonify({"message": "team created", "result": team_schema.dump(new_team)}), 201


@authenticate
def get_all_teams():
    teams_query = db.session.query(Teams).all()

    return jsonify({"message": "teams found", "results": teams_schema.dump(teams_query)}), 200