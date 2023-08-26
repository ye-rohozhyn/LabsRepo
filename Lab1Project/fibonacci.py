def fib(k):
    fibonacci_sequence = [0, 1]
    for i in range(2, k):
        next_num = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_num)
    return fibonacci_sequence
