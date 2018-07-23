import threading
import logging
import time

def daemon():
    logging.debug("Starting")
    time.sleep(0.2)
    logging.debug("Exiting")

def non_daemon():
    logging.debug("Starting")
    logging.debug("Exiting")

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] %(threadName)-10s %(message)s',
)

# d = threading.Thread(target=daemon, name="Daemon")
d = threading.Thread(target=daemon, name="Daemon", daemon=True)
nd = threading.Thread(target=non_daemon, name="Non Daemon")

d.start()
nd.start()

d.join()
nd.join()
