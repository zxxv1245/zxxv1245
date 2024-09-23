from heapq import heappop,heappush
import sys
INF = sys.maxsize

def dijkstra(h) :

    result = [INF]*(n+1)
    result[h] = 0
    heap = [(0,h)]

    while heap :
        cost,ky = heappop(heap)

        if cost > result[ky] : continue

        for next_cost,next in G[ky] :
            prev = result[next]
            new_cost = cost + next_cost

            if prev > new_cost :
                result[next] = new_cost

                heappush(heap,(new_cost, next))
    return result

T = int(input())
for _ in range(1,T+1) :

    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())

    G = [[] for _ in range(n+1)]
    for _ in range(m) :
        v1,v2,cost = map(int,input().split())
        if (v1 == g and v2 == h) or (v1==h and v2==g) :
            w = cost
        G[v1].append((cost,v2))
        G[v2].append((cost,v1))
    lst = []
    for _ in range(t) :
        x = int(input())
        lst.append(x)
    lst.sort()
    ret1 = dijkstra(s)
    ret2 = dijkstra(g)
    ret3 = dijkstra(h)

    ans = []
    for i in lst :
        if (ret1[i] == ret1[g]+w+ret3[i]) or (ret1[i] == ret1[h]+w+ret2[i]) :
            ans.append(i)

    print(*ans)



