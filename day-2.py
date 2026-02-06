# Python Variables Example

# 1. Assigning values to variables
name = "Alice"          # String variable
age = 25                # Integer variable
height = 5.6            # Float variable
is_student = True       # Boolean variable

# 2. Printing variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# 3. Reassigning variables (Python is dynamically typed)
age = "Twenty Five"     # Now 'age' holds a string instead of an integer
print("Updated Age:", age)

# 4. Multiple assignments
x, y, z = 10, 20, 30
print("x:", x, "y:", y, "z:", z)

# 5. Assigning the same value to multiple variables
a = b = c = 100
print("a:", a, "b:", b, "c:", c)



# Python program to demonstrate built-in data types

# Numeric types
integer_num = 42                # int
float_num = 3.1415              # float
complex_num = 2 + 3j            # complex

# Sequence types
string_val = "Hello, Python!"   # str
list_val = [1, 2, 3, "apple"]   # list
tuple_val = (10, 20, 30)        # tuple
range_val = range(5)            # range

# Mapping type
dict_val = {"name": "Alice", "age": 25}  # dict

# Set types
set_val = {1, 2, 3, 2}          # set (duplicates removed)
frozenset_val = frozenset([4, 5, 6])  # frozenset (immutable set)

# Boolean type
bool_val = True                 # bool


# None type
none_val = None                 # NoneType

# Display values and their types
variables = [
    integer_num, float_num, complex_num,
    string_val, list_val, tuple_val, range_val,
    dict_val, set_val, frozenset_val,
    bool_val, none_val
]

print("Python Built-in Data Types Demonstration:\n")
for var in variables:
    print(f"Value: {var} \t Type: {type(var).__name__}")

# Example usage of each type
print("\nExample Operations:")
print(f"Integer addition: {integer_num} + 8 = {integer_num + 8}")
print(f"Float multiplication: {float_num} * 2 = {float_num * 2}")
print(f"Complex conjugate: {complex_num.conjugate()}")
print(f"String upper: {string_val.upper()}")
print(f"List append: {list_val + ['banana']}")
print(f"Tuple indexing: {tuple_val[1]}")
print(f"Range to list: {list(range_val)}")
print(f"Dict get: {dict_val.get('name')}")
print(f"Set union: {set_val | {4, 5}}")
print(f"Frozenset intersection: {frozenset_val & {5, 7}}")
print(f"Boolean NOT: {not bool_val}")
print(f"None check: {none_val is None}")
