class Film:
    title = ''
    author = ''
    year = 0
    actors = []
    rating = 0.0 
    duration = 0
    is18 = False 
    localization = None

    
f2 = Film()
f2.title = 'HP'
f2.duration = 150


f1 = Film()
f1.title = 'LOTR'
f1.duration = 240

print(f1.title, f1.duration, f1.localization)


films = [f1, f2]

for film in films:
    print('Title:', film.title, 'Dur:', film.duration)

