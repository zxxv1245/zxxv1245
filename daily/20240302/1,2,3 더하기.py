def abc(k) :
    global cnt
    global N
    if k == N :
        cnt += 1
        return

    if k > N :
        return

    for i in range(1,4) :

        abc(k+i)




T = int(input())

for Test in range(T) :
    N = int(input())
    cnt = 0
    lst = []
    abc(0)
    print(cnt)