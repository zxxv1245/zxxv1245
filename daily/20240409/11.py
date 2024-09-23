from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = sys.maxsize

def dfs(x,k,sumV) :
    global minD
    if  x == e :
        if minD > k :
            minD = k
        ret.append([sumV,k])
        return

    for cost,ky in G[x] :
        if visited[ky] != 1 :
            visited[ky] = 1
            dfs(ky,k+1,sumV+cost)
            visited[ky] = 0

N,M,K = map(int,input().split())
s,e = map(int,input().split())
G = [[] for _ in range(N+1)]
for _ in range(M) :
    v1,v2,cost = map(int,input().split())
    G[v1].append((cost,v2))
    G[v2].append((cost,v1))
minD = INF
visited = [INF]*(N+1)
visited[s] = 1
P = 0
ret = []
dfs(s,0,0)
dee = min(ret)[1]
print(min(ret)[0])
for _ in range(K) :
    p = int(input())
    if minD != dee :
        for a in ret :
            a[0] += p*(a[1])
        dee = min(ret)[1]
        ans = min(ret)[0]
        print(ans)
    elif minD == dee :
        ans += p*dee
        print(ans)





