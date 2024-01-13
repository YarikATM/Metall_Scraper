import logging


class Intermet:
    def __init__(self):
        self.name = "Интермет"
        self.city = "Санкт-Петербург"

    def get_soup(self, soups):
        try:

            soup = soups[self.city][self.name]
            table = soup.find(class_="price-table__body table-body").find("div").findAll(class_='price-table__row catrgory-item')


            return table

        except Exception as e:

            logging.error(self.name + ' | ' + str(e))
            return []

    def parse_data(self, soups):

        table = self.get_soup(soups)
        price_data = list()

        if table is not None:
            try:
                for div in table:


                    block = div.findAll("div")

                    if len(block) != 0:

                        title = block[0].text.strip().replace('Медь микс', 'Медь (микс)') \
                            .replace('Медь кусок', 'Медь (кусок)').replace('Медь блеск', 'Медь (блеск)')
                        price = block[5].text.strip()
                        price_ur = block[7].text.strip()

                        if title in ["Медь (блеск)", "Медь (кусок)", "Медь (микс)"]:
                            price_data.append([self.city, self.name, title, price, price_ur])

                return price_data

            except Exception as e:
                logging.error(self.name + ' | ' + str(e))
                return []


class Metalist:
    def __init__(self):
        self.name = "Металист"
        self.city = "Санкт-Петербург"

    def get_soup(self, soups):
        try:

            soup = soups[self.city][self.name]
            table = soup.find(class_='price-table').find('tbody').findAll('tr')

            return table

        except Exception as e:

            logging.error(self.name + ' | ' + str(e))
            return None

    def parse_data(self, soups):

        table = self.get_soup(soups)
        price_data = list()

        if table is not None:
            try:
                for tr in table[:3]:
                    page = tr.findAll('td')
                    title = page[1].text.strip().replace('Медь блестящая', 'Медь (блеск)')
                    title = title.replace('Медь кусковая', 'Медь (кусок)')
                    title = title.replace('Медный микс', 'Медь (микс)')
                    price = page[2].text.strip()
                    price_ur = page[3].text.strip()

                    price_data.append([self.city, self.name, title, price, price_ur])

                return price_data

            except Exception as e:
                logging.error(self.name + ' | ' + str(e))
                return None


def GetCompanies() -> list:
    return [
        Intermet(),
        Metalist(),

    ]
