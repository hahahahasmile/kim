#슬라이드 알고리즘을 활용하기 위해서 deque을 활용 dequeue 첫번째에 값을 2번째에 인덱스 값을 넣어서 활용
from collections import deque
n,m = map(int,input().split())
mydeque = deque()
now = list(map(int,input().split()))
for i in range(n):
    while mydeque and mydeque[-1][0] >now[i]: #만약 mydeque의 마지막 숫자가 now[i] 보다 크면 그수는 필요가 없기에 제거 #첫번째 마이데은 마이덱이 존재하는 지 묻는것이다
        mydeque.pop()
    mydeque.append((now[i],i))
    if mydeque[0][1] <=i-m: #mydeque의 인덱스가 m개의 범위를 넘으면 제거
        mydeque.popleft()
    print(mydeque[0][0],end =' ')