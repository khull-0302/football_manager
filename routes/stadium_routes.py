from flask import Blueprint
import controllers

stadium = Blueprint('stadium', __name__)


@stadium.route("/stadium", methods=["POST"])
def add_stadium():
    return controllers.add_stadium()

@stadium.route("/stadiums", methods=["GET"])
def get_all_stadiums():
    return controllers.get_all_stadiums()