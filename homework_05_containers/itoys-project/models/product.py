from sqlalchemy import Column, Integer, String, Boolean

from .database import db


class Product(db.Model):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    img_href = Column(String, nullable=False)
    price = Column(Integer, nullable=False, default=0)
    is_sale = Column(Boolean, default=False, server_default='0')
    deleted = Column(Boolean, default=False, server_default='0')
