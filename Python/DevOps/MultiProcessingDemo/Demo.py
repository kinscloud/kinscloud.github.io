from multiprocessing import Process
import os
import time

class MyProcess(Process):
    def __init__(self,delay):
        self.delay = delay
        super().__init__()
        
    def run(self):
        num =0
        for i in range(self.delay*10000000):
            num+=i
        print(f"进程pid为 { os.getpid() },执行完成")
        
if __name__ == "__main__":
     print("父进程pid为 %s" % os.getpid())
     p0= MyProcess(3)
     p1= MyProcess(3)
     t0 = time.time()
     p0.start();p1.start()
     p0.join();p1.join()
     t1 = time.time()
     print(f'并发执行耗时 { t1 -t0 }')

# def task_process(delay):
#     print(f'{time.strftime("%Y-%m-%d %H:%m:%S")} subthread start.')
#     print(f'sleep {delay}s')
#     time.sleep(delay)
#     print(f'{time.strftime("%Y-%m-%d %H:%m:%S")} subthread finished.')
    
# if __name__ == "__main__":
#     print(f'{time.strftime("%Y-%m-%d %H:%m:%S")} thread start.')
#     p0 = Process(target=task_process,args=(3,))
#     p0.daemon = True #父进程终止后程序终止，不能产生新进程
#     p0.start()
#     print(f'{time.strftime("%Y-%m-%d %H:%m:%S")} thread finished.')