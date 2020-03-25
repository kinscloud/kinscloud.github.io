from multiprocessing import Process,Queue
import time

def ProducerA(q):
    count = 1
    while True:
        q.put(f'cold drink {count}')
        print(f'{time.strftime("%Y-%m-%d %H:%m:%S")} A push in : [cold drink {count}]')
        count += 1
        time.sleep(3)
        
def ConsumerB(q):
    while True:
        print(f'{time.strftime("%Y-%m-%d %H:%m:%S")} B pull out : [{q.get()}]')
        time.sleep(2)
        
if __name__ == "__main__":
    q = Queue(maxsize=5)
    p = Process(target=ProducerA,args=(q,))
    c = Process(target=ConsumerB,args=(q,))
    c.start()
    p.start()
    c.join()
    p.join()
    