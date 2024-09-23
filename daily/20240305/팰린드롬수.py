def check(w):
    M = len(w) // 2
    for i in range(M):
        if w[i] != w[-i - 1]:
            return 'no'
    return ('yes')


while True:
    w = int(input())
    if w == 0:
        break
    w = str(w)
    print(check(w))
