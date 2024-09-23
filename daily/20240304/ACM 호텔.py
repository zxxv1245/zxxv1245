T = int(input())

for Test in range(1,T+1) :
    N,M,K = map(int,input().split())

    lst = [[0]*M for _ in range(N)]
    v = 1
    for i in range(M) :
        for j in range(N) :
            lst[j][i] = v
            v += 1

            if lst[j][i] == K :
                if i < 9 :
                    print(f'{j+1}0{i+1}')
                else :
                    print(f'{j + 1}{i + 1}')