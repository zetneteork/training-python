#!/usr/bin/python3
import sys

class memoize:
    def __init__(self, f):
        self._f = f
        self._cache = {}

    def __call__(self, x):
        if x not in self._cache:            
            self._cache[x] = self._f(x)
        return self._cache[x]

@memoize
def fib(n):
    if n in (0, 1):
        return n
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    print(fib(int(sys.argv[1])))    
