def __sum(dices): # 3 of a kind, 4 of a kind, Chance
    return sum(dices)

def __sum_of_number(dices, i): #1s, 2s, 3s, 4s, 5s, 6s
    return sum(x for x in dices if x == i)

# Full House, Small Straight, Big Straight, The Yacht, (Bonus)
def __constant(dices, eval_fn, const_score_val): 
    if eval_fn(dices):
        return const_score_val
    else:
        return 0

################################################################

from abc import ABCMeta, abstractmethod
from collections import Counter

class BaseScoringModule(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, score):
        pass

    @abstractmethod
    def evaluate(self, dices):
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

    def evaluate(self, dices):
        return True

    def score(self, dices):
        if self.evaluate(dices):
            return self.score
        else:
            return 0

#1s, 2s, 3s, 4s, 5s, 6s, 3 of a kind, 4 of a kind, Chance
class NonConstantScoringModule(BaseScoringModule):
    nonConstantName = ['1s', '2s', '3s', '4s', '5s', '6s',
                       '3 of a Kind', '4 of a Kind', 'Chance'] #dict
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def evaluate(self, dices):
        return True

    def calScore(self, dices):
        return 0
    
    def score(self, dices):
        if self.evaluate(dices):
            return self.calScore(dices)
        else:
            return 0