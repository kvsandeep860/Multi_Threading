# import time
# import threading

# start = time.perf_counter()

# def do_something():
#     print("Sleeping for a second")
#     time.sleep(1)
#     print("Done Sleeping")

# threads = []

# for _ in range(10):
#     t = threading.Thread(target=do_something)
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

# finish = time.perf_counter()

# print(f"time taken to complete the code is {finish-start}")

import time
import concurrent.futures

start = time.perf_counter()

def do_something():
    print("Sleeping for a second")
    time.sleep(1)
    print("Done Sleeping")

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(do_something) for _ in range(10)]

finish = time.perf_counter()
print(f"Time taken: {finish - start:.2f}s")