N = int(input())

lst = [list(input())for _ in range(N)]

maxV = 0
for x in range(2) :
    for i in range(N) :
        for j in range(N) :
            if j < N-1 and lst[i][j] != lst[i][j+1] :
                lst[i][j],lst[i][j+1] = lst[i][j+1], lst[i][j]
                for a in range(N):
                    cnt = 1
                    for b in range(N) :
                        if b < N-1 and lst[a][b] == lst[a][b+1] :
                            cnt += 1
                            if maxV < cnt:
                                maxV = cnt
                        elif b < N - 1 and lst[b][a] != lst[b + 1][a]:
                            if maxV < cnt:
                                maxV = cnt
                            cnt = 1
                    cnt = 1
                    for b in range(N):
                        if b < N-1 and lst[b][a] == lst[b+1][a] :
                            cnt += 1
                            if maxV < cnt:
                                maxV = cnt
                        elif b< N-1 and lst[b][a] != lst[b+1][a] :
                            if maxV < cnt:
                                maxV = cnt
                            cnt = 1

                lst[i][j], lst[i][j + 1] = lst[i][j + 1], lst[i][j]
    lst = list(map(list,zip(*lst)))

print(maxV)