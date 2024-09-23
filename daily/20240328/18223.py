from heapq import heappop,heappush
import sys
INF = sys.maxsize
def dijkstra(k,v) :
    result = [INF]*(V+1)
    result[k] = 0
    heap = [(0,k)]

    while heap:
        cost,ky = heappop(heap)

        if cost > result[ky] :continue

        for next_cost,next in G[ky] :
            prev = result[next]
            new_cost = cost + next_cost

            if prev > new_cost :
                result[next] = new_cost
                heappush(heap,(new_cost,next))

    return result[v]
V,E,P = map(int,input().split())
G = [[]for _ in range(V+1)]

for _ in range(E) :
    v1,v2,cost = map(int,input().split())
    G[v1].append((cost,v2))
    G[v2].append((cost,v1))

ret1 = dijkstra(1,V)

ret2 = dijkstra(1,P)

ret3 = dijkstra(P,V)

if ret1 == ret2+ret3 :
    print('SAVE HIM')
else :
    print('GOOD BYE')
