def is_power_of(number, base):
    # Base case: when number is smaller than base.
    if number < base:
        # If number is equal to 1, it's a power (base**0).
        return number == 1

    # Recursive case: keep dividing number by base.
    return is_power_of(number / base, base)


print(is_power_of(8, 2))  # Should be True
print(is_power_of(64, 4))  # Should be True
print(is_power_of(70, 10))  # Should be False


def count_users(group):
    count = 0
    for member in get_members(group):
        count += 1
        if is_group(member):
            count += count_users(member) - 1
    return count


print(count_users("sales"))  # Should be 3
print(count_users("engineering"))  # Should be 8
print(count_users("everyone"))  # Should be 18<\code>


def sum_positive_numbers(n):
    sum = 0
    if n == 1:
        return 1
    else:
        sum += n + sum_positive_numbers(n - 1)

    return sum


print(sum_positive_numbers(3))  # Should be 6
print(sum_positive_numbers(5))  # Should be 15

number = 1
while number <= 7:
    print(number, end=" ")
    number += 1


def show_letters(word):
    for letter in word:
        print(letter)


show_letters("Hello")
# Should print one line per letter

import math


def digits(n):
    count = 0
    if n == 0:
        return 1
    while (n > 0):
        count += 1
        n = math.floor(n / 10)
    return count


print(digits(25))  # Should print 2
print(digits(144))  # Should print 3
print(digits(1000))  # Should print 4
print(digits(0))  # Should print 1


def multiplication_table(start, stop):
    for x in range(start, stop + 1):
        for y in range(start, stop + 1):
            print(x * y, end=" ")
        print()


multiplication_table(1, 3)


# Should print the multiplication table shown above

def counter(start, stop):
    x = start
    if start > stop:
        return_string = "Counting down: "
        while x >= stop:
            return_string += str(x)
            if x != stop:
                return_string += ","
            x -= 1

    else:
        return_string = "Counting up: "
        while x <= stop:
            return_string += str(x)
            if x != stop:
                return_string += ","
            x += 1
    return return_string


print(counter(1, 10))  # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1))  # Should be "Counting down: 2,1"
print(counter(5, 5))  # Should be "Counting up: 5"


def loop(start, stop, step):
    return_string = ""
    if step == 0:
        step = 1
    if start > stop:
        step = abs(step) * -1
    else:
        step = abs(step)
    for count in range(start, stop, step):
        return_string += str(count) + " "
    return return_string.strip()


print(loop(11, 2, 3))  # Should be 11 8 5
print(loop(1, 5, 0))  # Should be 1 2 3 4
print(loop(-1, -2, 0))  # Should be -1
print(loop(10, 25, -2))  # Should be 10 12 14 16 18 20 22 24
print(loop(1, 1, 1))  # Should be empty
