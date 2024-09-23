
T = 10
for a in range(1,T+1) :
    N = int(input())
    H = list(map(int,input().split()))

    second_count = 0

    for b in range(2,998) :
        if H[b] == max(H[b-2:b+3]):
            vv =0

            for c in H[b-2:b+3] :
                if H[b] == H[c] :
                    continue
                elif H[c] > vv :
                    vv = H[c]
    ret = H[b] - vv
    print(f'#{a} {ret}')

