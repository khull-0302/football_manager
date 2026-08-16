from flask import Blueprint
import controllers

division = Blueprint('division', __name__)


@division.route("/division", methods=["POST"])
def add_division():
    return controllers.add_division()

@division.route("/divisions", methods=["GET"])
def get_all_divisions():
    return controllers.get_all_divisions()