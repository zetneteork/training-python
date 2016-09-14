#!/usr/bin/python

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print("{}: Divisible by {}.".format(n, x))
            break
    else:
        print("{}: Prime number.".format(n))
