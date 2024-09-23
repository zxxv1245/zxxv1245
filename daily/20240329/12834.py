from heapq import heappush,heappop
import sys
INF = sys.maxsize

def dijkstra(k) :
    result = [INF]*(M+1)
    result[k] = 0
    heap = [(0,k)]

    while heap :
        cost,ky = heappop(heap)

        if cost > result[ky] : continue

        for next_cost,next in G[ky] :
            prev = result[next]
            new_cost = cost + next_cost

            if prev > new_cost :
                result[next] = new_cost
                heappush(heap,(new_cost,next))
    return result
N,M,E = map(int,input().split())
KI,CR = map(int,input().split())
lst = list(map(int,input().split()))
G = [[] for _ in range(M+1)]
for _ in range(E) :
    v1,v2,cost = map(int,input().split())
    G[v1].append((cost,v2))
    G[v2].append((cost,v1))
ret = 0
for i in range(N) :
    ans = dijkstra(lst[i])
    if ans[KI] == INF :
        ans[KI] = -1
    if ans[CR] == INF :
        ans[CR] = -1
    ret += ans[KI] + ans[CR]
print(ret)