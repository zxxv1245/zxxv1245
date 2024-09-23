T = int(input())

for Test in range(1,T+1) :
    N = int(input())
    leftV = []
    rightV = []
    cnt = 0
    for _ in range(N) :
        L,R = map(int,input().split())
        leftV.append(L)
        rightV.append(R)
        leftV.sort()
        rightV.sort()
        cnt += abs(leftV.index(L) - rightV.index(R))

    print(f'#{Test} {cnt}')