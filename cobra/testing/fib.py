#def fib(n):
#    x0=1
#    x1=1
#    i=1
#    while i < n:
#        xt=x1
#        x1=x1+x0
#        x0=xt
#        i += 1
#    
#    return x1

#a=int( input("Give: "))
#print(fib(a))

def fib1(n):
    if n==0 or n==1:
        return 1
    else:
        return fib1(n-1)+fib1(n-2)

b=int( input("Give: "))
print(fib1(b))
