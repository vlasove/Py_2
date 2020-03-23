#Add(2,3)

def Add(a:int):
    def Add_New(b:int):
        return a + b 
    return Add_New

bite = Add(10)
print(Add(2)(3))
print(bite(20))
print(bite(3))

