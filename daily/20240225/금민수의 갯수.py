
def abc(ret) :
    global N
    arr = ['4','7']
    if ret :
        lst.append(int(ret))

    if ret and int(ret) > N :
        lst.pop()
        return -1

    if lst and sum(lst) == N :
        return lst

    if lst and sum(lst) > N :
        return

    for i in range(2) :
        abc(ret+arr[i])


N = int(input())

lst = []
ret = ''

abc(ret)
if abc(ret) == -1 :
    print(-1)
else :
    print(lst)
