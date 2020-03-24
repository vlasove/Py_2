class Point:
    def __init__(self, X_set : int = 0, Y_set : int = 0):
        print('Point creation')
        self.X = X_set
        self.Y = Y_set

    def on_line_with(self, p1, p2):
        k =  (p1.Y - p2.Y) / (p1.X - p2.X)
        b = p2.Y - k * p2.X 
        return self.Y == k * self.X + b 

    # def __del__(self):
    #     print('TOTAL DESTRUCTION FOR ', self.X, self.Y)


