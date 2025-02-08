from flask import request, jsonify
from app.services.user_service import UserService
from app.utils.auth import token_required

@token_required
def create_user():
    data = request.get_json()
    user = UserService.create_user(data)
    return jsonify(user), 201

@token_required
def get_user(user_id):
    user = UserService.get_user_by_id(user_id)
    return jsonify(user), 200

@token_required
def update_user(user_id):
    data = request.get_json()
    user = UserService.update_user(user_id, data)
    return jsonify(user), 200

@token_required
def delete_user(user_id):
    UserService.delete_user(user_id)
    return '', 204