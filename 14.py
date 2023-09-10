from queue import PriorityQueue
import sys
print = sys.stdout.write
input = sys.stdin.readline
n = int(input())
q = PriorityQueue()
for i in range(n):
    request = int(input())
    if request ==0:
        if q.empty():
            print('\0\n')
        else:
            temp = q.get()
            print(str((temp[1]))+'\n') # 우선순위 큐에 넣는 게 두 개여서?
    else:
        q.put((abs(request),request)) # 우선순위 큐에 들어가는 함수들의 우선순위 정하기