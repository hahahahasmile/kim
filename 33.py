from queue import PriorityQueue #우선순위 큐를 import는 이런 식으로 처리한다.
queue = PriorityQueue()
n = int(input())
for i in range(n):
    data = int(input())
    queue.put(data) # 우선순위 큐에 수를 집어넣을 때는 put을 쓴다.

data1=0
data2=0
sum = 0
while queue.qsize()>1: # 우선순위 큐의 사이즈는 qsize()이다
    data1 = queue.get()
    data2 = queue.get()
    temp = data1+data2
    queue.put(temp)
    sum += temp

print(sum)
