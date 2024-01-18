import logging
from Scraper import Run
from env_reader_config import config
from db import Database
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler



def setup_logging() -> None:
    if config.DEBUG:
        logging.basicConfig(level=logging.DEBUG, filemode="a",
                            format="%(asctime)s %(levelname)s %(message)s")
    else:
        logging.basicConfig(level=logging.INFO, filemode="a",
                            format="%(asctime)s %(levelname)s %(message)s")



def setup_scheduler(db: Database, ) -> None:
    scheduler = AsyncIOScheduler(timezone="Asia/Yekaterinburg")

    scheduler.start()
    scheduler.add_job(Run, args=[db], trigger="interval", minutes=5)


async def setup_database(loop) -> Database:
    pool = Database(loop=loop, host=config.DB_HOST, user=config.DB_USER.get_secret_value(),
                    password=config.DB_PASSWORD.get_secret_value())
    await pool.connect()
    return pool


def main():
    setup_logging()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    db = loop.run_until_complete(setup_database(loop))

    setup_scheduler(db)



    loop.run_forever()



if __name__ == '__main__':
    main()
    # test()
