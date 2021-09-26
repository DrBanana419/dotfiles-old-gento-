class coord(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def __str__(self):
        return "("+str(self.x)+","+" "+str (self.y)+")"

    def distance (self, other):
        xsq=(self.x-other.x)**2
        ysq=(self.y-other.y)**2
        return (xsq+ysq)**0.5

    def __add__(self, other):
        X=self.x+other.x
        Y=self.y+other.y
        return(X, Y)
    
    def long(self):
        return (self.x**2+self.y**2)**0.5
    

print(coord(5, 7))
print(coord(5, 7)+coord(6,10))
c=coord (3,4)
print (c.x)
origin=coord (0,0)
print (coord.distance (c, origin))
print (c)
print (c.long())
