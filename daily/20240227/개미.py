import sys
input = sys.stdin.readline
w,h = map(int,input().split())
x,y = map(int,input().split())
t = int(input())

if (x+t) % w != 0 :
    if ((x+t) // w) % 2 == 0 :
        i = 0 + ((x + t) % w)
    else :
        i = w - ((x + t) % w)
elif (x+t) % w == 0 :
    if ((x+t) // w) % 2 == 0 :
        i = 0
    else :
        i = w

if (y+t) % h != 0 :
    if ((y+t) // h) % 2 == 0 :
        j = 0 + ((y + t) % h)
    else :
        j = h - ((y + t) % h)


elif (y+t) % h == 0 :
    if ((y+t) // h) % 2 == 0 :
        j = 0
    else :
        j = h

print(i, j)
