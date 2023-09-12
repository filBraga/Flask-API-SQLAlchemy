from api.repositories.user import UserRepository

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_all(self):
        return self.user_repository.get_all()
    
    def get_by_id(self, id):
        return self.user_repository.get_by_id(id)
    
    def create(self, user):
        return self.user_repository.create(user)

    def update(self, id, user):
        updated_user = self.user_repository.update(id, user)
        return updated_user is not None

    def delete(self, id):
        success = self.user_repository.delete(id)
        return success
