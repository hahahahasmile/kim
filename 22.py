#수의 개수는 범위가 크다 수의 범위는 10000정도 밖에 안 됨으로 범위를 배열로 지정하고 입력받은 수들을 그 배열에 집어넣으면 시간을 단축할 수 있다.
import sys
input = sys.stdin.readline
n = int(input())
count = [0] *10001
for i in range(n):
    index = int(input())
    count[index]+=1

for i in range(10001):
    while count[i]>0:
        print(i)
        count[i]-=1

