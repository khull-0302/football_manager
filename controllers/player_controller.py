from flask import jsonify, request

from db import db
from util.reflection import populate_object
from lib.authenticate import authenticate_return_auth, authenticate
from models.team import Teams, team_schema, teams_schema
from models.player import Players, player_schema, players_schema
from models.user import Users, user_schema, users_schema



@authenticate_return_auth
def add_player(auth_info):
    post_data = request.form if request.form else request.json

    team_id = post_data.get("team_id")

    if auth_info.user.role != 'super-admin':
        return jsonify({"message": "unauthorized"}), 401
    
    team_query = db.session.query(Teams).filter(Teams.team_id == team_id).first()

    if not team_query:
        return jsonify({"message": "team does not exist"}), 404

    new_player = Players.new_player_object()

    populate_object(new_player, post_data)

    try:
        db.session.add(new_player)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create record"}), 400
    
    return jsonify({"message": "player created", "result": player_schema.dump(new_player)}), 201


@authenticate
def get_player_by_id(player_id):
   
    player_query = db.session.query(Players).filter(Players.player_id == player_id).first()

    return jsonify ({
        "message": "player found",
        "results": player_schema.dump(player_query)
    }),200


@authenticate
def get_all_players():
    players_query = db.session.query(Players).all()
    
    return jsonify({"message": "players found", "results": players_schema.dump(players_query)}), 200


@authenticate
def get_players_by_team_id(team_id):
    
    players_query = db.session.query(Players).filter(Players.team_id == team_id).all()

    return jsonify ({
        "message": "players found",
        "results": players_schema.dump(players_query)
    }),200

@authenticate_return_auth
def get_my_players(auth_info):

    players_query = auth_info.user.players

    return jsonify({
        "message": "players found",
        "results": players_schema.dump(players_query)
    }), 200


@authenticate_return_auth
def update_player_by_id(player_id, auth_info):
    if auth_info.user.role != 'super-admin':
                return jsonify({"message": "unauthorized"}), 401
    
    post_data = request.form if request.form else request.json

    player_query = db.session.query(Players).filter(Players.player_id == player_id).first()

    if player_query:
        populate_object(player_query, post_data)

        try:
            db.session.commit()
        except:
            db.session.rollback()
            return jsonify({"message": "unable to update player"}), 400
        
        return jsonify({"message": "player updated", "result": player_schema.dump(player_query)}), 200
    
    return jsonify({"message": "unable to update player"}), 400

