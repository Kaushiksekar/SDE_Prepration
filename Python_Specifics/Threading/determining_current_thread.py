import threading
import time

def worker():
    print(threading.current_thread().getName(), "Starting")
    time.sleep(0.2)
    print(threading.current_thread().getName(), "Exiting")

def my_service():
    print(threading.current_thread().getName(), "Starting")
    time.sleep(0.3)
    print(threading.current_thread().getName(), "Exiting")

t = threading.Thread(target=my_service, name="my_service")
w = threading.Thread(target=worker, name="worker")
w2 = threading.Thread(target=worker, name="worker1")

w.start()
w2.start()
t.start()

print("End of program") # See how end of program is printed before actual end of
# program

w.join()
w2.join()
t.join()

print("Real end of program")
