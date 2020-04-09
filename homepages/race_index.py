from bs4 import BeautifulSoup

# ある日のあるレース会場のレース情報を保持するクラス
class RaceIndex:
    base_url = 'http://www.boatrace.jp'
    def __init__(self, request):
        self.text = request.text
        self.soup = BeautifulSoup(request.text, 'html.parser')
        self.race_urls = []
        
    def scrape(self):
        races = self.soup.select('div.contentsFrame1 div.table1 tbody')
        self.race_urls = [RaceIndex.base_url + race.select('td a')[0]['href'] for race in races]
        
    def has_race(self):
        return len(self.race_urls) > 0