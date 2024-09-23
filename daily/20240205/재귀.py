def abc(level) :
    print(level)
    if level == 2 :
        return

    abc(level +1)
    print(level)


abc(0)