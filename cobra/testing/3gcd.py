b= int ( input("Give: "))
s= int ( input("Give: "))
def gcd (x, y):
    if x==y:
        return x
    elif x==0 or y==o:
        return 0
    elif x>y:
        r=x%y
        while r != 0:
            x=y
            y=r
            r=x%y
        return y
    elif y>x:
        r=y%x
        while r != 0:
            y=x
            x=r
            r=y%x
        return x 

print (gcd (b ,s))

def lcm(a, b):
    return a*b/gcd(a, b)

