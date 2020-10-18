from loguru import logger
from sqlalchemy.orm import sessionmaker, scoped_session

from fetch_users import get_users
from db import engine, User

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

s = Session()


def add_users():
    for u in get_users():
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
        logger.success("Пользователь {}({}) успешно добавлен!", u["username"], u["email"])
    s.close()


if __name__ == '__main__':
    add_users()
