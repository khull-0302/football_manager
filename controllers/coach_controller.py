from flask import jsonify, request

from db import db
from util.reflection import populate_object
from lib.authenticate import authenticate_return_auth, authenticate
from models.team import Teams, team_schema, teams_schema
from models.player import Players, player_schema, players_schema
from models.coach import Coaches, coach_schema, coaches_schema



@authenticate_return_auth
def add_coach(auth_info):
    post_data = request.form if request.form else request.json

    team_id = post_data.get("team_id")

    if auth_info.user.role != 'super-admin':
        return jsonify({"message": "unauthorized"}), 401
    
    team_query = db.session.query(Teams).filter(Teams.team_id == team_id).first()

    if not team_query:
        return jsonify({"message": "team does not exist"}), 404

    new_coach = Coaches.new_coach_object()

    populate_object(new_coach, post_data)

    try:
        db.session.add(new_coach)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create record"}), 400
    
    return jsonify({"message": "coach created", "result": coach_schema.dump(new_coach)}), 201


@authenticate
def get_all_coaches():
    coaches_query = db.session.query(Coaches).all()
    
    return jsonify({"message": "coaches found", "results": coaches_schema.dump(coaches_query)}), 200


@authenticate_return_auth
def update_coach_by_id(coach_id, auth_info):
    if auth_info.user.role != 'super-admin':
                return jsonify({"message": "unauthorized"}), 401
    
    post_data = request.form if request.form else request.json

    coach_query = db.session.query(Coaches).filter(Coaches.coach_id == coach_id).first()

    if coach_query:
        populate_object(coach_query, post_data)

        try:
            db.session.commit()
        except:
            db.session.rollback()
            return jsonify({"message": "unable to update coach"}), 400
        
        return jsonify({"message": "coach updated", "result": coach_schema.dump(coach_query)}), 200
    
    return jsonify({"message": "unable to update coach"}), 400


@authenticate_return_auth
def delete_coach_by_id(coach_id, auth_info):
    if auth_info.user.role != 'super-admin': 
            return jsonify({"message": "unauthorized"}), 401
    
    coach_query = db.session.query(Coaches).filter(Coaches.coach_id == coach_id).first()

    if not coach_query:
        return jsonify({"message": "coach not found"}), 404

    db.session.delete(coach_query)
    db.session.commit()

    return jsonify({
        "message": "coach deleted"
    }), 200