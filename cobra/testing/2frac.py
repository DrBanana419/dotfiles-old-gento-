#Define gcd
def gcd (x, y):
    if x==y:
        return x
    elif x==0 or y==0:
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

#Define lcm
def lcm(a, b):
    return a*b/gcd(a, b)

#Define fraction class
class frac(object):
    def __init__(self, x, y):
        self.x=int(x)
        self.y=int(y)

    def __str__(self):
        return str (self.x)+"/"+str (self.y)

    def __add__(self, other):
        denom=lcm (self.y, other.y)
        l1=denom/self.y
        l2=denom/other.y
        numer=self.x*l1+other.x*l2
        if gcd(numer, denom)>1:
            g=gcd(numer, denom)
            numer=numer/g
            denom=denom/g 
        if numer>denom:
            return str(int(numer/denom))+"+"+str(frac(numer%denom, denom))
        else:
            return frac (numer, denom)

    def __sub__(self, other):
        denom=lcm (self.y, other.y)
        l1=denom/self.y
        l2=denom/other.y
        numer=self.x*l1-other.x*l2
        if gcd(numer, denom)>1:
            g=gcd(numer, denom)
            numer=numer/g
            denom=denom/g
        return frac (numer, denom)



#Inputs
m=int ( input("Give: "))
n=int ( input("Give: "))
M=int ( input("Give: "))
N=int ( input("Give: "))



#Fractions
f1=frac (m, n)
f2=frac (M, N)
#Sums
s=f1+f2
print(s)

print()
hello()

