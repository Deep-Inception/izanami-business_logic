import requests
from HomePages.BeforeInfo import BeforeInfo
from HomePages.RaceIndex import RaceIndex

# 事前情報取得
# r = requests.get('http://www.boatrace.jp/owpc/pc/race/beforeinfo?rno=1&jcd=06&hd=20200329')
# b = BeforeInfo(r)
# b.scrape()

# ある日のあるレース会場のレース情報を保持する
# レースある日
r = requests.get('http://www.boatrace.jp/owpc/pc/race/raceindex?jcd=06&hd=20200329')
# レースない日
# r = requests.get('http://www.boatrace.jp/owpc/pc/race/raceindex?jcd=06&hd=20200330')

rp = RaceIndex(r)
rp.scrape()
if rp.has_race():
    print(rp.race_urls)
else:
    print("no race")

print("end")