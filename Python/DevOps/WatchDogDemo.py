from watchdog.observers import Observer
from watchdog.events import *
import time

class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
    
    def on_moved(self, event):
        now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        if event.is_directory:
            print(f"{ now } directory { event.src_path } move to { event.dest_path }")
        else:
            print(f"{ now } file { event.src_path } move to { event.dest_path }")
            
    def on_created(self, event):
        now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        if event.is_directory:
            print(f"{ now } directory { event.src_path } created")
        else:
            print(f"{ now } file { event.src_path } created")
            
    def on_deleted(self, event):
        now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        if event.is_directory:
            print(f"{ now } directory { event.src_path } deleted")
        else:
            print(f"{ now } file { event.src_path } deleted")
            
    def on_modified(self, event):
        now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        if event.is_directory:
            print(f"{ now } directory { event.src_path } modified")
        else:
            print(f"{ now } file { event.src_path } modified")
            
if __name__ == "__main__":
    observer = Observer()
    path=r"d:\test"
    event_handler = FileEventHandler()
    observer.schedule(event_handler,path,True)
    print(f"Observer directory {path}")
    observer.start()
    observer.join()    