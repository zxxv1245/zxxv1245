N = int(input())

lst= [list(map(int,input().split()))for _ in range(N)]
lst.sort()

lst.sort(key = lambda x : x[1] )

end = 0
cnt = 0

for i in lst :
    if i[0] >= end :
        cnt += 1
        end = i[1]

print(cnt)