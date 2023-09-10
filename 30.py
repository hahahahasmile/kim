n,m = map(int,input().split())
music = list(map(int,input().split()))
def find(v):
    global music
    answer = 0
    sum =0
    for i in range(n):
        sum+=music[i]
        if sum >v:
            sum = music[i]
            answer+=1
    if sum !=0:
        answer+=1
    return answer

start =0
end =0
for i in music:
    if start<i:
        start = i
    end+=i
while start<=end:
    mid = int((start+end)/2)
    result = find(mid)
    if result>m:
        start = mid+1
    else:
        end = mid-1

print(start)
