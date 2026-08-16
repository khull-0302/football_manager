from flask import jsonify, request
from flask_bcrypt import generate_password_hash
from db import db
from models.division import Divisions, division_schema, divisions_schema
from util.reflection import populate_object
from lib.authenticate import authenticate, authenticate_return_auth


@authenticate_return_auth
def add_division(auth_info):
    post_data = request.form if request.form else request.get_json()
    if auth_info.user.role != 'super-admin':
            return jsonify({"message": "unauthorized"}), 401

    new_division = Divisions.new_division_object()

    populate_object(new_division, post_data)

    try:
        db.session.add(new_division)
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"message": "unable to create record"}), 400

    return jsonify({"message": "division created", "result": division_schema.dump(new_division)}), 201


@authenticate
def get_all_divisions():
    divisions_query = db.session.query(Divisions).all()

    return jsonify({"message": "divisions found", "results": divisions_schema.dump(divisions_query)}), 200