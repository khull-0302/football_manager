from flask import Blueprint
import controllers

player = Blueprint('player', __name__)


@player.route("/player", methods=["POST"])
def add_player():
    return controllers.add_player()

@player.route('/player/<player_id>', methods=['GET'])
def get_player_by_id(player_id):
    return controllers.get_player_by_id(player_id)

@player.route("/players", methods=["GET"])
def get_all_players():
    return controllers.get_all_players()

@player.route('/players/team/<team_id>', methods=['GET'])
def get_players_by_team_id(team_id):
    return controllers.get_players_by_team_id(team_id)

@player.route("/players/user", methods=["GET"])
def get_my_players():
    return controllers.get_my_players()

@player.route('/player/<player_id>', methods=['PUT'])
def update_player_by_id(player_id):
    return controllers.update_player_by_id(player_id)

@player.route("/player/delete/<player_id>", methods=["DELETE"])
def delete_player_by_id(player_id):
    return controllers.delete_player_by_id(player_id)

@player.route('/players/name/<first_name>', methods=['GET'])
def get_players_by_name(first_name):
    return controllers.get_players_by_name(first_name)