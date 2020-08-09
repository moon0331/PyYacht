from score_function import __sum, __sum_of_number

from random import randint
from recordtype import recordtype

Dice = recordtype('Dice', 'number value is_fixed roll')

class SixDices:
    def __init__(self):
        self.dices = [Dice(i, 0, False, lambda fixed : randint(1,6) if fixed else 0) for i in range(5)]

    def __repr__(self):
        repr_string = ''
        for dice in self.dices:
            repr_string += str(dice)
        return repr_string

    def before_first_roll(self):
        for dice in self.dices:
            dice.is_fixed = False

    def roll(self):
        return [dice.roll(dice.is_fixed) for dice in self.dices]

    def fix_value(self, fix_index):
        # ex) fix_index is '1 3 4'
        for idx in fix_index.split():
            self.dices[int(idx)].is_fixed = True

if __name__ == '__main__':
    dices = SixDices()
    print(dices)
    print(dices.roll())
    print(dices.fix_value('1 3 4'))