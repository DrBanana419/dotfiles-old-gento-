def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n==1:
        return printMove(fr, to)
    else:
        return Towers(n-1, fr, to, spare)

print(Towers(4, 'b', 'a', 'c'))
