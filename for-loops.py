def factorial(n):
    result = 1
    for x in range(2, n + 1):
        result *= x
    return result


for n in range(10):
    print(n, factorial(n))

for x in range(1, 11):
    print(x ** 3)

for i in range(0, 101, 7):
    print(i)
