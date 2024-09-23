from heapq import heappush,heappop

def dijkstra() :
    result = [21e8]*(N+1)
    result[X] = 0
    heap = [(0,X)]

    while heap :
        cost, ky = heappop(heap)

        if cost > result[ky] : continue

        for next_cost,next in G[ky] :
            prev = result[next]
            new_cost = cost + next_cost

            if prev > new_cost :
                result[next] = new_cost
                heappush(heap,(new_cost,next))
    return result

N,M,K,X = map(int,input().split())

G = [[] for _ in range(N+1)]

for _ in range(M) :
    v1,v2 = map(int,input().split())
    G[v1].append((1,v2))

ret = dijkstra()

for i in range(1,N+1) :
    if K not in ret :
        print(-1)
        break
    if ret[i] == K :
        print(i)

