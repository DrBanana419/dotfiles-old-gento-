class coord(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def __str__(self):
        return "Hello"

    def __add__(self, other):
        X=self.x+other.x
        Y=self.y+other.y
        return(X, Y)

print(coord(5, 7))
print(coord(5, 7)+coord(6,10))
