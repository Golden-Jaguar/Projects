# Instructions
#
# Prime numbers are numbers that can only be cleanly divided by themselves and 1.
#
# https://en.wikipedia.org/wiki/Prime_number
#
# You need to write a function that checks whether if the number passed into it is a prime number or not.
#
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
#
# But 4 is not a prime number because you can divide it by 1, 2 or 4.

# Write your code below this line 👇
import math
def prime_checker(number):
    numb_act = int(math.sqrt(number))
    num_list = []
    calc_number = []
    for num in range(2, (numb_act +1)):
        num_list.append(num)
    for n in num_list:
        calc_number.append(number % n)

    if 0 in calc_number:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")
# Write your code above this line 👆
# # Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
