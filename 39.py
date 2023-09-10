import math
n = int(input())
A = [0] *(1000001)
for i in range(1000001):
    A[i] = i
for i in range(2,int(math.sqrt(len(A))+1)):
    if A[i] ==0:
        continue
    for j in range(i+i,len(A),i):
        A[j] = 0

def ischeck(target):
    temp = list(str(target))
    start =0
    end = len(temp)-1
    while start<end:
        if temp[start]!= temp[end]:
            return False
        start+=1
        end-=1
    return True

i = n
while True:
    if A[i]!=0:
        result = A[i]
        if ischeck(result):
            print(result)
            break  
    i+=1

