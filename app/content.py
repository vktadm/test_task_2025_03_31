from flask import Blueprint, jsonify, request

from app.redis_client import get_redis_client
from app.auth.utils_jwt import token_required

bp = Blueprint("content", __name__, url_prefix="/")


@bp.route("", methods=["GET"])
@token_required
def main():
    return jsonify({"message": "Hello"})


@bp.route("set/", methods=["POST"])
def set_value():
    data = request.json
    if data["key"] and data["value"]:
        redis_client = get_redis_client()
        redis_client.set(name=data["key"], value=data["value"])
        return jsonify({"message": f"Value set for {data["key"]}"}), 200
    return jsonify({"message": "Value doesn't set"}), 400


@bp.route("get/", methods=["GET"])
def get_value():
    data = request.json
    redis_client = get_redis_client()
    value = redis_client.get(data["key"])
    if value:
        return jsonify({"key": data["key"], "value": value.decode("utf-8")}), 200
    return jsonify({"message": "Key not found"}), 404
