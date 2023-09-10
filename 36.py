answer = 0
A = list(map(str,input().split('-')))
def mysum(i):
    sum =0
    temp = str(i).split('+')
    for i in temp:
        sum+=int(i)
    return sum

for i in range(len(A)):
    if i==0:
        answer+=mysum(A[i])
    else:
        answer-=mysum(A[i])

print(answer)