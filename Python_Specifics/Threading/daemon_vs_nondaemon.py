import threading
import time
import logging

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

d = threading.Thread(name="daemon", target=daemon, daemon=True)
t = threading.Thread(name="non-daemon", target=non_daemon)

d.start()
t.start()
 # up till this, output does not include  daemon exit, because non_daemon does
 # not have sleep

 #To wait until a daemon thread has completed its work, use the join() method.

# d.join()
# t.join()

#By default, join() blocks indefinitely. It is also possible to pass a float
#value representing the number of seconds to wait for the thread to become
#inactive. If the thread does not complete within the timeout period, join()
#returns anyway.

d.join(0.1)
print("d.isAlive()",d.isAlive())
t.join()
