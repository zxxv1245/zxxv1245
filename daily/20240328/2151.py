from heapq import heappush,heappop
import sys
INF = sys.maxsize
def dijkstra(i,j) :
    distance = [[INF]*N for _ in range(N)]
    distance[i][j] = 0
    heap = [(0,i,j)]

    while heap :
        cost,x,y = heappop(heap)

        if cost > distance[x][y] : continue

        for a in range(4):
            b = 1
            while True :
                nr = x+dx[a]*b
                nc = y+dy[a]*b
                if nr == ex and nc == ey:
                    return distance[x][y]
                if 0 <= nr < N and 0 <= nc < N and lst[nr][nc] != '*':
                    if lst[nr][nc] == '!' :
                        new_cost = cost + 1
                        if distance[nr][nc] > new_cost :
                            distance[nr][nc] = new_cost
                            heappush(heap,(new_cost,nr,nc))
                    else :
                        b += 1
                        continue
                else :
                    break
                b+=1

N = int(input())
lst = [list(input()) for _ in range(N)]
ans = []
for i in range(N) :
    for j in range(N) :
        if lst[i][j] == '#' :
            ans.append((i,j))

dx = [1,0,-1,0]
dy = [0,1,0,-1]
sx,sy = ans[0][0],ans[0][1]
ex,ey = ans[1][0],ans[1][1]

print(dijkstra(sx,sy))