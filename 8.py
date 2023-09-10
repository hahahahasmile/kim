# 두수의 합으로 이루어진 수를 구하는 것이기 때문에 start end 를 양끝에서 시작한다.
import sys
input = sys.stdin.readline
n = int(input())
result =0
numbers = list(map(int,input().split()))
numbers.sort()
for k in range(n):
    temp  = numbers[k]
    start = 0
    end = n-1
    while start<end:
        if numbers[start]+numbers[end] == temp:
            if start!= k and end !=k:
                result+=1
                break
            elif start == k:
                start+=1
            elif end ==k:
                end-=1
        elif numbers[start]+numbers[end]<temp:
            start+=1
        else:
            end-=1

print(result)
