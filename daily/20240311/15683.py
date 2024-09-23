def abc(k) :
    global minV
    global cnt
    if k == len(path) :
        if minV > (N*M - cnt - len(ret)) :
            minV = (N*M - cnt - len(ret))
        return

    for a in range(len(arr[lst[path[k][0]][path[k][1]]])) :
        for b in range(1,9) :
            nx = path[k][0] + arr[lst[path[k][0]][path[k][1]]][a][0]*b
            ny = path[k][1] + arr[lst[path[k][0]][path[k][1]]][a][1]*b
            if 0<=nx<N and 0<=ny<M and visited[nx][ny] == 0 and (nx,ny) not in ret :

                ret.append((nx,ny))
            else :
                break
        abc(k+1)


N,M = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(N)]

arr = [0,[[0,1]],[[[0,1],[0,-1]]],[[[0,1],[-1,0]]],[[[0,1],[0,-1],[-1,0]]],[[[0,1],[0,-1],[-1,0],[1,0]]],1]

visited = [[0]*M for _ in range(N)]
path = []
ret = []
minV = 21e8
cnt = 0
for i in range(N) :
    for j in range(M) :
        if lst[i][j] != 0 :
            cnt += 1
            visited[i][j] = 1
            if lst[i][j] != 6 :
                path.append((i,j))

abc(0)
print(minV)