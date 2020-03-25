import multiprocessing
import time

def wait_for_event(e):
    e.wait()
    time.sleep(1)
    e.clear()
    print(f'{time.strftime("%Y-%m-%d %H:%m:%S")} process a: i wait u.')
    e.wait()
    print(f'{time.strftime("%Y-%m-%d %H:%m:%S")} process a: ok，let\'s go.')
    
def wait_for_event_timeout(e,t):
    e.wait()
    time.sleep(1)
    e.clear()
    print(f'{time.strftime("%Y-%m-%d %H:%m:%S")} process b: ok i wait u {t} seconds.')
    e.wait(t)
    print(f'{time.strftime("%Y-%m-%d %H:%m:%S")} process b: i go ahead.')
    
if __name__ == "__main__":
    e = multiprocessing.Event()
    w1 = multiprocessing.Process(target=wait_for_event,args=(e,))
    w2 =  multiprocessing.Process(target=wait_for_event_timeout,args=(e,5))
    w1.start()
    w2.start()
    print(f'{time.strftime("%Y-%m-%d %H:%m:%S")} process main: i need 8 seconds.')
    e.set()
    time.sleep(8)
    print(f'{time.strftime("%Y-%m-%d %H:%m:%S")} process main: okey...')
    e.set()
    w1.join()
    w2.join()
    print(f'{time.strftime("%Y-%m-%d %H:%m:%S")} process main: exit...')
    