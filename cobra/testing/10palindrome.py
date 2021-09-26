expt= input("")
empt=""
for i in expt:
    if i in "abcdefghijklmnopqrstuvwxyz":
        empt=empt+i
    elif i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        li=i.lower()
        empt=empt+li
    else:
        print("removed a space or non letter character")


print("Given expression (without spaces):", empt)

def ispalindrome(st):
    if len(st)==1:
        return True
    else:
        return st[0]==st[-1] and ispalindrome(st[1:-1])

print(ispalindrome(empt))

