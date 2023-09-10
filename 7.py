#6.py와는 틀리게 이것은 2개의 합으로 이루어진 수를 구하는 것이기 때문에 start end는 양 옆으로 배치한다.
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
A= list(map(int,input().split()))
A.sort()
start = 0
count =0
end = n-1
while start<end:
    if A[start]+A[end]==m:
        count+=1
        start+=1
        end-=1
    elif A[start]+A[end] <m:
        start+=1
    else:
        end-=1

print(count)