dx = [0,1,0,-1]
dy = [1,0,-1,0]
def dfs() :
    cc = 1
    while st :
        x,y = st.pop()
        for a in range(4) :
            nx = x + dx[a]
            ny = y + dy[a]
            if 0<= nx < M and 0<= ny < N and lst[nx][ny] == 0 :
                cc += 1
                lst[nx][ny] = 1
                st.append((nx,ny))
    return cc



N,M,K = map(int,input().split())

lst = [[0]*(N) for _ in range(M)]

for _ in range(K) :
    x1,y1,x2,y2  = map(int,input().split())

    for i in range(x1,x2) :
        for j in range(y1,y2) :
            lst[i][j] = 1

st = []
ans = []
cnt = 0
for x in range(M) :
    for y in range(N) :
        if lst[x][y] == 0 :
            lst[x][y] = 1
            st.append((x,y))
            cnt += 1
            ans.append(dfs())

print(cnt)
ans.sort()
print(*ans)