import logging


class Zsvr:
    def __init__(self):
        self.name = "ЗСВР"
        self.city = "Красноярск"


    def get_soup(self, soups):
        try:

            soup = soups[self.city][self.name]
            table = soup.find(class_='ts-table-section').find('tbody').findAll(itemtype="http://schema.org/Product")

            return table

        except Exception as e:

            logging.error(self.name + ' | ' + str(e))
            return None

    def parse_data(self, soups):

        table = self.get_soup(soups)
        price_data = list()

        if table is not None:
            try:
                for td in table:
                    tds = td.findAll('td')
                    title = tds[1].text.strip().replace('Лом меди А1-1А', 'Медь (кусок)') \
                        .replace('Лом меди А1-1', 'Медь (блеск)', ) \
                        .replace('Лом меди А1-2, А1-2а (микс)', 'Медь (микс)')

                    price = tds[3].text.strip()
                    price_ur = tds[4].text.strip()

                    if title in ["Медь (блеск)", "Медь (кусок)", "Медь (микс)"]:
                        price_data.append([self.city, self.name, title, price, price_ur])

                return price_data

            except Exception as e:
                logging.error(self.name + ' | ' + str(e))
                return None


class Vtormet:
    def __init__(self):
        self.name = "Втормет"
        self.city = "Красноярск"


    def get_soup(self, soups):
        try:

            soup = soups[self.city][self.name]
            table = soup.find(class_='price2').find('tbody').findAll('tr')

            return table

        except Exception as e:

            logging.error(self.name + ' | ' + str(e))
            return None

    def parse_data(self, soups):

        table = self.get_soup(soups)
        price_data = list()

        if table is not None:
            try:
                for li in table[2:5]:
                    tds = li.findAll('td')
                    title = tds[0].text.strip().replace('Лом меди А-1-1а', 'Медь (кусок)') \
                        .replace('Лом меди А-1-1', 'Медь (блеск)').replace('Лом меди А-1-2', 'Медь (микс)')

                    price = tds[1].text.strip()
                    price_ur = 0

                    price_data.append([self.city, self.name, title, price, price_ur])

                return price_data

            except Exception as e:
                logging.error(self.name + ' | ' + str(e))
                return None


class Sibintek:
    def __init__(self):
        self.name = "СибИнтек"
        self.city = "Красноярск"


    def get_soup(self, soups):
        try:

            soup = soups[self.city][self.name]
            table = soup.find(class_='tablepress').find('tbody').findAll(class_='product searchtable')

            return table

        except Exception as e:

            logging.error(self.name + ' | ' + str(e))
            return None

    def parse_data(self, soups):

        table = self.get_soup(soups)
        price_data = list()

        if table is not None:
            try:
                for tr in table:
                    td = tr.findAll('td')
                    title = td[0].find('a').text.strip()
                    price = td[1].text.strip()[:-1]
                    price_ur = td[2].text.strip()[:-1]
                    if title == 'Медь АI - 2':
                        title = 'Медь (микс)'
                    elif title == 'Медь АI -1а':
                        title = 'Медь (кусок)'
                    elif title == 'Медь АI - 1':
                        title = 'Медь (блеск)'
                    else:
                        continue
                    price_data.append([self.city, self.name, title, price, price_ur])

                return price_data

            except Exception as e:
                logging.error(self.name + ' | ' + str(e))
                return None


