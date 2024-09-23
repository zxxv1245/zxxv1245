import sys
input = sys.stdin.readline


def bingo(lst) :

    check = 0
    for i in range(5) :
        cnt = 0
        for j in range(5) :
            if lst[i][j] == 0 :
                cnt += 1
        if cnt == 5 :
            check += 1

    for i in range(5) :
        cnt = 0
        for j in range(5) :
            if lst[j][i] == 0 :
                cnt += 1
        if cnt == 5 :
            check += 1

    cnt = 0
    for a in range(5) :
        if lst[a][a] == 0 :
            cnt += 1
    if cnt == 5 :
        check += 1

    cnt = 0
    for a in range(5) :
        if lst[a][4-a] == 0 :
            cnt += 1
    if cnt == 5 :
        check += 1
    return check



def check(a) :

    for i in range(5) :
        for j in range(5) :
            if a == 15 :
                b = a
            if lst[i][j] == a :
                lst[i][j] = 0
    return lst

lst = [list(map(int,input().split())) for _ in range(5)]

arr = [list(map(int,input().split())) for _ in range(5)]

def abc() :
    cnt = 0
    for i in range(5) :
        for j in range(5) :
            a = arr[i][j]
            cnt += 1

            if bingo(check(a)) >= 3 :
                return cnt

print(abc())