
from flask import Blueprint, request, jsonify
from .models import User
from . import db

bp = Blueprint('main', __name__)

@bp.route('/users', methods=['GET'])
def list_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name} for u in users])

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(name=data['name'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"id": new_user.id, "name": new_user.name}), 201

@bp.route('/add_user')
def add_user():
    new_user = User(name="Carlos")
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": f"User {new_user.name} added with id {new_user.id}"})

