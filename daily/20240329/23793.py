from heapq import heappush,heappop
import sys
INF = sys.maxsize
input = sys.stdin.readline

def dijkstra(s,e,m) :

    result = [INF]*(N+1)
    result[s] = 0
    heap = [(0,s)]

    while heap :
        cost, ky = heappop(heap)

        if cost > result[ky] : continue

        for next_cost,next in G[ky] :
            if next == m : continue
            prev = result[next]
            new_cost = cost + next_cost

            if prev > new_cost :
                result[next] = new_cost
                heappush(heap,(new_cost,next))
    if result[e] == INF :
        return -1
    else :
        return result[e]
def dijkstra1(s,e) :

    result = [INF]*(N+1)
    result[s] = 0
    heap = [(0,s)]

    while heap :
        cost, ky = heappop(heap)

        if cost > result[ky] : continue

        for next_cost,next in G[ky] :
            prev = result[next]
            new_cost = cost + next_cost

            if prev > new_cost :
                result[next] = new_cost
                heappush(heap,(new_cost,next))
    if result[e] == INF :
        return -1
    else :
        return result[e]



N,M = map(int,input().split())
G = [[] for _ in range(N+1)]
for _ in range(M) :
    v1,v2,cost = map(int,input().split())
    G[v1].append((cost,v2))
X,Y,Z = map(int,input().split())

if dijkstra1(X,Y) != -1 and dijkstra1(Y,Z) != -1 :
    print(dijkstra1(X,Y) + dijkstra1(Y,Z),end = ' ')
else :
    print(-1,end = ' ')
if dijkstra(X,Z,Y) != -1 :
    print(dijkstra(X,Z,Y))
else :
    print(-1)

