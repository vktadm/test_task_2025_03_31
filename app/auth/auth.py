from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt

from app.auth.db_helper import validate_user, create_user
from app.auth.utils_jwt import set_jwt_token, revoked_jwt_token


bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    if not validate_user(username, password):
        return jsonify({"message": "Invalid login or password"}), 401

    return jsonify(set_jwt_token(username)), 200


@bp.route("/logout", methods=["DELETE"])
@jwt_required()
def logout():
    jti = get_jwt().get("jti")
    revoked_jwt_token(jti)
    return jsonify({"message": "Access token revoked"}), 401


@bp.route("/register", methods=["POST"])
def register():
    username = request.json.get("username")
    password = request.json.get("password")
    if username and password:
        user = create_user(username, password)
        if not user:
            return jsonify({"message": f"User: {username} already exists"}), 409
    return jsonify({"message": f"User: {username}, registered successfully"}), 201
