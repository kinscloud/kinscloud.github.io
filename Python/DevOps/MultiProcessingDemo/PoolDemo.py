import multiprocessing
import time


def task(name):
    print(f'{time.strftime("%Y-%m-%d %H:%m:%S")} : {name} start...')
    time.sleep(3)


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=3)
    for i in range(10):
        pool.apply_async(func = task,args=(i,))
    pool.close()
    pool.join()
    print("hello")