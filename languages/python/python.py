# Python

# Python is a dynamic multi-paradigm interpreted programming language.
# Python comments start with a `#`

"""
Additionally, python multi-line comments
can be done with triple quotes.
This is an example of that.
"""

"""
Style Guide

I'll be following the Python Enhancement Proposals style guide here:
https://peps.python.org/pep-0008/

1. Python is whitespace-sensitive. Use 4 spaces per indentation level.
2. Modules (and thus source file names) should be snake_case.
3. Names that begin with an _underscore are intended for module-unternal use.
4. Names that begin with __double_underscore are for naming class attributes.
5. Names that begin and end with __double_underscore__ are magic objects,
   and should be used, but not created.
6. Variables and functions should be snake_case.
7. Constants should be SCREAMING_SNAKE_CASE.
"""


# functions are declared with the `def` keyword, a function name,
# the function arguments, and a colon after the argument list.
def basics():
    # you can declare and assign a variable like this.
    variable_name = 10
    # you can print a variable by calling the `print` function like this:
    print(variable_name)

    # There are a few primitive types in python
    integer_example = 10
    float_example = 20.3
    boolean_example = True

    print(integer_example)
    print(float_example)
    print(boolean_example)

    # Python has the standard set of operators
    print(1 + 1)  # addition
    print(1 - 1)  # subtraction
    print(10 % 2)  # modulo
    print(10 ** 2)  # exponentiation
    print(True and False)  # logical AND
    print(True or False)  # logical OR
    print(not True)  # logical NOT
    print(0b1010 & 0b1100)  # bitwise AND
    print(0b1010 | 0b1100)  # bitwise OR
    print(0b1010 ^ 0b1100)  # bitwise XOR
    print(0b1010 << 1)  # bitwise shift left
    print(0b1010 >> 1)  # bitwise shift right
    print(10 == 10)  # equality
    print(10 != 10)  # inequality
    print(10 > 10)  # greater than
    print(10 >= 10)  # greater than or equal to
    print(10 < 10)  # less than
    print(10 <= 10)  # less than or equal to


def conditionals():
    # Python has the standard if-elif-else conditional
    x = 10
    if x == 10:
        print("x is 10")
    elif x == 20:
        print("x is 20")
    else:
        print("x is neither 10 nor 20")

    # Python also has the ternary operator
    x = 10
    y = "x is 10" if x == 10 else "x is not 10"
    print(y)


def loops():
    # Python has the standard for loop
    for i in range(10):
        print(i)

    # Python also has the standard while loop
    i = 0
    while i < 10:
        print(i)
        i += 1


def lists():
    # Python has lists, which are like arrays in other languages
    # Lists can contain any type of object
    list_example = [1, 2, 3, 4, 5]
    print(list_example)

    # You can access elements in a list by index
    print(list_example[0])

    # You can add elements to a list with the `append` method
    list_example.append(6)
    print(list_example)

    # You can remove elements from a list with the `remove` method
    list_example.remove(6)
    print(list_example)

    # You can iterate over a list with a for loop
    for i in list_example:
        print(i)

    # You can also iterate over a list with a for loop and an index
    for i in range(len(list_example)):
        print(list_example[i])
    
    # You can also use enumerate
    for index, value in enumerate(list_example):
        print(index, value)
    
    # Also, python has list comprehensions
    list_comprehension = [i for i in range(10)]
    print(list_comprehension)
    

def tuples():
    # Python has tuples, which are like lists, but immutable
    # Tuples can contain any type of object
    tuple_example = (1, 2, 3, 4, 5)
    print(tuple_example)

    # You can access elements in a tuple by index
    print(tuple_example[0])

    # You can unpack a tuple into variables
    a, b, c, d, e = tuple_example
    print(a, b, c, d, e)


def dictionaries():
    # Python has dictionaries, which are like hashmaps in other languages
    # Dictionaries can contain any type of object
    dictionary_example = {
        "key1": 1,
        "key2": 2,
        "key3": 3,
        "key4": 4,
        "key5": 5
    }
    print(dictionary_example)

    # You can access elements in a dictionary by key
    print(dictionary_example["key1"])

    # You can add elements to a dictionary by key
    dictionary_example["key6"] = 6
    print(dictionary_example)

    # You can remove elements from a dictionary by key
    del dictionary_example["key6"]
    print(dictionary_example)

    # You can iterate over a dictionary with a for loop
    for key, value in dictionary_example.items():
        print(key, value)
