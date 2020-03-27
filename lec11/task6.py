from collections import ChainMap

d1 = {'a':2, 'b':3}
d2 = {'c':200, 'q':-1}
chain_map = ChainMap(d1, d2)
print(chain_map)

print(chain_map['a'])
print(chain_map['c'])
print(chain_map.maps[0])

print(list(chain_map.keys()))
print(list(chain_map.values()))

d3 = {'w':200}
chain_map = chain_map.new_child(d3)
print(chain_map)