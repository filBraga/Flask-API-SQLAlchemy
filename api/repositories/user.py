from api.config.database import db
from api.entities.user import User

class UserRepository:
    def get_all(self):
        return [user.to_dict() for user in User.query.all()]

    def get_by_id(self, id):
        return user.to_dict() if (user := User.query.get(id)) else None

    def create(self, user_data):
        new_user = User(**user_data)
        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict()

    def update(self, id, user_data):
        user_to_update = User.query.get(id)
        if not user_to_update:
            return None

        # Update fields
        for key, value in user_data.items():
            setattr(user_to_update, key, value)

        db.session.commit()
        return user_to_update.to_dict()

    def delete(self, id):
        user_to_delete = User.query.get(id)
        if not user_to_delete:
            return False

        db.session.delete(user_to_delete)
        db.session.commit()
        return True
