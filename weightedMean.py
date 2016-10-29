n = int(input())
x= list(map(int, input().split()))
w= list(map(int, input().split()))

sumxw=0

for i in range(n):
    sumxw+=(x[i]*w[i])
sumw=sum(w)
if (sumxw/sumw)%1==0:
    print (sumxw/sumw)
else:
    print (round((sumxw/sumw),1))
