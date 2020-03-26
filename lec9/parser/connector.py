import requests 
from bs4 import BeautifulSoup as bs


BASE_URL = 'https://auto.ru/'

class Parser:
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "accept" : "*/*"    
    }

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.auto_bag = []

    def check_connect(self):
        if session.get(self.base_url, headers=self.headers).status_code == 200:
            return True 
        return False

    def get_info(self): 
        if self.check_connect():
            soup = bs(session.get(self.base_url, headers=self.headers).content, "lxml")
            columns = soup.find_all("a", attrs={"class":"IndexMarks__item"})
            _id = 0
            for col in columns:
                name = col.find("div", attrs={"class":"IndexMarks__item-name"}).text
                amount = col.find("div", attrs={"class":"IndexMarks__item-count"}).text

                self.auto_bag.append([_id, name, amount])
                _id += 1






        
    