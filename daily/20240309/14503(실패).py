dx = [-1,0,1,0]
dy = [0,1,0,-1]
def dfs(x,y,d) :
    global cnt
    visited = [[0]*M for _ in range(N)]
    st = []
    st.append((x,y))
    visited[x][y] = 1
    cnt += 1
    d -= 1
    if d < 0:
        d = 3
    while True :
        x,y = st.pop()
        if lst[x][y] == 0 and visited[x][y] == 0 :
            visited[x][y] = 1
            d -= 1
            if d < 0:
                d = 3
        for _ in range(4) :
            nx = x + dx[d]
            ny = y + dy[d]
            if lst[nx][ny] == 0 and visited[nx][ny] == 0 :
                st.append((nx,ny))
                cnt += 1
                visited[nx][ny] = 1
                d -= 1
                if d < 0:
                    d = 3
                break
            else :
                d -= 1
                if d < 0:
                    d = 3


        if not st :
            d -= 1
            if d < 0:
                d = 3
            nx = x-dx[d]
            ny = y-dy[d]
            if lst[nx][ny] == 1 :
                break
            elif lst[nx][ny] == 0 :
                st.append((nx,ny))

N,M = map(int,input().split())

x,y,d = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(N)]

cnt = 0

dfs(x,y,d)

print(cnt)