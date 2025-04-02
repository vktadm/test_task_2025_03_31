from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, current_user

from app.models import Role

bp = Blueprint("content", __name__, url_prefix="/")


@bp.route("", methods=["GET"])
@jwt_required()
def main():
    """Protected endpoint for all users."""

    return jsonify(
        {"message": "This is protected endpoint", "user": current_user.username}
    )


@bp.route("/admin", methods=["GET"])
@jwt_required()
def admin():
    """Protected endpoint for admin."""
    if current_user.role != Role.ADMIN:
        return jsonify({"message": "Access is denied"})
    return jsonify(
        {
            "message": "This is protected endpoint for admin",
            "user": current_user.username,
            "role": current_user.role.value,
        }
    )
