import time
import threading

class MyThread(threading.Thread):
    def __init__(self,counter):
        super().__init__()
        self.counter = counter

    def run(self):
        print(
            f'name: {threading.current_thread().name} args: {self.counter} begin at: {time.strftime("%Y-%m-%d %H:%m:%S")}'
        )
        num = self.counter
        while num:
            time.sleep(3)
            num -=1
        print(
            f'name: {threading.current_thread().name} args: {self.counter} end at: {time.strftime("%Y-%m-%d %H:%m:%S")}'
        )   
    
if __name__ == "__main__":
    print(
        f'main thread: {threading.current_thread().name} begin at: {time.strftime("%Y-%m-%d %H:%m:%S")}'
    )
    t1 = MyThread(3)
    t2 = MyThread(2)
    t3 = MyThread(1)
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()
    
    print(
        f'main thread: {threading.current_thread().name} end at: {time.strftime("%Y-%m-%d %H:%m:%S")}'
    )