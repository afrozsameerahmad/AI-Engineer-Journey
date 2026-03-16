# OPERATORS IN  PYTHON

# 1. Arithmetic Operators
# 2. Assignment Operators
# 3. Comparison Operators
# 4. Logical Operators


# 1. Arithmetic Operators
a = 10
b = 3
print("Addition:", a + b)          # 13
print("Subtraction:", a - b)       # 7      
print("Multiplication:", a * b)    # 30
print("Division:", a / b)          # 3.3333333333333335
print("Floor Division:", a // b)  # 3
print("Modulus:", a % b)         # 1
print("Exponentiation:", a ** b)  # 1000

# 2. Assignment Operators
x = 5
x += 3  # Equivalent to x = x + 3
print("After += 3:", x)  # 8
x -= 2  # Equivalent to x = x - 2
print("After -= 2:", x)  # 6
x *= 4  # Equivalent to x = x * 4
print("After *= 4:", x)  # 24
x /= 6  # Equivalent to x = x / 6
print("After /= 6:", x)  # 4.0
x //= 2  # Equivalent to x = x // 2
print("After //= 2:", x)  # 2.0
x %= 3  # Equivalent to x = x % 3
print("After %= 3:", x)  # 2.0
x **= 2  # Equivalent to x = x ** 2
print("After **= 2:", x)  # 4.0

# 3. Comparison Operators
p = 10
q = 20
print("p == q:", p == q)  # False
print("p != q:", p != q)  # True
print("p > q:", p > q)    # False
print("p < q:", p < q)    # True
print("p >= q:", p >= q)  # False
print("p <= q:", p <= q)  # True

# 4. Logical Operators
r = True
s = False
print("r and s:", r and s)  # False
print("r or s:", r or s)    # True
print("not r:", not r)      # False
print("not s:", not s)      # True


#BITWISE OPERATORS
# 1. Bitwise AND (&)
# 2. Bitwise OR (|)
# 3. Bitwise XOR (^)
# 4. Bitwise NOT (~)
# 5. Left Shift (<<)
# 6. Right Shift (>>)


# 1. Bitwise AND (&)
a = 5  # In binary: 0101
b = 3  # In binary: 0011
print("Bitwise AND:", a & b)  # 1 (In binary: 0001)

# 2. Bitwise OR (|)
print("Bitwise OR:", a | b)   # 7 (In binary: 0111)

# 3. Bitwise XOR (^)
print("Bitwise XOR:", a ^ b)  # 6 (In binary: 0110)

# 4. Bitwise NOT (~)
print("Bitwise NOT a:", ~a)  # -6 (In binary: 1010)

# 5. Left Shift (<<)
print("Left Shift a by 1:", a << 1)  # 10 (In binary: 1010)

# 6. Right Shift (>>)
print("Right Shift a by 1:", a >> 1)  # 2 (In binary: 0010)

#MEMBERSHIP OPERATORS
# 1. in
# 2. not in

# 1. in
my_list = [1, 2, 3, 4, 5]
print("Is 3 in my_list?", 3 in my_list)  # True
print("Is 6 in my_list?", 6 in my_list)  # False

# 2. not in
print("Is 3 not in my_list?", 3 not in my_list)  # False
print("Is 6 not in my_list?", 6 not in my_list)  # True




#IDENTITY OPERATORS
# 1. is
# 2. is not

# 1. is
x = [1, 2, 3]
y = x
print("x is y:", x is y)  # True
z = [1, 2, 3]
print("x is z:", x is z)  # False

# 2. is not
print("x is not y:", x is not y)  # False
print("x is not z:", x is not z)  # True

