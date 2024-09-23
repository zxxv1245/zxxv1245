from heapq import heappush,heappop


N,M = map(int,input().split())
G = [[] for _ in range(N+1)]
for _ in range(M) :
    v1,v2,cost = map(int,input().split())
    G[v1].append((cost,v2))
    G[v2].append((cost,v1))

result = [21e8]*(N+1)
result[1] = 0
heap = [(0,1)]

while heap :
    cost,ky = heappop(heap)

    if cost > result[ky] : continue

    for next_cost,next in G[ky] :
        prev = result[next]
        new_cost = cost + next_cost
        if prev > new_cost :
            result[next] = new_cost
            heappush(heap,(new_cost,next))

print(result[N])