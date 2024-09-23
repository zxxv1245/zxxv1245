import sys
input = sys.stdin.readline

def fb2(N) :
    return N-2

def fb1(N) :
    a = 1
    b = 1
    for i in range(3, N + 1):
        a,b = b, a+b
    return b

N = int(input())


print(fb1(N), fb2(N))