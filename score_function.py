from abc import ABCMeta, abstractmethod
from collections import Counter

class BaseScoringModule(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, name):
        pass

    @abstractmethod
    def evaluate(self, dice_value):
        #dices assume Six
        pass

    @abstractmethod
    def getScore(self):
        pass

# Full House, Small Straight, Big Straight, The Yacht, (Bonus)
class ConstantScoringModule(BaseScoringModule):
    constantName = ['Full House', 'Small Straight', 'Big Straight', 'The Yacht'] #dict로 수정
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def evaluate(self, dice_value):
        counter = Counter(dices)

    def getScore(self, dice_value):
        if self.evaluate(dices):
            return self.score
        else:
            return 0

#1s, 2s, 3s, 4s, 5s, 6s, 3 of a kind, 4 of a kind, Chance
class NonConstantScoringModule(BaseScoringModule):
    nonConstantName = ['1s', '2s', '3s', '4s', '5s', '6s',
                       '3 of a Kind', '4 of a Kind', 'Chance'] #dict
    def __init__(self, name, policy):
        self.name = name
        self.policy = policy # (all_sum, exact_sum)
    
    def evaluate(self, dice_value):
        return True

    def calScore(self, dice_value):
        return 0
    
    def getScore(self, dice_value):
        if self.evaluate(dice_value):
            return self.calScore(dices)
        else:
            return 0