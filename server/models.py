from sqlalchemy import (
    Column,
    Integer,
    String,
    UniqueConstraint
)

from .database import Base, engine


class Link(Base):
    __tablename__ = 'link'

    id = Column(Integer, primary_key=True)
    url = Column(String, unique=True)
    short_url = Column(String)

    def __init__(self, url=None, short_url=None):
        self.url = None
        self.short_url = None

    @classmethod
    def add_link(cls, url):
        new_link = cls.__init__(name=url)
        cls.add(new_link)
        cls.commit()

    @classmethod
    def get(cls, id):
        res = cls.query.filter_by(id=id)
        row_val = res.all()
        if len(row_val) > 0:
            return row_val[0].url
        return None


Base.metadata.create_all(bind=engine)
