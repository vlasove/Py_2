class Film:
    def __init__(self, _id, title, duration):
        self._id = _id 
        self.title = title 
        self.duration = duration
    def save(self):
        pass 
    def update_title(self, new_title):
        pass 
    def update_duration(self, new_duration):
        pass 
    def delete(self):
        pass 
    
f = Film(1, 'asd', 200)
f.save()


query_save = "INSERT INTO films VALUES(?,?,?)"
cur.execute(query_save, (self._id, self.title, self.duration))

