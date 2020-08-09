from recordtype import recordtype
from score_function import __sum, __sum_of_number
from score_function import ConstantScoringModule as CSM
from score_function import NonConstantScoringModule as NCSM

Category = recordtype('Category', 'name explanation is_selected score_function score card_set')

class Board:
    def __init__(self):
        self.scoreboard = [
            Category('1s',              '1 point for each 1 thrown', False, __sum_of_number, [0,0], [[],[]]),
            Category('2s',              '2 point for each 2 thrown', False, __sum_of_number, [0,0], [[],[]]),
            Category('3s',              '3 point for each 3 thrown', False, __sum_of_number, [0,0], [[],[]]),
            Category('4s',              '4 point for each 4 thrown', False, __sum_of_number, [0,0], [[],[]]),
            Category('5s',              '5 point for each 5 thrown', False, __sum_of_number, [0,0], [[],[]]),
            Category('6s',              '6 point for each 6 thrown', False, __sum_of_number, [0,0], [[],[]]),
            # Category('Bonus',           'If 1s to 6s total 63 or above, then 35 points', False, __sum, []),
            Category('3 of a Kind',     '3 of the same number. Scores total value of all dice.', False, __sum, [0,0], [[],[]]),
            Category('4 of a Kind',     '4 of the same number. Scores total value of all dice.', False, __sum, [0,0], [[],[]]),
            Category('Full House',      'A 3-of-a-kind and 2-of-a-kind. Scores 25 points', False, __constant, [0,0], [[],[]]),
            Category('Small Straight',  '4 numbers in a row (any order). Scores 30 points', False, __constant, [0,0], [[],[]]),
            Category('Big Straight',    '5 numbers in a row (any order). Scores 40 points', False, __constant, [0,0], [[],[]]),
            Category('The Yacht',       '5 of a kind. Scores 50 points', False, __constant, [0,0], [[],[]]),
            Category('Chance',          'No pattern needed. Scores total value of all dice.', False, __sum, [0,0], [[],[]]),
        ]
    
    def pprint(self):
        print(self.scoreboard)

if __name__ == '__main__':
    board = Board()
    board.pprint()