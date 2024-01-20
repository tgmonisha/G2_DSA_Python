def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence up to the", n, "th number:")
    for i in range(n):
        fib_value = fibonacci(i)
        print(f"F({i}) = {fib_value}")

