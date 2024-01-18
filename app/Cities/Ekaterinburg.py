import logging



class Grand:
    def __init__(self):
        self.name = "Гранд"
        self.city = "Екатеринбург"

    def get_soup(self, soups):
        try:

            soup = soups[self.city][self.name]
            table = soup.find('ul', class_="company-products-gallery").findAll("li")



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

                    title_raw = li.find(class_='cpgi-title-wrapper').text.strip()
                    if title_raw == 'Прием цветного металлолома, медь (микс),':
                        title = 'Медь (микс)'
                    elif title_raw == 'Прием цветного металлолома, медь (блеск),':
                        title = 'Медь (блеск)'
                    else:
                        continue
                    price = li.find(class_='bp-price fsn').text.strip()
                    price_ur = 0
                    price_data.append([self.city, self.name, title, price, price_ur])

                return price_data

            except Exception as e:
                logging.error(self.name + ' | ' + str(e))
                return None


class Texnosplav:
    def __init__(self):
        self.name = "Техносплав"
        self.city = "Екатеринбург"


    def get_soup(self, soups):
        try:

            soup = soups[self.city][self.name]
            table = soup.find('table', class_='table1').find('tbody').findAll("tr")

            return table

        except Exception as e:

            logging.error(self.name + ' | ' + str(e))
            return None

    def parse_data(self, soups):

        table = self.get_soup(soups)
        price_data = list()

        if table is not None:
            try:
                for tr in table[4:8]:
                    raw_data = tr.findAll('td')
                    title_raw = raw_data[0].text.split(' ')
                    title = title_raw[0] + ' ' + '(' + title_raw[1] + ')'
                    price = raw_data[2].text.strip().replace(' р.', '')
                    price_ur = 0
                    if title in ["Медь (блеск)", "Медь (кусок)", "Медь (микс)"]:
                        price_data.append([self.city, self.name, title, price, price_ur])

                return price_data

            except Exception as e:
                logging.error(self.name + ' | ' + str(e))
                return None


class Rmm:
    def __init__(self):
        self.name = "РММ"
        self.city = "Екатеринбург"


    def get_soup(self, soups):
        try:

            soup = soups[self.city][self.name]
            table = soup.find('table', id="table-id3").find('tbody').findAll('tr')

            return table

        except Exception as e:

            logging.error(self.name + ' | ' + str(e))
            return None

    def parse_data(self, soups):

        table = self.get_soup(soups)
        price_data = list()

        if table is not None:
            try:
                for tr in table[1:8]:
                    tds = tr.findAll('td')
                    title = tds[0].find('span').text.replace('Лом меди mix М4', 'Медь (микс)') \
                        .replace('Лом меди М1', 'Медь (блеск)').replace('Лом меди М2', 'Медь (кусок)')
                    if title in ["Медь (блеск)", "Медь (кусок)", "Медь (микс)"]:
                        price = tds[2].text.strip()
                        price_ur = tds[3].text.strip()

                        price_data.append([self.city, self.name, title, price, price_ur])

                return price_data

            except Exception as e:
                logging.error(self.name + ' | ' + str(e))
                return None


class Mida:
    def __init__(self):
        self.name = "МИДА"
        self.city = "Екатеринбург"


    def get_soup(self, soups):
        try:

            soup = soups[self.city][self.name]
            table = soup.find(class_="row-hover").findAll('tr')

            return table

        except Exception as e:

            logging.error(self.name + ' | ' + str(e))
            return None

    def parse_data(self, soups):

        table = self.get_soup(soups)
        price_data = list()

        if table is not None:
            try:
                for tr in table[1:4]:
                    tds = tr.findAll('td')
                    title = tds[1].find('h4').text.strip().replace('Медь 3', 'Медь (микс)') \
                        .replace('Медь 1', 'Медь (блеск)').replace('Медь 2', 'Медь (кусок)')

                    price = tds[-1].text.strip().replace(',', '.')
                    price_ur = tds[-2].text.strip().replace(',', '.')

                    price_data.append([self.city, self.name, title, price, price_ur])

                return price_data


            except Exception as e:
                logging.error(self.name + ' | ' + str(e))
                return None


class Stimul:
    def __init__(self):
        self.name = "Стимул"
        self.city = "Екатеринбург"


    def get_soup(self, soups):
        try:

            soup = soups[self.city][self.name]
            table = soup.find('table').find('tbody').findAll('tr')

            return table

        except Exception as e:

            logging.error(self.name + ' | ' + str(e))
            return None

    def parse_data(self, soups):

        table = self.get_soup(soups)
        price_data = list()

        if table is not None:
            try:
                for li in table[:7]:
                    tbl = li.findAll('td')
                    title = tbl[0].text.strip().replace('\xa0', '').replace('Медь А1-1 (блеск)', 'Медь (блеск)') \
                        .replace('Медь А1-1а (кусок)', 'Медь (кусок)').replace('Медь А1-2 (микс)', 'Медь (микс)')

                    price = tbl[1].text.strip().replace("руб.Б/Н", '')
                    price_ur = 0

                    if title in ["Медь (блеск)", "Медь (кусок)", "Медь (микс)"]:
                        price_data.append([self.city, self.name, title, price, price_ur])

                return price_data

            except Exception as e:
                logging.error(self.name + ' | ' + str(e))
                return None


def GetCompanies() -> list:
    return [
        Grand(),
        Texnosplav(),
        Rmm(),
        Mida(),
        Stimul(),

    ]



