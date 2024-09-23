from collections import deque

def bfs() :
    dp = [21e8] * 101
    dp[1] = 0
    Q = deque()
    Q.append(1)

    while Q :
        x = Q.popleft()

        for a in range(1,7) :
            nx = x+a
            if nx<=100 :
                if dp[nx] > dp[x]+1 :
                    dp[nx] = dp[x]+1
                    Q.append(nx)
                if nx in up :
                    if dp[up[nx]] > dp[x] + 1:
                        dp[up[nx]] = dp[x] + 1
                        Q.append(up[nx])
                if nx in down :
                    if dp[down[nx]] > dp[x] + 1:
                        dp[down[nx]] = dp[x] + 1
                        Q.append(down[nx])
                    dp[nx] = 21e8
    return dp[100]

N,M = map(int,input().split())
up = {}
down = {}
for _ in range(N) :
    u1,u2 = map(int,input().split())
    up[u1] = u2
for _ in range(M) :
    d1,d2 = map(int,input().split())
    down[d1] = d2

print(bfs())