T = int(input())

for Test in range(1,T+1) :
    A = list(input().split())
    N = int(A[0])
    lst = A[1:]
    M = len(lst)
    B = 1
    O = 1
    cnt = 0
    ant = 0
    P = 0
    a = 'C'
    p = 0
    for i in range(0,M,2) :
        if a == 'C' :
            a = lst[i]

        if a != lst[i] :
            P = p

        if lst[i] == 'B' :
            B += P
            jj = B
            if B == int(lst[i+1]) :
                ant = 1
                P = 1
            elif B > int(lst[i+1]) :
                B = int(lst[i+1])
                ant = abs(int(lst[i + 1]) - jj) + 1
                P = abs(int(lst[i + 1]) - jj)
            else :
                P = int(lst[i + 1]) - jj
                ant = int(lst[i+1])- jj + 1
        elif lst[i] == 'O' :

            O += P
            jj = O
            if O == int(lst[i + 1]):
                ant = 1
                P = 1
            elif O > int(lst[i + 1]):
                O = int(lst[i + 1])
                ant = abs(int(lst[i + 1]) - jj) + 1
                P = abs(int(lst[i + 1]) - jj)
            elif O < int(lst[i + 1]):
                P = int(lst[i + 1]) - jj
                ant = int(lst[i + 1]) - jj + 1

        cnt += ant
        if a == lst[i] :
            p += ant



    print(cnt)