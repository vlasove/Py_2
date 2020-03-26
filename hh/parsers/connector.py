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

    def get_last_page(self):
        if self.check_connect():
            soup = bs(self.session.get(self.base_url, headers=self.headers).content, "lxml")
            pages = soup.find_all('a', attrs ={'data-qa':'pager-page'})
            return int(pages[-1].text) - 1



    def parse_salary(self, salary_str):
        m_list = salary_str.split('\xa0')
        if len(m_list) == 3:
            #$m_list = ['170', '000-230', '000']
            answer = (int(m_list[0]) + int(m_list[1].split('-')[1]))/2
            return int(answer) * 1000
        else:
            answer = m_list[0].split()[1]
            return int(answer) * 1000

    def get_info(self): 
        if self.check_connect():
            soup = bs(self.session.get(self.base_url, headers=self.headers).content, "lxml")
            columns = soup.find_all("div", attrs={"data-qa":"vacancy-serp__vacancy"})
            for col in columns:
                try:
                    title = col.find("a", attrs={"data-qa":"vacancy-serp__vacancy-title"}).text
                    company = col.find("a", attrs={"data-qa":"vacancy-serp__vacancy-employer"}).text
                    salary = col.find("span", attrs={"data-qa":"vacancy-serp__vacancy-compensation"}).text
                    self.vacancy_bag.append([ title, company, self.parse_salary(salary)])
                except:
                    #print("VACANCY SKIPPED")
                    pass






        
    