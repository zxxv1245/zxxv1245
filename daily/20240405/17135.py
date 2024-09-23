from itertools import combinations
import copy


N,M,K = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(N)]

arr = []
for w in range(M) :
    arr.append((N,w))
combi = list(combinations(arr,3))
maxV = -21e8
for a in combi :
    tlst = copy.deepcopy(lst)
    cnt = 0
    for b in range(N) :
        rlst = []
        for c in a :
            alst = []
            for i in range(N) :
                for j in range(M) :
                    if abs(c[0]-i) + abs(c[1]-j) <= K and tlst[i][j] == 1 :
                        alst.append((i,j,(abs(c[0]-i) + abs(c[1]-j))))
            if alst :
                alst.sort(key = lambda x:x[0],reverse=True)
                alst.sort(key = lambda x:x[1])
                alst.sort(key = lambda x:x[2])
                rlst.append((alst[0][0],alst[0][1]))


        for ff in rlst :
            if tlst[ff[0]][ff[1]] == 1 :
                cnt += 1
                tlst[ff[0]][ff[1]] = 0


        for r in range(N-1,-1,-1) :
            for rr in range(0,M) :
                if r-1 < 0 :
                    tlst[r][rr] = 0
                else :
                    tlst[r][rr] = tlst[r-1][rr]


    if maxV < cnt :
        maxV = cnt
print(maxV)
