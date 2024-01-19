import logging
from Base import Company, try_table


class Grand(Company):

    @try_table
    def parse_table(self, soups):

        soup = soups[self.city][self.name]
        table = soup.find('ul', class_="company-products-gallery").findAll("li")
        return table


    def parse_data(self, soups):

        table = self.parse_table(soups)
        price_data = []

        if table is not None:
            for li in table:

                title = self.Normalize_name(li.find(class_='cpgi-title-wrapper').text.strip())
                if title is None:
                    continue

                price = self.Normalize_price(li.find(class_='bp-price fsn').text.strip())
                if price is None:
                    continue

                price_ur = self.Normalize_price(0)
                if price_ur is None:
                    continue

                price_data.append([self.city, self.name, title, price, price_ur])

        return price_data




class Texnosplav(Company):


    @try_table
    def parse_table(self, soups):

        soup = soups[self.city][self.name]
        table = soup.find('table', class_='table1').find('tbody').findAll("tr")
        return table


    def parse_data(self, soups):

        table = self.parse_table(soups)
        price_data = []

        if table is not None:
            for tr in table[4:8]:
                td = tr.findAll('td')

                title = self.Normalize_name(td[0].text.strip())
                if title is None:
                    continue

                price = self.Normalize_price(td[2].text.strip().replace(' р.', ''))
                if price is None:
                    continue

                price_ur = self.Normalize_price(0)
                if price_ur is None:
                    continue

                price_data.append([self.city, self.name, title, price, price_ur])

        return price_data




class Rmm(Company):


    @try_table
    def parse_table(self, soups):

        soup = soups[self.city][self.name]
        table = soup.find('table', id="table-id3").find('tbody').findAll('tr')
        return table


    def parse_data(self, soups):

        table = self.parse_table(soups)
        price_data = []

        if table is not None:
            for tr in table[1:8]:
                tds = tr.findAll('td')

                title = self.Normalize_name(tds[0].find('span').text.strip())
                if title is None:
                    continue

                price = self.Normalize_price(tds[2].text.strip())
                if price is None:
                    continue

                price_ur = self.Normalize_price(tds[3].text.strip())
                if price_ur is None:
                    continue

                price_data.append([self.city, self.name, title, price, price_ur])

        return price_data




class Mida(Company):


    @try_table
    def parse_table(self, soups):

        soup = soups[self.city][self.name]
        table = soup.find(class_="row-hover").findAll('tr')
        return table


    def parse_data(self, soups):

        table = self.parse_table(soups)
        price_data = []

        if table is not None:
            for tr in table[1:4]:
                tds = tr.findAll('td')

                title = self.Normalize_name(tds[1].find('h4').text.strip())
                if title is None:
                    continue

                price = self.Normalize_price(tds[-1].text.strip().replace(',', '.'))
                if price is None:
                    continue

                price_ur = self.Normalize_price(tds[-2].text.strip().replace(',', '.'))
                if price_ur is None:
                    continue

                price_data.append([self.city, self.name, title, price, price_ur])

        return price_data



class Stimul(Company):


    @try_table
    def parse_table(self, soups):

        soup = soups[self.city][self.name]
        table = soup.find('table').find('tbody').findAll('tr')
        return table


    def parse_data(self, soups):

        table = self.parse_table(soups)
        price_data = []

        if table is not None:
            for li in table[:4]:
                td = li.findAll('td')

                title = self.Normalize_name(td[0].text.strip().replace('\xa0', ''))
                if title is None:
                    continue

                price = self.Normalize_price(td[1].text.strip().replace("руб.Б/Н", ''))
                if title is None:
                    continue

                price_ur = self.Normalize_price(0)
                if title is None:
                    continue

                price_data.append([self.city, self.name, title, price, price_ur])

        return price_data



def GetCompanies() -> list:
    return [
        Grand("Гранд", "Екатеринбург"),
        Texnosplav("Техносплав", "Екатеринбург"),
        Rmm("РММ", "Екатеринбург"),
        Mida("МИДА", "Екатеринбург"),
        Stimul("Стимул", "Екатеринбург"),

    ]



