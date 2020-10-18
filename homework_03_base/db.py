from datetime import datetime

from loguru import logger
from sqlalchemy import create_engine, Integer, Column, DateTime, String, Boolean, MetaData
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://postgres:@localhost/postgres')
Base = declarative_base(bind=engine)
metadata = MetaData()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    id_in_services = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    name = Column(String(), unique=True)
    email = Column(String(), unique=True)
    city = Column(String())
    company = Column(String())
    website = Column(String(), unique=True)


class Todo(Base):
    __tablename__ = "users_todos"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    completed = Column(Boolean, default=False)
    title = Column(String())


def create_tables():
    Base.metadata.create_all()
    logger.info('Все таблицы созданы успешно')


if __name__ == '__main__':
    Base.metadata.create_all()
