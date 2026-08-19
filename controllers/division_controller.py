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


@authenticate
def get_division_by_id(division_id):
    
    division_query = db.session.query(Divisions).filter(Divisions.division_id == division_id).first()

    return jsonify ({
        "message": "division found",
        "results": division_schema.dump(division_query)
    }),200


@authenticate_return_auth
def update_division_by_id(division_id, auth_info):
    if auth_info.user.role != 'super-admin':
                return jsonify({"message": "unauthorized"}), 401
    
    post_data = request.form if request.form else request.json

    division_query = db.session.query(Divisions).filter(Divisions.division_id == division_id).first()

    if division_query:
        populate_object(division_query, post_data)

        try:
            db.session.commit()
        except:
            db.session.rollback()
            return jsonify({"message": "unable to update division"}), 400
        
        return jsonify({"message": "division updated", "result": division_schema.dump(division_query)}), 200
    
    return jsonify({"message": "unable to update division"}), 400


@authenticate_return_auth
def delete_division_by_id(division_id, auth_info):
    if auth_info.user.role != 'super-admin': 
            return jsonify({"message": "unauthorized"}), 401
    
    division_query = db.session.query(Divisions).filter(Divisions.division_id == division_id).first()

    if not division_query:
        return jsonify({"message": "division not found"}), 404

    db.session.delete(division_query)
    db.session.commit()

    return jsonify({
        "message": "division deleted"
    }), 200