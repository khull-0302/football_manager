from flask import Blueprint
import controllers

stadium = Blueprint('stadium', __name__)


@stadium.route("/stadium", methods=["POST"])
def add_stadium():
    return controllers.add_stadium()

@stadium.route("/stadiums", methods=["GET"])
def get_all_stadiums():
    return controllers.get_all_stadiums()

@stadium.route('/stadium/<stadium_id>', methods=['GET'])
def get_stadium_by_id(stadium_id):
    return controllers.get_stadium_by_id(stadium_id)

@stadium.route('/stadium/<stadium_id>', methods=['PUT'])
def update_stadium_by_id(stadium_id):
    return controllers.update_stadium_by_id(stadium_id)

@stadium.route("/stadium/delete/<stadium_id>", methods=["DELETE"])
def delete_stadium_by_id(stadium_id):
    return controllers.delete_stadium_by_id(stadium_id)