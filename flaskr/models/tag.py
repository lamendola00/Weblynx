from flaskr import db

class Tag(db.Model):
    __tablename__ = 't_tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)

    def __repr__(self):
        return f"<Tag id={self.id}, name='{self.name}'>"
