import math
min,max = map(int,input().split())
check = [False]*(max-min+1)
for i in range(2,int(math.sqrt(max)+1)):
    pow = i*i
    start = int(min/pow)
    if min%pow !=0:
        start+=1
    for j in range(start,int(max/pow)+1):
        check[int(pow*j)-min] = True

count = 0
for i in range(max-min+1):
    if not check[i]:
        count+=1
print(count)