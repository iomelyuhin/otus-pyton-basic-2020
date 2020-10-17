import asyncio
from dataclasses import dataclass
from datetime import datetime

from aiohttp import ClientSession
from loguru import logger
from sqlalchemy import create_engine, Table, Column, Integer, String, DateTime, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine('postgresql://postgres:@localhost/postgres')
# metadata = MetaData()
Base = declarative_base(bind=engine)

session_factory = sessionmaker(bind=engine)

users_table = Table(
    "users",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("id_in_services", Integer),
    Column("created_at", DateTime, default=datetime.utcnow),
    Column("name", String(), unique=True),
    Column("email", String(), unique=True),
    Column("city", String()),
    Column("company", String()),
    Column("website", String(), unique=True)
)


class User(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    id_in_services = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    name = Column(String, unique=True)
    email = Column(String, unique=True)
    city = Column(String)
    company = Column(String)
    website = Column(String, unique=True)


@dataclass
class Service:
    name: str
    url: str


jsp = Service("jsp", "http://jsonplaceholder.typicode.com/users")


async def fetch(session: ClientSession, url: str) -> dict:
    """
    :param session:
    :param url:
    :return:
    """
    async with session.get(url) as response:
        return await response.json()


async def fetch_users(service: Service):
    """
    :param service:
    :return:
    """
    async with ClientSession() as session:
        result = await fetch(session, service.url)
    logger.info("Найдено {} пользователей", len(result))
    for u in result:
        s = Session()
        logger.success("Пользователь {}({}) успешно добавлен!", u["username"], u["email"])
        user = User(
            id_in_services=u["id"],
            name=u["username"],
            email=u["email"],
            city=u["address"]["city"],
            company=u["company"]["name"],
            website=u["website"]
        )
        s.add(user)
        s.commit()
    return result


def run_main():
    asyncio.run(fetch_users(jsp))


if __name__ == '__main__':
    Base.metadata.create_all()
    run_main()
