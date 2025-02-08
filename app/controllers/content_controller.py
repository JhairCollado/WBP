from flask import request, jsonify
from app.services.content_service import ContentService
from app.utils.auth import token_required

@token_required
def create_content():
    data = request.get_json()
    content = ContentService.create_content(data)
    return jsonify(content), 201

@token_required
def get_content(content_id):
    content = ContentService.get_content_by_id(content_id)
    return jsonify(content), 200

@token_required
def update_content(content_id):
    data = request.get_json()
    content = ContentService.update_content(content_id, data)
    return jsonify(content), 200

@token_required
def delete_content(content_id):
    ContentService.delete_content(content_id)
    return '', 204