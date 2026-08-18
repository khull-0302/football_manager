from flask import Blueprint
import controllers

team = Blueprint('team', __name__)


@team.route("/team", methods=["POST"])
def add_team():
    return controllers.add_team()

@team.route("/teams", methods=["GET"])
def get_all_teams():
    return controllers.get_all_teams()

@team.route('/team/<team_id>', methods=['PUT'])
def update_team_by_id(team_id):
    return controllers.update_team_by_id(team_id)

@team.route("/team/delete/<team_id>", methods=["DELETE"])
def delete_team_by_id(team_id):
    return controllers.delete_team_by_id(team_id)