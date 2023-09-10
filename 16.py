#버블 정렬 프로그램 -> 몇 번 바뀌었는냐? 정렬하기 전의 인덱스와 정렬한후의 인덱스 차이가 가장 큰 것을 파악하면 끝이다.
import sys
input = sys.stdin.readline
n = int(input())
A = []
for i in range(n):
    A.append((int(input()),i))

max = 0
B = sorted(A)
for i in range(n):
    if max < B[i][1] -i:
        max = B[i][1]-i

print(max+1)
