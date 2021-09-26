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

i=-1
pempt=''
while i > -(len(empt))-1:
    pempt=pempt+empt[i]
    i=i-1
print("Flipped word:", pempt)
print("Is palindrome:", pempt==empt)


