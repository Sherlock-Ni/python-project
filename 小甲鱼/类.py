import random as r

class Fish:
    def __init__(self):
        self.x = r.randint (1,10)
        self.y = r.randint (1,10)
        def move(self):
            self.x -= 1
            print('我的位置是：',self.x,self.y)
class Golden(Fish):
    pass
class Carp(Fish):
    pass
class Salmon(Fish):
    pass
class Shark(Fish):
    def __init__(self):
        super().__init__(self)
        self.hunger = True
    def eat(self):
        if self.hunger:
            print('吃货的梦想就是天天有东西吃！！！！！！！^_^')
            self.hunger = False
        else:
            print('太撑了，吃不下了！！！！')
