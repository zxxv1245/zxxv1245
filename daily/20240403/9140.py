from heapq import heappop,heappush
import sys
INF = sys.maxsize
def dijkstra() :
    result = [INF]*(V+1)
    result[s] = 0
    heap = [(0,s)]

    while heap :
        cost,ky = heappop(heap)

        if cost > result[ky] : continue

        for next_cost,next in G[ky] :
            prev = result[next]
            new_cost = cost + next_cost

            if prev > new_cost :
                result[next] = new_cost
                heappush(heap,(new_cost,next))
    return result[e]

while True :
    V,E,s,e = map(int,input().split())
    if V==0 and E == 0 and s==0 and e== 0 :
        break
    G = [[] for _ in range(V+1)]
    for _ in range(E) :
        v1,v2,cost = map(int,input().split())
        G[v1].append((cost,v2))

    print(dijkstra())