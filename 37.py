import math
n,m = map(int,input().split())
A = [0] *(m+1)
for i in range(2,m+1):
    A[i] = i

for i in range(2,int(math.sqrt(m))+1):
    if A[i] ==0:
        continue
    for j in range(i+i, m+1,i):
        A[j] =0

for i in range(n,m+1):
    if A[i] !=0:
        print(A[i])