import threading
import time

# def coding():
#     for x in range(3):
#         print('正在写代码%s '%threading.current_thread())
#         time.sleep(1)

# def drawing():
#     for x in range(3):
#         print('正在画图%s '%threading.current_thread())
#         time.sleep(1)

# def single_thread():
#     coding()
#     drawing()


class CodingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print('正在写代码%s ' % threading.current_thread())
        time.sleep(1)


class DrawingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print('正在画图%s ' % threading.current_thread())
            time.sleep(1)


def multi_thread():
    # t1 = threading.Thread(target=coding)
    # t2 = threading.Thread(target=drawing)
    t1 = CodingThread()
    t2 = DrawingThread()

    t1.start()
    t2.start()

    # print(threading.enumerate())


if __name__ == "__main__":
    multi_thread()
