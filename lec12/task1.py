a_list = [1,2,3,4,5,6,7]

with open('output.txt', 'a') as f:
    for item in a_list:
        f.write(str(item))
        f.write('\n')

with open('output.txt', 'r') as f:
    for ..f.writelines()