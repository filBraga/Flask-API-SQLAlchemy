from flask import Blueprint
from api.controllers.user import UserController

user_controller = UserController()
user = Blueprint('user', __name__)

@user.route('/user', methods=['GET'])
def get_all():
    return user_controller.get_all()

@user.route('/user/<int:id>', methods=['GET'])
def get_one(id: int):
    return user_controller.get_by_id(id)

@user.route('/user', methods=['POST'])
def create():
    return user_controller.create()

@user.route('/user/<id>', methods=['PUT'])
def update(id):
    return user_controller.update(id)

@user.route('/user/<int:id>', methods=['DELETE'])
def delete(id: int):
    return user_controller.delete(id)