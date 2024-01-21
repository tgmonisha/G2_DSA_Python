def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage:
if __name__ == "__main__":
    terms = 10  # Change the number of terms in the sequence here

    if terms <= 0:
        print("Please enter a positive integer.")
    else:
        print("Fibonacci sequence:")
        for i in range(terms):
            print(fibonacci(i))

