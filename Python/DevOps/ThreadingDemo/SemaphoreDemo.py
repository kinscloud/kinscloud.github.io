import threading
import time

semaphore = threading.BoundedSemaphore(5)

def yewubanli(name):
    semaphore.acquire()
    time.sleep(3)
    print(f'{time.strftime("%Y-%m-%d %H:%m:%S")} {name} 正在办理业务',)
    semaphore.release()
    
thread_list = []
for i in range(12):
    t = threading.Thread(target=yewubanli,args=(i,))
    thread_list.append(t)
    
for thread in thread_list:
    thread.start()
    
for thread in thread_list:
    thread.join()