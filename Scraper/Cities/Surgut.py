import logging



class Vchm:
    def __init__(self):
        self.name = "ВЧМ"
        self.city = "Сургут"


    def get_soup(self, soups):
        try:

            soup = soups[self.city][self.name]
            tables = soup.find(id="ceny").find(class_="container").find("div").find("div", {"data-city": "Сургут"}) \
                .findAll(class_="mt-5")
            table = tables[1].find(class_="table-reg").find('tbody').findAll('tr')

            return table

        except Exception as e:

            logging.error(self.name + ' | ' + str(e))
            return []

    def parse_data(self, soups):

        table = self.get_soup(soups)
        price_data = list()

        if table is not []:
            try:
                for li in table[:3]:
                    tds = li.findAll('td')
                    title = tds[0].text.strip().replace(', жила от 1 мм', '').replace(', жженная', '')
                    price = tds[3].text.strip()
                    price_ur = 0.0

                    price_data.append([self.city, self.name, title, price, price_ur])

                return price_data

            except Exception as e:
                logging.error(self.name + ' | ' + str(e))



def GetCompanies() -> list:
    return [
        Vchm(),

    ]



