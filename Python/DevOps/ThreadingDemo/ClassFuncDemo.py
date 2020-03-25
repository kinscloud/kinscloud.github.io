import time
import threading


def task_thread(counter):
    print(
        f'name: {threading.current_thread().name} args: {counter} begin at: {time.strftime("%Y-%m-%d %H:%m:%S")}'
    )
    num = counter
    while num:
        time.sleep(3)
        num -= 1
    print(
        f'name: {threading.current_thread().name} args: {counter} end at: {time.strftime("%Y-%m-%d %H:%m:%S")}'
    )


class MyThread(threading.Thread):
    def __init__(self, target,args):
        super().__init__()
        self.target = target
        self.args = args

    def run(self):
        self.target(*self.args)


if __name__ == "__main__":
    print(
        f'main thread: {threading.current_thread().name} begin at: {time.strftime("%Y-%m-%d %H:%m:%S")}'
    )
    t1 = MyThread(target=task_thread,args={3,})
    t2 = MyThread(target=task_thread,args={2,})
    t3 = MyThread(target=task_thread,args={1,})

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print(
        f'main thread: {threading.current_thread().name} end at: {time.strftime("%Y-%m-%d %H:%m:%S")}'
    )
