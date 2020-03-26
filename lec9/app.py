from model.auto import Auto 
from parser.connector import Parser 

BASE_URL = 'https://auto.ru/'

p = Parser(BASE_URL)
p.get_info()

for item in p.auto_bag:
    auto = Auto(item[0], item[1], item[2])
    auto.add_to_database()