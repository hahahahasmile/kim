#오일러 피 함수  그 수에서 소인수로 나눈 값을 그 수에서 뺀다. 
import math
n = int(input())
result = n
for p in range(2,int(math.sqrt(n)+1)):
    if n%p ==0:
        result -=result/p
    while n%p ==0:
        n /=p

if n>1:
    result -=result/n
print(int(result))