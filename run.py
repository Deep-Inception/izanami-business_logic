# 各クラステスト実行用のクラス

from models.Model import Model
from NiceBoatUtils import RaceUtil
import boatticket as bt
import numpy as np

ml = Model()
pred = ml.predict(0)
print("predict race time")
print(pred)
print("win rate")
win_rate = RaceUtil.win_rate(pred)
print(win_rate)
ex = bt.exacta.Exacta(win_rate)
print("2連単")
print(ex.predict())

qu = bt.quinella.Quinella(win_rate)
print("2連複")
print(qu.predict())

tri = bt.trio.Trio(win_rate)
print("3連複")
print(tri.predict())