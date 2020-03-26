import requests 
from bs4 import BeautifulSoup as bs
import sqlite3 

conn = sqlite3.connect('data.db')
cur = conn.cursor()

query_create = "CREATE TABLE IF NOT EXISTS autos (id INT, mark TEXT, amount INT)"
cur.execute(query_create)

query_insert = "INSERT INTO autos VALUES(?, ? ,?)"


BASE_URL = 'https://auto.ru/'
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "accept" : "*/*"    
}

session = requests.Session()
my_request = session.get(BASE_URL, headers=headers)

if my_request.status_code == 200:
    print("CONNECT SUCCESSFULL!")
    soup = bs(my_request.content, "lxml")
    columns = soup.find_all("a", attrs={"class":"IndexMarks__item"})
    _id = 0
    for col in columns:
        name = col.find("div", attrs={"class":"IndexMarks__item-name"}).text
        amount = col.find("div", attrs={"class":"IndexMarks__item-count"}).text

        cur.execute(query_insert, (_id, name, int(amount)))
        _id += 1
        
    conn.commit()
    conn.close()