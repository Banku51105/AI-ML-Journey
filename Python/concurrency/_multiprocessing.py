# Q1 — Create Your First Process
import multiprocessing
def greet():
    print("Hello from Process")
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=greet)
    p1.start()
    p1.join()
    print("Main Process Finished")