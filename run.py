# 各クラステスト実行用のクラス

from models.Model import Model
from NiceBoatUtils import RaceUtil
from BoatTicket.Exacta import Exacta
from BoatTicket.Quinella import Quinella
import numpy as np

ml = Model()
pred = ml.predict(0)
print("predict race time")
print(pred)
print("win rate")
win_rate = RaceUtil.win_rate(pred)
print(win_rate)
ex = Exacta(win_rate)
print("2連単")
print(ex.predict())

qu = Quinella(win_rate)
print("2連複")
print(qu.predict())


