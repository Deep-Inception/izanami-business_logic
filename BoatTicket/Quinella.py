import numpy as np
from BoatTicket.BoatTicketBase import BoatTicketBase

class Quinella(BoatTicketBase):
    def __init__(self, pred):
        super().__init__(pred)
        
    # 第３予想は1-4の可能性もあるからそこは作る
    def predict(self):
        first = super().first_prize_index()
        second = super().second_prize_index()
        third = super().third_prize_index()
        pred1_2 = [first, second]
        pred1_3 = [first, third]
        pred2_3 = [second, third]
        return pred1_2, pred1_3, pred2_3