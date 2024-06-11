from flaskr import db

class LinkTag(db.Model):
    __tablename__ = 't_link_tags'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    link_id = db.Column(db.Integer, db.ForeignKey('t_links.id'), nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey('t_tags.id'), nullable=False)

    def __repr__(self):
        return f"<LinkTag id={self.id}, link_id={self.link_id}, tag_id={self.tag_id}>"
