from concurrent.futures import ThreadPoolExecutor
import time
def print_numbers(number):
        time.sleep(2)
        return f"Number:{number}"
numbers = [1,2,3,4,5]
with ThreadPoolExecutor(max_workers=3) as executor:
    result = executor.map(print_numbers,numbers)


for res in result:
    print(res)