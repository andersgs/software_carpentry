# write a function that calculates the factorial of an integer

import sys

number = (int) (sys.argv[1])

def factorial(number):
    results = 1
    for i in range(1,number+1):
        results *= i
    return results
    
print "The factorial of {} is {}.".format(number,factorial(number))

def fib(n):
    a,b = 0,1
    while b < n:
        a,b = b, a+b
    return b
    
def fib_seq(n):
    a,b = 0,1
    results = [a,b]
    while b < n:
        a,b = b, a+b
        results.append(b)
    return results
    
print "The {} number in the Fibonacci sequence is {}.".format(number,fib(number))
print "The fibonacci sequence of {} number(s) is {}.".format(number,fib_seq(number))
