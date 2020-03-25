class Stack:
    def __init__(self):
        self.body = []

    def add(self, elem):
        self.body.append(elem) 

    def remove(self):
        if self.is_empty():
            return None 
        return self.body.pop()

    def is_empty(self):
        return len(self.body) == 0 

    def __str__(self):
         return str(self.body)

s1 = Stack()
s1.add(10)
s1.add(10)
s1.add(140)
s1.add(20)
s1.remove()
s1.remove()
print(s1.is_empty(), s1)
