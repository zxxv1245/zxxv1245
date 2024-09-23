import copy

def is_clock(k,x) :
    if k == 1:
        lst[x].insert(0, lst[x].pop())
        k = -1
    elif k == -1:
        lst[x].append(lst[x].pop(0))
        k = 1
    return k
#톱니바퀴
# 2 & 6 비교하기

T = int(input())
for Test in range(1,T+1) :
    N = int(input())
    lst = [list(input().split()) for _ in range(4)]

    for _ in range(N) :
        num, k = map(int,input().split())
        arr = copy.deepcopy(lst)
        x = num - 1
        k = is_clock(k,x)
        pk = k
        left = x - 1
        while left >=0 :
            if arr[x][6] != arr[left][2] :
                k = is_clock(k,left)
                x = left
                left = left - 1
            else :
                break

        x = num-1
        right = x + 1
        while right < 4 :
            if arr[x][2] != arr[right][6] :
                pk = is_clock(pk,right)
                x = right
                right = right + 1
            else :
                break

    result = 0
    for w in range(4) :
        if lst[w][0] == '1' :
            result += 2**w

    print(f'#{Test} {result}')
