import requests
import HomePages as hp
# from HomePages.BeforeInfo import BeforeInfo
# from HomePages.RaceIndex import RaceIndex
# from HomePages.RaceList import RaceList

# 事前情報取得
r = requests.get('http://www.boatrace.jp/owpc/pc/race/beforeinfo?rno=1&jcd=06&hd=20200329')
b = hp.BeforeInfo.BeforeInfo(r)
b.scrape()

# ある日のあるレース会場のレース情報を保持する
# レースある日
# r = requests.get('http://www.boatrace.jp/owpc/pc/race/raceindex?jcd=06&hd=20200329')
# レースない日
# r = requests.get('http://www.boatrace.jp/owpc/pc/race/raceindex?jcd=06&hd=20200330')

# rp = RaceIndex(r)
# rp.scrape()
# if rp.has_race():
#     print(rp.race_urls)
# else:
#     print("no race")

r = requests.get('http://www.boatrace.jp/owpc/pc/race/racelist?rno=1&jcd=06&hd=20200329')
rp = hp.RaceList.RaceList(r)
rp.scrape()
print("end")