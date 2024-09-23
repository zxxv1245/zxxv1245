T = int(input())
for Test in range(1,T+1) :
    N,L = map(int,input().split())

    def check(x,y) :
        check_preV = lst[x][y]
        check_cnt = 0
        for k in range(y,N) :
            if check_cnt == L :
                return True
            if check_preV == lst[i][k] :
                check_cnt += 1
            else :
                return False
        if check_cnt == L:
            return True

    lst = [list(map(int,input().split())) for _ in range(N)]
    # lst_rev = list(map(list,zip(*lst)))
    ret = 0
    for _ in range(2) :
        for i in range(N) :
            prev = lst[i][0]
            cnt = 1
            tot = 1
            for j in range(1,N) :

                if prev == lst[i][j] :
                    cnt += 1
                    tot += 1
                elif prev < lst[i][j] and lst[i][j]-prev == 1 :
                    if cnt < L :
                        break
                    elif cnt >= L :
                        prev = lst[i][j]
                        cnt = 1
                        tot += 1
                elif prev > lst[i][j] and prev-lst[i][j] == 1 :
                    if check(i,j) :
                        cnt = -L+1
                        tot += 1
                    else :
                        break
                    prev = lst[i][j]
                else :
                    break
            if tot == N :
                ret+=1
        lst = list(map(list, zip(*lst)))

    print(f'#{Test} {ret}')