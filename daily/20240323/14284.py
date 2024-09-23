from heapq import heappop,heappush
import sys
INF = sys.maxsize

N,M = map(int,input().split())

G = [[]for _ in range(N+1)]

for _ in range(M) :
    v1,v2,weight = map(int,input().split())
    G[v1].append((weight,v2))
    G[v2].append((weight,v1))
s,t = map(int,input().split())

result = [INF]*(N+1)
result[s] = 0
heap = [(0,s)]

while heap :
    weight,ky = heappop(heap)

    if weight > result[ky] : continue

    for next_weight,next in G[ky] :
        prev = result[next]
        new_weight = weight + next_weight

        if prev > new_weight :
            result[next] = new_weight
            heappush(heap,(new_weight,next))

print(result[t])