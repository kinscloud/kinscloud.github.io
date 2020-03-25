import threading

class Boy(threading.Thread):
    def __init__(self,cond,name):
        super(Boy,self).__init__()
        self.cond = cond
        self.name = name
        
    def run(self):
        self.cond.acquire()
        print(self.name + ": 嫁给我吧！？")
        self.cond.notify()
        self.cond.wait()
        print(self.name + ": 我单膝跪地，送上戒指！")
        self.cond.notify()
        self.cond.wait()
        print(self.name + ": li 太太，你的选择太明智了。")
        self.cond.release()
        
class Girl(threading.Thread):
    def __init__(self,cond,name):
        super(Girl,self).__init__()
        self.cond = cond
        self.name = name
        
    def run(self):
        self.cond.acquire()
        self.cond.wait()
        print(self.name + ": 没有情调，不够浪漫，不答应")
        self.cond.notify()
        self.cond.wait()
        print(self.name + ": 好吧，答应你了")
        self.cond.notify()
        self.cond.release()
        
if __name__ == "__main__":
    cond = threading.Condition()
    boy = Boy(cond,"LiLei")
    girl = Girl(cond,"HanMeiMei")
    girl.start()
    boy.start()