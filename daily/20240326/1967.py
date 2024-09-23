from heapq import heappop,heappush

def dijkstra() :

    while heap :
        cost,ky = heappop(heap)

        if cost > result[ky] : continue

        for next_cost,next in G[ky] :
            prev = result[next]
            new_cost = cost + next_cost

            if prev > new_cost :
                result[next] = new_cost
                heappush(heap,(new_cost,next))

N = int(input())

G = [[] for _ in range(N+1)]
for _ in range(N-1) :
    v1,v2,cost = map(int,input().split())
    G[v1].append((cost,v2))
    G[v2].append((cost,v1))


result = [21e8] * (N + 1)
result[1] = 0
heap = [(0,1)]
dijkstra()
maxV = -21e8
ret = []
for i in range(1,N+1) :
    if maxV < result[i] :
        ret.clear()
        maxV = result[i]
        maxP = i
        ret.append(i)
    elif maxV == result[i] :
        ret.append(i)

ans = -21e8
for k in ret :
    result = [21e8] * (N + 1)
    result[k] = 0
    heap = [(0,k)]
    dijkstra()
    if ans < max(result[1:]) :
        ans = max(result[1:])

print(ans)