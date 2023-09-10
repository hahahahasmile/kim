#파이썬은 집합 자료형을 이용하여서 이런 문자열 문제를 쉽게 풀 수 있다.
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
textlist = set([input() for _ in range(n)])
count =0
for _ in range(m):
    subtext = input()
    if subtext in textlist:
        count+=1
print(count)
