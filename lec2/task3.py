def a_def(x,y):
    return x + y

a_lambda = lambda x,y: x + y
print(a_lambda(1,2) )
print(a_lambda)
print(a_def)

f_list = [a_lambda, a_def]
f_list[0](1,2)