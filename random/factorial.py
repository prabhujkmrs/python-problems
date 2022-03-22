def factorial(val: int) -> int:
    if val == 0 or val == 1:
        return 1
    return val * factorial(val - 1)


print(factorial(100))
