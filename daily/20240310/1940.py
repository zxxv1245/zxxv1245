N = int(input())
M = int(input())
lst = list(map(int,input().split()))
cnt = 0
for i in range(N-1) :
    for j in range(i+1,N) :
        if lst[i]+lst[j] == M :
            cnt += 1

print(cnt)