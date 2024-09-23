def step1() :
    tlst = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            while lst[i][j] :
                m,s,d = lst[i][j].pop(0)
                x, y = i, j
                for _ in range(s) :
                    nx,ny = x+dx[d],y+dy[d]
                    nx,ny = nx%N,ny%N
                    x,y = nx,ny
                tlst[x][y].append((m,s,d))
    return tlst

def step2() :
    tlst = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N) :
        for j in range(N) :
            if len(lst[i][j]) >= 2 :
                lenfire = len(lst[i][j])
                dcheck2 = 0 # 짝수 여기에 더하기
                dcheck1 = 0 # 홀수 여기에 더하기
                sumM = 0
                sumS = 0
                while lst[i][j] :
                    m, s, d = lst[i][j].pop(0)
                    sumM += m
                    sumS += s
                    if d % 2 == 0 :
                        dcheck2 += 1
                    elif d % 2 == 1 :
                        dcheck1 += 1
                fireM = sumM//5
                if fireM == 0 :
                    continue
                fireS = sumS//lenfire
                if dcheck1 == lenfire or dcheck2 == lenfire :
                    dlst = [0,2,4,6]
                else :
                    dlst = [1,3,5,7]
                for d in dlst :
                    tlst[i][j].append((fireM,fireS,d))


            else :
                while lst[i][j] :
                    m, s, d = lst[i][j].pop(0)
                    tlst[i][j].append((m,s,d))

    return tlst

N,M,K = map(int,input().split())
lst = [[[]for _ in range(N)] for _ in range(N)]
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

# 1. 모든 파이어볼은 자신의 방향 d로 속력 s칸 만큼 이동
#  - 이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
# 2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
  # 2-1. 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다 .
  # 2-2. 파이어볼은 4개의 파이어볼로 나누어진다.
  # 2-3. 나누어진 파이어볼의 질량,속력, 방향은 다음과 같다.
    # 3-1. 질량은 합쳐진 파이어볼 질량의 합/5
    # 3-2. 속력은 합쳐인 파이어볼 속력의 합/ 합쳐진 파이어볼의 개수
    # 3-3. 합쳐지는 파이어볼의 방향이 모두 홀수 이거나 짝수면 뱡항은 0,2,4,6 아니면 1,3,5,7
    # 3-4. 질량이 0인 파이어볼은 소멸된다.
# K번 명령 후 남아있는 파이어볼의 질량의 합 출력

# 파이어볼의 위치
for _ in range(M) :
    r,c,m,s,d = map(int,input().split()) # r 행 c 열 m 질량 s 속력 d 방향
    if m == 0 :
        continue
    lst[r-1][c-1].append((m,s,d))

# K번 명령 위의 순서에 따라 파이어볼이 움직임
# for i in lst :
#     print(*i)
for a in range(K) :
    # step1 파이어볼 이동 (1번,2번)
    lst = step1()
    # print(a+1,'step1')
    # for i in lst:
    #     print(*i)

    # step2 파이어볼 합치고 나누기(2-1 ~ 2-3, 3-1 ~ 3-3)
    lst = step2()
    # print(a+1,'step2')
    # for i in lst :
    #     print(*i)


result = 0
for i in range(N) :
    for j in range(N) :
        if lst[i][j] :
            for m,s,d in lst[i][j] :
                result += m

print(result)