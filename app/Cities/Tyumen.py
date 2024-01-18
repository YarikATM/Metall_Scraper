import logging





class Metallokassa:
    def __init__(self):
        self.name = "Мет.касса"
        self.city = "Тюмень"


    def get_soup(self, soups):
        try:

            soup = soups[self.city][self.name]
            table = soup.find(class_='table_table__LVYHg').findAll(class_='table_tableRow__0mobE')

            return table

        except Exception as e:

            logging.error(self.name + ' | ' + str(e))
            return None

    def parse_data(self, soups):

        table = self.get_soup(soups)
        price_data = list()

        if table is not None:
            try:
                for div in table:
                    divs = div.findAll('div')
                    title = divs[0].find(class_='table_subCategory__45Rz_').text.strip().replace(' ', ' ') \
                        .replace('Лом меди (блеск)', 'Медь (блеск)').replace('Лом меди', 'Медь (микс)')

                    price = divs[3].text.strip().replace(' ₽', '')
                    price_ur = 0

                    if title in ["Медь (блеск)", "Медь (кусок)", "Медь (микс)"]:
                        price_data.append([self.city, self.name, title, price, price_ur])

                return price_data

            except Exception as e:
                logging.error(self.name + ' | ' + str(e))
                return None




class Avamet:
    def __init__(self):
        self.name = "Авамет"
        self.city = "Тюмень"


    def get_soup(self, soups):
        try:

            soup = soups[self.city][self.name]
            table = soup.find(class_='table table-kavv table-striped table-bordered').find('tbody').findAll('tr')

            return table

        except Exception as e:

            logging.error(self.name + ' | ' + str(e))
            return None

    def parse_data(self, soups):

        table = self.get_soup(soups)
        price_data = list()

        if table is not None:
            try:
                for li in table[:3]:
                    block = li.findAll('td')
                    title = block[0].text.replace('блеск', '(блеск)').replace('кусок', '(кусок)') \
                        .replace('микс', '(микс)')

                    price = block[1].text
                    price_ur = block[2].text

                    price_data.append([self.city, self.name, title, price, price_ur])

                return price_data

            except Exception as e:
                logging.error(self.name + ' | ' + str(e))
                return None



class Tzvm:
    def __init__(self):
        self.name = "ТЗВМ"
        self.city = "Тюмень"


    def get_soup(self, soups):
        try:

            soup = soups[self.city][self.name]
            table = soup.find(class_='has-fixed-layout').find('tbody').findAll('tr')

            return table

        except Exception as e:

            logging.error(self.name + ' | ' + str(e))
            return None

    def parse_data(self, soups):

        table = self.get_soup(soups)
        price_data = list()

        if table is not None:
            try:
                for li in table[:3]:
                    page = li.findAll('td')
                    price = page[1].text.replace('₽', '')
                    title = page[0].text.replace('М1', '(блеск)').replace('М2', '(кусок)').replace('М3', '(микс)')
                    try:
                        price = int(price) + int(page[2].text.replace('₽', ''))
                    except:
                        pass
                    price_ur = 0

                    price_data.append([self.city, self.name, title, price, price_ur])

                return price_data

            except Exception as e:
                logging.error(self.name + ' | ' + str(e))
                return None



class Sibmet:
    def __init__(self):
        self.name = "СИБМЕТ"
        self.city = "Тюмень"


    def get_soup(self, soups):
        try:

            soup = soups[self.city][self.name]
            table = soup.find(class_='panda-article').find('table').find("tbody").findAll('tr')

            return table

        except Exception as e:

            logging.error(self.name + ' | ' + str(e))
            return None

    def parse_data(self, soups):

        table = self.get_soup(soups)
        price_data = list()

        if table is not None:
            try:
                for li in table[1:3]:
                    block = li.findAll('td')
                    title = block[0].text.strip().replace("МЕДЬ БЛЕСК", "Медь (блеск)") \
                        .replace("МЕДЬ МИКС", 'Медь (микс)')
                    price = block[2].text.strip()
                    price_ur = 0

                    price_data.append([self.city, self.name, title, price, price_ur])

                return price_data

            except Exception as e:
                logging.error(self.name + ' | ' + str(e))
                return None


def GetCompanies() -> list:
    return [
        Metallokassa(),
        Tzvm(),
        Avamet(),
        Sibmet(),


    ]