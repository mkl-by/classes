"""Все о классах"""

class One:
    def __init__(self):
        self.a = 1
        self.b = 2

    def setdata(self, aaa):
        self.data = aaa

    def setdispl(self):
        print(self.data)

class Two:
    def __init__(self):
        self.b = 1
        self.a = 2
        self.e = 4

    def setdispl(self):
        print('aaaaaa')

class Tree(Two, One):
    def __init__(self):
        # One().__init__()
        # Two().__init__()
        self.d = 3
        self.c = 3
        self.b = 3

    def setdispl(self):
        print('asdasd', self.data)


if __name__=='__main__':
    #рассматриваем класс tree переопределяем атрибуты его класса
    tree = Tree()
    tree.setdata('qwe')
    tree.setdispl()
    print(tree.__dict__)


