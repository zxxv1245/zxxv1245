N,M,B = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
while True :
    for i in range(N) :
        for j in range(M-1) :
            if lst[i][j] == lst[i][j+1] :
                continue
            else :
                if lst[i][j] > lst[i][j+1] and B >= (lst[i][j]-lst[i][j+1]) :
                    cnt += (lst[i][j]-lst[i][j+1])
                    B -= (lst[i][j]-lst[i][j+1])
                    lst[i][j+1] += (lst[i][j]-lst[i][j+1])
                elif lst[i][j] > lst[i][j+1] and B == 0 :
                    cnt += (lst[i][j]-lst[i][j+1])* 2
                    B += (lst[i][j]-lst[i][j+1])
                    lst[i][j] -= (lst[i][j]-lst[i][j+1])

                elif lst[i][j]<lst[i][j+1] and B >= (lst[i][j+1]-lst[i][j]) :
                    cnt += (lst[i][j+1]-lst[i][j])
                    B -= (lst[i][j+1]-lst[i][j])
                    lst[i][j+1] -= (lst[i][j+1] - lst[i][j])

                elif lst[i][j]<lst[i][j+1] and B == 0 :
                    cnt += (lst[i][j+1] - lst[i][j])*2
                    B += (lst[i][j+1] - lst[i][j])
                    lst[i][j + 1] -= (lst[i][j + 1] - lst[i][j])
    ans = 0
    for x in range(N) :
        for y in range(M-1) :
            if lst[x][y] != lst[x][y+1] :
                ans += 1
    if ans == 0 :
        break

print(cnt ,lst[x][y])