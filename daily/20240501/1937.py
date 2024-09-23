import sys
sys.setrecursionlimit(10**6)

dx = [0,1,0,-1]
dy = [1,0,-1,0]


def dfs(x,y) :




    for a in range(4) :
        nx,ny = x + dx[a], y + dy[a]
        


N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
check = [[0]*N for _ in range(N)]

for i in range(N) :
    for j in range(N) :
        dfs(i,j)