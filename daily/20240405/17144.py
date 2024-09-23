N,M,T = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(N)]
air = []  #air[0] 이 위(반시계) air[1] 이 아래(시계)
top_dx = [0,-1,0,1]
top_dy = [1,0,-1,0]
bottom_dx = [0,1,0,-1]
bottom_dy = [1,0,-1,0]
for c in range(N) :
    if lst[c][0] == -1 :
        air.append((c,0))

t = 0
while True :
    if t == T :
        break
    # 1.미세먼지 확산
    arr = [[0]*M for _ in range(N)]
    arr[air[0][0]][air[0][1]] = -1
    arr[air[1][0]][air[1][1]] = -1
    for i in range(N) :
        for j in range(M) :
            if lst[i][j] >= 1:
                five = lst[i][j]//5
                cnt = 0
                for p in range(4) :
                    ni,nj = i+top_dx[p],j+top_dy[p]
                    if 0<=ni<N and 0<=nj<M and lst[ni][nj] != -1:
                        arr[ni][nj] += five
                        cnt += 1
                arr[i][j] += lst[i][j] - (five*cnt)
    lst = arr
    # for tt in arr:
    #     print(*tt)
    # print()
    # for g in lst:
    #     print(*g)
    # print()
    # 2. 공기청정기 돌리기
    for z in range(2) :
        sx,sy = air[z][0],air[z][1]
        # print(sx,sy)
        if z == 0 :
            a = 0
            prev = 0
            nx, ny = sx + top_dx[a], sy + top_dy[a]
            while lst[nx][ny] != -1 :
                jj = lst[nx][ny]
                lst[nx][ny] = prev
                prev = jj
                sx,sy = nx,ny
                nx, ny = sx + top_dx[a], sy + top_dy[a]
                if nx<0 or nx>=N or ny<0 or ny>=M :
                    a += 1
                    if a == 4 :
                        a = 0
                    nx, ny = sx + top_dx[a], sy + top_dy[a]
            # for g in lst:
            #     print(*g)
            # print()
        else :
            a = 0
            prev = 0
            nx, ny = sx + bottom_dx[a], sy + bottom_dy[a]
            while lst[nx][ny] != -1:
                jj = lst[nx][ny]
                lst[nx][ny] = prev
                prev = jj
                sx,sy = nx,ny
                nx, ny = sx + bottom_dx[a], sy + bottom_dy[a]
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    a += 1
                    if a == 4 :
                        a = 0
                    nx, ny = sx + bottom_dx[a], sy + bottom_dy[a]
    t += 1
# for g in lst :
#     print(*g)
ret = 0
for q in range(N) :
    for w in range(M) :
        if lst[q][w] > 0 :
            ret += lst[q][w]

print(ret)
