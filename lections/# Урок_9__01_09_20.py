# Урок_9__01_09_20

# //!ASYNC IO
from loguru import logger #?Красивое оформление вывода в консоли

import asyncio #//?io - input-output


#?синхронный
def foo_sync():
	logger.info("foo_sync start")
	sleep(.1)
	logger.info("foo_sync finish")


def bar_sync():
	logger.info("foo_sync start")
	sleep(.1)
	logger.info("foo_sync finish")


def run_sync():
	logger.info("start sync")
	foo_sync()
	bar_sync()


# ?асинхронный
async def bar():
	logger.info("bar_async start")
	await asyncio.sleep(.1)
	logger.info("bar_async finish")


async def foo():
	logger.info("foo_async start")
	await asyncio.sleep(.1)
	logger.info("foo_async finish")


async def run_async():
	await bar()
	await foo()

# ! пример из жизни
from aiohttp import ClientSession
from dataclasses import dataclass

@dataclass
class Service:
	name: str
	url: str
	ip_field: str


SERVICES = [
	Service("ipify", "https://api.ipify.org/?format=json", "ip"),
	Service("ip-apy", "https://ip.api.com/json", "query"),
]

async def fetch(session: ClientSession, url: str) -> dict:
	async with session.get(url) as response:
		return await response.json

async  def fetch_ip(service: Service) -> str:
	my_ip = "not found"
	async with ClientSession() as session:
		result = await fetch(session. service.url)
	logger.info("Got result", service.name, result)
	return my_ip

def run_main_1():
	asyncio.run(fetch_ip(SERVICES[1]))


if __name__ == "__main__":
	# asyncio.run(run_async())
	run_main_1
