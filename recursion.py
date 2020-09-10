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
