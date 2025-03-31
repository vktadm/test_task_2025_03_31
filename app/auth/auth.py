from flask import Blueprint, request, jsonify, session

from . import utils_jwt
from .db_helper import validate_user

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/register", methods=["POST"])
def register():
    username = request.json.get("username")
    password = request.json.get("password")
    # Here you would hash the password and save the user to the database
    return jsonify(message="User: username, registered successfully"), 201


@bp.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    username = validate_user(username, password)
    jwt_payload = {
        "sub": username,
        "username": username,
    }
    access_token = utils_jwt.encode_jwt(payload=jwt_payload)
    return jsonify({"token": access_token}), 200
