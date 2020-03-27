from collections import deque

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['johny'] = []

def moto_saller(name):
    return name[-1] == 'j'



def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if  person not in searched:
            if moto_saller(person):
                print(person + "is seller!")
                return True 
            else:
                search_queue += graph[person]
                searched.append(person)
    return False 

print(search("you"))