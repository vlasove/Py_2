import pickle 

a_list = [1,2,3,4,5,6,7]
b_dict = {'a' : 2, 'c':10}

a_list_in_bytes = pickle.dumps(a_list)
print(a_list_in_bytes)
print(pickle.dumps(b_dict))

with open('data', 'wb') as f:
    pickle.dump(a_list, f)
    pickle.dump(b_dict, f)

del a_list
del b_dict 

with open('data', 'rb') as f:
    a = pickle.load(f)
    b = pickle.load(f)

    print(a)
    print(b)