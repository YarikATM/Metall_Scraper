import aiohttp
import asyncio
import logging
from bs4 import BeautifulSoup
from config.config import urls, headers


class Parce_pages:
    def __init__(self, urls: dict, timeout: int, headers: dict):
        self.name = "Parse_pages"
        self.timeout = timeout
        self.headers = headers
        self.urls = urls
        self.soup_data = {
            "Челябинск": {},
            "Екатеринбург": {},
            "Красноярск": {},
            "Санкт-Петербург": {},
            "Сургут": {},
            "Тюмень": {}
        }

    async def load_page(self):
        try:
            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ttl_dns_cache=300)) as session:
                tasks = []
                for name_city in self.urls.keys():
                    for name_url in self.urls[name_city]:

                        task = asyncio.create_task(self.get_page(session, name_url, name_city))
                        tasks.append(task)

                await asyncio.gather(*tasks)

        except Exception as e:
            logging.error(self.name + " | " + str(e))

    async def get_page(self, session, name_url, name_city):
        try:

            async with session.get(self.urls[name_city][name_url], headers=self.headers, ssl=False,
                                   timeout=aiohttp.ClientTimeout(total=self.timeout)) as response:
                if response.status != 200:
                    logging.error(self.name + " | " + str(response.status) + " | " + self.urls[name_url])

                resp_text = await response.text()

                soup = BeautifulSoup(resp_text, 'lxml')
                self.soup_data[name_city][name_url] = soup

        except Exception as e:
            logging.error(self.name + " | " + str(e))

    async def get_data(self):
        await self.load_page()
        return self.soup_data



async def parce():
    parcer = Parce_pages(urls, timeout=0, headers=headers)
    data = await parcer.get_data()
    return data


