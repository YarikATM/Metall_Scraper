import logging
from Base import try_table, Company


class Vchm(Company):

    @try_table
    def parse_table(self, soups):

        soup = soups[self.city][self.name]
        tables = soup.find(id="ceny").find(class_="container").find("div").find("div", {"data-city": "Сургут"}) \
            .findAll(class_="mt-5")
        table = tables[1].find(class_="table-reg").find('tbody').findAll('tr')
        return table

    def parse_data(self, soups):

        table = self.parse_table(soups)
        price_data = []

        if table is not None:
            for li in table[:3]:
                tds = li.findAll('td')

                title = self.Normalize_name(tds[0].text.strip())
                if title is None:
                    continue

                price = self.Normalize_price(tds[3].text.strip())
                if price is None:
                    continue

                price_ur = self.Normalize_price(0)
                if price_ur is None:
                    continue

                price_data.append([self.city, self.name, title, price, price_ur])

        return price_data


def GetCompanies() -> list:
    return [
        Vchm("ВЧМ", "Сургут"),

    ]
