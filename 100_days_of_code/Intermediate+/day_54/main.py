import time

def speed_calc_decorator(function):
  start = time.time()
  function()
  end = time.time()
  total = end - start
  print(f"{function.__name__} run speed: {total}s")

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i