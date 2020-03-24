class Point:
    def __init__(self, X_set : int = 0, Y_set : int = 0):
        self.X = X_set
        self.Y = Y_set

    def on_line_with(self, p1, p2):
        k =  (p1.Y - p2.Y) / (p1.X - p2.X)
        b = p2.Y - k * p2.X 
        return self.Y == k * self.X + b 

    def __del__(self):
        print('TOTAL DESTRUCTION FOR ', self.X, self.Y)

p1 = Point(1, 1)
p2 = Point(2 ,2)
p3 = Point(3 ,3)

del p2
#print(p1.on_line_with(p2, p3))






