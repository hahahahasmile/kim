#투 포인터는 다수의 수로 이루어진 수를 찾을 때 배열의 처음부터 시작과 끝이 시작한다.
n = int(input()) #수로 입력받음
count=1
start=1
end =1
sum=1
while end != n:
    if sum == n:
        count+=1
        end+=1
        sum+=end
    elif sum > n:
        sum-=start
        start+=1
    else:
       end+=1
       sum+=end

print(count)