from CeleryDemo.app import app

import time
import socket,os

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

@app.task
def add(x, y):
    time.sleep(3)
    s = x + y
    print("host ip {}: x + y = {}".format(get_host_ip(), s))
    return s

@app.task
def taskA():
    time.sleep(3)
    print("taskA")
    
@app.task
def taskB():
    time.sleep(3)
    print("taskB")