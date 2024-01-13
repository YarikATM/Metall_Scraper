import logging



class Dominant:
    def __init__(self):
        self.name = "Доминант"
        self.city = "Челябинск"


    def get_soup(self, soups):
        try:

            soup = soups[self.city][self.name]
            table = soup.find(class_="welcome").find(class_="inner").find(class_='price').findAll(class_='price__line')

            return table

        except Exception as e:

            logging.error(self.name + ' | ' + str(e))
            return None

    def parse_data(self, soups):

        table = self.get_soup(soups)
        data = list()

        if table is not None:
            try:
                for div in table[:3]:
                    spans = div.findAll('span')
                    title = spans[0].text.strip().replace('Лом меди (блеск)', 'Медь (блеск)') \
                        .replace('Лом меди (кусок)', 'Медь (кусок)').replace('Лом меди (mix)', 'Медь (микс)')

                    price = spans[1].text.strip().replace(' ₽', '')
                    price_ur = spans[2].text.strip().replace(' ₽', '')

                    data.append([self.city, self.name, title, price, price_ur])

                return data

            except Exception as e:
                logging.error(self.name + ' | ' + str(e))
                return None


class Vtormet:
    def __init__(self):
        self.name = "Втормет"
        self.city = "Челябинск"


    def get_soup(self, soups):
        try:

            soup = soups[self.city][self.name]
            table = soup.find(class_="price__content", id='17').find(class_='price__content-list').findAll(
                class_='price__content-item decor')
            # print(soup)
            # print(table)
            return table

        except Exception as e:

            logging.error(self.name + ' | ' + str(e))
            return None

    def parse_data(self, soups):

        table = self.get_soup(soups)
        price_data = list()
        # print(soup)

        if table is not None:
            try:
                for div in table[1:6]:

                    # print(li)
                    title = div.find(class_='price__content-item-wrap-title').text.strip()

                    title = title.replace('Лом меди, блеск', 'Медь (блеск)').replace('Лом меди, кусок', 'Медь (кусок)',
                                                                                     2)
                    title = title.replace('Лом меди, микс', 'Медь (микс)')

                    price = div.find(class_='price__content-item-cash').text.strip()
                    price_ur = div.find(class_='price__content-item-cashless').text.strip()
                    #price__content-item-cashless

                    if title in ["Медь (блеск)", "Медь (кусок)", "Медь (микс)"]:
                        price_data.append([self.city, self.name, title, price, price_ur])

                return price_data

            except Exception as e:
                logging.error(self.name + ' | ' + str(e))
                return None


class Lom_74:
    def __init__(self):
        self.name = "Лом_74"
        self.city = "Челябинск"


    def get_soup(self, soups):
        try:

            soup = soups[self.city][self.name]
            table = soup.find(class_='prices__table').findAll(class_='prices__table__line')

            return table

        except Exception as e:

            logging.error(self.name + ' | ' + str(e))
            return None

    def parse_data(self, soups):

        table = self.get_soup(soups)
        price_data = list()

        if table is not None:
            try:
                for li in table[3:9]:
                    div = li.findAll('div')
                    if len(div) == 3:
                        title = div[0].text
                        price = div[2].text
                        price_ur = 0

                        title = title.replace('Блеск', 'Медь (блеск)').replace('Микс', 'Медь (микс)') \
                            .replace('Кусок', 'Медь (кусок)')

                        if title in ["Медь (блеск)", "Медь (кусок)", "Медь (микс)"]:
                            price_data.append([self.city, self.name, title, price, price_ur])

                return price_data

            except Exception as e:
                logging.error(self.name + ' | ' + str(e))
                return None


def GetCompanies() -> list:
    return [
        Dominant(),
        Vtormet(),
        Lom_74(),

    ]
