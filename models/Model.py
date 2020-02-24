import numpy as np

# ランダムな予想結果を返却する手動テスト用クラス
class Model:
    
    def __init__(self):
        self.pred = np.random.rand(6,1) * 5 + np.full((6, 1), 110)
    
    def fit(self, X, y):
        return None

    def predict(self, X):
        return self.pred