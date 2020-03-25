class Queue:
    def __init__(self):
        self.body = [] 
    def add(self, elem):
        self.body.append(elem) 
    def remove(self):
        if self.is_empty():
            return None 
        else:   
            out = self.body[0]
            self.body = self.body[1:] 
            return out
    def is_empty(self):
        return len(self.body) == 0 
    def __str__(self):
        return str(self.body) 


q = Queue()