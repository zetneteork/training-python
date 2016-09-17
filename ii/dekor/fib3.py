#!/usr/bin/python3
import sys

class memoize:
    _cache = {}

    def __init__(self, f):
        self._f = f

    def __call__(self, x):
        if (self._f, x) not in self._cache:            
            self._cache[self._f, x] = self._f(x)
        return self._cache[self._f, x]

@memoize
def fib(n):
    if n in (0, 1):
        return n
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    print(fib(int(sys.argv[1])))    
