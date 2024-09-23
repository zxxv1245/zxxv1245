def check() :
    visited = [[0]*M for _ in range(N)]
    cnt = 0
    for i in range(len(cctvlst)) :
        cctv = cctvlst[i]
        x,y = cctvxy[i]
        w = path[i]
        if cctv == 1 :
            nx,ny = x+dx[w],y+dy[w]
            while True :
                if 0<=nx<N and 0<=ny<M :
                    if lst[nx][ny] == 0 and visited[nx][ny] == 0 :
                        visited[nx][ny] = 1
                        cnt += 1
                        nx,ny = nx+dx[w],ny+dy[w]
                    elif visited[nx][ny] == 1:
                        nx, ny = nx + dx[w], ny + dy[w]
                    elif lst[nx][ny] in [1, 2, 3, 4, 5]:
                        nx, ny = nx + dx[w], ny + dy[w]
                    else :
                        break
                else :
                    break
        elif cctv == 2 :
            if w in [0,2] :
                for a in [0,2] :
                    nx, ny = x + dx[a], y + dy[a]
                    while True:
                        if 0 <= nx < N and 0 <= ny < M:
                            if lst[nx][ny] == 0 and visited[nx][ny] == 0:
                                visited[nx][ny] = 1
                                cnt += 1
                                nx, ny = nx + dx[a], ny + dy[a]
                            elif visited[nx][ny] == 1:
                                nx, ny = nx + dx[a], ny + dy[a]
                            elif lst[nx][ny] in [1, 2, 3, 4, 5]:
                                nx, ny = nx + dx[a], ny + dy[a]
                            else:
                                break
                        else :
                            break
            else :
                for a in [1,3] :
                    nx, ny = x + dx[a], y + dy[a]
                    while True:
                        if 0 <= nx < N and 0 <= ny < M:
                            if lst[nx][ny] == 0 and visited[nx][ny] == 0:
                                visited[nx][ny] = 1
                                cnt += 1
                                nx, ny = nx + dx[a], ny + dy[a]
                            elif visited[nx][ny] == 1:
                                nx, ny = nx + dx[a], ny + dy[a]
                            elif lst[nx][ny] in [1, 2, 3, 4, 5]:
                                nx, ny = nx + dx[a], ny + dy[a]
                            else:
                                break
                        else:
                            break
        elif cctv == 3 :
            if w == 0 :
                for a in [0,1] :
                    nx, ny = x + dx[a], y + dy[a]
                    while True:
                        if 0 <= nx < N and 0 <= ny < M:
                            if lst[nx][ny] == 0 and visited[nx][ny] == 0:
                                visited[nx][ny] = 1
                                cnt += 1
                                nx, ny = nx + dx[a], ny + dy[a]
                            elif visited[nx][ny] == 1:
                                nx, ny = nx + dx[a], ny + dy[a]
                            elif lst[nx][ny] in [1, 2, 3, 4, 5]:
                                nx, ny = nx + dx[a], ny + dy[a]
                            else:
                                break
                        else:
                            break
            elif w == 1 :
                for a in [1,2] :
                    nx, ny = x + dx[a], y + dy[a]
                    while True:
                        if 0 <= nx < N and 0 <= ny < M:
                            if lst[nx][ny] == 0 and visited[nx][ny] == 0:
                                visited[nx][ny] = 1
                                cnt += 1
                                nx, ny = nx + dx[a], ny + dy[a]
                            elif visited[nx][ny] == 1:
                                nx, ny = nx + dx[a], ny + dy[a]
                            elif lst[nx][ny] in [1, 2, 3, 4, 5]:
                                nx, ny = nx + dx[a], ny + dy[a]
                            else:
                                break
                        else:
                            break
            elif w == 2 :
                for a in [2,3] :
                    nx, ny = x + dx[a], y + dy[a]
                    while True:
                        if 0 <= nx < N and 0 <= ny < M:
                            if lst[nx][ny] == 0 and visited[nx][ny] == 0:
                                visited[nx][ny] = 1
                                cnt += 1
                                nx, ny = nx + dx[a], ny + dy[a]
                            elif visited[nx][ny] == 1:
                                nx, ny = nx + dx[a], ny + dy[a]
                            elif lst[nx][ny] in [1, 2, 3, 4, 5]:
                                nx, ny = nx + dx[a], ny + dy[a]
                            else:
                                break
                        else:
                            break
            elif w == 3 :
                for a in [0,3] :
                    nx, ny = x + dx[a], y + dy[a]
                    while True:
                        if 0 <= nx < N and 0 <= ny < M:
                            if lst[nx][ny] == 0 and visited[nx][ny] == 0:
                                visited[nx][ny] = 1
                                cnt += 1
                                nx, ny = nx + dx[a], ny + dy[a]
                            elif visited[nx][ny] == 1:
                                nx, ny = nx + dx[a], ny + dy[a]
                            elif lst[nx][ny] in [1, 2, 3, 4, 5]:
                                nx, ny = nx + dx[a], ny + dy[a]
                            else:
                                break
                        else:
                            break
        elif cctv == 4 :
            if w == 0 :
                for a in [0,1,3] :
                    nx, ny = x + dx[a], y + dy[a]
                    while True:
                        if 0 <= nx < N and 0 <= ny < M:
                            if lst[nx][ny] == 0 and visited[nx][ny] == 0:
                                visited[nx][ny] = 1
                                cnt += 1
                                nx, ny = nx + dx[a], ny + dy[a]
                            elif visited[nx][ny] == 1:
                                nx, ny = nx + dx[a], ny + dy[a]
                            elif lst[nx][ny] in [1, 2, 3, 4, 5]:
                                nx, ny = nx + dx[a], ny + dy[a]
                            else:
                                break
                        else:
                            break
            elif w == 1 :
                for a in [0,1,2] :
                    nx, ny = x + dx[a], y + dy[a]
                    while True:
                        if 0 <= nx < N and 0 <= ny < M:
                            if lst[nx][ny] == 0 and visited[nx][ny] == 0:
                                visited[nx][ny] = 1
                                cnt += 1
                                nx, ny = nx + dx[a], ny + dy[a]
                            elif visited[nx][ny] == 1:
                                nx, ny = nx + dx[a], ny + dy[a]
                            elif lst[nx][ny] in [1, 2, 3, 4, 5]:
                                nx, ny = nx + dx[a], ny + dy[a]
                            else:
                                break
                        else:
                            break
            elif w == 2 :
                for a in [1,2,3] :
                    nx, ny = x + dx[a], y + dy[a]
                    while True:
                        if 0 <= nx < N and 0 <= ny < M:
                            if lst[nx][ny] == 0 and visited[nx][ny] == 0:
                                visited[nx][ny] = 1
                                cnt += 1
                                nx, ny = nx + dx[a], ny + dy[a]
                            elif visited[nx][ny] == 1:
                                nx, ny = nx + dx[a], ny + dy[a]
                            elif lst[nx][ny] in [1, 2, 3, 4, 5]:
                                nx, ny = nx + dx[a], ny + dy[a]
                            else:
                                break
                        else:
                            break
            elif w == 3 :
                for a in [0,2,3] :
                    nx, ny = x + dx[a], y + dy[a]
                    while True:
                        if 0 <= nx < N and 0 <= ny < M:
                            if lst[nx][ny] == 0 and visited[nx][ny] == 0:
                                visited[nx][ny] = 1
                                cnt += 1
                                nx, ny = nx + dx[a], ny + dy[a]
                            elif visited[nx][ny] == 1:
                                nx, ny = nx + dx[a], ny + dy[a]
                            elif lst[nx][ny] in [1, 2, 3, 4, 5]:
                                nx, ny = nx + dx[a], ny + dy[a]
                            else:
                                break
                        else:
                            break
        elif cctv == 5 :
            for a in range(4):
                nx, ny = x + dx[a], y + dy[a]
                while True:
                    if 0 <= nx < N and 0 <= ny < M:
                        if lst[nx][ny] == 0 and visited[nx][ny] == 0:
                            visited[nx][ny] = 1
                            cnt += 1
                            nx, ny = nx + dx[a], ny + dy[a]
                        elif visited[nx][ny] == 1:
                            nx, ny = nx + dx[a], ny + dy[a]
                        elif lst[nx][ny] in [1, 2, 3, 4, 5]:
                            nx, ny = nx + dx[a], ny + dy[a]
                        else:
                            break
                    else:
                        break
    return cnt
def abc(k) :
    global minV

    if k == len(cctvlst) :
        ret = N*M - check() - len(cctvlst) - six
        if minV > ret :
            minV = ret
        return

    for a in range(4) :
        path[k] = a
        abc(k+1)

N,M = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
cctvlst = []
cctvxy = []
six = 0
for i in range(N) :
    for j in range(M) :
        if lst[i][j] in list(range(1,6)) :
            cctvlst.append(lst[i][j])
            cctvxy.append((i,j))
        elif lst[i][j] == 6 :
            six += 1
path = [0]*(len(cctvlst))
minV = 21e8
abc(0)
print(minV)
