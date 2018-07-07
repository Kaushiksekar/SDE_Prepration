import threading
import logging

class MyThread(threading.Thread):
    def run(self):
        logging.debug("running")

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] %(threadName)-10s %(message)s',
)

for i in range(5):
    t = MyThread()
    t.start() # return value of run is ignored
