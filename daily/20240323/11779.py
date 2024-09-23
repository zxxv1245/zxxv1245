from heapq import heappush,heappop
import sys
INF = sys.maxsize
N = int(input())
M = int(input())

G = [[] for _ in range(N+1)]

for _ in range(M) :
    v1,v2,cost = map(int,input().split())
    G[v1].append((cost,v2))
s,e = map(int,input().split())


result = [[INF,[s]] for _ in range(N+1)]
result[s][0] = 0
heap = [(0,s,[s])]

while heap :
    cost, ky,ret = heappop(heap)

    if cost > result[ky][0] : continue

    for next_cost,next in G[ky] :
        prev = result[next][0]
        new_cost = cost + next_cost

        if prev > new_cost :
            result[next][0] = new_cost
            ret = result[ky][1] + [next]
            result[next][1] = ret
            heappush(heap,(new_cost,next,ret))


print(result[e][0])
print(len(result[e][1]))
print(*result[e][1])