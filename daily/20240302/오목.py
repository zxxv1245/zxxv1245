def check(x,y) :

    for a in range(4):
        cnt = 0
        for b in range(19):
            nx = x + dx[a] * b
            ny = y + dy[a] * b
            if 0 <= nx < 19 and 0 <= ny < 19 and lst[nx][ny] == lst[x][y]:
                cnt += 1
                if cnt == 5 :
                    nx = nx + dx[a]
                    ny = ny + dy[a]
                    mx = x - dx[a]
                    my = y - dy[a]
                    if 0 <= nx < 19 and 0 <= ny < 19 and lst[nx][ny] != lst[x][y] :
                        if 0 <= mx < 19 and 0 <= my < 19 and lst[mx][my] != lst[x][y] :
                            return lst[x][y]
                        elif mx < 0 or  my < 0 :
                            if lst[nx][ny] != lst[x][y] :
                                return lst[x][y]
                    elif nx >= 19 or ny >= 19 :
                        if lst[mx][my] != lst[x][y] :
                            return lst[x][y]
                    elif nx >= 19 or ny >= 19 or nx < 0 or ny < 0 :
                        if lst[mx][my] != lst[x][y] :
                            return lst[x][y]
                    elif mx < 0 or my < 0 or mx >= 19 or my >= 19 :
                        if lst[nx][ny] != lst[x][y] :
                            return lst[x][y]
            elif 0 <= nx < 19 and 0 <= ny < 19 and lst[nx][ny] != lst[x][y] :
                cnt = 0
                break
            elif nx >= 19 or ny >= 19 or nx <0 or ny < 0 :
                break
    return 0

lst = [list(map(int,input().split())) for _ in range(19)]

dx = [-1,0,1,1]
dy = [1,1,1,0]
dool = 0
for x in range(19) :
    for y in range(19) :
        if x== 0 and y==0 :
            a = x
        if lst[x][y] != 0 :
            dool = check(x,y)
            if dool != 0 :
                break
    if dool != 0 :
        break

print(dool)
if dool != 0 :
    print(x+1,y+1)
