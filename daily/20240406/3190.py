from collections import deque
# 입력
N = int(input())
lst = [[0]*N for _ in range(N)]

K = int(input())
for _ in range(K) :
    r,c =map(int,input().split())
    lst[r-1][c-1] = 1

L = int(input())
move = []
for _ in range(L) :
    X,C = input().split()
    move.append((int(X),C))

# 변수 설정
snake = deque()
snake.append((0,0))
snakex,snakey = 0,0
lst[snakex][snakey] = 'S'
dx = [0,1,0,-1]
dy = [1,0,-1,0]
ret = 0
flag = 1
a = 0

# 조건
# 1. 뱀은 몸길이를 늘려 머리를 다음칸에 위치 시킨다.
# 2. 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
# 3. 이동한 칸에 사과가 있다면, 사과는 없어지고 꼬리는 움직이지 않는다.
# 4. 이동한 칸에 사과가 없다면, 몸길이를 줄여 꼬리가 위치한 칸을 비워준다.(즉, 몸길이는 변하지 않는다.)

# 뱀은 입력 받은 방향 변환 정보에 따라 움직인다.
for cnt,turn in move :
    for _ in range(ret,cnt) :
        # 이동할 칸
        nx,ny = snakex+dx[a],snakey+dy[a]
        ret += 1
        # 기저조건
        if nx < 0 or nx >= N or ny < 0 or ny >= N or lst[nx][ny] == 'S' :
            flag = 0
            break
        # 이동한 칸에 사과가 있으면
        if lst[nx][ny] == 1 :
            lst[nx][ny] = 'S'
            snake.append((nx,ny))
            snakex,snakey = nx,ny

        # 이동한 칸에 사과가 없으면
        else :
            lst[nx][ny] = 'S'
            snake.append((nx,ny))
            snakex, snakey = nx, ny
            deletex,deletey = snake.popleft()
            lst[deletex][deletey] = 0
    # 기저 조건
    if flag == 0 :
        print(ret)
        exit()
    # 방향 전환
    if turn == 'D' :
        a += 1
    else :
        a -= 1
    if a == 4 :
        a = 0
    if a == -1 :
        a = 3

# if turn == 'D' :
#     a += 1
# else :
#     a -= 1
# if a == 4 :
#     a == 0
# if a == -1 :
#     a == 3

nx, ny = snakex + dx[a], snakey + dy[a]
while 0<=nx<N and 0<=ny<N and lst[nx][ny] != 'S':
    ret += 1
    # 이동한 칸에 사과가 있으면
    if lst[nx][ny] == 1:
        lst[nx][ny] = 'S'
        snake.append((nx, ny))
        snakex, snakey = nx, ny
    # 이동한 칸에 사과가 없으면
    else:
        lst[nx][ny] = 'S'
        snake.append((nx, ny))
        snakex, snakey = nx, ny
        deletex, deletey = snake.popleft()
        lst[deletex][deletey] = 0
    nx, ny = snakex + dx[a], snakey + dy[a]

# 출력
print(ret+1)