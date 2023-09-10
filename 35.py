n = int(input())
A = [[0]*2 for _ in range(n)] # 2차원 배열을 만들기 위한 절차
for i in range(n):
    start,end = map(int,input().split())
    A[i][0] = end
    A[i][1] = start # 정렬을 할 때는 처음에 있는 수를 기준으로 정렬을 한다. 그럼으로 end를 중점으로 정렬을 해야하기 때문에 end를 처음으로 넣어준다.
A.sort()
end =-1
count =0
for i in range(n):
    if A[i][1] >=end:
        end = A[i][0]
        count+=1


print(count)