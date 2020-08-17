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
            repr_string += '[value = {}, fixed = {}]'.format(dice.value, ' True' if dice.is_fixed else 'False')
        return repr_string

    def before_first_roll(self):
        for dice in self.dices:
            dice.is_fixed = False

    def roll(self):
        return list(val.value for val in filter(roll, self.dices)) # 이중 접근?

    def fix_value(self, fix_index): # 최적화 필요
        # ex) fix_index is '1 3 4'
        for dice in self.dices:
            dice.is_fixed = False
        for idx in fix_index.split():
            self.dices[int(idx)].is_fixed = True

    def getValue(self):
        return list(dice.value for dice in self.dices)

if __name__ == '__main__':
    dices = FiveDices()
    print(dices)
    dices.before_first_roll()
    print('='*100)
    dices.roll()
    print(dices)
    dices.fix_value('1 3 4')
    dices.roll()
    print(dices)
    dices.fix_value('2')
    dices.roll()
    print(dices)
    print(dices.getValue())