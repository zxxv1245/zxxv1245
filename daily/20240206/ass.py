T = int(input())

for Test in range(1,T+1) :
    lst = [input() for _ in range(5)]

    ret = ''

    maxV = 0
    for i in lst:
        if maxV < len(i):
            maxV = len(i)
        if len(i) < maxV:
            i += ' ' * (maxV - len(i))
    print(lst)