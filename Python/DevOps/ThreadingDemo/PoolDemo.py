from multiprocessing.dummy import Pool as ThreadPool
import time

def fun(n):
    time.sleep(2)
    
start = time.time()
for i in range(5):
    fun(i)
    
print(f"singer thread times: {time.time() - start}")

start2 = time.time()

pool = ThreadPool(processes=5)
results2 = pool.map(fun,range(5))
pool.close()
pool.join()
print(f"five thread times: {time.time() - start2}")