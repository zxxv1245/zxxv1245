from heapq import heappush,heappop
import sys
INF = sys.maxsize
def dijkstra() :

    result = [INF]*N
    result[0] = 0
    heap = [(0,0)]

    while heap :
        time,ky = heappop(heap)

        if time > result[ky] : continue

        for next_time,next in G[ky] :
            prev = result[next]
            new_time = time + next_time

            if prev > new_time and see[next] == 0:
                result[next] = new_time
                heappush(heap,(new_time,next))
    return result
N,M = map(int,input().split())

see = list(map(int,input().split()))
see[N-1] = 0
G = [[] for _ in range(N+1)]

for _ in range(M) :
    v1,v2,time = map(int,input().split())
    G[v1].append((time,v2))
    G[v2].append((time,v1))


if dijkstra()[N-1] == INF :
    print(-1)
else :
    print(dijkstra()[N-1])