from collections import deque

my_queue = deque([1,2,3,4,5])
my_queue.append(10) # [1,2,3,4,5,10]
my_queue.appendleft(2) #[20, 1,2,3,4,5, 10]
my_queue.count(10) # 1 
#my_queue.clear() 
my_queue.extend([20,30,40,50]) # [20, 1,2,3,4,5, 10, 20,30,40,50 ]
my_queue.extendleft([20,30,40]) # ..

my_queue.pop()
my_queue.popleft()

my_queue.reverse()

len(my_queue)
