from heapq import heappop,heappush
import sys
INF = sys.maxsize
input = sys.stdin.readline
def dijkstra(k) :
    result = [INF]*(N+1)
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
A,B,C = map(int,input().split())
G = [[] for _ in range(N+1)]
M = int(input())
for _ in range(M) :
    v1,v2,cost = map(int,input().split())
    G[v1].append((cost,v2))
    G[v2].append((cost,v1))

dijk_A = dijkstra(A)
dijk_B = dijkstra(B)
dijk_C = dijkstra(C)

ret = [-1]
for i in range(1,N+1) :
    minV = min(dijk_A[i],dijk_B[i],dijk_C[i])
    ret.append(minV)
maxV = max(ret)
print(ret.index(maxV))