# 알파벳
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(x,y,cnt) :
    global maxV

    maxV = max(maxV,cnt)
    for a in range(4) :
        nx = x + dx[a]
        ny = y + dy[a]
        if not(0<=nx<N and 0<=ny<M) or lst[nx][ny] in ret : continue
        ret.add(lst[nx][ny])
        dfs(nx,ny,cnt + 1)
        ret.remove(lst[nx][ny])


N,M = map(int,input().split())

lst = [list(input()) for _ in range(N)]
ret = set()
ret.add(lst[0][0])

maxV = -21e8
dfs(0,0,1)
print(maxV)

