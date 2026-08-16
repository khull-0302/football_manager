from flask import jsonify, request
from flask_bcrypt import generate_password_hash
from db import db
from models.user import Users, user_schema, users_schema
from models.player import Players, player_schema, players_schema
from util.reflection import populate_object
from lib.authenticate import authenticate, authenticate_return_auth

def add_user():
    post_data = request.form if request.form else request.get_json()

    new_user = Users.new_user_obj()

    populate_object(new_user, post_data)

    new_user.password = generate_password_hash(new_user.password).decode("utf8")

    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"message": "unable to create record"}), 400

    return jsonify({"message": "user created", "result": user_schema.dump(new_user)}), 201


@authenticate_return_auth
def add_user_player_association(auth_info):
    post_data = request.form if request.form else request.json
    user_id = post_data.get('user_id')
    player_id = post_data.get('player_id')

    if auth_info.user.role != 'super-admin':
            return jsonify({"message": "unauthorized"}), 401

    user_query = db.session.query(Users).filter(Users.user_id == user_id).first()
    player_query = db.session.query(Players).filter(Players.player_id == player_id).first()

    if not user_query or not player_query:
        return jsonify({
            "message": "user or player record does not exist"
        }), 400
    
    if player_query in user_query.players:
        return jsonify({
            "message": "player is already a favorite"
        }), 400
    
    user_query.players.append(player_query)

    db.session.commit()

    return jsonify({
        "message": "player added to user", "result": user_schema.dump(user_query)
    })


@authenticate_return_auth
def get_all_users(auth_info):
    if auth_info.user.role != 'super-admin':
        return jsonify({"message": "unauthorized"}), 401
    
    users_query = db.session.query(Users).all()

    return jsonify({"message": "users found", "results": users_schema.dump(users_query)}), 200



