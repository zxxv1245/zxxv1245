import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(k,ret) :
    global maxV
    if k == 3 :
        if maxV < ret :
            maxV = ret
        return

    for x,y in arr:
        for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=nx<N and 0<=ny<M and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                arr.append((nx,ny))
                dfs(k+1,ret+lst[nx][ny])
                arr.pop()
                visited[nx][ny] = 0
N,M = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
maxV = -21e8
for i in range(N) :
    for j in range(M) :
        visited[i][j] = 1
        arr = [(i,j)]
        dfs(0,lst[i][j])

print(maxV)