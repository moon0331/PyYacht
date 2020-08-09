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

class BaseScoringModule:
    def __init__(self, score):
        self.score = score

    def evaluate(self, dices):
        raise NotImplementedError

    def getScore(self):
        raise NotImplementedError

class ConstantScoringModule(BaseScoringModule):
    def __init__(self, score):
        BaseScoringModule.__init__(self, score)

    def evaluate(self, dices):
        return True

    def score(self):
        return self.score

class NonConstantScoringModule(BaseScoringModule):
    def __init__(self, score):
        BaseScoringModule.__init__(self, score)
    
    def evaluate(self, dices):
        return True
    
    def score(self):
        return self.score