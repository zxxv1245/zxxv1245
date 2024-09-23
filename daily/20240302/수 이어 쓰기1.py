import sys
input = sys.stdin.readline

N = int(input())

arr = 0
i = 1
while i <= N :
    arr += len(str(i))
    i += 1

print(arr)