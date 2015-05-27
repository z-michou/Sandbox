import math

__author__ = 'igore_000'

class Solver:
    def demo(self):
        a = int(input('a '))
        b = int(input('b '))
        c = int(input('c '))
        pre_dis = b**2 - 4*a*c
        if pre_dis >= 0:
            discreminant = math.sqrt(pre_dis)
            root1 = (-b + discreminant) / (2*a)
            root2 = (-b - discreminant) / (2*a)
            print (root1, root2)
        else:
            print('error')


Solver().demo()
