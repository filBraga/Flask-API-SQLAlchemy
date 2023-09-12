from flask import request, jsonify

from api.services.user import UserService

class UserController:
    def __init__(self):
        self.user_service = UserService()

    def get_all(self):
        users = self.user_service.get_all()
        return jsonify(users), 200  # OK status code
    
    def get_by_id(self, id):
        user = self.user_service.get_by_id(id)
        if not user:
            return jsonify({"error": "User not found"}), 404  # NOT FOUND status code
        return jsonify(user), 200  # OK status code
    
    def create(self):
        user_data = request.get_json()
        if not user_data:
            return jsonify({"error": "Invalid input"}), 400  # BAD REQUEST status code
        user = self.user_service.create(user_data)
        return jsonify(user), 201  # CREATED status code

    def update(self, id):
        user_data = request.get_json()
        if not user_data:
            return jsonify({"error": "Invalid input"}), 400  # BAD REQUEST status code
        user = self.user_service.update(id, user_data)
        if not user:
            return jsonify({"error": "User not found"}), 404  # NOT FOUND status code
        return jsonify(user), 200  # OK status code

    def delete(self, id):
        success = self.user_service.delete(id)
        if not success:
            return jsonify({"error": "User not found or could not be deleted"}), 404  # NOT FOUND status code
        return jsonify({"message": "User deleted successfully"}), 200  # OK status code
