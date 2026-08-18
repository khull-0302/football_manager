from flask import Blueprint
import controllers

coach = Blueprint('coach', __name__)


@coach.route("/coach", methods=["POST"])
def add_coach():
    return controllers.add_coach()

@coach.route("/coaches", methods=["GET"])
def get_all_coaches():
    return controllers.get_all_coaches()

@coach.route('/coach/<coach_id>', methods=['PUT'])
def update_coach_by_id(coach_id):
    return controllers.update_coach_by_id(coach_id)

@coach.route("/coach/delete/<coach_id>", methods=["DELETE"])
def delete_coach_by_id(coach_id):
    return controllers.delete_coach_by_id(coach_id)