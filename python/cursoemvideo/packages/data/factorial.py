def factorial(n):
    """Returns the factorial of a number."""
    f = 1
    for counter in range(1, n + 1):
        f *= counter
    return f
