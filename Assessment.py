def format_address(address_string):
    # Declare variables
    words = address_string.split()
    num = ""
    nam = ""
    # Separate the address string into parts

    # Traverse through the address parts
    for i, word in enumerate(words):
        if i == 0:
            num += word
        elif i != len(words) - 1:
            nam += word + " "
        else:
            nam += word
        # Determine if the address part is the
        # house number or part of the street name

    # Does anything else need to be done
    # before returning the result?

    # Return the formatted string
    return "house number {} on street named {}".format(num, nam)


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))


# Should print "house number 55 on street named North Center Drive"

def highlight_word(sentence, word):
    ret = ""
    l = len(word)
    words = sentence.split()
    for i, w in enumerate(words):
        if w[:l] == word:
            ret += w[:l].upper() + w[l:]
        else:
            ret += w
        if i != len(words) - 1:
            ret += " "
    return ret


print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))


def combine_lists(list1, list2):
    # Generate a new list containing the elements of list2
    for i in range(len(list1) - 1, -1, -1):
        list2.append(list1[i])
    return list2
    # Followed by the elements of list1 in reverse order


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))
