import logging
from Base import Company, try_table


class Dominant(Company):

    @try_table
    def parse_table(self, soups):

        soup = soups[self.city][self.name]
        table = soup.find(class_="welcome").find(class_="inner").find(class_='price').findAll(class_='price__line')
        return table

    def parse_data(self, soups) -> list:

        table = self.parse_table(soups)
        data = []

        if table is not None:
            for div in table[:3]:
                spans = div.findAll('span')

                title = self.Normalize_name(spans[0].text)
                if title is None:
                    continue

                price = self.Normalize_price(spans[1].text.strip().replace(' ₽', ''))
                if price is None:
                    continue

                price_ur = self.Normalize_price(spans[2].text.strip().replace(' ₽', ''))
                if price_ur is None:
                    continue

                data.append([self.city, self.name, title, price, price_ur])

        return data


class Vtormet(Company):

    @try_table
    def parse_table(self, soups):

        soup = soups[self.city][self.name]
        table = soup.find(class_="price__content", id='17').find(class_='price__content-list').findAll(
            class_='price__content-item decor')
        return table

    def parse_data(self, soups):

        table = self.parse_table(soups)
        data = []

        if table is not None:
            for div in table[1:6]:

                title = self.Normalize_name(div.find(class_='price__content-item-wrap-title').text.strip())
                if title is None:
                    continue

                price = self.Normalize_price(div.find(class_='price__content-item-cash').text.strip())
                if price is None:
                    continue

                price_ur = self.Normalize_price(div.find(class_='price__content-item-cashless').text.strip())
                if price_ur is None:
                    continue

                data.append([self.city, self.name, title, price, price_ur])

        return data


class Lom_74(Company):

    @try_table
    def parse_table(self, soups):

        soup = soups[self.city][self.name]
        table = soup.find(class_='prices__table').findAll(class_='prices__table__line')
        return table

    def parse_data(self, soups):

        table = self.parse_table(soups)
        data = []

        if table is not None:
            for li in table[3:9]:
                div = li.findAll('div')
                if len(div) == 3:

                    title = self.Normalize_name(div[0].text)
                    if title is None:
                        continue

                    price = self.Normalize_price(div[2].text)
                    if price is None:
                        continue

                    price_ur = self.Normalize_price(0)
                    if price_ur is None:
                        continue


                    data.append([self.city, self.name, title, price, price_ur])

        return data


def GetCompanies() -> list:
    return [
        Dominant("Доминант", "Челябинск"),
        Vtormet("Втормет", "Челябинск"),
        Lom_74("Лом_74", "Челябинск"),

    ]
