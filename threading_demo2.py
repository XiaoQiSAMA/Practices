import threading
import time

class mythread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("start: " + self.name)
        #获得锁,用于线程同步
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        #释放锁,开启下一个进程
        threadLock.release()

def print_time(threadname, delay, counter):
    while counter:
        time.sleep(delay)
        print(f'{threadname} : {time.asctime()}')
        counter -= 1


threadLock = threading.Lock()
threads = []

thread1 = mythread(1, 'thread1', 3)
thread2 = mythread(2, 'thread2', 3)

thread1.start()
thread2.start()

#添加线程到线程表
threads.append(thread1)
threads.append(thread2)

#等待所有线程完成
for t in threads:
    t.join()
print("finish!")