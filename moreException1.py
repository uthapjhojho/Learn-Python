class Calculator:
    @staticmethod
    def power(n, p):
        try:
            if n < 0 or p < 0:
                raise
            else:
                return n ** p
        except:
            return ('n and p should be non-negative')




x = int(input("input Number Data : "))


arr = [input().split() for i in range(x)]
arr = [[int(j) for j in i] for i in arr]

for item in arr:
    print(Calculator.power(item[0], item[1]))
