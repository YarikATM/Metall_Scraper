from SoupScraper import parce
from Cities import Ekaterinburg, Krasnoyarsk, Tyumen, St_Petersburg, Chelyabinsk, Surgut
import datetime
import logging
import time

def int_or_float(obj):
    try:
        return float(obj)
    except:
        return 0.0


async def add_query(db, pricelist):
    query_select = "SELECT t1.* " \
                   "FROM Metall.Price t1 " \
                   "LEFT JOIN Metall.Price t2 " \
                   "    ON t1.Name = t2.Name AND t1.Company = t2.Company " \
                   "    AND t1.City = t2.City AND t1.time < t2.time " \
                   "WHERE t2.time IS NULL"

    res = await db.execute_query(query_select)
    if len(res) == 0:
        return
    res2 = []
    for i in res:
        res2.append(i[2:])

    new_pricelist = []
    for price in pricelist:
        if tuple(price[1:]) in res2:
            pass
        else:
            new_pricelist.append(price)

    if len(new_pricelist) > 0:
        query = "INSERT INTO Metall.Price (time, City, Company, Name, Price_Fiz, Price_Ur)  VALUES (%s,%s,%s,%s,%s,%s)"
        await db.execute_many(query, new_pricelist)
        logging.info(f"Обновлено {len(new_pricelist)} записей")


async def Run(db):
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


            # Проверка данных
            for i in range(len(price)):
                res = [tm]
                res.extend(price[i])
                price[i] = res
                price[i][-1] = int_or_float(price[i][-1])
                price[i][-2] = int_or_float(price[i][-2])

            pricelist.extend(price)

    await add_query(db, pricelist)
    logging.info(f"The program completed the work in {round(time.time() - start_time, 2)} seconds")