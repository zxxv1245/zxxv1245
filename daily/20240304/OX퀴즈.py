T = int(input())

for Test in range(1,T+1) :
    arr = input()
    ret = []
    cnt = 0
    for i in arr :
        if i == 'O' :
            cnt += 1
            ret.append(cnt)
        elif i == 'X' :
            cnt = 0

    result = sum(ret)
    print(result)