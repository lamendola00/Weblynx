from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from flaskr import db
from datetime import datetime

class Link(db.Model):
    __tablename__ = 't_links'
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True)
    url = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    image_resized = Column(Text, nullable=True)
    image_original = Column(Text, nullable=True)
    tags = relationship("Tag", secondary="t_link_tags", backref="links")
    created_by = Column(Integer, ForeignKey('t_users.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    modified_by = Column(Integer, ForeignKey('t_users.id'), nullable=True)
    modified_at = Column(DateTime, onupdate=datetime.utcnow, nullable=True)
    
    created_by_user = relationship("User", foreign_keys=[created_by], backref="created_links")
    modified_by_user = relationship("User", foreign_keys=[modified_by], backref="modified_links")

    def __repr__(self):
        return f"<Link id={self.id}, url='{self.url}', description='{self.description}', image_resized='{self.image_resized}', image_original='{self.image_original}'>"
