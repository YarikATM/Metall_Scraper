import logging
from Base import try_table, Company


class Intermet(Company):

    @try_table
    def parse_table(self, soups):

        soup = soups[self.city][self.name]
        table = soup.find(class_="price-table__body table-body").find("div").findAll(
            class_='price-table__row catrgory-item')
        return table

    def parse_data(self, soups):

        table = self.parse_table(soups)
        price_data = []

        if table is not None:
            for div in table[:6]:
                block = div.findAll("div")

                title = self.Normalize_name(block[0].text.strip())
                if title is None:
                    continue

                price = self.Normalize_price(block[5].text.strip())
                if price is None:
                    continue

                price_ur = self.Normalize_price(block[7].text.strip())
                if price_ur is None:
                    continue

                price_data.append([self.city, self.name, title, price, price_ur])

        return price_data


class Metalist(Company):

    @try_table
    def parse_table(self, soups):

        soup = soups[self.city][self.name]
        table = soup.find(class_='price-table').find('tbody').findAll('tr')
        return table

    def parse_data(self, soups):

        table = self.parse_table(soups)
        price_data = []

        if table is not None:
            for tr in table[:3]:
                page = tr.findAll('td')

                title = self.Normalize_name(page[1].text.strip())
                if title is None:
                    continue

                price = self.Normalize_price(page[2].text.strip())
                if price is None:
                    continue

                price_ur = self.Normalize_price(page[3].text.strip())
                if price_ur is None:
                    continue

                price_data.append([self.city, self.name, title, price, price_ur])

        return price_data


def GetCompanies() -> list:
    return [
        Intermet("Интермет", "Санкт-Петербург"),
        Metalist("Металист", "Санкт-Петербург"),

    ]
