from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint("content", __name__, url_prefix="/")


@bp.route("", methods=["GET"])
@jwt_required()
def main():
    current_user = get_jwt_identity()
    return jsonify({"message": "This is protected endpoint", "user": current_user})
