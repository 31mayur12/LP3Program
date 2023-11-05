# Recursive Fibonacci Calculation 

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = 10  # Change this to the desired Fibonacci number you want to calculate
result = fibonacci_recursive(n)
print(f"Fibonacci({n}) = {result}")



# Non-Recursive Fibonacci Calculation

def fibonacci_non_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
            print(fib[i])
        return fib[n]

n = 10  # Change this to the desired Fibonacci number you want to calculate
result = fibonacci_non_recursive(n)
print(f"Fibonacci({n}) = {result}")




# IF asked about time and space complexit⬇️⬇️⬇️
import timeit


def fibonacci(n):
    """Non recursive fibonacci function"""
    for i in range(2, n + 1):
        fib_list[i] = fib_list[i - 1] + fib_list[i - 2]
    return fib_list[n]


def fibonacci_recursive(n):
    """Recursive fibonacci function"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    fib_recur_list[n] = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    return fib_recur_list[n]


N = 20
RUNS = 1000
print(f"Given N = {N}\n{RUNS} runs")

fib_list = [0] * (N + 1)
fib_list[0] = 0
fib_list[1] = 1
print(
    "Fibonacci non-recursive:",
    fibonacci(N),
    "\tTime:",
    f'{timeit.timeit("fibonacci(N)", setup=f"from __main__ import fibonacci;N={N}", number=RUNS):5f}',
    "O(n)\tSpace: O(1)",
)

fib_recur_list = [0] * (N + 1)
fib_recur_list[0] = 0
fib_recur_list[1] = 1
print(
    "Fibonacci recursive:\t",
    fibonacci_recursive(N),
    "\tTime:",
    f'{timeit.timeit("fibonacci_recursive(N)", setup=f"from __main__ import fibonacci_recursive;N={N}", number=RUNS,):5f}',
    "O(2^n)\tSpace: O(n)",
)

