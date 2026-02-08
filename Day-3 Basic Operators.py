# 1. Arithmetic Operators

a = 10
b = 3

print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division (float): 3.3333
print(a % b)  # Modulus: 1
print(a ** b) # Exponentiation: 1000
print(a // b) # Floor division: 3

# 2. Comparison (Relational) Operators


print(a == b)  # Equal: False
print(a != b)  # Not equal: True
print(a > b)   # Greater than: True
print(a < b)   # Less than: False
print(a >= b)  # Greater than or equal: True
print(a <= b)  # Less than or equal: False

# 3. Assignment Operators
c = 5   # Simple assignment
c += 2  # c = c + 2
c -= 1  # c = c - 1
c *= 3  # c = c * 3
c /= 2  # c = c / 2
c %= 4  # c = c % 4
c **= 2 # c = c ** 2
c //= 2 # c = c // 2

# 4. Logical Operators
# Used for boolean logic:

x = True
y = False
print(x and y)  # AND: False
print(x or y)   # OR: True
print(not x)    # NOT: False

# 5. Bitwise Operators
a = 5   # 0101 in binary
b = 3   # 0011 in binary
print(a & b)  # AND: 1
print(a | b)  # OR: 7
print(a ^ b)  # XOR: 6
print(~a)     # NOT: -6
print(a << 1) # Left shift: 10
print(a >> 1) # Right shift: 2

# 6. Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)   # True, same object
print(a is c)   # False, different object
print(a is not c) # True

# 7. Membership Operators
my_list = [1, 2, 3]
print(2 in my_list)     # True
print(5 not in my_list) # True