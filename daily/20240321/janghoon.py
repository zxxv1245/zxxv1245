
def top(k,ret) :
    global minV
    if ret >= B :
        minV = min(minV,ret-B)
        return

    if k == N :
        return


    top(k+1,ret)
    top(k+1,ret+lst[k])


T = int(input())
for Test in range(1,T+1) :
    N,B = map(int,input().split())

    lst = list(map(int,input().split()))

    minV = 21e8
    top(0,0)

    print(f'#{Test} {minV}')