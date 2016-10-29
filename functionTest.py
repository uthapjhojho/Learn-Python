
from math import sqrt
def cube(number):
    print number**3

def by_three(number):
    if number/3==0:
        return cube(sqrt(number))
    else:
        return False

n = input("Number : ")
by_three(n)
