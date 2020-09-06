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


def retry(operation, attempts):
    for n in range(attempts):
        if operation():
            print("Attempt " + str(n) + " succeeded")
            break
        else:
            print("Attempt " + str(n) + " failed")


def create_user(args):
    pass


retry(create_user, 3)


def stop_service(args):
    pass


retry(stop_service, 5)
