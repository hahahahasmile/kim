from queue import PriorityQueue
mq = PriorityQueue()
pq = PriorityQueue()
zero =0
one =0
sum = 0
n = int(input())
for i in range(n):
    data = int(input())
    if data>1:
        pq.put(-1*data)
    elif data==1:
        one+=1
    elif data==0:
        zero+=1
    else:
        mq.put(data)

while pq.qsize()>1:
    data1 = pq.get()*-1
    data2 = pq.get()*-1
    sum += data1*data2

if pq.qsize()>0:
    sum+= pq.get()*-1

while mq.qsize()>1:
    data1 =mq.get()
    data2 =mq.get()
    sum+= (data1*data2)

if mq.qsize()>0:
    data1 = mq.get()
    if zero>0:
        sum+=0
    else:
        sum+=data1

sum+=one
print(sum)
