import sys
import numpy as np
import time

python_list = list(range(1,10))
np_list = np.arange(1,10)


print(python_list*2)
print(np_list*2)


# print(sys.getsizeof(python_list))
# print(sys.getsizeof(np_list))

def sum_sqrs(sequence):
  sum = 0
  for i in sequence:
    sum += i**2

  # print(f'sum = {sum}')


# start_time = time.time()
# sum_sqrs(python_list)
# start_end = time.time()

# python_list_time = start_end - start_time
# print(f'python_list_time = {python_list_time}')



# start_time = time.time()
# sum_sqrs(np_list)
# start_end = time.time()

# np_list_time = start_end - start_time
# print(f'np_list_time = {np_list_time}')