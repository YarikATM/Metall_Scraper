from SoupScraper import parce
from Cities import Ekaterinburg, Krasnoyarsk, Tyumen, St_Petersburg, Chelyabinsk, Surgut
import datetime
import logging
import time
from DB.db import Database


async def Run(db: Database):
    start_time = time.time()
    logging.info("Запуск парсера")


    cities = {
        "Chelyabinsk": Chelyabinsk.GetCompanies(),
        "Ekaterinburg": Ekaterinburg.GetCompanies(),
        "Krasnoyarsk": Krasnoyarsk.GetCompanies(),
        "St_Petersburg": St_Petersburg.GetCompanies(),
        "Surgut": Surgut.GetCompanies(),
        "Tyumen": Tyumen.GetCompanies(),

    }

    soup = await parce()

    pricelist = []
    tm = datetime.datetime.now()
    for city in cities.values():
        for company in city:
            price = company.parse_data(soup)
            pricelist.extend(price)


    await db.compare_metal(pricelist)
    logging.info(f"The program completed the work in {round(time.time() - start_time, 2)} seconds")
