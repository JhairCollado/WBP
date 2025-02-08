from app.models.content import Content

class ContentRepository:
    @staticmethod
    def create(data):
        content = Content(**data)
        db.session.add(content)
        db.session.commit()
        return content

    @staticmethod
    def get_by_id(content_id):
        return Content.query.get(content_id)

    @staticmethod
    def update(content_id, data):
        content = Content.query.get(content_id)
        for key, value in data.items():
            setattr(content, key, value)
        db.session.commit()
        return content

    @staticmethod
    def delete(content_id):
        content = Content.query.get(content_id)
        db.session.delete(content)
        db.session.commit()