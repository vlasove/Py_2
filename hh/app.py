from model.auto import Auto 
from parsers.connector import Parser 

BASE_URL = 'https://hh.ru/search/vacancy?L_is_autosearch=false&area=1&clusters=true&enable_snippets=true&search_period=30&text=Python&page=0'

p = Parser(BASE_URL)
p.get_info()

print(p.vacancy_bag)

# for item in p.auto_bag:
#     auto = Auto(item[0], item[1], item[2])
#     auto.add_to_database()