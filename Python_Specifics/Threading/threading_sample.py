import threading

def worker():
    print("Worker")

threads = []
for _ in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
