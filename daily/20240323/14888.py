def abc(k,ret,a,b,c,d) :
    global maxV
    global minV
    if a < 0 or b < 0 or c < 0 or d < 0 :

        return
    if k == N :
        if maxV < ret :
            maxV = ret
        if minV > ret :
            minV = ret
        return


    abc(k + 1, ret+lst[k],a-1, b, c, d)
    abc(k + 1, ret-lst[k],a, b-1, c, d)
    abc(k + 1, ret*lst[k],a, b, c-1, d)
    abc(k + 1, int(ret/lst[k]),a, b, c, d-1)



N = int(input())
lst = list(map(int,input().split()))
a,b,c,d = map(int,input().split())
maxV = -21e8
minV = 21e8

abc(1,lst[0],a,b,c,d)
print(maxV)
print(minV)


