import time

def subroutine_A():
  print('subroutine_A starts!')
  time.sleep(3)
  print('subroutine_A completed!')

def subroutine_B():
  print('subroutine_B starts!')
  time.sleep(2)
  print('subroutine_B completed!')

def main():
  subroutine_A()
  subroutine_B()


time_start = time.time()
main()
time_end = time.time()

print(f'Took {time_end - time_start}')