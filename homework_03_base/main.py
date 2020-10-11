import psycopg2
from loguru import logger

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password=""
)
logger.info(conn)

cur = conn.cursor()
logger.info(cur)

res = cur.execute("SELECT * FROM users;")
logger.info(res)

users = cur.fetchall()
logger.info(users)

cur.execute("INSERT INTO users (username, full_name) VALUES ('Vin', 'Diesel')")
conn.commit()
logger.info(users)

conn.close();