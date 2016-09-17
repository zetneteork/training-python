import threading, queue
import math
import sys
import time

class Factorial(threading.Thread):

    def __init__(self, n, queue):
        threading.Thread.__init__(self)
        self.n = n
        self.queue = queue

    def run(self):
        result = 1
        for i in range(1, self.n+1):
            result *= i
        self.queue.put(result)

if __name__ == '__main__':
    queue = queue.Queue()
    thread = Factorial(int(sys.argv[1]), queue)
    thread.start()
    while queue.empty():
        print('.', end='', file=sys.stderr)
        sys.stderr.flush()
        time.sleep(0.2)
    print("Result: {0}".format(queue.get()), file=sys.stderr)
    thread.join()
