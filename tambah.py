# Complete the function below.
from math import *
import os

def  sum(numbers):
    for i in range(numbers):
        temp += numbers


f = open(os.environ['OUTPUT_PATH'], 'w')


_numbers_cnt = 0
_numbers_cnt = int(input())
_numbers_i=0
_numbers = []
while _numbers_i < _numbers_cnt:
    _numbers_item = int(input());
    _numbers.append(_numbers_item)
    _numbers_i+=1


res = sum(_numbers);
f.write(str(res) + "\n")

f.close()
