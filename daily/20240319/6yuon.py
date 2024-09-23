from collections import deque
def bfs() :

    while Q :
        x = Q.popleft()
        if x == M :
            print(f'#{Test} {dp[x]}')
            return
        for i in [x+1,x-1,x*2,x-10] :
            if 0<= i <= 1000000 and dp[i] == 0 :
                dp[i] = dp[x]+1
                Q.append(i)
            elif 0<= i <= 1000000 and dp[i] != 0 :
                dp[i] = min(dp[i],dp[x]+1)
T = int(input())

for Test in range(1,T+1) :
    N,M = map(int,input().split())

    dp = [0]*1000001
    Q = deque()
    Q.append(N)
    bfs()
