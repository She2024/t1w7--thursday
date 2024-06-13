# Creating a tuple
my_tuple = (1, 2, 3, 'a', 'happy')

# Accessing elements
print(my_tuple[3])
print(my_tuple[0])

# Attempting to change an element
# my_tuple[0] = 10 will return an error TypeError: 'tuple' object does not support item assignment

# a = my_tuple[0]
# b = my_tuple[1]
# c = my_tuple[2
# d = my_tuple[0]


# Tuples can be unpacked
a, b, c, d, e = my_tuple
print(a, e)

# Tuples can contain other tuples (nested tuples)
nested_tuple = (1, (2, 3), (4,5), (0,0))
print(nested_tuple[1])