from board import Board
from dice import SixDices

class Player:
    board = Board() # 공유
    dices = SixDices() # 공유
    
    def __init__(self, _id):
        self.id = _id
        self.score = score

    def roll(self):
        return Player.dices.roll() # 다섯개 주사위값

    def getScore(self, input_board):
        # 입력하고
        # 점수 받고