from flask import Blueprint
import controllers

division = Blueprint('division', __name__)


@division.route("/division", methods=["POST"])
def add_division():
    return controllers.add_division()

@division.route("/divisions", methods=["GET"])
def get_all_divisions():
    return controllers.get_all_divisions()

@division.route('/division/<division_id>', methods=['PUT'])
def update_division_by_id(division_id):
    return controllers.update_division_by_id(division_id)

@division.route("/division/delete/<division_id>", methods=["DELETE"])
def delete_division_by_id(division_id):
    return controllers.delete_division_by_id(division_id)