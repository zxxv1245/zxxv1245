from heapq import heappop,heappush
import sys
INF = sys.maxsize
def dijkstra(k) :


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
    return max(result[1:])

N = int(input())
G = [[] for _ in range(N+1)]
for _ in range(N) :
    info = list(map(int,input().split()))
    v1 = info[0]
    i = 1
    while info[i] != -1 :
        G[v1].append((info[i+1],info[i]))
        i+=2
result = [INF]*(N+1)
a = result.index(dijkstra(1))
result = [INF]*(N+1)
print(dijkstra(a))