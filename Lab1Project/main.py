from prime_numbers import *
from fibonacci import *

a = int(input("Task 1\nEnter first number: "))
b = int(input("Enter second number: "))

if a > b:
    a, b = b, a

print_prime_numbers(a, b)

k = int(input("Task 2\nEnter count fibonacci numbers: "))
print(fib(k))
