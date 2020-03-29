import re

# 直前情報のレーサーごとの情報を保持するクラス
class BeforeInfoRacer:
    number_index = 1
    weight_index = 3
    exhibition_index = 4
    tilt_index = 5
    
    def __init__(self, elm):
        self.elm = elm
        self.number = None
        self.weight = None
        self.exhibition = None
        self.tilt = None
        self.scrape()
        
    def scrape(self):
        self.pase_elm()
        print("number: %s, weight: %s, exb: %s, tilt: %s" % (self.number, self.weight, self.exhibition, self.tilt))
    
    def pase_elm(self):
        tds = self.elm.select_one("tr").select("td")
        self.weight = tds[BeforeInfoRacer.weight_index].get_text()
        self.exhibition = tds[BeforeInfoRacer.exhibition_index].get_text()
        self.tilt = tds[BeforeInfoRacer.tilt_index].get_text()
        src = tds[BeforeInfoRacer.number_index].select_one("img")['src']
        self.number = self.parse_src(src)
    
    def parse_src(self, string):
        return re.findall('/racerphoto/(.*).jpg', string)[0]
