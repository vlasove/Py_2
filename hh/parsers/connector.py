import requests 
from bs4 import BeautifulSoup as bs



class Parser:
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "accept" : "*/*"    
    }

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.vacancy_bag = []

    def check_connect(self):
        if self.session.get(self.base_url, headers=self.headers).status_code == 200:
            return True 
        return False

    def parse_salary(self, salary_str) -> int:
        если строка '170\xa0000-230\xa0000 руб.' -- > (230 + 170)/2 * 1000
        если строка 'от 200\xa0000 руб.' --> 200000
        если строка 'до 200\xa0000 руб.' --> 200000

    def get_info(self): 
        if self.check_connect():
            soup = bs(self.session.get(self.base_url, headers=self.headers).content, "lxml")
            columns = soup.find_all("div", attrs={"data-qa":"vacancy-serp__vacancy"})
            _id = 0
            for col in columns:
                try:
                    title = col.find("a", attrs={"data-qa":"vacancy-serp__vacancy-title"}).text
                    company = col.find("a", attrs={"data-qa":"vacancy-serp__vacancy-employer"}).text
                    salary = col.find("span", attrs={"data-qa":"vacancy-serp__vacancy-compensation"}).text
                    self.vacancy_bag.append([_id, title, company, self.parse_salary(salary)])
                    _id += 1
                except:
                    print("VACANCY SKIPPED")






        
    