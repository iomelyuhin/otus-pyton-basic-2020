from loguru import logger
from sqlalchemy.orm import sessionmaker, scoped_session

from fetch_todos import get_todos
from db import engine, Todo

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
s = Session()


def add_todos():
    for td in get_todos():
        logger.success("Задание: {}, для пользователя с id:{}", td["title"], td["userId"])
        todo = Todo(
            user_id=td["userId"],
            title=td["title"],
            completed=td["completed"],
        )
        s.add(todo)
        s.commit()
    s.close()


if __name__ == '__main__':
    add_todos()
