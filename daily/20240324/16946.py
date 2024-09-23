from collections import deque

def zero_bfs(i,j) :
    global group_key
    zero_Q = deque()
    zero_Q.append((i,j))
    cnt = 1
    while zero_Q :
        x,y = zero_Q.popleft()
        zero_group[x][y] = group_key
        for r,c in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)] :
            if 0<= r < N and 0<= c < M :
                if lst[r][c] == 0 and visited[r][c] == 0 :
                    visited[r][c] = 1
                    zero_Q.append((r,c))
                    cnt += 1

    group[group_key] = cnt
    group_key += 1

N,M = map(int,input().split())
lst = [list(map(int,input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
zero_group = [[0]*M for _ in range(N)]
group = {}
group[0]= 0
group_key = 1
for i in range(N) :
    for j in range(M) :
        if lst[i][j] == 0 and visited[i][j] == 0:
            visited[i][j] = 1
            zero_bfs(i,j)

for i in range(N) :
    for j in range(M) :
        if lst[i][j] == 1 :
            check = set()
            for r, c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= r < N and 0 <= c < M :
                    if lst[r][c] == 0 or lst[r][c] == '0':
                        check.add(zero_group[r][c])
            for x in check :
                lst[i][j] += group[x]
        lst[i][j] = str(lst[i][j]%10)


for k in lst :
    print(''.join(k))