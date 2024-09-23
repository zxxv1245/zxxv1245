from heapq import heappop,heappush
import sys
INF = sys.maxsize
T = int(input())
def dijkstra(i) :
    result = [INF]*(N+1)
    result[i] = 0
    heap = [(0,i)]

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
for _ in range(T) :
    N,M = map(int,input().split())
    G = [[] for _ in range(N+1)]
    for _ in range(M) :
        v1,v2,cost = map(int,input().split())
        G[v1].append((cost,v2))
        G[v2].append((cost,v1))
    K = int(input())
    lst = list(map(int,input().split()))

    minV = INF
    for i in range(1,N+1) :
        ret = 0
        arr = dijkstra(i)
        for j in lst :
            ret += arr[j]
        if minV > ret :
            minV = ret
            minP = i
        elif minV == ret :
            minP = min(minP,i)
    print(minP)