card=['W','B','R']
path=['']*3

def abc(level):

    if level==3:
        if 'B' in path :
            print(path)
        return

    for i in range(3):
        path[level]=card[i]
        abc(level+1)

abc(0)