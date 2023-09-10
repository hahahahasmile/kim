#단순하게 반복문으로 하면 시간초과가 된다. for문과 while문(스택)을 활용하여서 시간을 단축시켰다.
n = int(input())
ans = [0]*n
stack = []
a = list(map(int,input().split()))

for i in range(n):
    while stack and a[stack[-1]]<a[i]:
        ans[stack.pop()] = a[i]
    stack.append(i)

while stack:
    ans[stack.pop()] = -1

result = ""
for i in range(n):
    result+=str(ans[i])+""

print(result)