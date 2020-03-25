class A:
    __tablename__ = 'bob'

    def __init__(self):
        self.__a = 2 
        self.__b = 3

    def get_a(self):
        return self.__a
        
    def method1(self):
        query = 'SELECT * FROM ?'
        q = (query, (self.__tablename__,)) 

    def __method2(self):
        pass 

