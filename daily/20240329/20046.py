from heapq import heappush,heappop
import sys
INF = sys.maxsize
input = sys.stdin.readline

def dijkstra() :

    distance = [[INF]*M for _ in range(N)]
    distance[0][0] = lst[0][0]
    if distance[0][0] == -1 :
        return -1
    heap = [(lst[0][0],0,0)]

    while heap :
        cost,x,y = heappop(heap)
        if cost > distance[x][y] : continue
        for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)] :
            if 0 <= i < N and 0 <= j < M and lst[i][j] != -1 :
                new_cost = distance[x][y] + lst[i][j]
                if distance[i][j] > new_cost :
                    distance[i][j] = new_cost
                    heappush(heap,(new_cost,i,j))
    if distance[N-1][M-1] == INF :
        return -1
    else :
        return distance[N-1][M-1]


N,M = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(N)]

print(dijkstra())
