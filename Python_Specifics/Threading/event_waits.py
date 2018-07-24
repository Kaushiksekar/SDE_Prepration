import threading
import logging
import time

def wait_for_event(e):
    logging.debug("wait for event")
    event_is_set = e.wait()
    logging.debug("event_is_set : %s", event_is_set)

def wait_for_event_timeout(e, t):
    logging.debug("wait for event timeout")
    event_is_set = e.wait(t)
    logging.debug("event_is_set : %s", event_is_set)
    if event_is_set:
        logging.debug("processing event")
    else:
        logging.debug("waiting for other event")

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

e = threading.Event()

t1 = threading.Thread(name="block", target=wait_for_event, args=(e,))
t1.start()

t2 = threading.Thread(name="non-block", target=wait_for_event_timeout, args=(e,0.3))
t2.start()

logging.debug("Waiting before calling event.set")
time.sleep(0.5) # wait for event timeout exits if control event is not set within 0.3
e.set()
logging.debug("Event is set")
