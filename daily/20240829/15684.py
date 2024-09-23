N = int(input())

arr = [1]*4000001
arr[0] = arr[1] = 0

for i in range(2001) :
    if arr[i] == 1 :
        for j in range(i+i,4000001,i) :
            arr[j] = 0

sumV = 0
end = 0
cnt = arr[N]
for start in range(N) :
    if arr[start] == 1 :
        while sumV < N and end <= N:
            if arr[end] == 1:
                sumV += end
            end += 1
        if sumV == N :
            cnt += 1
        sumV -= start

print(cnt)