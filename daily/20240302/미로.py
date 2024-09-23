def dfs(x, y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    st = []
    st.append((x, y))
    while st:
        x, y = st.pop()
        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]
            if 0 <= nx < N and 0 <= ny < N and lst[nx][ny] == '0':
                st.append((nx, ny))
                lst[nx][ny] = '1'
            elif 0 <= nx < N and 0 <= ny < N and lst[nx][ny] == '3':
                return 1
    return 0


T = int(input())

for Test in range(1, T + 1):
    N = int(input())
    lst = [list(input()) for _ in range(N)]

    for x in range(N):
        for y in range(N):
            if lst[x][y] == '2':
                stx = x
                sty = y
    print(f'#{Test} {dfs(stx, sty)}')