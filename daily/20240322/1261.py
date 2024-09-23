from heapq import heappush,heappop

def dijkstra() :

    distance = [[21e8] * M for _ in range(N)]
    distance[0][0] = 0
    heap = [(0, 0, 0)]

    while heap :
        cost,x,y = heappop(heap)
        if x == N-1 and y == M-1 :
            return cost
        for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)] :
            if 0<= i < N and 0<= j < M :
                cost = distance[x][y] + lst[i][j]

                if distance[i][j] > cost :
                    distance[i][j] = cost
                    heappush(heap,(distance[i][j],i,j))



M,N = map(int,input().split())
lst = [list(map(int,input())) for _ in range(N)]

print(dijkstra())
