from heapq import heappop,heappush

def dijkstra() :

    result = [21e8]*(V+1)
    result[S] = 0
    heap = [(0,S)]

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

T = int(input())

for _ in range(1,T+1) :
    V,E,S = map(int,input().split())
    G = [[] for _ in range(V+1)]
    for _ in range(E) :
        v2,v1,cost = map(int,input().split())
        G[v1].append((cost,v2))

    ret = dijkstra()
    maxV = -21e8
    cnt = 0
    for i in ret :
        if i != 21e8 :
            cnt += 1
            if maxV < i :
                maxV = i

    print(cnt, maxV)