from flask import Blueprint
import controllers

team = Blueprint('team', __name__)


@team.route("/team", methods=["POST"])
def add_team():
    return controllers.add_team()

@team.route("/teams", methods=["GET"])
def get_all_teams():
    return controllers.get_all_teams()