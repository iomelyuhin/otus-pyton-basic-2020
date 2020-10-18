from dataclasses import dataclass

import asyncio
from aiohttp import ClientSession
from loguru import logger


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
    logger.info(result)
    return result


def get_users():
    return asyncio.run(fetch_users(jsp))


if __name__ == '__main__':
    get_users()
