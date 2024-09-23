from heapq import heappop,heappush
import sys
INF = sys.maxsize
def dijkstra(k) :

    result = [[INF,[]] for _ in range(N+1)]
    result[k][0] = 0
    heap = [(0,k,[])]
    while heap :
        cost,ky,ret = heappop(heap)

        if cost > result[ky][0] : continue

        for next_cost,next in G[ky] :
            prev = result[next][0]
            new_cost = cost + next_cost

            if prev > new_cost :
                result[next][0] = new_cost
                ret = result[ky][1] + [next]
                result[next][1] = ret
                heappush(heap,(new_cost,next,ret))
    return result
N,M = map(int,input().split())

G = [[] for _ in range(N+1)]

for _ in range(M) :
    v1,v2,cost = map(int,input().split())
    G[v1].append((cost,v2))
    G[v2].append((cost,v1))

lst = [['-']*N for _ in range(N)]
for i in range(1,N+1) :
    arr = dijkstra(i)
    for j in range(1,N+1) :
        if arr[j][1] :
            lst[i-1][j-1] = arr[j][1][0]

for x in lst :
    print(*x)