def abc(k) :
    global cnt

    if k == N :
        cnt += 1
        return

    for i in range(N) :
        if V1[i] == 1 or V2[k+i] == 1 or V3[k-i] == 1 : continue
        V1[i]=V2[k+i]=V3[k-i] = 1
        abc(k+1)
        V1[i]=V2[k + i]=V3[k - i] = 0
N = int(input())
V1 = [0]*(N+1) # 행 ?
V2 = [0]*(2*N) # 우상향
V3 = [0]*(2*N) # 좌상향
cnt = 0

abc(0)
print(cnt)