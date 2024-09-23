people  = [1,2,3,4]
path = [0]*3
used = [0]*4

def abc(level) :

    if level == 3 :
        print(path)
        return

    for i in range(4) :
        if used[i] == 1 : continue
        path[level] = i + 1
        used[i] = 1
        abc(level+1)
        used[i] = 0

abc(0)