def factorial(n):
    result = 1
    for x in range(2, n + 1):
        result *= x
    return result


for n in range(10):
    print(n, factorial(n))

