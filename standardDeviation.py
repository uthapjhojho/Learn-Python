import numpy as np
import math
from scipy import stats

size = int(input())
numbers = list(map(int, input().split()))
meanx=np.mean(numbers)
totArr = sum(list(map(lambda x:(x - meanx) ** 2, numbers)))
print(round(math.sqrt(totArr/size), 1))

#input  :
#5
#10 40 30 50 20

#output :
#14.1
