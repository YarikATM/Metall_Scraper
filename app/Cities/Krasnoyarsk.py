import logging
from Base import Company, try_table, try_parse


class Zsvr(Company):

    @try_table
    def parse_table(self, soups):

        soup = soups[self.city][self.name]
        table = soup.find(class_='ts-table-section').find('tbody').findAll(itemtype="http://schema.org/Product")
        return table

    @try_parse
    def parse_data(self, soups):

        table = self.parse_table(soups)
        price_data = []

        if table is not None:
            for td in table[:9]:
                tds = td.findAll('td')

                title = self.Normalize_name(tds[1].text.strip())
                if title is None:
                    continue

                price = self.Normalize_price(tds[3].text.strip())
                if price is None:
                    continue

                price_ur = self.Normalize_price(tds[4].text.strip())
                if price_ur is None:
                    continue

                price_data.append([self.city, self.name, title, price, price_ur])

        return price_data


class Vtormet(Company):

    @try_table
    def parse_table(self, soups):

        soup = soups[self.city][self.name]
        table = soup.find(class_='price2').find('tbody').findAll('tr')
        return table

    @try_parse
    def parse_data(self, soups):

        table = self.parse_table(soups)
        price_data = []

        if table is not None:
            for li in table[2:5]:
                tds = li.findAll('td')

                title = self.Normalize_name(tds[0].text.strip())
                if title is None:
                    continue

                price = self.Normalize_price(tds[1].text.strip())
                if price is None:
                    continue

                price_ur = self.Normalize_price(0)
                if price_ur is None:
                    continue

                price_data.append([self.city, self.name, title, price, price_ur])

        return price_data


class Sibintek(Company):

    @try_table
    def parse_table(self, soups):

        soup = soups[self.city][self.name]
        table = soup.find(class_='tablepress').find('tbody').findAll(class_='product searchtable')
        return table

    @try_parse
    def parse_data(self, soups):

        table = self.parse_table(soups)
        price_data = []

        if table is not None:
            for tr in table[:6]:
                td = tr.findAll('td')

                title = self.Normalize_name(td[0].find('a').text.strip())
                if title is None:
                    continue

                price = self.Normalize_price(td[1].text.strip()[:-1])
                if price is None:
                    continue

                price_ur = self.Normalize_price(td[2].text.strip()[:-1])
                if price_ur is None:
                    continue

                price_data.append([self.city, self.name, title, price, price_ur])

        return price_data


class Alkom(Company):

    @try_table
    def parse_table(self, soups):

        soup = soups[self.city][self.name]
        table = soup.find(class_='wp-block-table is-style-stripes').find('table').find('tbody').findAll('tr')
        return table

    @try_parse
    def parse_data(self, soups):

        table = self.parse_table(soups)
        price_data = []

        if table is not None:
            for tr in table[2:5]:
                tds = tr.findAll('td')

                title = self.Normalize_name(tds[0].text.strip())
                if title is None:
                    continue

                price = self.Normalize_price(tds[1].text.strip())
                if price is None:
                    continue

                price_ur = self.Normalize_price(0)
                if price_ur is None:
                    continue

                price_data.append([self.city, self.name, title, price, price_ur])

        return price_data


class Mbaza(Company):

    @try_table
    def parse_table(self, soups):

        soup = soups[self.city][self.name]
        table = soup.find('body').findAll('li')
        return table

    @try_parse
    def parse_data(self, soups):

        table = self.parse_table(soups)
        price_data = []

        if table is not None:
            for li in table[:6]:

                title = self.Normalize_name(li.text.strip())
                if title is None:
                    continue

                price = self.Normalize_price(li['data-price'])
                if price is None:
                    continue

                price_ur = self.Normalize_price(0)
                if price_ur is None:
                    continue

                price_data.append([self.city, self.name, title, price, price_ur])

        return price_data


class Krasmet(Company):

    @try_table
    def parse_table(self, soups):

        soup = soups[self.city][self.name]
        table = soup.find(class_="table1").find("tbody").findAll('tr')
        return table

    @try_parse
    def parse_data(self, soups):

        table = self.parse_table(soups)
        price_data = []

        if table is not None:
            for tr in table[1:2]:
                tds = tr.findAll('td')

                title = self.Normalize_name(tds[1].text.strip())
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


class Cslk(Company):

    @try_table
    def parse_table(self, soups):

        soup = soups[self.city][self.name]
        table = soup.find(class_='price--color price-block').find(
            class_='price__card-accordion price__card-accordion--el') \
            .findAll(class_='accordion-line')
        return table

    @try_parse
    def parse_data(self, soups):

        table = self.parse_table(soups)
        price_data = []

        if table is not None:

            for i in range(2, 4):

                title = self.Normalize_name(table[i].find(class_='price__card-name').text.strip())

                if title == "медь блеск/кусок":


                    price = table[i].find(class_='price__card-coast--730').find("p").text.strip().split(
                        '/')
                    price_data.append([self.city, self.name, "Медь (блеск)", self.Normalize_price(price[0]), 0.0])
                    price_data.append([self.city, self.name, "Медь (кусок)", self.Normalize_price(price[1]), 0.0])

                else:
                    if title is None:
                        continue

                    price = self.Normalize_price(
                        table[i].find(class_='price__card-coast--730').find("p").text.strip())
                    if price is None:
                        continue

                    price_ur = self.Normalize_price(0)
                    if price_ur is None:
                        continue

                    price_data.append([self.city, self.name, title, price, price_ur])

        return price_data


def GetCompanies() -> list:
    return [
        Zsvr("ЗСВР", "Красноярск"),
        Vtormet("Втормет", "Красноярск"),
        Sibintek("СибИнтек", "Красноярск"),
        Alkom("Алком", "Красноярск"),
        Mbaza("МБаза", "Красноярск"),
        Krasmet("Красмет", "Красноярск"),
        Cslk("ЦСЛК", "Красноярск")
    ]
