# 주사위 index
#    2
#  4 1 3
#    5
#    6

# 시작할 때 주사위의 모든 면은 0
# 시작할 때 주사위의 윗면 index는  1 동쪽 index는 3
# 주사위를 배열안에서 굴릴 때마다 밑면은 index에 배열값을 복사한다.(가장 윗면 출력)
# 배열을 벗어나면 pass
#
N,M,x,y,K = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(N)]
dice = [0]*6 # start index 0이 윗면 index 5 가 밑면
# 서쪽 index 3 동쪽 index 2 북쪽 index 1 남쪽 index 4
arr = list(map(int,input().split()))
NS = [0,1,5] # 북 남 4랑 스위칭
EW = [5,3,0] # 동 서 2랑 스위칭

dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]
for a in arr :
    nx,ny = x+dx[a],y+dy[a]
    if nx < 0 or nx >= N or ny < 0 or ny >= M : continue
    if a == 1 :
        for i in EW :
            dice[i],dice[2] = dice[2],dice[i]
    elif a == 2 :
        for i in reversed(EW) :
            dice[i],dice[2] = dice[2],dice[i]
    elif a == 3 :
        for i in NS :
            dice[i],dice[4] = dice[4],dice[i]
    elif a == 4 :
        for i in reversed(NS) :
            dice[i],dice[4] = dice[4],dice[i]
    if lst[nx][ny] == 0 :
        lst[nx][ny] = dice[5]  # 배열의 값이 0 이면 배열에 다이스 값 복사
    else :
        dice[5] = lst[nx][ny] # 배열에 값이 있다면 다이스에 배열 값을 복사 후
        lst[nx][ny] = 0     # 배열은 0
    x, y = nx, ny
    print(dice[0])
