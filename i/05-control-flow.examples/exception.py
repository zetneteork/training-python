#!/usr/bin/python

x = int(input("x = "))
y = int(input("y = "))

try:
    z = x / y
except ZeroDivisionError:
    print("Next time try non-zero `y`.")
else:
    print("Result is {:.2f}".format(z))
finally:
    print("Goodbye.")
