dx = [0,1,0,-1]
dy = [1,0,-1,0]
def check(x,y) :
    lst[x][y] = 0
    cnt = 1
    st = []
    st.append((x,y))
    while st :
        x,y = st.pop()
        for a in range(4) :
            nx = x + dx[a]
            ny = y + dy[a]
            if 0<=nx<N and 0<=ny< N and lst[nx][ny] == 1 :
                cnt += 1
                st.append((nx,ny))
                lst[nx][ny] = 0
    return cnt

N = int(input())
lst = [list(map(int,input())) for _ in range(N)]
ret = []
for x in range(N) :
    for y in range(N) :
        if lst[x][y] == 1 :
            ret.append(check(x,y))

print(len(ret))
ret.sort()
for i in ret :
    print(i)