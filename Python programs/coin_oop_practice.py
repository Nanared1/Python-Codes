import math
from random import randint

class coin:
    def __init__(self,face):
        self.side = face;
    def flipCoin(self):
        if(self.side == 0):
            return('Heads');
        else:
            return('Tails');
    def __repr__(self):
        return('Face # is %.2f'%(self.side));

money = coin(randint(0,1));
print(money.flipCoin());
