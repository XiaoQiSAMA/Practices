import _thread
import time

def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(f'{thread_name} : {time.asctime()}')

#创建线程
try:
    _thread.start_new_thread(print_time, ('thread1', 2))
    _thread.start_new_thread(print_time, ('thread2', 4))
except:
    print("ERROR")

while 1:
    pass