class Alkom:
    def __init__(self):
        self.name = "Алком"
        self.city = "Красноярск"


    def get_soup(self, soups):
        try:

            soup = soups[self.city][self.name]
            table = soup.find(class_='wp-block-table is-style-stripes').find('table').find('tbody').findAll('tr')

            return table

        except Exception as e:

            logging.error(self.name + ' | ' + str(e))
            return None

    def parse_data(self, soups):

        table = self.get_soup(soups)
        price_data = list()

        if table is not None:
            try:
                for tr in table:
                    tds = tr.findAll('td')
                    title = tds[0].text.strip()
                    price = tds[1].text.strip()
                    price_ur = 0
                    if title == 'Лом меди кусок  (от 10 кг)':
                        title = 'Медь (кусок)'
                    elif title == 'Лом меди микс А1-2А':
                        title = 'Медь (микс)'
                    elif title == 'Медь блеск А1-1':
                        title = 'Медь (блеск)'
                    else:
                        continue
                    price_data.append([self.city, self.name, title, price, price_ur])

                return price_data

            except Exception as e:
                logging.error(self.name + ' | ' + str(e))
                return None


class Mbaza:
    def __init__(self):
        self.name = "МБаза"
        self.city = "Красноярск"


    def get_soup(self, soups):
        try:

            soup = soups[self.city][self.name]
            table = soup.find('body').findAll('li')

            return table

        except Exception as e:

            logging.error(self.name + ' | ' + str(e))
            return None

    def parse_data(self, soups):

        table = self.get_soup(soups)
        price_data = list()

        if table is not None:
            try:
                for li in table:
                    title = li.text.strip()
                    try:
                        price = li['data-price']
                    except:
                        continue
                    if title == 'Медь (mix)':
                        title = 'Медь (микс)'
                    elif title == 'Медь А-1-1':
                        title = 'Медь (блеск)'
                    else:
                        continue
                    price_ur = 0

                    price_data.append([self.city, self.name, title, price, price_ur])

                return price_data

            except Exception as e:
                logging.error(self.name + ' | ' + str(e))



class Krasmet:
    def __init__(self):
        self.name = "Красмет"
        self.city = "Красноярск"


    def get_soup(self, soups):
        try:

            soup = soups[self.city][self.name]
            table = soup.find(class_="table1").find("tbody").findAll('tr')


            return table

        except Exception as e:

            logging.error(self.name + ' | ' + str(e))
            return []

    def parse_data(self, soups):

        table = self.get_soup(soups)
        price_data = list()

        if table is not []:
            try:
                for tr in table[1:]:
                    tds = tr.findAll('td')
                    title = tds[1].text.strip()
                    price = tds[3].text.strip()
                    price_ur = 0
                    if title == 'Лом меди':
                        title = 'Медь (микс)'
                        price_data.append([self.city, self.name, title, price, price_ur])
                        break

                return price_data

            except Exception as e:
                logging.error(self.name + ' | ' + str(e))



class Cslk:
    def __init__(self):
        self.name = "ЦСЛК"
        self.city = "Красноярск"


    def get_soup(self, soups):
        try:

            soup = soups[self.city][self.name]
            table = soup.find(class_='price--color price-block').find(
                class_='price__card-accordion price__card-accordion--el') \
                .findAll(class_='accordion-line')

            return table

        except Exception as e:

            logging.error(self.name + ' | ' + str(e))
            return []

    def parse_data(self, soups):

        table = self.get_soup(soups)
        price_data = list()

        if table is not []:
            try:
                for i in range(1, len(table)):
                    title = table[i].find(class_='price__card-name').text.strip()
                    price = None
                    price_ur = 0
                    try:
                        price = table[i].find(class_='price__card-coast--730').find("p").find("span").text.strip()
                    except:
                        pass
                    if title == 'Медь смешанная':
                        title = 'Медь (микс)'
                        price_data.append([self.city, self.name, title, price, price_ur])

                    if title == 'Медь блеск/кусок':
                        price = price.split('/')
                        price_data.append([self.city, self.name, "Медь (блеск)", price[0], price_ur])
                        price_data.append([self.city, self.name, "Медь (кусок)", price[1], price_ur])

                return price_data

            except Exception as e:
                logging.error(self.name + ' | ' + str(e))



def GetCompanies() -> list:
    return [
        Zsvr(),
        Vtormet(),
        Sibintek(),
        Alkom(),
        Mbaza(),
        Krasmet(),
        Cslk()
    ]
