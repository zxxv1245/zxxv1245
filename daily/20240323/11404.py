from heapq import heappop,heappush
import sys
INF = sys.maxsize
def dijkstra(k) :

    result = [INF] * (N+1)
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

N = int(input())
M = int(input())

G = [[] for _ in range(N+1)]

for _ in range(M) :
    v1,v2,cost = map(int,input().split())
    G[v1].append((cost,v2))


lst = [[0]*N for _ in range(N)]
for i in range(1,N+1) :
    arr = dijkstra(i)
    for j in range(1,N+1) :
        if arr[j] == INF : continue
        lst[i-1][j-1] = arr[j]

for x in lst :
    print(*x)