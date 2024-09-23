N = int(input())

lst = [list(map(int,input().split())) for _ in range(6)]

for _ in range(6) :
    if lst[2][0] == lst[4][0] and lst[3][0] == lst[5][0] :
        area = lst[0][1]*lst[1][1] - lst[3][1]*lst[4][1]
    lst.append(lst.pop(0))

ret = N * area

print(ret)