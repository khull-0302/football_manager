from flask import Blueprint
import controllers

coach = Blueprint('coach', __name__)


@coach.route("/coach", methods=["POST"])
def add_coach():
    return controllers.add_coach()

@coach.route("/coaches", methods=["GET"])
def get_all_coaches():
    return controllers.get_all_coaches()