from heapq import heappush,heappop

def dijkstra() :

    while heap :
        cost,x,y = heappop(heap)
        if x == N-1 and y == N-1 :
            return cost
        for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)] :
            if 0<= i < N and 0<= j < N :
                cost = lst[i][j] + distance[x][y]

                if distance[i][j] > cost :
                    distance[i][j] = cost
                    heappush(heap,(distance[i][j],i,j))


T = int(input())

for Test in range(1,T+1) :
    N = int(input())
    lst = [list(map(int,input())) for _ in range(N)]

    distance = [[21e8]*N for _ in range(N)]
    distance[0][0] = 0
    heap = [(0,0,0)]

    print(f'#{Test} {dijkstra()}')
