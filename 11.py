#숫자들이 연속으로 연결되는 것이기 때문에 스택을 사용?
n = int(input())
A = [0]*n
for i in range(n):
    A[i] = int(input())
stack = []
num=1
result = True
answer = ""
for i in range(n):
    su = A[i]
    if su>=num:
        while su>=num: 
            stack.append(num)
            num+=1
            answer+="+\n"
        stack.pop()
        answer+="-\n"
    else:
        n = stack.pop() #스택에서의 마지막 수가 현재 배열에서의 수보다 크면 바로 연결이 안 되기 때문에 no가 되는 것이다.
        if n>su:
            print("NO")
            result =  False
            break
        else:
            answer+="-\n"
if result:
    print(answer)
