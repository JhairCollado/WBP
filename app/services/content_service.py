from app.repositories.content_repository import ContentRepository

class ContentService:
    @staticmethod
    def create_content(data):
        return ContentRepository.create(data)

    @staticmethod
    def get_content_by_id(content_id):
        return ContentRepository.get_by_id(content_id)

    @staticmethod
    def update_content(content_id, data):
        return ContentRepository.update(content_id, data)

    @staticmethod
    def delete_content(content_id):
        return ContentRepository.delete(content_id)