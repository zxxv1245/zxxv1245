T = int(input())

for Test in range(1,T+1) :
    V, E = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    stack = [S]
    for i in range(5) :
        if lst[i][0] == S :
            stack.append(lst[i][1])
