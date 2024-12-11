# importing random library
import random

# setting a random seed as 2
random.seed(2)

# reading a string text from the user
string = input()

# creating an empty list to store our ASCII numbers
ascii_value = []

# Iterating through a string bz each characters, converting into ASCII number and storing in a list
for i in string:
    ascii_value.append(ord(i))

# Iterating through our ASCII list and multiplying all numbers in prod variable
prod = 1
for i in ascii_value:
    prod *= i

# Generating a random number between the length of the string and 2000000
random_num = random.randint(len(string), 2000000)

# making a xor operation between our product and a random number
xor_operator = prod ^ random_num

# Converting our XOR into a hexadecimal
hex_dec_value = hex(xor_operator)

# Checking if the length of our hexagonal number is greater than 16
if len(hex_dec_value) > 16:
    # printing out only 16 characters in case if our number contains more than 16 numbers
    for i in range(0, 16):
        print(hex_dec_value[i], end="")
else:
    # printing original number
    print(hex_dec_value)
