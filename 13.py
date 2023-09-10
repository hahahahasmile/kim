#deque을 이용해서 문제 해결
from collections import deque
n = int(input())
dq = deque()
for i in range(1,n+1):
    dq.append(i)
while len(dq)>1:
    dq.popleft() #popleft() 가장 위에 있는 수를 제거하는 것이다.
    dq.append(dq.popleft())

print(dq[0])