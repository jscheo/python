def garo():
    for x in range(2, 10):
        for y in range(1, 10):
            print(x, 'X', y, '=', x * y)
        print()

def sero():
    for x in range(2, 10):
        print(x,"단")
        for y in range(1, 10):
            print(x, 'X', y, '=', x * y, end="\t")
        print()