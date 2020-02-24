# レース結果の予想を返すクラス
import numpy as np
from NiceBoatUtils import mathUtils
from sklearn.preprocessing import StandardScaler
print("Run race.py")

def win_rate(pred):
    recip = mathUtils.reciprocal(pred)
    scaler = StandardScaler()
    recip_scaler = scaler.fit_transform(recip)
    return mathUtils.softmax(recip_scaler) 