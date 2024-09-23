from heapq import heappop,heappush

def dijkstra() :

    distance = [[21e8]*N for _ in range(N)]
    distance[0][0] = 0
    heap = [(0,0,0)]

    while heap :
        cost,x,y = heappop(heap)
        if x == N-1 and y == N-1 :
            return cost
        if cost > distance[x][y] : return
        for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)] :
            if 0<=i<N and 0<=j<N :
                if lst[i][j] == 0 :
                    cost = distance[x][y] + 1
                else :
                    cost = distance[x][y]
                if distance[i][j] > cost :
                    distance[i][j] = cost
                    heappush(heap,(distance[i][j],i,j))





N = int(input())
lst = [list(map(int,input())) for _ in range(N)]


print(dijkstra())