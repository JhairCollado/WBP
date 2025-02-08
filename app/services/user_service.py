from app.repositories.user_repository import UserRepository

class UserService:
    @staticmethod
    def create_user(data):
        return UserRepository.create(data)

    @staticmethod
    def get_user_by_id(user_id):
        return UserRepository.get_by_id(user_id)

    @staticmethod
    def update_user(user_id, data):
        return UserRepository.update(user_id, data)

    @staticmethod
    def delete_user(user_id):
        return UserRepository.delete(user_id)