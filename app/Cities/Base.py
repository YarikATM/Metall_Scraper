import logging
from abc import ABCMeta, abstractmethod, abstractproperty
from bs4 import BeautifulSoup


class Company:
    __metaclass__ = ABCMeta

    def __init__(self, name, city):
        self.name = name
        self.city = city

    @abstractmethod
    def parse_table(self, soups: dict):
        """Получить таблицу цен из soup"""

    @abstractmethod
    def parse_data(self, soups):
        """Получить данные из таблицы"""

    def Normalize_name(self, string: str):
        string = string.strip()
        string = string.lower()
        if string in normal_dict:
            return normal_dict[string]
        else:
            logging.warning(f"{self.city} {self.name} [{string}] not in normal dict",
                            extra={"city": self.city, "company": self.name})
            return None

    def Normalize_price(self, price: str):
        try:
            return float(price)
        except:
            logging.warning(f"{self.city} {self.name} [{price}] not in normal form")
            return 0.0


def try_table(func):
    def wrapper(self, *args, **kwargs):
        try:
            table = func(self, *args, **kwargs)

            if table is None:
                raise Exception("Table is Null")

            return table

        except Exception as e:
            logging.error(f"{self.city} {self.name} ошибка при получении таблицы данных: {str(e)}")
            return None

    return wrapper

# class (Company):
#
#     @try_table
#     def parse_table(self, soups):
#
#         soup = soups[self.city][self.name]
#         table =
#         return table
#
#     def parse_data(self, soups):
#
#         table = self.parse_table(soups)
#         price_data = []
#
#         if table is not None:
#             for li in table:
#
#                 title = self.Normalize_name()
#                 if title is None:
#                     continue
#
#                 price = self.Normalize_price()
#                 if price is None:
#                     continue
#
#                 price_ur = self.Normalize_price()
#                 if price_ur is None:
#                     continue
#
#                 price_data.append([self.city, self.name, title, price, price_ur])
#
#         return price_data


normal_dict = {
    "лом меди, кусок д": None,
    "лом меди, полуда": None,
    "кусок д": None,
    "луженка": None,
    "стружка": None,
    "медь д (прокат, высечка, труба без примесей и окислов толщина не менее 2 мм, минимальный размер 50*50 мм)": None,
    "лом меди в изоляции за %": None,
    "лом меди (луженка,автопр.) м4-л, м4-а": None,
    "газовые колонки м9": None,
    "газовые колонки м9-л (лужёные)": None,
    "медьд": None,
    "лом меди а1-1б, а1-1т": None,
    "лом меди а1-1д": None,
    "лом меди а1-1е": None,
    "лом меди а1-1ж": None,
    "лом меди мф-9, мф-10 (фосфористая)": None,
    "медь (прокат, чушка, анод, катод)": None,
    "медь a i - 1д": None,
    "медь аi - 1е": None,
    "медь аi - 1ж": None,
    "медь а-1-3 (луженая,фольга)": None,
    "медь (стружка)": None,
    "медный кабель": None,
    "медь в масле": None,
    "медь отборка": None,
    "медь блеск тонкий": None,
    # "": None,
    # "": None,
    # "": None,
    # "": None,



    "медь блеск/кусок": "медь блеск/кусок",


    # Медь (микс)
    "лом меди mix м4": "Медь (микс)",
    "лом меди (mix)": "Медь (микс)",
    "лом меди, микс": "Медь (микс)",
    "медь микс": "Медь (микс)",
    "микс": "Медь (микс)",
    "прием цветного металлолома, медь (микс),": "Медь (микс)",
    'медь 3': 'Медь (микс)',
    "медь а1-2 (микс)": "Медь (микс)",
    "лом меди а1-2, а1-2а (микс)": "Медь (микс)",
    "лом меди а-1-2": "Медь (микс)",
    "медь аi - 2": "Медь (микс)",
    "лом меди микс а1-2а": "Медь (микс)",
    "медь (mix)": "Медь (микс)",
    "медь смешанная": "Медь (микс)",
    "лом меди": "Медь (микс)",
    "медный микс": "Медь (микс)",
    "медь (микс, жженная)": "Медь (микс)",
    "медь м3": "Медь (микс)",
    # "": "Медь (микс)",
    # "": "Медь (микс)",
    # "": "Медь (микс)",
    # "": "Медь (микс)",



    # Медь (блеск)
    "лом меди м1": "Медь (блеск)",
    "лом меди (блеск)": "Медь (блеск)",
    "лом меди, блеск": "Медь (блеск)",
    "блеск": "Медь (блеск)",
    "прием цветного металлолома, медь (блеск),": "Медь (блеск)",
    "медь блеск (блестящая, без полуды, пайки, масла, краски, клемм, толщина не менее 1 мм)": "Медь (блеск)",
    'медь 1': 'Медь (блеск)',
    "медь а1-1 (блеск)": "Медь (блеск)",
    "лом меди а1-1": "Медь (блеск)",
    "лом меди а-1-1": "Медь (блеск)",
    "медь аi - 1": "Медь (блеск)",
    "медь блеск а1-1": "Медь (блеск)",
    "медь а-1-1": "Медь (блеск)",
    "медь блеск": "Медь (блеск)",
    "медь блестящая": "Медь (блеск)",
    "медь (блеск, жила от 1 мм)": "Медь (блеск)",
    "медь м1": "Медь (блеск)",
    # "": "Медь (блеск)",
    # "": "Медь (блеск)",
    # "": "Медь (блеск)",
    # "": "Медь (блеск)",
    # "": "Медь (блеск)",
    # "": "Медь (блеск)",





    # Медь (кусок)
    "лом меди м2": "Медь (кусок)",
    "лом меди (кусок)": "Медь (кусок)",
    "лом меди, кусок": "Медь (кусок)",
    "кусок": "Медь (кусок)",
    "прием цветного металлолома, медь (стружка),": "Медь (кусок)",
    "медь кусок (обожженный провод без зелени, полуды,"
    " пайки, клемм, остатков изоляции, толщина не менее 2 мм)": "Медь (кусок)",
    'медь 2': 'Медь (кусок)',
    "медь а1-1а (кусок)": "Медь (кусок)",
    "лом меди а1-1а": "Медь (кусок)",
    "лом меди а-1-1a": "Медь (кусок)",
    "лом меди а-1-1а": "Медь (кусок)",
    "медь аi -1а": "Медь (кусок)",
    "лом меди кусок  (от 10 кг)": "Медь (кусок)",
    "медь а-1-1а": "Медь (кусок)",
    "медь кусок": "Медь (кусок)",
    "медь кусковая": "Медь (кусок)",
    "медь (кусок)": "Медь (кусок)",
    "медь м2": "Медь (кусок)",
    # "": "Медь (кусок)",





}
