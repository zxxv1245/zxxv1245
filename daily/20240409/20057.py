N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]

# step1 배열 돌기
# 1. 배열의 중앙 찾기
x,y = N//2,N//2

# 2. 배열 돌기
# 어캐 돌지? 일단 좌(0,-1) 하(1,0) 우(0,1) 상(-1,0) 순서
# 2 2 3 3 4 4 5 5 6 6 7 7 ?
dx = [0,1,0,-1]
dy = [-1,0,1,0]
# 가로
rx = [-1,1,-1,1,-2,2,-1,1,0]
ry = [-1,-1,0,0,0,0,1,1,-2]
# 세로
cx = [1,1,0,0,0,0,-1,-1,2]
cy = [-1,1,-1,1,-2,2,-1,1,0]
v = [10,10,7,7,2,2,1,1,5]
i = 2 # 해당 방향으로 진행할 횟수
cnt = 1 # 해당 방향으로 진행한 횟수
d = 0 # 이게 2가 되면 i += 1
a = 0 # 방향 배열 index
result = 0 # 결과값 변수

while True :
    nx,ny = x+dx[a],y+dy[a]


    # step2 배열 값 처리
    # 1. 진행 방향에 따라 값을 처리 할 위치가 달라져야한다.
    # 이것도 방향배열 만들어야할듯? 좌하우상 배열 4개 만들어야하나? ...
    # 좌 하 일땐 + 우 상 일땐 -
    value = lst[nx][ny]
    tvalue = value
    lst[nx][ny] = 0
    if a == 0 :
        for b in range(9) :
            ax,ay = nx+rx[b],ny+ry[b]
            if 0<=ax<N and 0<=ay<N :
                lst[ax][ay] += int(tvalue*(v[b]*0.01))
                value -= int(tvalue*(v[b]*0.01))
            else :
                result += int(tvalue*(v[b]*0.01))
                value -= int(tvalue*(v[b]*0.01))
        ax,ay = nx,ny-1
        if 0 <= ax < N and 0 <= ay < N:
            lst[ax][ay] += value
        else :
            result += value

    elif a == 1 :
        for b in range(9) :
            ax,ay = nx+cx[b],ny+cy[b]
            if 0<=ax<N and 0<=ay<N :
                lst[ax][ay] += int(tvalue*(v[b]*0.01))
                value -= int(tvalue*(v[b]*0.01))
            else :
                result += int(tvalue*(v[b]*0.01))
                value -= int(tvalue*(v[b]*0.01))
        ax,ay = nx+1,ny
        if 0 <= ax < N and 0 <= ay < N:
            lst[ax][ay] += value
        else :
            result += value
    elif a == 2 :
        for b in range(9) :
            ax,ay = nx-rx[b],ny-ry[b]
            if 0<=ax<N and 0<=ay<N :
                lst[ax][ay] += int(tvalue*(v[b]*0.01))
                value -= int(tvalue*(v[b]*0.01))
            else :
                result += int(tvalue*(v[b]*0.01))
                value -= int(tvalue*(v[b]*0.01))
        ax,ay = nx,ny+1
        if 0 <= ax < N and 0 <= ay < N:
            lst[ax][ay] += value
        else :
            result += value

    elif a == 3 :
        for b in range(9) :
            ax,ay = nx-cx[b],ny-cy[b]
            if 0<=ax<N and 0<=ay<N :
                lst[ax][ay] += int(tvalue*(v[b]*0.01))
                value -= int(tvalue*(v[b]*0.01))
            else :
                result += int(tvalue*(v[b]*0.01))
                value -= int(tvalue*(v[b]*0.01))
        ax,ay = nx-1,ny
        if 0 <= ax < N and 0 <= ay < N:
            lst[ax][ay] += value
        else :
            result += value


    x,y = nx,ny
    if x == 0 and y == 0 :
        break
    cnt += 1
    if cnt == i:
        d += 1
        a += 1
        cnt = 1
        if a == 4:
            a = 0
    if d == 2:
        i += 1
        d = 0


print(result)

