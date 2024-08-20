# Exercise #1: Construct for loops that accomplish the following tasks:
    # a. Print the numbers 0 - 20, one number per line.
# The code below returns the output as numbers 0 to 20, one number per line

for num in range(21):
    print(num)

    # b. Print only the ODD values from 3 - 29, one number per line.
# The code below returns the output as numbers 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27 and 29 - one number per line.

for num in range(3,30,2):
    print(num)

    # c. Print the EVEN numbers 12 to -14 in descending order, one number per line.
# The code below returns the output as numbers 12, 10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10, -12 and -14, one number per line.

for num in range(12, -15, -2):
    print(num)

    # d. Challenge - Print the numbers 50 - 20 in descending order, but only if the numbers are multiples of 3. (Your code should work even if you replace 50 or 20 with other numbers).
# The codes below returns the output as numbers 48, 45, 42, 39, 36, 33, 30, 27, 24 and 21, one number per line.
# Code written without 50

for num in range(48,20,-3):
    print(num)

#Code written with 50

for num in range(50,19,-1):
    if num % 3 == 0:
       print(num)







