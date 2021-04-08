"""Все о классах"""


class One:
    def __init__(self):
        self.a = 1
        self.b = 2

class Two:
    def __init__(self):
        self.b = 1
        self.a = 2
        self.e = 4

class Tree(One, Two):
    def __init__(self):
        super().__init__()
        self.d = 3
        self.c = 3
        self.b = 3

if __name__=='__main__':
    #рассматриваем класс tree
    #one = One()
    #two = Two()
    tree = Tree()
    #
    # print(one.__dict__)
    # print(two.__dict__)
    print(tree.__dict__)


