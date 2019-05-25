import threading
import time


#多线程
class mythreading(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("thread started :" + self.name)
        print_name(self.name, self.counter, 5)
        print("thread stopped :" + self.name)


def print_name(threadname, delay, counter):
    while counter:
#        if exitFlag:
#            threadname.exit()
        time.sleep(delay)
        print(f'{threadname}: {time.asctime()} \n')
        counter -= 1

thread1 = mythreading(1, "Thread1", 5)
thread2 = mythreading(2, "Thread2", 5)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出")