from fetch_users import get_users
from fetch_todos import get_todos
from db import create_tables
from add_users_to_db import add_users
from add_todos_to_db import add_todos


def run_main():
    create_tables()
    get_users()
    get_todos()
    add_users()
    add_todos()


if __name__ == '__main__':
    run_main()
