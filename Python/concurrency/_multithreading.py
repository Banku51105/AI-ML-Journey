# Q1 — Create Your First Thread
import threading
def greet():
    print("Hello from Thread")
t = threading.Thread(target = greet)
t.start()
t.join()
print("Main Thread Finished")

# Q2 — Multiple Threads
def program():
    print("Working...")
threads = []
for i in range(5):
    t = threading.Thread(target = program)
    t.start()
    threads.append(t)
for thread in threads:
    thread.join()
print("Main Thread Finished")

# Q3 — Passing Arguments
def square(n):
    print(n*n)
t = threading.Thread(target = square, args = (7,))
t.start()
t.join()

# Q4 — Lock
counter = 0
lock = threading.Lock()
def increment(x):
    global counter
    with lock:
        counter = counter + 1
threads = [threading.Thread(target = increment, args = (i,)) for i in range(5)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(counter)