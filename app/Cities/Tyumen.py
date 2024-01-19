import logging
from Base import try_table, Company



class Metallokassa(Company):

    @try_table
    def parse_table(self, soups):

        soup = soups[self.city][self.name]
        table = soup.find(class_='table_table__LVYHg').findAll(class_='table_tableRow__0mobE')
        return table

    def parse_data(self, soups):

        table = self.parse_table(soups)
        price_data = []

        if table is not None:
            for div in table[:2]:
                divs = div.findAll('div')

                title = self.Normalize_name(divs[0].find(class_='table_subCategory__45Rz_').text.strip().replace(' ', ' '))
                if title is None:
                    continue

                price = self.Normalize_price(divs[3].text.strip().replace(' ₽', ''))
                if price is None:
                    continue

                price_ur = self.Normalize_price(0)
                if price_ur is None:
                    continue

                price_data.append([self.city, self.name, title, price, price_ur])

        return price_data


class Avamet(Company):

    @try_table
    def parse_table(self, soups):

        soup = soups[self.city][self.name]
        table = soup.find(class_='table table-kavv table-striped table-bordered').find('tbody').findAll('tr')
        return table

    def parse_data(self, soups):

        table = self.parse_table(soups)
        price_data = []

        if table is not None:
            for li in table[:3]:
                block = li.findAll('td')

                title = self.Normalize_name(block[0].text.strip())
                if title is None:
                    continue

                price = self.Normalize_price(block[1].text.strip())
                if price is None:
                    continue

                price_ur = self.Normalize_price(block[2].text.strip())
                if price_ur is None:
                    continue

                price_data.append([self.city, self.name, title, price, price_ur])

        return price_data


class Tzvm(Company):

    @try_table
    def parse_table(self, soups):

        soup = soups[self.city][self.name]
        table = soup.find(class_='has-fixed-layout').find('tbody').findAll('tr')
        return table

    def parse_data(self, soups):

        table = self.parse_table(soups)
        price_data = []

        if table is not None:
            for li in table[:3]:
                page = li.findAll('td')

                title = self.Normalize_name(page[0].text.strip())
                if title is None:
                    continue

                price = self.Normalize_price(page[2].text.replace('₽', '').strip())
                if price is None:
                    continue

                price_ur = self.Normalize_price(0)
                if price_ur is None:
                    continue

                price_data.append([self.city, self.name, title, price, price_ur])

        return price_data







                    # title = page[0].text.replace('М1', '(блеск)').replace('М2', '(кусок)').replace('М3', '(микс)')



class Sibmet(Company):

    @try_table
    def parse_table(self, soups):

        soup = soups[self.city][self.name]
        table = soup.find(class_='panda-article').find('table').find("tbody").findAll('tr')
        return table

    def parse_data(self, soups):

        table = self.parse_table(soups)
        price_data = []

        if table is not None:
            for li in table[1:3]:
                block = li.findAll('td')

                title = self.Normalize_name(block[0].text.strip())
                if title is None:
                    continue

                price = self.Normalize_price(block[2].text.strip())
                if price is None:
                    continue

                price_ur = self.Normalize_price(0)
                if price_ur is None:
                    continue

                price_data.append([self.city, self.name, title, price, price_ur])

        return price_data




def GetCompanies() -> list:
    return [
        Metallokassa("Мет.касса", "Тюмень"),
        Tzvm("ТЗВМ", "Тюмень"),
        Avamet("Авамет", "Тюмень"),
        Sibmet("СИБМЕТ", "Тюмень"),


    ]