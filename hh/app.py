from model.vacancy import Vacancy
from parsers.connector import Parser 

from tqdm import tqdm 

BASE_URL = 'https://hh.ru/search/vacancy?L_is_autosearch=false&area=1&clusters=true&enable_snippets=true&search_period=30&text=JavaScript&page=%i'

p = Parser(BASE_URL%(0))
last_page = p.get_last_page()
for j in tqdm(range(0, last_page + 1)):
    current_parser = Parser(BASE_URL%j)
    current_parser.get_info()
    for vac in current_parser.vacancy_bag:
        new_vac = Vacancy(vac[0], vac[1], vac[2])
        new_vac.add_to_database()
