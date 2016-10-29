class Calculator:
    def power(n, p):
        try:
            pass
        except Exception as e:
            raise


    x = int(input("input Number Data : "))


    arr = [input().split() for i in range(x)]
    arr = [[int(j) for j in i] for i in arr]

    for item in arr:
         for member in item:
             if member<0:
                 print("n and p should be non-negative")
             

    #print (3**3)

    #barr = [int(x) for x in arr]
    #arr[i] = list(map(int, input().split()))
    #magazine = raw_input("Magazine  : ").strip().split(' ')
