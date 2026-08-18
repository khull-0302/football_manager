from flask import Blueprint
import controllers

user = Blueprint('user', __name__)


@user.route("/user", methods=["POST"])
def add_user():
    return controllers.add_user()

@user.route("/user/player", methods=["POST"])
def add_user_player_association():
    return controllers.add_user_player_association()


@user.route("/users", methods=["GET"])
def get_all_users():
    return controllers.get_all_users()

@user.route('/user/<user_id>', methods=['PUT'])
def update_user_by_id(user_id):
    return controllers.update_user_by_id(user_id)

@user.route("/user/delete/<user_id>", methods=["DELETE"])
def delete_user_by_id(user_id):
    return controllers.delete_user_by_id(user_id)
