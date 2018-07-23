import threading
import time

def worker():
    print(threading.current_thread().getName(), "Starting")
    time.sleep(0.7)
    print(threading.current_thread().getName(), "Exiting")

def my_service():
    print(threading.current_thread().getName(), "Starting")
    time.sleep(0.2)
    print(threading.current_thread().getName(), "Exiting")

t = threading.Thread(target=worker, name="Worker")
w1 = threading.Thread(target=my_service, name="My Service")

t.start()
w1.start()
