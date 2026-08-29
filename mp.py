import multiprocessing
import math
import sys
import time

sys.set_int_max_str_digits(1000000)

def compute_factorial(n):
    print(f"Computing factorial of {n}")
    result = math.factorial(n)
    print(f"Factorial of {n} is {result}")
    return result

if __name__=="__main__":
    n = [5000,6000,7000,8000,9000,10000]
    start_time = time.time()


    with multiprocessing.Pool(processes=6) as pool:
        results = pool.map(compute_factorial, n)

    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
    print(f"Results: {results}")


    
