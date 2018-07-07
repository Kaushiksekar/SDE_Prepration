import threading
import time
import logging

def worker():
    logging.debug("Starting")
    time.sleep(0.3)
    logging.debug("Exiting")

def my_service():
    logging.debug("Starting")
    time.sleep(0.2)
    logging.debug("Exiting")

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] %(threadName)-10s %(message)s',
)

threads = []
for i in range(5):
    w = threading.Thread(target=worker, name="worker")
    w2 = threading.Thread(target=worker)
    t = threading.Thread(target=my_service, name="my_service")

w.start()
w2.start()
t.start()
