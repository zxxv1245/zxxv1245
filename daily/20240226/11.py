def fir(lst) :   # 첫 번째 작업
    global i
    global j
    global N
    for a in range(i, i+j) :
        if a <= N :  # a가 lst 의 안에 있는 인덱스 일 때....
            if lst[a] == 1 :  # 1일때 0으로 ...
                lst[a] = 0
            elif lst[a] == 0 :
                lst[a] = 1

def seco(lst) :   # 두 번째 작업
    global i
    global j
    global N
    for a in range(i+1,i+j) :
        if a <= N and lst[i] != lst[a] :      # i번째 돌과 색깔이 다를 때....
            lst[a] = lst[i]    # a번째 돌을 i번째 돌의 색깔로 바꿈

def thi(lst) :   # 세 번째 작업
    global i
    global j
    global N

    for a in range(1,j+1) :
        if 1<= i-a and lst[i+a] <= N :
            if lst[i-a] == lst[i+a] :   # i의 양 옆을 시작으로 1씩 넓혀 나감
                if lst[i-a] == 1 :
                    lst[i-a] = 0      # 대칭인 돌이 색이 같으면 뒤집기
                    lst[i+a] = 0
                elif lst[i-a] == 0 :
                    lst[i-a] = 1
                    lst[i+a] = 1

T = int(input())

for Test in range(1,T+1) :
    N, M = map(int,input().split()) # N개 줄 M번 작업 진행
    lst = [-1]+list(map(int,input().split()))  # 돌 초기 상태  # 0 흰돌 1 검은돌

    for _ in range(M) :
        i,j,w = map(int,input().split())  # i번째, j개, w번 작업 시행

        if w == 1 :
            fir(lst)
        elif w == 2 :
            seco(lst)
        elif w == 3 :
            thi(lst)

    print(f'#{Test}', *lst[1:])  # 처음에 -1을 더했으므로 lst의 1번부터 언패킹...

