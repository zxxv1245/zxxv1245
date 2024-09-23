from heapq import heappush,heappop
import sys
INF = sys.maxsize


def dijkstart(a):
    result = [INF] * (N + 1)
    result[a] = 0
    heap = [(0, a)]

    while heap:
        cost, ky = heappop(heap)

        if cost > result[ky]: continue

        for next_cost, next in G[ky]:
            prev = result[next]
            new_cost = cost + next_cost

            if prev > new_cost:
                result[next] = new_cost
                heappush(heap, (new_cost, next))
    return result[1:]
N,M,X = map(int,input().split())

G = [[] for _ in range(N+1)]

for _ in range(M) :
    v1,v2,cost = map(int,input().split())
    G[v1].append((cost,v2))


for i in range(1,N+1) :
    print(dijkstart(i))