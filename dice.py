from score_function import __sum, __sum_of_number

from random import randint
from recordtype import recordtype

Dice = recordtype('Dice', 'number value is_fixed roll')
# 이전값 저장해야 함 (익명함수로 불가능) -> 클래스로?

def roll(dice):
    if dice.is_fixed:
        return str(dice.value)+'f'
    else:
        dice.value = randint(1,6)
        return dice.value

class FiveDices:
    def __init__(self):
        self.dices = [Dice(i, 0, False, roll) for i in range(5)]

    def __repr__(self):
        repr_string = ''
        for dice in self.dices:
            repr_string += str(dice)
        return repr_string

    def before_first_roll(self):
        for dice in self.dices:
            dice.is_fixed = False

    def roll(self):
        return [dice.value for dice in filter(roll, self.dices)]

    def fix_value(self, fix_index):
        # ex) fix_index is '1 3 4'
        for idx in fix_index.split():
            self.dices[int(idx)].is_fixed = True

if __name__ == '__main__':
    dices = FiveDices()
    #print(dices)
    dices.before_first_roll()
    print('='*100)
    print(dices.roll())
    print(dices)
    dices.fix_value('1 3 4')
    print(dices.roll())
    print(dices)
    dices.fix_value('2')
    print(dices.roll())
    print(dices)