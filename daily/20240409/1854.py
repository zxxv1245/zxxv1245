from heapq import heappop,heappush
import sys
INF = sys.maxsize
input = sys.stdin.readline

def dijkstra() :

    result = [[INF]*(501) for _ in range(N+1)]
    # result = [INF]*(N+1)
    result[1][0] = 0
    heap = [(0,1,0)]

    while heap :
        cost,ky,depth = heappop(heap)

        # flag = False
        # for i in range(depth) :
        #     if cost > result[ky][i] :
        #         flag = True
        #         break
        if cost > result[ky][depth] :
            continue

        if depth+1 <= 500 :
            for next_cost,next in G[ky] :
                prev = result[next][depth+1]
                new_cost = cost + next_cost
                if prev > new_cost :
                    result[next][depth+1] = new_cost
                    heappush(heap,(new_cost,next,depth+1))
    return result

N,M,K = map(int,input().split())
G = [[] for _ in range(N+1)]

for _ in range(M) :
    v1,v2,cost = map(int,input().split())
    G[v1].append((cost,v2))
    # G[v2].append((cost,v1))

distance = dijkstra()

for dist in distance[1:] :

    dist.sort()
    if dist[K-1] == INF :
        print(-1)
    else :
        print(dist[K-1])
