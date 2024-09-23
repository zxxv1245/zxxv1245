def abc(k,midV) :
    global cnt
    if k == N :
        cnt += 1
        return


    for i in range(N) :
        if visited[i] == 1: continue
        visited[i] = 1
        abc(k+1,midV*(lst[k][i]))
        visited[i] = 0


T = int(input())

for Test in range(1,T+1) :
    N = int(input())
    lst = [list(map(lambda x : x*0.01,map(int,input().split()))) for _ in range(N)]
    visited = [0]*N
    maxV = 0
    cnt = 0
    abc(0,100)
    print(f'#{Test} {maxV:.6f}')